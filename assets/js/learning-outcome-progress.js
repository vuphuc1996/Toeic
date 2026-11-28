/**
 * Outcome evidence ledger. This is deliberately separate from content inventory
 * and from the existing per-resource answer history. It stores the latest
 * result for each stable question identity and retains every attempt.
 * A threshold result is a practice signal, not CEFR/ETS certification or proof
 * that every rubric-based outcome has been mastered.
 */
export function buildObjectiveResourceIndex(resourceMap = {}) {
  const index = {};
  const objectives = Array.isArray(resourceMap?.objectives) ? resourceMap.objectives : [];
  for (const objective of objectives) {
    if (!objective || typeof objective !== 'object' || typeof objective.id !== 'string' || !objective.id.trim()) continue;
    const resourceIds = Array.isArray(objective.resourceIds) ? objective.resourceIds : [];
    for (const resourceId of resourceIds) {
      if (typeof resourceId !== 'string' || !resourceId.trim()) continue;
      if (!index[resourceId]) index[resourceId] = [];
      if (!index[resourceId].includes(objective.id)) index[resourceId].push(objective.id);
    }
  }
  return index;
}

export function buildObjectiveCriterionIndex(criterionMap = {}) {
  const index = {};
  const mappings = Array.isArray(criterionMap?.mappings) ? criterionMap.mappings : [];
  for (const row of mappings) {
    if (!row || typeof row !== 'object' || typeof row.criterionId !== 'string' || !row.criterionId.trim()) continue;
    const keys = [row.questionKey, row.questionId].filter(value => typeof value === 'string' && value.trim());
    for (const key of keys) {
      if (!index[key]) index[key] = [];
      if (!index[key].includes(row.criterionId)) index[key].push(row.criterionId);
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

// Read-only consumers must never initialize or normalize learner data as a side effect.
// Keep this separate from ensureObjectiveProgress(), which is intentionally mutating
// and is used only by write operations.
function readObjectiveProgress(progress) {
  if (!progress || typeof progress !== 'object' || Array.isArray(progress)) return {};
  const objectives = progress.objectives;
  return objectives && typeof objectives === 'object' && !Array.isArray(objectives)
    ? objectives
    : {};
}

export function recordObjectiveAttempt(progress, objectiveIds, itemId, correct, answeredAt = Date.now(), durationMs = null) {
  const ledger = ensureObjectiveProgress(progress);
  if (!Array.isArray(objectiveIds) || !objectiveIds.length || typeof itemId !== 'string' || !itemId.trim()) return ledger;
  if (!Number.isFinite(answeredAt) || answeredAt < 0) return ledger;
  const safeObjectiveIds = [...new Set(objectiveIds.filter(id => typeof id === 'string' && id.trim()))];
  if (!safeObjectiveIds.length) return ledger;
  for (const objectiveId of safeObjectiveIds) {
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
  if (!Array.isArray(objectiveIds) || !objectiveIds.length || typeof itemId !== 'string' || !itemId.trim() || !Array.isArray(ratings) || ratings.length !== 3 || ratings.some(value => typeof value !== 'boolean') || !Number.isFinite(answeredAt) || answeredAt < 0) return ledger;
  const safeObjectiveIds = [...new Set(objectiveIds.filter(id => typeof id === 'string' && id.trim()))];
  if (!safeObjectiveIds.length) return ledger;
  for (const objectiveId of safeObjectiveIds) {
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


export function listDueRecallItems(progress, resourceMap = {}, now = Date.now(), limit = 100, outcomeRegistry = {}, criterionMap = {}) {
  const evaluationTime = typeof now === 'number' && Number.isFinite(now) ? now : Date.now();
  const parsedLimit = limit !== null && typeof limit !== 'boolean' && limit !== '' && Number.isFinite(Number(limit))
    ? Math.max(0, Math.floor(Number(limit)))
    : 100;
  const objectives = readObjectiveProgress(progress);
  const resourceObjectives = Array.isArray(resourceMap?.objectives) ? resourceMap.objectives : [];
  const objectiveById = new Map(resourceObjectives.filter(objective => objective && typeof objective === 'object' && typeof objective.id === 'string').map(objective => [objective.id, objective]));
  const criterionById = new Map();
  for (const group of (Array.isArray(outcomeRegistry?.objectives) ? outcomeRegistry.objectives : [])) {
    if (!group || String(group.objectiveId || '').startsWith('foundation-')) continue;
    const parent = objectiveById.get(group.objectiveId);
    for (const outcome of (Array.isArray(group.outcomes) ? group.outcomes : [])) {
      if (outcome?.id) criterionById.set(outcome.id, {
        id: outcome.id, title: outcome.title || outcome.id, kind: 'outcome_criterion',
        part: parent?.part || '', resourceIds: parent?.resourceIds || [], parentObjectiveId: group.objectiveId
      });
    }
  }
  const mappingByCriterionAndItem = new Map();
  const mappingsByGroup = new Map();
  for (const mapping of (Array.isArray(criterionMap?.mappings) ? criterionMap.mappings : [])) {
    if (!mapping || typeof mapping.criterionId !== 'string' || typeof mapping.questionKey !== 'string') continue;
    mappingByCriterionAndItem.set(`${mapping.criterionId}::${mapping.questionKey}`, mapping);
    if (!mappingsByGroup.has(mapping.objectiveId)) mappingsByGroup.set(mapping.objectiveId, []);
    mappingsByGroup.get(mapping.objectiveId).push(mapping);
  }
  const due = [];
  const criterionQuestionIndex = new Map();
  for (const [objectiveId, objectiveState] of Object.entries(objectives)) {
    const criterion = criterionById.get(objectiveId);
    const objective = objectiveById.get(objectiveId) || criterion;
    if (!objective || !objectiveState || typeof objectiveState !== 'object' || Array.isArray(objectiveState)) continue;
    const itemRecords = objectiveState.items && typeof objectiveState.items === 'object' && !Array.isArray(objectiveState.items) ? objectiveState.items : {};
    for (const [itemId, item] of Object.entries(itemRecords)) {
      if (!item || typeof item !== 'object' || Array.isArray(item)) continue;
      const dueAt = Number(item?.recallDueAt) || 0;
      if (!dueAt || dueAt > evaluationTime) continue;
      const mapping = criterion ? mappingByCriterionAndItem.get(`${objectiveId}::${itemId}`) : null;
      if (!criterion) {
        // When a mapped criterion already owns the same question, show the
        // criterion-level recall card rather than a duplicate Part-level card.
        const candidates = mappingsByGroup.get(objectiveId) || [];
        const covered = candidates.some(candidate => {
          const byQuestionId = typeof candidate.questionId === 'string' && itemId === candidate.questionId;
          const byIndex = Number.isInteger(candidate.questionIndex)
            && itemId.startsWith(`${candidate.resourceId}::index:${candidate.questionIndex}::`);
          if (!byQuestionId && !byIndex) return false;
          const criterionItem = objectives[candidate.criterionId]?.items?.[candidate.questionKey];
          return criterionItem && typeof criterionItem === 'object';
        });
        if (covered) continue;
      }
      if (criterion && mapping) {
        const key = `${mapping.resourceId}::${mapping.questionKey}`;
        const existing = criterionQuestionIndex.get(key);
        if (existing) {
          existing.relatedOutcomeIds.push(objectiveId);
          continue;
        }
      }
      const dueItem = {
        objectiveId, objectiveTitle: objective.title || objectiveId, kind: objective.kind || '',
        part: objective.part || '', itemId, dueAt, latestCorrect: item.latestCorrect === true,
        attempts: Array.isArray(item.attempts) ? item.attempts.length : 0,
        recallChecks: Array.isArray(item.recallChecks) ? item.recallChecks.length : 0,
        resourceIds: Array.isArray(objective.resourceIds) ? objective.resourceIds.slice() : [],
        ...(criterion ? { isOutcomeCriterion: true, parentObjectiveId: criterion.parentObjectiveId } : {}),
        ...(mapping ? { mappedResourceId: mapping.resourceId, mappedQuestionId: mapping.questionId || '', questionKey: mapping.questionKey, relatedOutcomeIds: [objectiveId] } : {})
      };
      due.push(dueItem);
      if (criterion && mapping) criterionQuestionIndex.set(`${mapping.resourceId}::${mapping.questionKey}`, dueItem);
    }
  }
  return due.sort((a, b) => a.dueAt - b.dueAt || a.objectiveTitle.localeCompare(b.objectiveTitle) || a.itemId.localeCompare(b.itemId)).slice(0, parsedLimit);
}

export function summarizeObjectiveProgress(progress, objectiveId, policy = {}, now = Date.now()) {
  const safePolicy = policy && typeof policy === 'object' && !Array.isArray(policy) ? policy : {};
  const objectives = readObjectiveProgress(progress);
  const objective = objectives[objectiveId];
  const itemRecords = objective?.items && typeof objective.items === 'object' && !Array.isArray(objective.items) ? objective.items : {};
  const items = Object.values(itemRecords).filter(item => item && typeof item === 'object' && !Array.isArray(item));
  const uniqueItems = items.length;
  const correct = items.filter(item => item.latestCorrect === true).length;
  const rawThreshold = safePolicy.defaultThreshold;
  const threshold = typeof rawThreshold === 'number' && Number.isFinite(rawThreshold) && rawThreshold > 0 && rawThreshold <= 1 ? rawThreshold : 0.8;
  const rawMinimum = safePolicy.minimumUniqueItems;
  const minimumUniqueItems = typeof rawMinimum === 'number' && Number.isFinite(rawMinimum) && rawMinimum >= 1 ? Math.floor(rawMinimum) : 10;
  const accuracy = uniqueItems ? correct / uniqueItems : null;
  // First-attempt performance is reported independently from the latest-attempt
  // view. It uses only explicit attempt history; legacy/malformed records with
  // no attempts are excluded rather than treating the latest result as a first try.
  const firstAttemptItems = items.filter(item => Array.isArray(item.attempts) && item.attempts.length > 0
    && item.attempts[0] && typeof item.attempts[0] === 'object'
    && typeof item.attempts[0].correct === 'boolean');
  const firstAttemptCorrect = firstAttemptItems.filter(item => item.attempts[0].correct === true).length;
  const firstAttemptAccuracy = firstAttemptItems.length ? firstAttemptCorrect / firstAttemptItems.length : null;
  const timedAttempts = items.flatMap(item => (Array.isArray(item.attempts) ? item.attempts : []).filter(attempt => attempt && typeof attempt === 'object' && Number.isFinite(attempt.durationMs) && attempt.durationMs >= 0));
  const averageResponseTimeMs = timedAttempts.length ? Math.round(timedAttempts.reduce((sum, attempt) => sum + attempt.durationMs, 0) / timedAttempts.length) : null;
  const rubricRecords = objective?.explanationRubrics && typeof objective.explanationRubrics === 'object' && !Array.isArray(objective.explanationRubrics) ? objective.explanationRubrics : {};
  const explanationRubrics = Object.values(rubricRecords).filter(item => item && typeof item === 'object' && !Array.isArray(item));
  const explanationScores = explanationRubrics.map(item => Number(item.latestScore)).filter(score => Number.isFinite(score) && score >= 0 && score <= 3);
  const recallChecks = items.flatMap(item => Array.isArray(item.recallChecks) ? item.recallChecks.filter(check => check && typeof check === 'object') : []);
  const recallCorrect = recallChecks.filter(check => check.correct === true).length;
  const evaluationTime = typeof now === 'number' && Number.isFinite(now) ? now : Date.now();
  const dueRecallItems = items.filter(item => Number(item.recallDueAt) > 0 && Number(item.recallDueAt) <= evaluationTime).length;
  const eligible = uniqueItems >= minimumUniqueItems;
  return {
    objectiveId,
    uniqueItems,
    correct,
    accuracy,
    accuracyPercent: accuracy === null ? null : Math.round(accuracy * 100),
    firstAttemptItems: firstAttemptItems.length,
    firstAttemptCorrect: firstAttemptCorrect,
    firstAttemptAccuracy: firstAttemptAccuracy,
    firstAttemptAccuracyPercent: firstAttemptAccuracy === null ? null : Math.round(firstAttemptAccuracy * 100),
    evidenceCoveragePercent: Math.min(100, Math.round((uniqueItems / minimumUniqueItems) * 100)),
    threshold,
    minimumUniqueItems,
    eligible,
    status: !eligible ? 'insufficient_evidence' : accuracy >= threshold ? 'practice_threshold_met' : 'in_progress',
    totalAttempts: items.reduce((sum, item) => sum + (Array.isArray(item.attempts) ? item.attempts.filter(attempt => attempt && typeof attempt === 'object').length : 0), 0),
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

export function summarizeAllObjectives(progress, resourceMap = {}, policy = {}, now = Date.now()) {
  const resourceObjectives = Array.isArray(resourceMap?.objectives) ? resourceMap.objectives.filter(objective => objective && typeof objective === 'object' && typeof objective.id === 'string') : [];
  return resourceObjectives.map(objective => {
    const summary = summarizeObjectiveProgress(progress, objective.id, policy, now);
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

/**
 * Summarize evidence against the 33 stable learning-outcome criteria.
 * All reads are non-mutating. Mapping counts describe available inventory,
 * while observed counts come only from this learner's own completed attempts.
 */
export function summarizeOutcomeCriteria(progress, registry = {}, resourceMap = {}, criterionMap = {}, now = Date.now()) {
  const outcomes = Array.isArray(registry?.objectives) ? registry.objectives : [];
  const objectives = Array.isArray(resourceMap?.objectives) ? resourceMap.objectives : [];
  const objectiveById = new Map(objectives.filter(row => row && typeof row.id === 'string').map(row => [row.id, row]));
  const mappings = Array.isArray(criterionMap?.mappings) ? criterionMap.mappings : [];
  const measuredCounts = {};
  for (const row of mappings) {
    if (row && typeof row.criterionId === 'string') measuredCounts[row.criterionId] = (measuredCounts[row.criterionId] || 0) + 1;
  }
  const declaredCounts = criterionMap?.mappingCountsByCriterion && typeof criterionMap.mappingCountsByCriterion === 'object'
    ? criterionMap.mappingCountsByCriterion
    : measuredCounts;
  const ledger = readObjectiveProgress(progress);
  const rows = [];
  for (const group of outcomes) {
    // Foundation evidence is intentionally maintained by foundation-evidence.js,
    // foundation-reading-evidence.js and foundation-listening-evidence.js.
    // This summary is limited to the 27 TOEIC criteria in objectiveProgress.
    if (String(group?.objectiveId || '').startsWith('foundation-')) continue;
    const parent = objectiveById.get(group?.objectiveId);
    const reviewState = String(parent?.reviewState || '');
    const reviewPending = reviewState.includes('pending_independent_review') || reviewState.includes('requires_second_review');
    for (const outcome of Array.isArray(group?.outcomes) ? group.outcomes : []) {
      const criterionId = outcome?.id;
      if (typeof criterionId !== 'string' || !criterionId) continue;
      const state = ledger[criterionId];
      const itemRecords = state?.items && typeof state.items === 'object' && !Array.isArray(state.items) ? state.items : {};
      const items = Object.values(itemRecords).filter(item => item && typeof item === 'object' && !Array.isArray(item));
      const rawMetric = outcome.evidenceMetric;
      let observedItemCount = 0;
      let observedCorrectCount = 0;
      let observedPercent = null;
      let timeTargetMs = Number.isFinite(outcome.timeTargetMs) && outcome.timeTargetMs > 0 ? outcome.timeTargetMs : null;

      if (rawMetric === 'correct_rate') {
        observedItemCount = items.length;
        observedCorrectCount = items.filter(item => item.latestCorrect === true).length;
        observedPercent = observedItemCount ? Math.round(observedCorrectCount / observedItemCount * 100) : null;
      } else if (rawMetric === 'delayed_correct_rate') {
        const recalls = items.map(item => {
          const checks = Array.isArray(item.recallChecks) ? item.recallChecks.filter(check => check && typeof check === 'object' && typeof check.correct === 'boolean') : [];
          return checks.length ? checks[checks.length - 1] : null;
        }).filter(Boolean);
        observedItemCount = recalls.length;
        observedCorrectCount = recalls.filter(check => check.correct === true).length;
        observedPercent = observedItemCount ? Math.round(observedCorrectCount / observedItemCount * 100) : null;
      } else if (rawMetric === 'timed_accuracy') {
        if (!timeTargetMs) timeTargetMs = 30000;
        const latestTimed = items.map(item => {
          const attempts = Array.isArray(item.attempts) ? item.attempts.filter(attempt => attempt && typeof attempt === 'object') : [];
          const latest = attempts.length ? attempts[attempts.length - 1] : null;
          return latest && Number.isFinite(latest.durationMs) && latest.durationMs >= 0 ? latest : null;
        }).filter(Boolean);
        observedItemCount = latestTimed.length;
        observedCorrectCount = latestTimed.filter(attempt => attempt.correct === true && attempt.durationMs <= timeTargetMs).length;
        observedPercent = observedItemCount ? Math.round(observedCorrectCount / observedItemCount * 100) : null;
      } else if (rawMetric === 'explanation_rubric') {
        const rubrics = state?.explanationRubrics && typeof state.explanationRubrics === 'object' && !Array.isArray(state.explanationRubrics)
          ? Object.values(state.explanationRubrics).filter(item => item && typeof item === 'object' && !Array.isArray(item))
          : [];
        const scores = rubrics.map(item => Number(item.latestScore)).filter(score => Number.isFinite(score) && score >= 0 && score <= 3);
        observedItemCount = scores.length;
        observedCorrectCount = scores.filter(score => score >= 2.4).length;
        observedPercent = observedItemCount ? Math.round(scores.reduce((sum, score) => sum + score / 3 * 100, 0) / observedItemCount) : null;
      }

      const minimumUniqueItems = Number.isInteger(outcome.minimumUniqueItems) && outcome.minimumUniqueItems > 0 ? outcome.minimumUniqueItems : 10;
      const threshold = typeof outcome.masteryThreshold === 'number' && Number.isFinite(outcome.masteryThreshold) && outcome.masteryThreshold > 0 && outcome.masteryThreshold <= 1
        ? outcome.masteryThreshold
        : 0.8;
      const mappingCount = Number.isInteger(declaredCounts[criterionId]) ? declaredCounts[criterionId] : measuredCounts[criterionId] || 0;
      let status = 'not_instrumented';
      if (reviewPending) status = 'content_review_pending';
      else if (outcome.status === 'criteria_defined_not_yet_instrumented' || mappingCount < 1) status = 'not_instrumented';
      else if (observedItemCount < minimumUniqueItems) status = 'insufficient_evidence';
      else status = observedPercent !== null && observedPercent / 100 >= threshold ? 'practice_threshold_met' : 'in_progress';

      rows.push({
        objectiveId: group.objectiveId,
        objectiveTitle: parent?.title || group.objectiveId,
        objectiveKind: parent?.kind || '',
        outcomeId: criterionId,
        title: outcome.title || criterionId,
        evidenceMetric: rawMetric,
        mappingCount,
        observedItemCount,
        observedCorrectCount,
        observedPercent,
        minimumUniqueItems,
        evidenceCoveragePercent: Math.min(100, Math.round(observedItemCount / minimumUniqueItems * 100)),
        threshold,
        timeTargetMs,
        reviewState,
        status,
        runtimeStatusNote: outcome.runtimeStatusNote || ''
      });
    }
  }
  return rows;
}

/**
 * Read-only integrity audit for the learner-local objective evidence ledger.
 * It reports malformed or orphaned records but never repairs, deletes, or
 * rewrites learner data. Callers may safely run it before displaying evidence.
 */
export function auditObjectiveProgress(progress, resourceMap = {}, outcomeRegistry = {}) {
  const issues = [];
  const add = (code, path, severity = 'warning') => issues.push({ code, path, severity });
  if (!progress || typeof progress !== 'object' || Array.isArray(progress)) {
    add('invalid_ledger', '$', 'error');
    return { valid: false, issueCount: issues.length, errorCount: 1, warningCount: 0, objectiveCount: 0, itemCount: 0, attemptCount: 0, issues };
  }
  if (progress.schemaVersion !== undefined && (!Number.isInteger(progress.schemaVersion) || progress.schemaVersion < 1)) {
    add('invalid_schema_version', 'schemaVersion', 'error');
  }
  if (!progress.objectives || typeof progress.objectives !== 'object' || Array.isArray(progress.objectives)) {
    add('invalid_objectives_container', 'objectives', 'error');
    return { valid: false, issueCount: issues.length, errorCount: issues.filter(x => x.severity === 'error').length, warningCount: 0, objectiveCount: 0, itemCount: 0, attemptCount: 0, issues };
  }

  const resourceObjectives = Array.isArray(resourceMap?.objectives) ? resourceMap.objectives : [];
  const knownObjectiveIds = new Set(resourceObjectives.filter(objective => objective && typeof objective === 'object' && typeof objective.id === 'string').map(objective => objective.id));
  const knownOutcomeIds = new Set((Array.isArray(outcomeRegistry?.objectives) ? outcomeRegistry.objectives : [])
    .flatMap(group => Array.isArray(group?.outcomes) ? group.outcomes.map(outcome => outcome?.id).filter(id => typeof id === 'string') : []));
  let itemCount = 0;
  let attemptCount = 0;
  for (const [objectiveId, objective] of Object.entries(progress.objectives)) {
    const objectivePath = `objectives.${objectiveId}`;
    if (!knownObjectiveIds.has(objectiveId) && !knownOutcomeIds.has(objectiveId)) add('orphan_objective', objectivePath);
    if (!objective || typeof objective !== 'object' || Array.isArray(objective)) {
      add('invalid_objective_record', objectivePath, 'error');
      continue;
    }
    if (!objective.items || typeof objective.items !== 'object' || Array.isArray(objective.items)) {
      add('invalid_items_container', `${objectivePath}.items`, 'error');
      continue;
    }
    for (const [itemId, item] of Object.entries(objective.items)) {
      itemCount += 1;
      const itemPath = `${objectivePath}.items.${itemId}`;
      if (!item || typeof item !== 'object' || Array.isArray(item)) {
        add('invalid_item_record', itemPath, 'error');
        continue;
      }
      if (typeof item.latestCorrect !== 'boolean') add('invalid_latest_correct', `${itemPath}.latestCorrect`, 'error');
      if (!Number.isFinite(item.latestAnsweredAt) || item.latestAnsweredAt < 0) add('invalid_latest_answered_at', `${itemPath}.latestAnsweredAt`, 'error');
      if (item.recallDueAt !== undefined && (!Number.isFinite(item.recallDueAt) || item.recallDueAt < 0)) add('invalid_recall_due_at', `${itemPath}.recallDueAt`, 'warning');
      if (!Array.isArray(item.attempts)) {
        add('invalid_attempts_container', `${itemPath}.attempts`, 'error');
      } else {
        item.attempts.forEach((attempt, index) => {
          attemptCount += 1;
          const attemptPath = `${itemPath}.attempts.${index}`;
          if (!attempt || typeof attempt !== 'object' || typeof attempt.correct !== 'boolean' || !Number.isFinite(attempt.answeredAt) || attempt.answeredAt < 0) add('invalid_attempt', attemptPath, 'error');
          if (attempt?.durationMs !== undefined && (!Number.isFinite(attempt.durationMs) || attempt.durationMs < 0)) add('invalid_attempt_duration', `${attemptPath}.durationMs`, 'warning');
        });
      }
      if (item.recallChecks !== undefined && !Array.isArray(item.recallChecks)) add('invalid_recall_checks_container', `${itemPath}.recallChecks`, 'error');
      else (item.recallChecks || []).forEach((check, index) => {
        if (!check || typeof check !== 'object' || typeof check.correct !== 'boolean' || !Number.isFinite(check.answeredAt) || check.answeredAt < 0 || !Number.isFinite(check.dueAt) || check.dueAt < 0) add('invalid_recall_check', `${itemPath}.recallChecks.${index}`, 'error');
      });
      if (Array.isArray(item.attempts) && item.attempts.length) {
        const latestAttempt = item.attempts[item.attempts.length - 1];
        if (latestAttempt && typeof latestAttempt === 'object' && (latestAttempt.correct !== item.latestCorrect || latestAttempt.answeredAt !== item.latestAnsweredAt)) {
          add('latest_attempt_mismatch', itemPath, 'warning');
        }
      }
    }
    if (objective.explanationRubrics !== undefined && (!objective.explanationRubrics || typeof objective.explanationRubrics !== 'object' || Array.isArray(objective.explanationRubrics))) {
      add('invalid_explanation_rubrics_container', `${objectivePath}.explanationRubrics`, 'error');
    } else for (const [rubricId, rubric] of Object.entries(objective.explanationRubrics || {})) {
      const rubricPath = `${objectivePath}.explanationRubrics.${rubricId}`;
      if (!rubric || typeof rubric !== 'object' || !Array.isArray(rubric.latestRatings) || rubric.latestRatings.length !== 3 || rubric.latestRatings.some(value => typeof value !== 'boolean')) {
        add('invalid_rubric_latest_ratings', `${rubricPath}.latestRatings`, 'error');
      }
      if (rubric?.attempts !== undefined && !Array.isArray(rubric.attempts)) add('invalid_rubric_attempts_container', `${rubricPath}.attempts`, 'error');
      else (rubric?.attempts || []).forEach((attempt, index) => {
        if (!attempt || typeof attempt !== 'object' || !Array.isArray(attempt.ratings) || attempt.ratings.length !== 3 || attempt.ratings.some(value => typeof value !== 'boolean') || !Number.isFinite(attempt.answeredAt) || attempt.answeredAt < 0) add('invalid_rubric_attempt', `${rubricPath}.attempts.${index}`, 'error');
      });
    }
  }
  const errorCount = issues.filter(issue => issue.severity === 'error').length;
  const warningCount = issues.length - errorCount;
  return { valid: errorCount === 0, issueCount: issues.length, errorCount, warningCount, objectiveCount: Object.keys(progress.objectives).length, itemCount, attemptCount, issues };
}
