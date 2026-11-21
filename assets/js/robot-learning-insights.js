/**
 * Read-only learning insights for Robot Buddy.
 * Receives already-loaded local snapshots ONLY after the user explicitly enables Learning Insights.
 * Never opens storage, never mutates progress, never sends data outside the device.
 * This is an opt-in snapshot summary, not background tracking or an AI diagnosis.
 */
const asObject = value => value && typeof value === 'object' && !Array.isArray(value) ? value : {};
function getDueObjectiveRecallItems(progress = {}, resourceMap = {}, now = Date.now()) {
  const objectiveById = new Map((resourceMap?.objectives || []).map(item => [item.id, item]));
  const due = [];
  for (const [objectiveId, objectiveState] of Object.entries(asObject(progress?.objectives))) {
    const objective = objectiveById.get(objectiveId);
    if (!objective) continue;
    for (const [itemId, item] of Object.entries(asObject(objectiveState?.items))) {
      const dueAt = Number(item?.recallDueAt) || 0;
      if (dueAt > 0 && dueAt <= now) due.push({area:objective.title || 'Ôn nhớ lại', title:itemId, dueAt});
    }
  }
  return due.sort((a,b)=>a.dueAt-b.dueAt);
}
const values = value => Object.values(asObject(value));
const latestAnswer = (progress, index) => {
  const current = progress?.answers?.[String(index)];
  if (current?.answered) return current;
  const history = progress?.attemptHistory?.[String(index)];
  return Array.isArray(history) && history.length && history[history.length - 1]?.answered ? history[history.length - 1] : null;
};

function summarizePracticeMap(items = [], progressMap = {}) {
  let learn = 0, practice = 0, attempted = 0, questions = 0, correct = 0, studiedUnits = 0, totalUnits = 0;
  const weak = [], learnItems = [], practiceItems = [];
  for (const item of items) {
    const qs = item.questions || item.exercises || [];
    if (!qs.length) continue;
    questions += qs.length;
    totalUnits += 1;
    const progress = asObject(progressMap[item.id]);
    const answers = asObject(progress.answers);
    let seen = 0, right = 0;
    for (let i = 0; i < qs.length; i += 1) {
      const answer = latestAnswer(progress, i);
      if (answer) { seen += 1; if (answer.correct === true) right += 1; }
    }
    attempted += seen; correct += right;
    if (seen) studiedUnits += 1;
    if (!seen) { learn += 1; learnItems.push({area:item.areaLabel || '',title:item.title || item.id}); }
    else if (seen >= 5 && right / seen < 0.7) { practice += 1; const row={area:item.areaLabel || '',title:item.title || item.id,accuracy:Math.round(right/seen*100),attempted:seen}; weak.push(row); practiceItems.push(row); }
  }
  return { learn, practice, attempted, questions, correct, accuracy: attempted ? Math.round(correct / attempted * 100) : null, studiedUnits, totalUnits, coveragePercent: totalUnits ? Math.round(studiedUnits / totalUnits * 100) : null, weak, learnItems, practiceItems };
}

function summarizeFoundationEvidence(groups = [], now = Date.now()) {
  let learn = 0, practice = 0, review = 0, attempted = 0, questions = 0, correct = 0, studiedUnits = 0, totalUnits = 0;
  const learnItems = [], practiceItems = [], reviewItems = [];
  for (const group of groups) {
    const items = Array.isArray(group.items) ? group.items : [];
    const progressMap = asObject(group.progress);
    for (const item of items) {
      const record = asObject(progressMap[item.id]);
      const evidence = values(record.evidence);
      const itemQuestions = item.questionBank || item.questions || [];
      if (!itemQuestions.length) continue;
      questions += itemQuestions.length;
      totalUnits += 1;
      if (!evidence.length) { learn += 1; learnItems.push({area:'Foundation',title:item.title || item.id}); continue; }
      studiedUnits += 1;
      attempted += evidence.length;
      const itemCorrect = evidence.filter(entry => entry.latestCorrect === true).length;
      correct += itemCorrect;
      const dueEntries=evidence.filter(entry => Number(entry.recallDueAt) > 0 && Number(entry.recallDueAt) <= now);
      review += dueEntries.length; if(dueEntries.length)reviewItems.push({area:'Foundation',title:item.title || item.id,count:dueEntries.length});
      if (evidence.length >= 3 && itemCorrect / evidence.length < 0.8) { practice += 1; practiceItems.push({area:'Foundation',title:item.title || item.id,accuracy:Math.round(itemCorrect/evidence.length*100),attempted:evidence.length}); }
    }
  }
  return { learn, practice, review, attempted, questions, correct, accuracy: attempted ? Math.round(correct / attempted * 100) : null, studiedUnits, totalUnits, coveragePercent: totalUnits ? Math.round(studiedUnits / totalUnits * 100) : null, evidence: attempted, learnItems, practiceItems, reviewItems };
}

export function buildRobotLearningInsights(snapshot = {}, now = Date.now()) {
  const words = Array.isArray(snapshot.words) ? snapshot.words : [];
  const vocab = asObject(snapshot.vocabularyProgress);
  const flash = asObject(snapshot.flashProgress);
  let vocabularyLearn = 0, vocabularyPractice = 0, vocabularyReview = 0, vocabularyStudied = 0;
  const learnItems=[], practiceItems=[], reviewItems=[];
  for (const word of words) {
    const p = asObject(vocab[word.id]);
    const reviews = Number(p.reviewCount) || 0;
    if (!reviews) { vocabularyLearn += 1; learnItems.push({area:'Từ vựng',title:word.word || word.id}); continue; }
    vocabularyStudied += 1;
    const correct = Number(p.correctCount) || 0, wrong = Number(p.wrongCount) || 0;
    if (Number(p.dueAt) > 0 && Number(p.dueAt) <= now) { vocabularyReview += 1; reviewItems.push({area:'Từ vựng',title:word.word || word.id}); }
    else if (reviews >= 3 && (wrong > correct || correct / reviews < 0.7)) { vocabularyPractice += 1; practiceItems.push({area:'Từ vựng',title:word.word || word.id,accuracy:Math.round(correct/reviews*100),attempted:reviews}); }
  }
  let flashLearn = 0, flashPractice = 0, flashReview = 0, flashStudied = 0;
  for (const word of words) {
    const p = asObject(flash[word.id]);
    const reps = Number(p.reps) || 0;
    if (!reps) { flashLearn += 1; learnItems.push({area:'Flashcard',title:word.word || word.id}); continue; }
    flashStudied += 1;
    if (Number(p.dueAt) > 0 && Number(p.dueAt) <= now) { flashReview += 1; reviewItems.push({area:'Flashcard',title:word.word || word.id}); }
    else { const quizAttempts=(Number(p.lapses)||0)+(Number(p.correct)||0); if(quizAttempts>=3&&((Number(p.lapses)||0)>(Number(p.correct)||0)||(Number(p.correct)||0)/quizAttempts<0.7)){flashPractice += 1;practiceItems.push({area:'Flashcard',title:word.word || word.id,accuracy:Math.round((Number(p.correct)||0)/quizAttempts*100),attempted:quizAttempts});} }
  }

  const grammar = summarizePracticeMap(snapshot.grammarItems, snapshot.grammarProgress);
  const reading = summarizePracticeMap(snapshot.readingItems, snapshot.readingProgress);
  const listening = summarizePracticeMap(snapshot.listeningItems, snapshot.listeningProgress);
  const foundation = summarizeFoundationEvidence([
    {items:snapshot.foundationItems,progress:snapshot.foundationProgressMap},
    {items:snapshot.foundationReadingItems,progress:snapshot.foundationReadingProgress},
    {items:snapshot.foundationListeningItems,progress:snapshot.foundationListeningProgress}
  ], now);

  learnItems.push(...grammar.learnItems.map(item=>({...item,area:'Ngữ pháp'})),...reading.learnItems.map(item=>({...item,area:'Đọc hiểu'})),...listening.learnItems.map(item=>({...item,area:'Nghe hiểu'})),...foundation.learnItems);
  practiceItems.push(...grammar.practiceItems.map(item=>({...item,area:'Ngữ pháp'})),...reading.practiceItems.map(item=>({...item,area:'Đọc hiểu'})),...listening.practiceItems.map(item=>({...item,area:'Nghe hiểu'})),...foundation.practiceItems);
  reviewItems.push(...foundation.reviewItems);
  const objectiveDueItems = Array.isArray(snapshot.dueRecallItems) ? snapshot.dueRecallItems.map(item=>({area:item.objectiveTitle || 'Ôn nhớ lại',title:item.itemId || item.title || 'Mục tiêu đến hạn'})) : getDueObjectiveRecallItems(snapshot.objectiveProgress, snapshot.objectiveResourceMap, now);
  reviewItems.push(...objectiveDueItems);
  const objectiveDueRecall = objectiveDueItems.length;
  const dueRecall = objectiveDueRecall + foundation.review;
  const mockHistory = Array.isArray(snapshot.mockHistory) ? snapshot.mockHistory : [];
  const completedMocks = mockHistory.filter(item => item?.status === 'completed' && Number.isFinite(Number(item.accuracy)));
  const weakMockRows = completedMocks.filter(item => Number(item.accuracy) < 75);
  const weakMocks = weakMockRows.length;
  practiceItems.push(...weakMockRows.map(item=>({area:'Thi thử',title:item.modeLabel || item.mode || 'Bài thi thử',accuracy:Number(item.accuracy),attempted:Number(item.questions)||0}))); 
  const attemptedModules = [grammar, reading, listening, foundation].filter(item => item.attempted > 0).length;
  const totalLearn = vocabularyLearn + flashLearn + grammar.learn + reading.learn + listening.learn + foundation.learn;
  const totalPractice = vocabularyPractice + flashPractice + grammar.practice + reading.practice + listening.practice + foundation.practice + weakMocks;
  const totalReview = vocabularyReview + flashReview + dueRecall;

  const hasEvidence = vocabularyStudied > 0 || flashStudied > 0 || attemptedModules > 0 || completedMocks > 0 || dueRecall > 0;
  const sections = [
    { name: 'Từ vựng', learn: vocabularyLearn, practice: vocabularyPractice, review: vocabularyReview, evidence: vocabularyStudied, studiedUnits: vocabularyStudied, totalUnits: words.length },
    { name: 'Flashcard', learn: flashLearn, practice: flashPractice, review: flashReview, evidence: flashStudied, studiedUnits: flashStudied, totalUnits: words.length },
    { name: 'Ngữ pháp', ...grammar, evidence: grammar.attempted, review: 0 },
    { name: 'Đọc hiểu', ...reading, evidence: reading.attempted, review: 0 },
    { name: 'Nghe hiểu', ...listening, evidence: listening.attempted, review: 0 },
    { name: 'Foundation', ...foundation, evidence: foundation.attempted },
    { name: 'Thi thử', learn: 0, practice: weakMocks, review: 0, evidence: completedMocks.length, studiedUnits: completedMocks.length, totalUnits: null, attempted: completedMocks.reduce((sum,item)=>sum+(Number(item.questions)||0),0), accuracy: completedMocks.length ? Math.round(completedMocks.reduce((sum,item)=>sum+Number(item.accuracy),0)/completedMocks.length) : null }
  ];
  return {
    hasEvidence, generatedAt: now,
    totals: { learn: totalLearn, practice: totalPractice, review: totalReview },
    dueRecall, vocabularyStudied, vocabularyTotal: words.length,
    sections: sections.map(({ name, learn = 0, practice = 0, review = 0, evidence = 0, accuracy = null, attempted = 0, studiedUnits = 0, totalUnits = null, coveragePercent = null }) => ({ name, learn, practice, review, evidence, accuracy, attempted, studiedUnits, totalUnits, coveragePercent:coveragePercent ?? (Number.isFinite(totalUnits) && totalUnits > 0 ? Math.round(studiedUnits / totalUnits * 100) : null) })),
    items: {learn:learnItems,practice:practiceItems,review:reviewItems},
    notes: { weakMockCount: weakMocks, completedMockCount: completedMocks.length }
  };
}

export function formatRobotLearningInsights(insights) {
  if (!insights?.hasEvidence) {
    const count=Number(insights?.totals?.learn)||0;
    const examples=(insights?.items?.learn||[]).slice(0,5).map(item=>`${item.area}: ${item.title}`).join('; ');
    return `Mình chưa có lịch sử học tập đủ để đánh giá điểm mạnh/yếu trên thiết bị này. Hiện có ${count.toLocaleString('vi-VN')} mục chưa có bằng chứng học tập nên được xếp vào Cần học${examples?`: ${examples}`:''}. Chưa có đủ căn cứ để kết luận mục nào Cần luyện hoặc Cần ôn. Bạn hãy bắt đầu một vài bài học/lượt luyện; mình sẽ cập nhật khi có kết quả. Mình không suy đoán kỹ năng yếu khi chưa có bằng chứng.`;
  }
  const { totals, sections, vocabularyStudied, vocabularyTotal, dueRecall } = insights;
  const lines = [
    'Mình vừa xem các bản ghi tiến độ đang có trên thiết bị. Đây là thống kê theo dữ liệu đã lưu, không phải điểm TOEIC chính thức:',
    `• Cần học: ${totals.learn.toLocaleString('vi-VN')} mục/bài chưa có lượt hoàn thành được ghi nhận.`,
    `• Cần luyện: ${totals.practice.toLocaleString('vi-VN')} mục có kết quả chưa ổn định hoặc dưới ngưỡng nội bộ.`,
    `• Cần ôn: ${totals.review.toLocaleString('vi-VN')} mục đã đến hạn ôn, trong đó ${dueRecall} mục nhớ lại theo lịch.`,
    `• Từ vựng: ${vocabularyStudied.toLocaleString('vi-VN')}/${vocabularyTotal.toLocaleString('vi-VN')} từ có lịch sử ôn.`
  ];
  const evidenced = sections.filter(item => item.evidence > 0 || item.learn > 0).slice(0, 6);
  if (evidenced.length) {
    lines.push('Chi tiết theo khu vực:');
    for (const item of evidenced) {
      const status = [];
      if (item.learn) status.push(`${item.learn} cần học`);
      if (item.practice) status.push(`${item.practice} cần luyện`);
      if (item.review) status.push(`${item.review} cần ôn`);
      const score = item.accuracy === null || item.attempted < 5 ? `chưa đủ dữ liệu để kết luận${item.attempted ? ` (${item.attempted} câu đã trả lời)` : ''}` : `${item.accuracy}% đúng trên ${item.attempted} câu đã trả lời`;
      lines.push(`• ${item.name}: ${status.join(', ') || 'đã có dữ liệu'}; ${score}.`);
    }
  }
  for (const key of ['learn','practice','review']) {
    const rows=(insights.items?.[key]||[]).slice(0,5);
    if(rows.length){const label=key==='learn'?'Ví dụ cần học':key==='practice'?'Ví dụ cần luyện':'Ví dụ cần ôn';lines.push(`${label}: ${rows.map(item=>`${item.area}: ${item.title}${Number.isFinite(item.accuracy)?` (${item.accuracy}% · ${item.attempted} câu)`:''}`).join('; ')}.`);}
  }
  lines.push('Số lượng được tính theo từng khu vực; một từ có thể xuất hiện ở cả Từ vựng và Flashcard. Ngưỡng luyện tập là tiêu chí gợi ý nội bộ. Nếu số lượt làm quá ít, mình sẽ để trạng thái chưa đủ dữ liệu thay vì kết luận bạn yếu ở kỹ năng đó.');
  return lines.join('\n');
}
