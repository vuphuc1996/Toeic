/**
 * Detect known legacy migration artifacts where a workspace snapshot predates
 * vocabulary releases and missing canonical records were incorrectly inferred
 * as user deletions. Each repair profile is exact: the legacy base count and
 * every release-addition ID must match before any user-hidden IDs are restored.
 */
export function detectLegacyReleaseAdditionRepair({
  deletedBaseIds = [], legacyRecords = [], baseWords = [],
  releaseAdditionIds = [], previousTotalWords = 0, currentTotalWords = 0,
  releaseRepairProfiles = []
} = {}) {
  if (!Array.isArray(legacyRecords) || !Array.isArray(baseWords) || !Array.isArray(releaseAdditionIds) || !Array.isArray(releaseRepairProfiles)) return [];
  if (!Number.isInteger(currentTotalWords) || currentTotalWords !== baseWords.length) return [];

  const profiles = releaseRepairProfiles.length
    ? releaseRepairProfiles
    : [{ previousTotalWords, releaseAdditionIds }];
  const baseById = new Map(baseWords.map(word => [String(word.id), word]));
  const baseByWord = new Map(baseWords.map(word => [String(word.word || '').trim().toLocaleLowerCase('en-US'), word]));
  const legacyBaseIds = new Set();
  for (const record of legacyRecords) {
    if (!record || typeof record !== 'object') continue;
    const match = baseById.get(String(record.id || '')) || baseByWord.get(String(record.word || '').trim().toLocaleLowerCase('en-US'));
    if (match) legacyBaseIds.add(String(match.id));
  }
  const deleted = new Set((Array.isArray(deletedBaseIds) ? deletedBaseIds : []).map(String));

  for (const profile of profiles) {
    const previous = profile?.previousTotalWords;
    const rawIds = profile?.releaseAdditionIds;
    if (!Number.isInteger(previous) || !Array.isArray(rawIds)) continue;
    if (legacyBaseIds.size !== previous || currentTotalWords - previous !== rawIds.length) continue;
    const additions = [...new Set(rawIds.map(String))];
    if (additions.length !== rawIds.length) continue;
    if (additions.every(id => baseById.has(id) && deleted.has(id) && !legacyBaseIds.has(id))) return additions;
  }
  return [];
}
