/**
 * Outcome evidence ledger. This is deliberately separate from content inventory
 * and from the existing per-resource answer history. It stores the latest
 * result for each stable question identity and retains every attempt.
 * A threshold result is a practice signal, not CEFR/ETS certification or proof
 * that every rubric-based outcome has been mastered.
 */
export function buildObjectiveResourceIndex(resourceMap = {}) {
  const index = {};
  for (const objective of resourceMap.objectives || []) {
    for (const resourceId of objective.resourceIds || []) {
      if (!index[resourceId]) index[resourceId] = [];
      index[resourceId].push(objective.id);
    }
  }
  return index;
}

export function ensureObjectiveProgress(progress = {}) {
  if (!progress || typeof progress !== 'object' || Array.isArray(progress)) progress = {};
  if (!progress.schemaVersion) progress.schemaVersion = 1;
  if (!progress.objectives || typeof progress.objectives !== 'object' || Array.isArray(progress.objectives)) progress.objectives = {};
  return progress;
}

export function recordObjectiveAttempt(progress, objectiveIds, itemId, correct, answeredAt = Date.now(), durationMs = null) {
  const ledger = ensureObjectiveProgress(progress);
  if (!Array.isArray(objectiveIds) || !objectiveIds.length || !itemId) return ledger;
  for (const objectiveId of objectiveIds) {
    if (!ledger.objectives[objectiveId]) ledger.objectives[objectiveId] = { items: {} };
    const objective = ledger.objectives[objectiveId];
    if (!objective.items || typeof objective.items !== 'object') objective.items = {};
    const prior = objective.items[itemId];
    const attempts = Array.isArray(prior?.attempts) ? prior.attempts : [];
    const priorRecall = Array.isArray(prior?.recallChecks) ? prior.recallChecks : [];
    const recallDueAt = Number(prior?.recallDueAt) || 0;
    const isRecallCheck = Boolean(prior && recallDueAt && answeredAt >= recallDueAt);
    attempts.push({ correct: Boolean(correct), answeredAt, ...(Number.isFinite(durationMs) && durationMs >= 0 ? { durationMs } : {}) });
    const recallChecks = priorRecall.slice();
    let nextRecallDueAt = Number(prior?.recallDueAt) || (answeredAt + 24 * 60 * 60 * 1000);
    if (isRecallCheck) {
      recallChecks.push({ correct: Boolean(correct), answeredAt, dueAt: recallDueAt });
      nextRecallDueAt = answeredAt + (correct ? 3 : 1) * 24 * 60 * 60 * 1000;
    }
    objective.items[itemId] = {
      latestCorrect: Boolean(correct),
      latestAnsweredAt: answeredAt,
      attempts,
      recallDueAt: nextRecallDueAt,
      recallChecks
    };
  }
  return ledger;
}

export function recordExplanationRubric(progress, objectiveIds, itemId, ratings, answeredAt = Date.now()) {
  const ledger = ensureObjectiveProgress(progress);
  if (!Array.isArray(objectiveIds) || !objectiveIds.length || !itemId || !Array.isArray(ratings) || ratings.length !== 3 || ratings.some(value => typeof value !== 'boolean')) return ledger;
  for (const objectiveId of objectiveIds) {
    if (!ledger.objectives[objectiveId]) ledger.objectives[objectiveId] = { items: {} };
    const objective = ledger.objectives[objectiveId];
    if (!objective.explanationRubrics || typeof objective.explanationRubrics !== 'object') objective.explanationRubrics = {};
    const prior = objective.explanationRubrics[itemId];
    const attempts = Array.isArray(prior?.attempts) ? prior.attempts : [];
    const score = ratings.filter(Boolean).length;
    attempts.push({ ratings: ratings.slice(), score, maxScore: 3, answeredAt, assessmentType: 'learner_self_report' });
    objective.explanationRubrics[itemId] = { latestScore: score, latestRatings: ratings.slice(), latestAnsweredAt: answeredAt, attempts };
  }
  return ledger;
}


export function listDueRecallItems(progress, resourceMap = {}, now = Date.now(), limit = 100) {
  const ledger = ensureObjectiveProgress(progress);
  const objectiveById = new Map((resourceMap.objectives || []).map(objective => [objective.id, objective]));
  const due = [];
  for (const [objectiveId, objectiveState] of Object.entries(ledger.objectives || {})) {
    const objective = objectiveById.get(objectiveId);
    if (!objective) continue;
    for (const [itemId, item] of Object.entries(objectiveState.items || {})) {
      const dueAt = Number(item?.recallDueAt) || 0;
      if (!dueAt || dueAt > now) continue;
      due.push({
        objectiveId, objectiveTitle: objective.title || objectiveId, kind: objective.kind || '',
        part: objective.part || '', itemId, dueAt, latestCorrect: item.latestCorrect === true,
        attempts: Array.isArray(item.attempts) ? item.attempts.length : 0,
        recallChecks: Array.isArray(item.recallChecks) ? item.recallChecks.length : 0,
        resourceIds: Array.isArray(objective.resourceIds) ? objective.resourceIds.slice() : []
      });
    }
  }
  return due.sort((a, b) => a.dueAt - b.dueAt || a.objectiveTitle.localeCompare(b.objectiveTitle) || a.itemId.localeCompare(b.itemId)).slice(0, Math.max(0, Number(limit) || 0));
}

export function summarizeObjectiveProgress(progress, objectiveId, policy = {}) {
  const ledger = ensureObjectiveProgress(progress);
  const objective = ledger.objectives[objectiveId];
  const items = Object.values(objective?.items || {});
  const uniqueItems = items.length;
  const correct = items.filter(item => item.latestCorrect === true).length;
  const threshold = Number(policy.defaultThreshold) > 0 ? Number(policy.defaultThreshold) : 0.8;
  const minimumUniqueItems = Number(policy.minimumUniqueItems) > 0 ? Number(policy.minimumUniqueItems) : 10;
  const accuracy = uniqueItems ? correct / uniqueItems : null;
  const timedAttempts = items.flatMap(item => (item.attempts || []).filter(attempt => Number.isFinite(attempt.durationMs) && attempt.durationMs >= 0));
  const averageResponseTimeMs = timedAttempts.length ? Math.round(timedAttempts.reduce((sum, attempt) => sum + attempt.durationMs, 0) / timedAttempts.length) : null;
  const explanationRubrics = Object.values(objective?.explanationRubrics || {});
  const explanationScores = explanationRubrics.map(item => Number(item.latestScore)).filter(score => Number.isFinite(score) && score >= 0 && score <= 3);
  const recallChecks = items.flatMap(item => item.recallChecks || []);
  const recallCorrect = recallChecks.filter(check => check.correct === true).length;
  const dueRecallItems = items.filter(item => Number(item.recallDueAt) > 0 && Number(item.recallDueAt) <= Date.now()).length;
  const eligible = uniqueItems >= minimumUniqueItems;
  return {
    objectiveId,
    uniqueItems,
    correct,
    accuracy,
    accuracyPercent: accuracy === null ? null : Math.round(accuracy * 100),
    evidenceCoveragePercent: Math.min(100, Math.round((uniqueItems / minimumUniqueItems) * 100)),
    threshold,
    minimumUniqueItems,
    eligible,
    status: !eligible ? 'insufficient_evidence' : accuracy >= threshold ? 'practice_threshold_met' : 'in_progress',
    totalAttempts: items.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.length : 0), 0),
    timedAttempts: timedAttempts.length,
    averageResponseTimeMs,
    recallChecks: recallChecks.length,
    recallAccuracyPercent: recallChecks.length ? Math.round((recallCorrect / recallChecks.length) * 100) : null,
    dueRecallItems,
    explanationRubricItems: explanationScores.length,
    explanationRubricAverage: explanationScores.length ? Math.round((explanationScores.reduce((sum, score) => sum + score, 0) / explanationScores.length) * 100) / 100 : null,
    explanationRubricAttempts: explanationRubrics.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.length : 0), 0)
  };
}

export function summarizeAllObjectives(progress, resourceMap = {}, policy = {}) {
  return (resourceMap.objectives || []).map(objective => {
    const summary = summarizeObjectiveProgress(progress, objective.id, policy);
    const reviewState = objective.reviewState || '';
    const reviewPending = reviewState.includes('pending_independent_review') || reviewState.includes('requires_second_review');
    return {
      id: objective.id,
      title: objective.title,
      kind: objective.kind,
      part: objective.part || '',
      reviewState,
      ...summary,
      status: reviewPending ? 'content_review_pending' : summary.status
    };
  });
}
