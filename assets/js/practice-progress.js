/**
 * Shared attempt-history helpers for Reading, Listening and Grammar practice.
 * `answers` stores the latest submitted attempt for each question index.
 * `attemptHistory` stores earlier attempts and is additive to existing v1 progress.
 */
export function ensurePracticeProgress(progress = {}) {
  if (!progress || typeof progress !== 'object' || Array.isArray(progress)) progress = {};
  if (!progress.answers || typeof progress.answers !== 'object' || Array.isArray(progress.answers)) progress.answers = {};
  if (!progress.attemptHistory || typeof progress.attemptHistory !== 'object' || Array.isArray(progress.attemptHistory)) progress.attemptHistory = {};
  if (!progress.draftAnswers || typeof progress.draftAnswers !== 'object' || Array.isArray(progress.draftAnswers)) progress.draftAnswers = {};
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
  if (p.draftAnswers) delete p.draftAnswers[key];
  return true;
}

export function archiveAllPracticeAnswersForRetry(progress, archivedAt = Date.now()) {
  const p = ensurePracticeProgress(progress);
  let archived = 0;
  for (const key of Object.keys(p.answers)) {
    if (archivePracticeAnswerForRetry(p, Number(key), archivedAt)) archived += 1;
  }
  p.draftAnswers = {};
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

/**
 * Draft-before-reveal workflow for multi-question practice sets.
 * Drafts contain only learner selections; correctness and explanations are
 * materialized only after the learner confirms the completed set.
 */
export function stagePracticeChoice(progress, index, choiceIndex, answeredAt = Date.now(), startedAt = answeredAt) {
  const p = ensurePracticeProgress(progress);
  const key = String(index);
  if (!Number.isInteger(index) || index < 0 || !Number.isInteger(choiceIndex) || choiceIndex < 0) return false;
  if (p.answers[key]?.answered) return false;
  if (!p.draftAnswers || typeof p.draftAnswers !== 'object' || Array.isArray(p.draftAnswers)) p.draftAnswers = {};
  const existing = p.draftAnswers[key];
  p.draftAnswers[key] = {
    choiceIndex,
    answeredAt: Number.isFinite(Number(answeredAt)) ? Number(answeredAt) : Date.now(),
    startedAt: Number.isFinite(Number(existing?.startedAt)) ? Number(existing.startedAt) : (Number.isFinite(Number(startedAt)) ? Number(startedAt) : Date.now()),
  };
  return true;
}

export function getPracticeDraftChoice(progress, index) {
  const p = ensurePracticeProgress(progress);
  const draft = p.draftAnswers?.[String(index)];
  return Number.isInteger(draft?.choiceIndex) ? draft.choiceIndex : null;
}

export function getPracticeDraftEntries(progress) {
  const p = ensurePracticeProgress(progress);
  return Object.entries(p.draftAnswers || {})
    .filter(([, draft]) => Number.isInteger(draft?.choiceIndex))
    .map(([index, draft]) => ({ index: Number(index), ...draft }))
    .filter(item => Number.isInteger(item.index) && item.index >= 0)
    .sort((a, b) => a.index - b.index);
}

export function clearPracticeDraftAnswers(progress) {
  const p = ensurePracticeProgress(progress);
  const count = getPracticeDraftEntries(p).length;
  p.draftAnswers = {};
  return count;
}

/**
 * A set is ready when every currently-unlocked question has a draft selection.
 * Previously submitted questions remain historical and are not silently
 * counted as part of a new retry attempt.
 */
export function isPracticeDraftSetComplete(progress, questionCount) {
  const p = ensurePracticeProgress(progress);
  for (let index = 0; index < questionCount; index += 1) {
    if (p.answers[String(index)]?.answered) continue;
    if (!Number.isInteger(p.draftAnswers?.[String(index)]?.choiceIndex)) return false;
  }
  return questionCount > 0;
}

export function summarizePracticeDraftSet(progress, questions) {
  const p = ensurePracticeProgress(progress);
  const entries = getPracticeDraftEntries(p).filter(({ index, choiceIndex }) => {
    const question = questions?.[index];
    return question && Number.isInteger(choiceIndex) && choiceIndex >= 0 && choiceIndex < (question.choices || []).length;
  });
  let correct = 0;
  for (const entry of entries) if (entry.choiceIndex === Number(questions[entry.index].answerIndex)) correct += 1;
  return { answered: entries.length, correct, incorrect: entries.length - correct, total: entries.length, accuracy: entries.length ? Math.round(correct / entries.length * 100) : 0 };
}

/**
 * Atomically commit a complete draft set using the existing attempt-history
 * schema. The supplied record factory may add stable choice IDs and metadata.
 */
export function commitPracticeDraftSet(progress, questions, recordFactory, now = Date.now()) {
  const p = ensurePracticeProgress(progress);
  const entries = getPracticeDraftEntries(p);
  const expectedIndices = [];
  for (let index = 0; index < (questions || []).length; index += 1) {
    if (!p.answers[String(index)]?.answered) expectedIndices.push(index);
  }
  if (!expectedIndices.length || expectedIndices.some(index => !Number.isInteger(p.draftAnswers?.[String(index)]?.choiceIndex))) {
    return { committed: 0, complete: false, records: [] };
  }
  const records = [];
  for (const index of expectedIndices) {
    const question = questions[index];
    const draft = p.draftAnswers[String(index)];
    const choiceIndex = draft.choiceIndex;
    const correct = choiceIndex === Number(question.answerIndex);
    const record = typeof recordFactory === 'function'
      ? recordFactory({ question, index, choiceIndex, correct, draft })
      : { choiceIndex, correct, answeredAt: Number(draft.answeredAt) || now };
    if (!recordPracticeAnswer(p, index, record)) return { committed: records.length, complete: false, records };
    records.push({ index, choiceIndex, correct, answeredAt: Number(draft.answeredAt) || now, startedAt: Number(draft.startedAt) || now });
  }
  clearPracticeDraftAnswers(p);
  return { committed: records.length, complete: true, records };
}
