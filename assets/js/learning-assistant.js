// Shared, data-backed vocabulary completion helpers for the in-app learning assistant.
export function normalizeAssistantPrefix(value = '') {
  return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z]/g, '');
}

export function findAssistantVocabularyMatches(words, prefix, limit = 6) {
  const needle = normalizeAssistantPrefix(prefix);
  if (needle.length < 2 || !Array.isArray(words)) return [];
  const seen = new Set();
  return words
    .filter(item => {
      const word = String(item?.word || '').toLowerCase();
      if (!/^[a-z]+$/.test(word) || !word.startsWith(needle) || seen.has(word)) return false;
      seen.add(word);
      return true;
    })
    .sort((a, b) => String(a.word).localeCompare(String(b.word)))
    .slice(0, Math.max(1, Math.min(12, Number(limit) || 6)));
}

export function maskAssistantHeadword(word, prefix) {
  const target = String(word || '').toLowerCase();
  const known = normalizeAssistantPrefix(prefix);
  if (!target.startsWith(known)) return '';
  return `${target.slice(0, known.length)}${'•'.repeat(Math.max(0, target.length - known.length))}`;
}

export function validateAssistantWordCompletion(word, prefix, suffix) {
  const target = String(word || '').toLowerCase();
  const known = normalizeAssistantPrefix(prefix);
  const entered = String(suffix || '').toLowerCase();
  return /^[a-z]+$/.test(target) && /^[a-z]*$/.test(entered) && target.startsWith(known) && target.length > known.length && entered === target.slice(known.length);
}
