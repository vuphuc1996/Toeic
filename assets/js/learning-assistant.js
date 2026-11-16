/**
 * TOEIC Buddy — deterministic, device-local learning companion.
 * Reads existing learner evidence only; it does not call a model, API or network service.
 * No writes or new persistence contracts are introduced by this module.
 */

function asObject(value) {
  return value && typeof value === 'object' && !Array.isArray(value) ? value : {};
}

function hasPracticeEvidence(progress = {}) {
  const source = asObject(progress);
  const answers = asObject(source.answers);
  const history = asObject(source.attemptHistory);
  return Object.values(answers).some(item => item?.answered === true)
    || Object.values(history).some(items => Array.isArray(items) && items.some(item => item?.answered === true));
}

function hasFoundationEvidence(progress = {}) {
  return Object.values(asObject(progress)).some(record => {
    const item = asObject(record);
    return Object.keys(asObject(item.evidence)).length > 0
      || Object.keys(asObject(item.applicationEvidence)).length > 0
      || Object.keys(asObject(item.productionEvidence)).length > 0
      || Object.values(asObject(item.evidence)).some(entry => Number(entry?.recallDueAt) > 0 || (Array.isArray(entry?.attempts) && entry.attempts.length > 0))
      || Number(item.lastAnsweredAt) > 0;
  });
}

/** True only when the device already has meaningful learning activity. */
export function hasLearningFootprint(context = {}) {
  const wordProgress = asObject(context.wordProgress);
  if (Object.values(wordProgress).some(item => Number(item?.reviewCount || item?.correctCount || item?.wrongCount) > 0)) return true;

  const flashProgress = asObject(context.flashProgress);
  if (Object.values(flashProgress).some(item => Number(item?.correct || item?.lapses || item?.reps || item?.lastQuiz) > 0)) return true;

  for (const key of ['grammarProgress', 'readingProgress', 'listeningProgress']) {
    if (Object.values(asObject(context[key])).some(hasPracticeEvidence)) return true;
  }
  if (hasFoundationEvidence(context.foundationProgress)) return true;

  const objectives = asObject(asObject(context.objectiveProgress).objectives);
  if (Object.values(objectives).some(objective => {
    const data = asObject(objective);
    return Object.values(asObject(data.items)).some(item => Array.isArray(item?.attempts) && item.attempts.length > 0)
      || Object.values(asObject(data.explanationRubrics)).some(item => Array.isArray(item?.attempts) && item.attempts.length > 0);
  })) return true;

  if ((Array.isArray(context.mockHistory) ? context.mockHistory : []).some(item => item?.status === 'completed' || Number(item?.completedAt) > 0)) return true;
  if (Number(context.placementResult?.completedAt) > 0) return true;

  const letters = asObject(context.alphabetSoundProgress).letters;
  if (Object.values(asObject(letters)).some(item => Number(item?.letterName?.count || item?.exampleWord?.count) > 0)) return true;
  return false;
}

function latestAttempt(progress, index) {
  const source = asObject(progress);
  const key = String(index);
  const current = asObject(source.answers)[key];
  if (current?.answered) return current;
  const history = asObject(source.attemptHistory)[key];
  if (Array.isArray(history)) {
    for (let cursor = history.length - 1; cursor >= 0; cursor -= 1) {
      if (history[cursor]?.answered) return history[cursor];
    }
  }
  return null;
}

/** Summarize latest learner answers by TOEIC part; retry history is not double-counted. */
export function summarizePartProgress(items = [], progressMap = {}, parts = []) {
  const rows = [];
  for (const part of parts) {
    const subset = (Array.isArray(items) ? items : []).filter(item => item?.part === part);
    let total = 0;
    let answered = 0;
    let correct = 0;
    let attempts = 0;
    for (const item of subset) {
      const questions = Array.isArray(item?.questions) ? item.questions : [];
      total += questions.length;
      const progress = asObject(progressMap?.[item.id]);
      questions.forEach((_, index) => {
        const latest = latestAttempt(progress, index);
        if (latest) {
          answered += 1;
          if (latest.correct === true) correct += 1;
        }
        const history = asObject(progress.attemptHistory)[String(index)];
        attempts += (Array.isArray(history) ? history.length : 0) + (progress.answers?.[String(index)]?.answered ? 1 : 0);
      });
    }
    rows.push({ part, total, answered, correct, attempts, accuracy: answered ? Math.round(correct / answered * 100) : null });
  }
  return rows;
}


/** Summarize a local practice collection (for example Grammar exercises) by latest answer per question. */
export function summarizeCollectionProgress(items = [], progressMap = {}, questionsKey = 'questions') {
  let total = 0, answered = 0, correct = 0, attempts = 0, lessonsStarted = 0;
  for (const item of Array.isArray(items) ? items : []) {
    const questions = Array.isArray(item?.[questionsKey]) ? item[questionsKey] : [];
    const progress = asObject(progressMap?.[item?.id]);
    let lessonAnswered = 0;
    total += questions.length;
    questions.forEach((_, index) => {
      const latest = latestAttempt(progress, index);
      if (latest) {
        answered += 1;
        lessonAnswered += 1;
        if (latest.correct === true) correct += 1;
      }
      const history = asObject(progress.attemptHistory)[String(index)];
      attempts += (Array.isArray(history) ? history.length : 0) + (progress.answers?.[String(index)]?.answered ? 1 : 0);
    });
    if (lessonAnswered) lessonsStarted += 1;
  }
  return { total, answered, correct, attempts, lessonsStarted, accuracy: answered ? Math.round(correct / answered * 100) : null };
}

/** Summarize Foundation's separate per-question evidence ledgers without merging their scores. */
export function summarizeEvidenceLedger(progress = {}) {
  let lessonsStarted = 0, uniqueQuestions = 0, correct = 0, attempts = 0;
  for (const lesson of Object.values(asObject(progress))) {
    const evidence = asObject(asObject(lesson).evidence);
    const rows = Object.values(evidence);
    if (rows.length) lessonsStarted += 1;
    uniqueQuestions += rows.length;
    for (const row of rows) {
      if (row?.latestCorrect === true) correct += 1;
      attempts += Array.isArray(row?.attempts) ? row.attempts.length : 0;
    }
  }
  return { lessonsStarted, uniqueQuestions, correct, attempts, accuracy: uniqueQuestions ? Math.round(correct / uniqueQuestions * 100) : null };
}

/** Read-only summary from the existing vocabulary, practice, mock and Foundation stores. */
export function buildCompanionSnapshot(context = {}, now = Date.now()) {
  const wordProgress = asObject(context.wordProgress);
  const words = Array.isArray(context.words) ? context.words : [];
  let reviewed = 0;
  let correct = 0;
  let reviewedWords = 0;
  let dueWords = 0;
  const weakWords = [];

  for (const word of words) {
    const progress = asObject(wordProgress[word.id]);
    const reviewCount = Math.max(0, Number(progress.reviewCount) || 0);
    const correctCount = Math.max(0, Number(progress.correctCount) || 0);
    const wrongCount = Math.max(0, Number(progress.wrongCount) || 0);
    if (reviewCount > 0) {
      reviewedWords += 1;
      reviewed += reviewCount;
      correct += correctCount;
    }
    const needsReview = reviewCount > 0 && (wrongCount > correctCount || (Number(progress.dueAt) > 0 && Number(progress.dueAt) <= now));
    if (needsReview) {
      dueWords += 1;
      weakWords.push({ id: word.id, word: word.word, meaning: word.senses?.[0]?.meaning_vi || '', wrongCount, correctCount, dueAt: Number(progress.dueAt) || 0 });
    }
  }
  weakWords.sort((a, b) => (b.wrongCount - b.correctCount) - (a.wrongCount - a.correctCount) || a.dueAt - b.dueAt);

  const flashCards = Object.values(asObject(context.flashProgress));
  const flashReviewedCards = flashCards.filter(item => Number(item?.reps || item?.lastQuiz || item?.correct || item?.lapses) > 0).length;
  const flashRepetitions = flashCards.reduce((sum, item) => sum + Math.max(0, Number(item?.reps) || 0), 0);
  const flashPendingLapses = flashCards.reduce((sum, item) => sum + Math.max(0, Number(item?.lapses) || 0), 0);
  const grammarSummary = summarizeCollectionProgress(context.grammarLessons, context.grammarProgress, 'exercises');
  const grammarByLesson = (Array.isArray(context.grammarLessons) ? context.grammarLessons : []).map(lesson => {
    const summary = summarizeCollectionProgress([lesson], context.grammarProgress, 'exercises');
    return { id: lesson.id, title: lesson.title || lesson.id, ...summary };
  });
  const attemptedGrammar = grammarByLesson.filter(item => item.answered >= 3).sort((a, b) => (a.accuracy ?? 100) - (b.accuracy ?? 100) || b.answered - a.answered);
  const foundationReading = summarizeEvidenceLedger(context.foundationReadingProgress);
  const foundationListening = summarizeEvidenceLedger(context.foundationListeningProgress);
  const listeningParts = summarizePartProgress(context.listening, context.listeningProgress, ['Part 1', 'Part 2', 'Part 3', 'Part 4']);
  const readingParts = summarizePartProgress(context.readings, context.readingProgress, ['Part 5', 'Part 6', 'Part 7']);
  const partStats = [...listeningParts.map(item => ({ ...item, area: 'listening' })), ...readingParts.map(item => ({ ...item, area: 'reading' }))];
  const attemptedParts = partStats.filter(item => item.answered >= 3).sort((a, b) => a.accuracy - b.accuracy || b.answered - a.answered);
  const mockHistory = Array.isArray(context.mockHistory) ? context.mockHistory : [];
  const completedMocks = mockHistory.filter(item => item?.status === 'completed' || Number(item?.completedAt) > 0).length;
  const placementResult = context.placementResult && typeof context.placementResult === 'object' ? context.placementResult : null;
  const portfolio = context.a2Portfolio && typeof context.a2Portfolio === 'object' ? context.a2Portfolio : null;

  return {
    reviewed,
    reviewedWords,
    flashReviewedCards,
    flashRepetitions,
    flashPendingLapses,
    grammarSummary,
    weakestGrammarLesson: attemptedGrammar[0] || null,
    foundationReading,
    foundationListening,
    accuracy: reviewed ? Math.round(correct / reviewed * 100) : null,
    dueWords,
    weakWords: weakWords.slice(0, 5),
    partStats,
    weakestPart: attemptedParts[0] || null,
    foundationDue: Math.max(0, Number(context.foundationDue) || 0),
    completedMocks,
    latestMock: context.latestMock?.score?.total ? {
      accuracy: Number(context.latestMock.score.total.accuracy) || 0,
      correct: Number(context.latestMock.score.total.correct) || 0,
      questions: Number(context.latestMock.score.total.questions) || 0
    } : null,
    placementLevel: placementResult?.recommended || '',
    a2Portfolio: portfolio ? {
      startedTasks: Number(portfolio.startedTasks) || 0,
      totalTasks: Number(portfolio.totalTasks) || 13,
      revisedTasks: Number(portfolio.revisedTasks) || 0,
      improved: Number(portfolio.selfReportedImproved) || 0,
      unchanged: Number(portfolio.selfReportedUnchanged) || 0,
      reduced: Number(portfolio.selfReportedReduced) || 0
    } : null
  };
}

/** A restrained message generator: all statements derive from measured local progress. */
export function buildCompanionMessage(snapshot, page = 'dashboard', event = null) {
  if (event?.message) return { title: event.title || 'Mình có tin mới cho bạn!', message: event.message, tone: event.tone || 'info' };
  const s = snapshot || {};
  if (page === 'mock' && s.latestMock) {
    return { title: 'Mình đã xem kết quả thi thử của bạn.', message: `Bài gần nhất đạt ${s.latestMock.accuracy}% (${s.latestMock.correct}/${s.latestMock.questions} câu đúng). ${s.weakestPart ? `Bạn có thể ưu tiên ${s.weakestPart.part} (${s.weakestPart.accuracy}% sau ${s.weakestPart.answered} câu).` : 'Hãy làm thêm câu hỏi để xác định phần cần ưu tiên.'}`, tone: s.latestMock.accuracy >= 75 ? 'success' : 'encourage' };
  }
  if (page === 'grammar' && s.weakestGrammarLesson) {
    return { title: `Mình cùng củng cố ${s.weakestGrammarLesson.title} nhé!`, message: `Bạn đã làm ${s.weakestGrammarLesson.answered} câu ở bài này và đạt ${s.weakestGrammarLesson.accuracy}%. Đây là gợi ý ôn tập từ dữ liệu hiện có, không phải kết luận năng lực.`, tone: 'encourage' };
  }
  if (page === 'foundation' && s.foundationDue > 0) {
    return { title: 'Đến lượt ôn lại rồi!', message: `Bạn có ${s.foundationDue} câu Foundation đến hạn. Ôn đúng thời điểm giúp bạn củng cố nội dung đã học.`, tone: 'encourage' };
  }
  if (page === 'reading' || page === 'listening') {
    if (s.weakestPart && s.weakestPart.area === page) return { title: `Mình cùng củng cố ${s.weakestPart.part} nhé!`, message: `Hiện bạn đúng ${s.weakestPart.accuracy}% trên ${s.weakestPart.answered} câu đã làm ở phần này. Mình đã đánh dấu đây là ưu tiên luyện tập, không phải kết luận năng lực.`, tone: 'encourage' };
    return { title: page === 'reading' ? 'Cùng luyện đọc hiểu nhé!' : 'Cùng luyện nghe hiểu nhé!', message: 'Khi bạn hoàn thành thêm câu hỏi, mình sẽ tổng hợp kết quả theo từng Part để gợi ý phần cần củng cố.', tone: 'info' };
  }
  if (page === 'practice' && s.dueWords > 0) {
    return { title: 'Mình tìm thấy từ cần ôn lại.', message: `Có ${s.dueWords} từ đã học đang cần củng cố. Mình sẽ đưa bạn về khu vực Ôn tập để tiếp tục.`, tone: 'encourage' };
  }
  if (s.reviewed > 0) {
    return { title: 'Chào mừng bạn quay lại!', message: `Bạn đã có ${s.reviewedWords} từ được luyện qua ${s.reviewed} lượt, độ chính xác theo dữ liệu hiện có là ${s.accuracy}%. ${s.weakestPart ? `Phần nên ưu tiên hiện tại là ${s.weakestPart.part}.` : 'Mình sẽ tiếp tục theo dõi kết quả khi bạn học thêm.'}`, tone: 'success' };
  }
  return { title: 'Mình ở đây để đồng hành cùng bạn!', message: 'Bạn có thể bắt đầu bằng một lượt ôn từ, một bài Foundation hoặc bài thi thử. Khi có kết quả, mình sẽ tổng hợp và gợi ý phần cần luyện dựa trên dữ liệu học của bạn.', tone: 'info' };
}
