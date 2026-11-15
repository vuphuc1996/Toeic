/**
 * Detect the known legacy migration artifact where a 979-word workspace snapshot
 * caused the 13 v2.30.0 additions to be inferred as user-hidden base records.
 * Only those exact 13 IDs are restored, and only when the full fingerprint matches.
 */
export function detectLegacyReleaseAdditionRepair({
  deletedBaseIds = [], legacyRecords = [], baseWords = [],
  releaseAdditionIds = [], previousTotalWords = 0, currentTotalWords = 0
} = {}) {
  if (!Array.isArray(legacyRecords) || !Array.isArray(baseWords) || !Array.isArray(releaseAdditionIds)) return [];
  if (!Number.isInteger(previousTotalWords) || !Number.isInteger(currentTotalWords)) return [];
  if (currentTotalWords !== baseWords.length || currentTotalWords - previousTotalWords !== releaseAdditionIds.length) return [];
  const baseById = new Map(baseWords.map(word => [String(word.id), word]));
  const baseByWord = new Map(baseWords.map(word => [String(word.word || '').trim().toLocaleLowerCase('en-US'), word]));
  const legacyBaseIds = new Set();
  for (const record of legacyRecords) {
    if (!record || typeof record !== 'object') continue;
    const match = baseById.get(String(record.id || '')) || baseByWord.get(String(record.word || '').trim().toLocaleLowerCase('en-US'));
    if (match) legacyBaseIds.add(String(match.id));
  }
  if (legacyBaseIds.size !== previousTotalWords) return [];
  const deleted = new Set((Array.isArray(deletedBaseIds) ? deletedBaseIds : []).map(String));
  const additions = [...new Set(releaseAdditionIds.map(String))];
  if (additions.length !== releaseAdditionIds.length) return [];
  if (!additions.every(id => baseById.has(id) && deleted.has(id) && !legacyBaseIds.has(id))) return [];
  return additions;
}
