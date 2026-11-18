/**
 * Evidence-only TOEIC L&R readiness summary.
 * It reports repeated full-mock practice accuracy, never converts raw accuracy
 * into an ETS scaled score or claims a guaranteed 500+/850+ result.
 */
export function buildMockScoreReadiness(history = []) {
  const completed = (Array.isArray(history) ? history : [])
    .filter(row => row && row.status === 'completed' && row.modeId === 'full'
      && Number(row.questions) === 200
      && Number.isFinite(Number(row.listeningAccuracy))
      && Number.isFinite(Number(row.readingAccuracy))
      && Number.isFinite(Number(row.completedAt)))
    .sort((a, b) => Number(a.completedAt) - Number(b.completedAt));
  const recent = completed.slice(-3);
  if (!recent.length) return { count: 0, required: 3, enough: false, recent: [], listeningAverage: null, readingAverage: null, listeningChange: null, readingChange: null };
  const average = key => Math.round(recent.reduce((sum, row) => sum + Number(row[key]), 0) / recent.length);
  const first = recent[0], last = recent[recent.length - 1];
  return {
    count: completed.length,
    required: 3,
    enough: recent.length >= 3,
    recent,
    listeningAverage: average('listeningAccuracy'),
    readingAverage: average('readingAccuracy'),
    listeningChange: recent.length >= 2 ? Math.round(Number(last.listeningAccuracy) - Number(first.listeningAccuracy)) : null,
    readingChange: recent.length >= 2 ? Math.round(Number(last.readingAccuracy) - Number(first.readingAccuracy)) : null
  };
}
