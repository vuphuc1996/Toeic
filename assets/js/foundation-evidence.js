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
  return {
    ...ledger,
    [lessonId]: {
      ...prior,
      attempted: true,
      lastCorrect: Boolean(correct),
      lastAnsweredAt: Number(answeredAt),
      evidence: {
        ...evidence,
        [questionId]: { latestCorrect: Boolean(correct), latestAnsweredAt: Number(answeredAt), attempts }
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
