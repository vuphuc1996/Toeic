const DAY_MS = 24 * 60 * 60 * 1000;

/**
 * Foundation lesson evidence. Keeps the legacy foundation progress fields intact
 * while recording results by stable question ID. A practice threshold is not a
 * CEFR claim and does not certify listening, speaking or real-world transfer.
 */
export function recordFoundationAttempt(progress = {}, lessonId, questionId, correct, answeredAt = Date.now()) {
  const ledger = progress && typeof progress === 'object' && !Array.isArray(progress) ? progress : {};
  if (!lessonId || !questionId || !Number.isFinite(Number(answeredAt))) return ledger;
  const prior = ledger[lessonId] && typeof ledger[lessonId] === 'object' ? ledger[lessonId] : {};
  const evidence = prior.evidence && typeof prior.evidence === 'object' && !Array.isArray(prior.evidence) ? prior.evidence : {};
  const item = evidence[questionId] && typeof evidence[questionId] === 'object' ? evidence[questionId] : {};
  const attempts = Array.isArray(item.attempts) ? item.attempts.slice() : [];
  attempts.push({ correct: Boolean(correct), answeredAt: Number(answeredAt) });
  const recallDueAt = Number(item.recallDueAt) || (Number(answeredAt) + DAY_MS);
  return {
    ...ledger,
    [lessonId]: {
      ...prior,
      attempted: true,
      lastCorrect: Boolean(correct),
      lastAnsweredAt: Number(answeredAt),
      evidence: {
        ...evidence,
        [questionId]: { ...item, latestCorrect: Boolean(correct), latestAnsweredAt: Number(answeredAt), attempts, recallDueAt }
      }
    }
  };
}

export function summarizeFoundationLesson(progress = {}, lessonId, policy = {}) {
  const lesson = progress?.[lessonId] || {};
  const evidence = lesson.evidence && typeof lesson.evidence === 'object' ? Object.values(lesson.evidence) : [];
  const uniqueQuestions = evidence.length;
  const correct = evidence.filter(item => item.latestCorrect === true).length;
  const minimumUniqueQuestions = Number(policy.minimumUniqueQuestions) > 0 ? Number(policy.minimumUniqueQuestions) : 3;
  const threshold = Number(policy.practiceAccuracyThreshold) > 0 ? Number(policy.practiceAccuracyThreshold) : 0.8;
  const accuracy = uniqueQuestions ? correct / uniqueQuestions : null;
  const eligible = uniqueQuestions >= minimumUniqueQuestions;
  return {
    uniqueQuestions, correct, accuracy,
    accuracyPercent: accuracy === null ? null : Math.round(accuracy * 100),
    minimumUniqueQuestions, threshold,
    evidenceCoveragePercent: Math.min(100, Math.round(uniqueQuestions / minimumUniqueQuestions * 100)),
    status: !eligible ? 'insufficient_evidence' : accuracy >= threshold ? 'practice_threshold_met' : 'in_progress',
    totalAttempts: evidence.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.length : 0), 0)
  };
}

/** Separate contextual-application evidence; never mixes with recognition checks. */
export function recordFoundationApplicationAttempt(progress = {}, lessonId, taskId, correct, answeredAt = Date.now()) {
  const ledger = progress && typeof progress === 'object' && !Array.isArray(progress) ? progress : {};
  if (!lessonId || !taskId || !Number.isFinite(Number(answeredAt))) return ledger;
  const prior = ledger[lessonId] && typeof ledger[lessonId] === 'object' ? ledger[lessonId] : {};
  const applicationEvidence = prior.applicationEvidence && typeof prior.applicationEvidence === 'object' && !Array.isArray(prior.applicationEvidence) ? prior.applicationEvidence : {};
  const item = applicationEvidence[taskId] && typeof applicationEvidence[taskId] === 'object' ? applicationEvidence[taskId] : {};
  const attempts = Array.isArray(item.attempts) ? item.attempts.slice() : [];
  attempts.push({ correct: Boolean(correct), answeredAt: Number(answeredAt) });
  return { ...ledger, [lessonId]: { ...prior, applicationEvidence: { ...applicationEvidence, [taskId]: { latestCorrect: Boolean(correct), latestAnsweredAt: Number(answeredAt), attempts } } } };
}

export function summarizeFoundationApplication(progress = {}, lessonId) {
  const lesson = progress?.[lessonId] || {};
  const evidence = lesson.applicationEvidence && typeof lesson.applicationEvidence === 'object' ? Object.values(lesson.applicationEvidence) : [];
  const correct = evidence.filter(item => item.latestCorrect === true).length;
  return { uniqueTasks: evidence.length, correct, accuracyPercent: evidence.length ? Math.round(correct / evidence.length * 100) : null, totalAttempts: evidence.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.length : 0), 0), status: !evidence.length ? 'not_attempted' : correct === evidence.length ? 'application_check_passed' : 'needs_practice' };
}


/**
 * Record a delayed-recall check only after its scheduled due time. The original
 * recognition evidence and denominator remain unchanged. A correct recall is
 * scheduled again in three days; an incorrect recall is rescheduled in one day.
 */
export function recordFoundationRecallAttempt(progress = {}, lessonId, questionId, correct, checkedAt = Date.now()) {
  const ledger = progress && typeof progress === 'object' && !Array.isArray(progress) ? progress : {};
  if (!lessonId || !questionId || !Number.isFinite(Number(checkedAt))) return ledger;
  const prior = ledger[lessonId] && typeof ledger[lessonId] === 'object' ? ledger[lessonId] : {};
  const evidence = prior.evidence && typeof prior.evidence === 'object' && !Array.isArray(prior.evidence) ? prior.evidence : {};
  const item = evidence[questionId];
  if (!item || typeof item !== 'object') return ledger;
  const dueAt = Number(item.recallDueAt) || 0;
  if (!dueAt || Number(checkedAt) < dueAt) return ledger;
  const recallChecks = Array.isArray(item.recallChecks) ? item.recallChecks.slice() : [];
  recallChecks.push({ correct: Boolean(correct), answeredAt: Number(checkedAt), dueAt });
  const nextDueAt = Number(checkedAt) + (correct ? 3 : 1) * DAY_MS;
  return {
    ...ledger,
    [lessonId]: {
      ...prior,
      evidence: {
        ...evidence,
        [questionId]: {
          ...item,
          recallChecks,
          latestRecallCorrect: Boolean(correct),
          latestRecallAnsweredAt: Number(checkedAt),
          recallDueAt: nextDueAt
        }
      }
    }
  };
}

export function listDueFoundationRecallItems(progress = {}, lessons = [], now = Date.now()) {
  const due = [];
  for (const lesson of Array.isArray(lessons) ? lessons : []) {
    const evidence = progress?.[lesson.id]?.evidence || {};
    for (const question of lesson.questionBank || []) {
      const item = evidence[question.id];
      const dueAt = Number(item?.recallDueAt) || 0;
      if (!dueAt || dueAt > Number(now)) continue;
      due.push({
        lessonId: lesson.id, lessonTitle: lesson.title || lesson.id, level: lesson.level || '',
        questionId: question.id, question: question.question, choices: question.choices || [],
        answerIndex: question.answerIndex, rationale: question.rationale || '', dueAt,
        recallChecks: Array.isArray(item.recallChecks) ? item.recallChecks.length : 0
      });
    }
  }
  return due.sort((a, b) => a.dueAt - b.dueAt || a.lessonId.localeCompare(b.lessonId) || a.questionId.localeCompare(b.questionId));
}

export function summarizeFoundationRetention(progress = {}, lessons = [], policy = {}) {
  const minimumUniqueItems = Number(policy.minimumUniqueItems) > 0 ? Number(policy.minimumUniqueItems) : 10;
  const threshold = Number(policy.threshold) > 0 ? Number(policy.threshold) : 0.8;
  const retained = [];
  let dueItems = 0;
  for (const lesson of Array.isArray(lessons) ? lessons : []) {
    const evidence = progress?.[lesson.id]?.evidence || {};
    for (const question of lesson.questionBank || []) {
      const item = evidence[question.id];
      const checks = Array.isArray(item?.recallChecks) ? item.recallChecks : [];
      if (checks.length) retained.push(checks[checks.length - 1].correct === true);
      if (Number(item?.recallDueAt) > 0 && Number(item.recallDueAt) <= Number(policy.now ?? Date.now())) dueItems++;
    }
  }
  const uniqueItems = retained.length;
  const correct = retained.filter(Boolean).length;
  const accuracy = uniqueItems ? correct / uniqueItems : null;
  const eligible = uniqueItems >= minimumUniqueItems;
  return {
    uniqueItems, correct, accuracy, accuracyPercent: accuracy === null ? null : Math.round(accuracy * 100),
    minimumUniqueItems, threshold, dueItems,
    evidenceCoveragePercent: Math.min(100, Math.round(uniqueItems / minimumUniqueItems * 100)),
    status: !eligible ? 'insufficient_evidence' : accuracy >= threshold ? 'delayed_recall_threshold_met' : 'in_progress'
  };
}

/**
 * Store a learner-authored sentence with a three-point self-assessment. The
 * sentence remains in the device-local Foundation ledger; no server sync or
 * automatic grammar verdict is implied by this self-report.
 */
export function recordFoundationProductionAttempt(progress = {}, lessonId, taskId, responseText, rubricRatings, assessedAt = Date.now(), minimumWords = 3) {
  const ledger = progress && typeof progress === 'object' && !Array.isArray(progress) ? progress : {};
  const response = String(responseText || '').trim().slice(0, 500);
  const requiredWords = Math.max(3, Math.min(60, Number(minimumWords) || 3));
  const responseWords = response.split(/\s+/).filter(Boolean);
  if (!lessonId || !taskId || responseWords.length < requiredWords || !Array.isArray(rubricRatings) || rubricRatings.length !== 3 || rubricRatings.some(value => typeof value !== 'boolean') || !Number.isFinite(Number(assessedAt))) return ledger;
  const prior = ledger[lessonId] && typeof ledger[lessonId] === 'object' ? ledger[lessonId] : {};
  const productionEvidence = prior.productionEvidence && typeof prior.productionEvidence === 'object' && !Array.isArray(prior.productionEvidence) ? prior.productionEvidence : {};
  const item = productionEvidence[taskId] && typeof productionEvidence[taskId] === 'object' ? productionEvidence[taskId] : {};
  const attempts = Array.isArray(item.attempts) ? item.attempts.slice() : [];
  const score = rubricRatings.filter(Boolean).length;
  const wordCount = responseWords.length;
  attempts.push({ response, ratings: rubricRatings.slice(), score, maxScore: 3, wordCount, minimumWords: requiredWords, assessedAt: Number(assessedAt), assessmentType: 'learner_self_report' });
  return {
    ...ledger,
    [lessonId]: {
      ...prior,
      productionEvidence: {
        ...productionEvidence,
        [taskId]: {
          ...item,
          initialResponse: item.initialResponse || item.latestResponse || response,
          latestScore: score, latestRatings: rubricRatings.slice(), latestWordCount: wordCount,
          minimumWords: requiredWords, latestAssessedAt: Number(assessedAt), latestResponse: response,
          latestAssessmentType: 'learner_self_report', attempts
        }
      }
    }
  };
}

/**
 * Record a learner-led revision after a first production attempt. It links the
 * new response to the version the learner reviewed and stores checklist and
 * rubric values as self-reports only; it does not evaluate linguistic quality.
 */
export function recordFoundationProductionRevision(progress = {}, lessonId, taskId, responseText, rubricRatings, reviewChecks, assessedAt = Date.now(), minimumWords = 8) {
  const ledger = progress && typeof progress === 'object' && !Array.isArray(progress) ? progress : {};
  const response = String(responseText || '').trim().slice(0, 500);
  const requiredWords = Math.max(3, Math.min(60, Number(minimumWords) || 8));
  const responseWords = response.split(/\s+/).filter(Boolean);
  if (!lessonId || !taskId || responseWords.length < requiredWords || !Array.isArray(rubricRatings) || rubricRatings.length !== 3 || rubricRatings.some(value => typeof value !== 'boolean') || !Array.isArray(reviewChecks) || reviewChecks.length !== 3 || reviewChecks.some(value => value !== true) || !Number.isFinite(Number(assessedAt))) return ledger;
  const prior = ledger[lessonId] && typeof ledger[lessonId] === 'object' ? ledger[lessonId] : {};
  const productionEvidence = prior.productionEvidence && typeof prior.productionEvidence === 'object' && !Array.isArray(prior.productionEvidence) ? prior.productionEvidence : {};
  const item = productionEvidence[taskId] && typeof productionEvidence[taskId] === 'object' ? productionEvidence[taskId] : {};
  const previousResponse = String(item.latestResponse || '').trim();
  const normalize = value => value.toLowerCase().replace(/\s+/g, ' ').trim();
  if (!previousResponse || normalize(previousResponse) === normalize(response)) return ledger;
  const attempts = Array.isArray(item.attempts) ? item.attempts.slice() : [];
  const score = rubricRatings.filter(Boolean).length;
  const wordCount = responseWords.length;
  const revisionCount = Math.max(0, Number(item.revisionCount) || 0) + 1;
  attempts.push({ response, basedOnResponse: previousResponse, reviewChecks: reviewChecks.slice(), ratings: rubricRatings.slice(), score, maxScore: 3, wordCount, minimumWords: requiredWords, assessedAt: Number(assessedAt), assessmentType: 'guided_revision' });
  return {
    ...ledger,
    [lessonId]: {
      ...prior,
      productionEvidence: {
        ...productionEvidence,
        [taskId]: {
          ...item,
          initialResponse: item.initialResponse || previousResponse,
          lastRevisionSource: previousResponse,
          latestRevisionChecks: reviewChecks.slice(),
          revisionCount,
          latestScore: score, latestRatings: rubricRatings.slice(), latestWordCount: wordCount,
          minimumWords: requiredWords, latestAssessedAt: Number(assessedAt), latestResponse: response,
          latestAssessmentType: 'guided_revision', attempts
        }
      }
    }
  };
}

/**
 * Summarize A2 writing history from the learner's own rubric ratings.
 * The trend is explicitly self-reported and must never be presented as
 * objective writing quality, automated correction or CEFR mastery.
 */
export function summarizeFoundationProductionPortfolio(progress = {}, lessons = [], policy = {}) {
  const level = String(policy.level || 'A2').toUpperCase();
  const scopedLessons = (Array.isArray(lessons) ? lessons : []).filter(lesson => String(lesson?.level || '').toUpperCase() === level);
  const records = [];
  let totalAttempts = 0;

  for (const lesson of scopedLessons) {
    const taskId = lesson?.productionTask?.id || lesson?.applicationTask?.id;
    const saved = taskId ? progress?.[lesson.id]?.productionEvidence?.[taskId] : null;
    if (!saved || typeof saved !== 'object') continue;

    const attempts = Array.isArray(saved.attempts) ? saved.attempts.filter(item => item && typeof item === 'object') : [];
    const attemptScores = attempts.map(item => {
      const score = Number(item.score);
      return Number.isFinite(score) && score >= 0 && score <= 3 ? score : null;
    });
    const latestAttempt = attempts.at(-1) || null;
    const firstAttemptIndex = attemptScores.findIndex(score => score !== null);
    const firstScoreFromHistory = firstAttemptIndex >= 0 ? attemptScores[firstAttemptIndex] : null;
    const storedLatest = Number(saved.latestScore);
    const latestScore = Number.isFinite(storedLatest) && storedLatest >= 0 && storedLatest <= 3
      ? storedLatest
      : latestAttempt && Number.isFinite(Number(latestAttempt.score)) ? Number(latestAttempt.score) : null;
    if (latestScore === null) continue;

    const initialStored = Number(saved.initialScore);
    const initialScore = firstScoreFromHistory !== null
      ? firstScoreFromHistory
      : Number.isFinite(initialStored) && initialStored >= 0 && initialStored <= 3 ? initialStored : latestScore;
    const guidedRevisionAttempts = attempts.filter(item => item.assessmentType === 'guided_revision').length;
    const revisionCount = Math.max(guidedRevisionAttempts, Math.max(0, Number(saved.revisionCount) || 0));
    const latestRatings = Array.isArray(saved.latestRatings) && saved.latestRatings.length === 3
      ? saved.latestRatings
      : Array.isArray(latestAttempt?.ratings) && latestAttempt.ratings.length === 3 ? latestAttempt.ratings : [];
    const rubric = Array.isArray(lesson?.productionTask?.rubric) && lesson.productionTask.rubric.length === 3
      ? lesson.productionTask.rubric
      : Array.isArray(lesson?.applicationTask?.rubric) ? lesson.applicationTask.rubric : [];
    const latestAssessedAt = Number(saved.latestAssessedAt || latestAttempt?.assessedAt);
    records.push({
      lessonId: lesson.id,
      title: String(lesson.title || lesson.id || 'Bài viết A2'),
      attemptCount: Math.max(attempts.length, 1),
      revisionCount,
      initialScore,
      latestScore,
      trend: revisionCount === 0 ? 'not_revised' : latestScore > initialScore ? 'self_report_up' : latestScore < initialScore ? 'self_report_down' : 'self_report_same',
      latestRatings: latestRatings.slice(0, 3),
      rubric: rubric.map(String),
      latestAssessedAt: Number.isFinite(latestAssessedAt) ? latestAssessedAt : null
    });
    totalAttempts += Math.max(attempts.length, 1);
  }

  const revised = records.filter(item => item.revisionCount > 0);
  const compareRows = revised.filter(item => Number.isFinite(item.initialScore) && Number.isFinite(item.latestScore));
  return {
    level,
    totalTasks: scopedLessons.filter(lesson => lesson?.productionTask?.id || lesson?.applicationTask?.id).length,
    startedTasks: records.length,
    revisedTasks: revised.length,
    totalAttempts,
    selfReportedImproved: compareRows.filter(item => item.latestScore > item.initialScore).length,
    selfReportedUnchanged: compareRows.filter(item => item.latestScore === item.initialScore).length,
    selfReportedReduced: compareRows.filter(item => item.latestScore < item.initialScore).length,
    records: records.sort((a, b) => a.title.localeCompare(b.title, 'vi')),
    selfReportOnly: true,
    objectiveGrading: false
  };
}

export function summarizeFoundationProduction(progress = {}, lessons = [], policy = {}) {
  const minimumUniqueItems = Number(policy.minimumUniqueItems) > 0 ? Number(policy.minimumUniqueItems) : 10;
  const threshold = Number(policy.threshold) > 0 ? Number(policy.threshold) : 0.8;
  const evidence = [];
  for (const lesson of Array.isArray(lessons) ? lessons : []) {
    const taskId = lesson.productionTask?.id || lesson.applicationTask?.id;
    const saved = taskId ? progress?.[lesson.id]?.productionEvidence?.[taskId] : null;
    if (saved && Number.isFinite(Number(saved.latestScore))) evidence.push(saved);
  }
  const uniqueItems = evidence.length;
  const scorePercent = uniqueItems ? Math.round(evidence.reduce((sum, item) => sum + Number(item.latestScore || 0), 0) / (uniqueItems * 3) * 100) : null;
  const totalAttempts = evidence.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.length : 0), 0);
  const eligible = uniqueItems >= minimumUniqueItems;
  return {
    uniqueItems, minimumUniqueItems, scorePercent, threshold, totalAttempts, selfReportOnly: true,
    evidenceCoveragePercent: Math.min(100, Math.round(uniqueItems / minimumUniqueItems * 100)),
    status: !eligible ? 'insufficient_evidence' : scorePercent / 100 >= threshold ? 'self_report_threshold_met' : 'in_progress'
  };
}

/** Build objective-level Foundation evidence without mixing Recognition, Production or Retention. */
export function summarizeFoundationOutcomeProgress(progress = {}, lessons = [], outcomeRegistry = {}, now = Date.now()) {
  const result = [];
  for (const objective of outcomeRegistry.objectives || []) {
    if (!String(objective.objectiveId || '').startsWith('foundation-')) continue;
    const isA2 = objective.objectiveId === 'foundation-a2';
    const scopeLessons = (lessons || []).filter(lesson => isA2 ? lesson.level === 'A2' : ['PRE-A1', 'A1'].includes(lesson.level));
    for (const outcome of objective.outcomes || []) {
      const id = String(outcome.id || '');
      const kind = id.endsWith('-recognition') ? 'recognition' : id.endsWith('-production') || id.endsWith('-application') ? 'production' : id.endsWith('-retention') ? 'retention' : 'unsupported';
      const minimumUniqueItems = Number(outcome.minimumUniqueItems) > 0 ? Number(outcome.minimumUniqueItems) : 10;
      const threshold = Number(outcome.masteryThreshold) > 0 ? Number(outcome.masteryThreshold) : 0.8;
      let correct = 0, uniqueItems = 0, accuracyPercent = null, dueItems = 0;
      if (kind === 'recognition') {
        const evidence = [];
        for (const lesson of scopeLessons) for (const question of lesson.questionBank || []) {
          const saved = progress?.[lesson.id]?.evidence?.[question.id];
          if (saved && Array.isArray(saved.attempts) && saved.attempts.length) evidence.push(saved.latestCorrect === true);
        }
        uniqueItems = evidence.length; correct = evidence.filter(Boolean).length;
        accuracyPercent = uniqueItems ? Math.round(correct / uniqueItems * 100) : null;
      } else if (kind === 'production') {
        const evidence = [];
        for (const lesson of scopeLessons) {
          const taskId = lesson.productionTask?.id || lesson.applicationTask?.id;
          const saved = taskId ? progress?.[lesson.id]?.productionEvidence?.[taskId] : null;
          if (saved && Number.isFinite(Number(saved.latestScore))) evidence.push(Number(saved.latestScore));
        }
        uniqueItems = evidence.length;
        accuracyPercent = uniqueItems ? Math.round(evidence.reduce((sum, score) => sum + score, 0) / (uniqueItems * 3) * 100) : null;
        correct = evidence.filter(score => score === 3).length;
      } else if (kind === 'retention') {
        const evidence = [];
        for (const lesson of scopeLessons) for (const question of lesson.questionBank || []) {
          const saved = progress?.[lesson.id]?.evidence?.[question.id];
          const checks = Array.isArray(saved?.recallChecks) ? saved.recallChecks : [];
          if (checks.length) evidence.push(checks[checks.length - 1].correct === true);
          if (Number(saved?.recallDueAt) > 0 && Number(saved.recallDueAt) <= now) dueItems++;
        }
        uniqueItems = evidence.length; correct = evidence.filter(Boolean).length;
        accuracyPercent = uniqueItems ? Math.round(correct / uniqueItems * 100) : null;
      }
      const eligible = uniqueItems >= minimumUniqueItems;
      const met = eligible && accuracyPercent !== null && accuracyPercent / 100 >= threshold;
      result.push({
        objectiveId: objective.objectiveId, outcomeId: outcome.id, title: outcome.title, kind, metric: outcome.evidenceMetric,
        uniqueItems, minimumUniqueItems, correct, accuracyPercent, threshold, dueItems, selfReportOnly: kind === 'production',
        evidenceCoveragePercent: Math.min(100, Math.round(uniqueItems / minimumUniqueItems * 100)),
        status: !eligible ? 'insufficient_evidence' : !met ? 'in_progress' : kind === 'production' ? 'self_report_threshold_met' : kind === 'retention' ? 'delayed_recall_threshold_met' : 'practice_threshold_met'
      });
    }
  }
  return result;
}
