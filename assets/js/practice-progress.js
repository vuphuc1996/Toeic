/**
 * Shared attempt-history helpers for Reading, Listening and Grammar practice.
 * `answers` stores the latest submitted attempt for each question index.
 * `attemptHistory` stores earlier attempts and is additive to existing v1 progress.
 */
export function ensurePracticeProgress(progress = {}) {
  if (!progress || typeof progress !== 'object' || Array.isArray(progress)) progress = {};
  if (!progress.answers || typeof progress.answers !== 'object' || Array.isArray(progress.answers)) progress.answers = {};
  if (!progress.attemptHistory || typeof progress.attemptHistory !== 'object' || Array.isArray(progress.attemptHistory)) progress.attemptHistory = {};
  return progress;
}

export function getPracticeAttemptHistory(progress, index) {
  const p = ensurePracticeProgress(progress);
  const history = p.attemptHistory[String(index)];
  return Array.isArray(history) ? history : [];
}

export function getPracticeAttemptCount(progress, index) {
  const p = ensurePracticeProgress(progress);
  const current = p.answers[String(index)];
  return getPracticeAttemptHistory(p, index).length + (current?.answered ? 1 : 0);
}

export function getLatestPracticeAttempt(progress, index) {
  const p = ensurePracticeProgress(progress);
  const current = p.answers[String(index)];
  if (current?.answered) return current;
  const history = getPracticeAttemptHistory(p, index);
  return history.length ? history[history.length - 1] : null;
}

export function recordPracticeAnswer(progress, index, record) {
  const p = ensurePracticeProgress(progress);
  const key = String(index);
  const current = p.answers[key];
  if (current?.answered) return false;
  const attemptNumber = getPracticeAttemptHistory(p, index).length + 1;
  p.answers[key] = { ...record, answered: true, attemptNumber };
  return true;
}

export function archivePracticeAnswerForRetry(progress, index, archivedAt = Date.now()) {
  const p = ensurePracticeProgress(progress);
  const key = String(index);
  const current = p.answers[key];
  if (!current?.answered) return false;
  const history = getPracticeAttemptHistory(p, index);
  history.push({ ...current, archivedAt });
  p.attemptHistory[key] = history;
  delete p.answers[key];
  return true;
}

export function archiveAllPracticeAnswersForRetry(progress, archivedAt = Date.now()) {
  const p = ensurePracticeProgress(progress);
  let archived = 0;
  for (const key of Object.keys(p.answers)) {
    if (archivePracticeAnswerForRetry(p, key, archivedAt)) archived += 1;
  }
  return archived;
}

export function countAttemptedPracticeQuestions(progress, questionCount) {
  const p = ensurePracticeProgress(progress);
  let count = 0;
  for (let index = 0; index < questionCount; index += 1) {
    if (getLatestPracticeAttempt(p, index)?.answered) count += 1;
  }
  return count;
}

export function summarizePracticeProgress(progress, questionCount) {
  const p = ensurePracticeProgress(progress);
  let attempted = 0;
  let correct = 0;
  let totalAttempts = 0;
  for (let index = 0; index < questionCount; index += 1) {
    const latest = getLatestPracticeAttempt(p, index);
    if (latest?.answered) {
      attempted += 1;
      if (latest.correct) correct += 1;
    }
    totalAttempts += getPracticeAttemptCount(p, index);
  }
  return { attempted, correct, totalAttempts, accuracy: attempted ? Math.round((correct / attempted) * 100) : null };
}
