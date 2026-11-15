const VALID_KINDS = new Set(['letterName', 'exampleWord']);

export function recordAlphabetSoundPractice(progress, letterId, kind, timestamp = Date.now()) {
  const id = String(letterId || '').trim().toUpperCase();
  if (!/^[A-Z]$/.test(id) || !VALID_KINDS.has(kind)) return progress && typeof progress === 'object' ? progress : { schemaVersion: 1, letters: {} };
  const current = progress && typeof progress === 'object' ? progress : {};
  const letters = current.letters && typeof current.letters === 'object' ? current.letters : {};
  const previous = letters[id] && typeof letters[id] === 'object' ? letters[id] : {};
  const old = previous[kind] && typeof previous[kind] === 'object' ? previous[kind] : {};
  return {
    schemaVersion: 1,
    letters: {
      ...letters,
      [id]: {
        ...previous,
        [kind]: {
          count: Math.max(0, Number(old.count) || 0) + 1,
          firstAt: Number(old.firstAt) || timestamp,
          lastAt: timestamp
        }
      }
    }
  };
}

export function summarizeAlphabetSoundProgress(progress, expectedLetters = 26) {
  const letters = progress && progress.letters && typeof progress.letters === 'object' ? progress.letters : {};
  const values = Object.values(letters);
  const practicedLetters = values.filter(item => Number(item?.letterName?.count) > 0 || Number(item?.exampleWord?.count) > 0).length;
  const completedPairs = values.filter(item => Number(item?.letterName?.count) > 0 && Number(item?.exampleWord?.count) > 0).length;
  const totalPlays = values.reduce((sum, item) => sum + Math.max(0, Number(item?.letterName?.count) || 0) + Math.max(0, Number(item?.exampleWord?.count) || 0), 0);
  return {
    expectedLetters: Math.max(0, Number(expectedLetters) || 0),
    practicedLetters: Math.min(practicedLetters, expectedLetters),
    completedPairs: Math.min(completedPairs, expectedLetters),
    totalPlays
  };
}
