/**
 * Evidence-only TOEIC L&R readiness summary.
 * Listening trend is gated on distinct question-ID forms, not attempt count alone.
 * Raw accuracy is never converted into an ETS scaled score.
 */
function listeningIds(row) {
  return [...new Set((Array.isArray(row?.questionIds) ? row.questionIds : [])
    .filter(id => typeof id === 'string' && id.startsWith('listening:')))].sort();
}
function formKey(ids) { return ids.length ? ids.join('\u001f') : ''; }
function overlapPercent(a, b) {
  if (!a.length || !b.length) return null;
  const right = new Set(b);
  const shared = a.reduce((count, id) => count + Number(right.has(id)), 0);
  return Math.round(shared / Math.min(a.length, b.length) * 100);
}

function strictFiniteNumber(value) {
  if (typeof value === 'number') return Number.isFinite(value) ? value : null;
  if (typeof value === 'string' && value.trim() !== '') {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  }
  return null;
}

export function buildMockScoreReadiness(history = []) {
  const validRows = (Array.isArray(history) ? history : [])
    .filter(row => {
      if (!row || typeof row !== 'object' || row.status !== 'completed' || row.modeId !== 'full') return false;
      const questions = strictFiniteNumber(row.questions);
      const listening = strictFiniteNumber(row.listeningAccuracy);
      const reading = strictFiniteNumber(row.readingAccuracy);
      const completedAt = strictFiniteNumber(row.completedAt);
      return questions === 200
        && listening !== null && listening >= 0 && listening <= 100
        && reading !== null && reading >= 0 && reading <= 100
        && completedAt !== null && completedAt >= 0;
    });
  const byAttemptId = new Map();
  const anonymousRows = [];
  for (const row of validRows) {
    const attemptId = typeof row.attemptId === 'string' ? row.attemptId.trim() : '';
    if (!attemptId) {
      anonymousRows.push(row);
      continue;
    }
    const prev = byAttemptId.get(attemptId);
    if (!prev || Number(row.completedAt) >= Number(prev.completedAt)) {
      byAttemptId.set(attemptId, row);
    }
  }
  const completed = [...anonymousRows, ...byAttemptId.values()]
    .sort((a, b) => Number(a.completedAt) - Number(b.completedAt));
  const recent = completed.slice(-3);
  const base = {
    count: completed.length, required: 3, enough: recent.length >= 3, recent,
    listeningAverage: null, readingAverage: null,
    listeningChange: null, readingChange: null,
    listeningTrendEnough: false, listeningDistinctForms: 0,
    listeningDistinctQuestionCount: 0, listeningOverlapPercent: null,
    listeningWarning: 'Chưa có đủ dữ liệu định danh câu hỏi Listening để xác nhận hai bộ đề khác nhau.'
  };
  if (!recent.length) return base;

  const average = key => Math.round(recent.reduce((sum, row) => sum + Number(row[key]), 0) / recent.length);
  const forms = recent.map(row => ({ row, ids: listeningIds(row) })).filter(form => form.ids.length);
  const distinct = new Map();
  // Keep the latest attempt for each exact Listening form.
  for (const form of forms) distinct.set(formKey(form.ids), form);
  const distinctForms = [...distinct.values()].sort((a, b) => Number(a.row.completedAt) - Number(b.row.completedAt));
  const distinctAttempts = distinctForms.map(form => form.row);
  const union = new Set(distinctForms.flatMap(form => form.ids));
  const overlap = distinctForms.length >= 2
    ? overlapPercent(distinctForms[distinctForms.length - 2].ids, distinctForms[distinctForms.length - 1].ids)
    : null;
  const listeningTrendEnough = distinctAttempts.length >= 2;
  const listeningAverage = listeningTrendEnough
    ? Math.round(distinctAttempts.reduce((sum, row) => sum + Number(row.listeningAccuracy), 0) / distinctAttempts.length)
    : null;
  const firstDistinct = distinctAttempts[0], lastDistinct = distinctAttempts[distinctAttempts.length - 1];

  return {
    ...base,
    listeningAverage,
    readingAverage: average('readingAccuracy'),
    listeningChange: listeningTrendEnough ? Math.round(Number(lastDistinct.listeningAccuracy) - Number(firstDistinct.listeningAccuracy)) : null,
    readingChange: recent.length >= 2 ? Math.round(Number(recent[recent.length - 1].readingAccuracy) - Number(recent[0].readingAccuracy)) : null,
    listeningTrendEnough,
    listeningDistinctForms: distinctForms.length,
    listeningDistinctQuestionCount: union.size,
    listeningOverlapPercent: overlap,
    listeningWarning: !listeningTrendEnough
      ? 'Tạm ẩn xu hướng Listening: cần ít nhất hai bộ câu hỏi Listening khác nhau; số lượt thi không thay thế được số bộ đề độc lập.'
      : overlap !== null && overlap >= 90
        ? `Hai bộ Listening gần nhất trùng ${overlap}% câu hỏi. Xu hướng chỉ mang tính tham khảo, chưa đại diện cho hai lần đo độc lập.`
        : ''
  };
}
