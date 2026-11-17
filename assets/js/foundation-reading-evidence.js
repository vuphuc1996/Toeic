/** Separate short-reading evidence; keyed by stable question IDs. */
export function recordFoundationReadingAttempt(progress = {}, lessonId, questionId, correct, answeredAt = Date.now()) {
  const ledger = progress && typeof progress === 'object' && !Array.isArray(progress) ? progress : {};
  if (!lessonId || !questionId || !Number.isFinite(Number(answeredAt))) return ledger;
  const prior = ledger[lessonId] && typeof ledger[lessonId] === 'object' ? ledger[lessonId] : {};
  const evidence = prior.evidence && typeof prior.evidence === 'object' && !Array.isArray(prior.evidence) ? prior.evidence : {};
  const item = evidence[questionId] && typeof evidence[questionId] === 'object' ? evidence[questionId] : {};
  const attempts = Array.isArray(item.attempts) ? item.attempts.slice() : [];
  attempts.push({ correct: Boolean(correct), answeredAt: Number(answeredAt) });
  return { ...ledger, [lessonId]: { ...prior, evidence: { ...evidence, [questionId]: { latestCorrect: Boolean(correct), latestAnsweredAt: Number(answeredAt), attempts } } } };
}
export function summarizeFoundationReading(progress = {}, lessonId, policy = {}) {
  const evidence = Object.values(progress?.[lessonId]?.evidence || {});
  const uniqueQuestions = evidence.length;
  const correct = evidence.filter(item => item.latestCorrect === true).length;
  const minimumUniqueQuestions = Number(policy.minimumUniqueQuestions) > 0 ? Number(policy.minimumUniqueQuestions) : 2;
  const threshold = Number(policy.practiceAccuracyThreshold) > 0 ? Number(policy.practiceAccuracyThreshold) : 0.8;
  const accuracy = uniqueQuestions ? correct / uniqueQuestions : null;
  const accuracyPercent = accuracy === null ? null : Math.round(accuracy * 100);
  const thresholdPercent = Math.round(threshold * 100);
  return { uniqueQuestions, correct, accuracy, accuracyPercent, minimumUniqueQuestions, threshold, status: uniqueQuestions < minimumUniqueQuestions ? 'insufficient_evidence' : accuracyPercent >= thresholdPercent ? 'practice_threshold_met' : 'in_progress', totalAttempts: evidence.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.length : 0), 0) };
}
