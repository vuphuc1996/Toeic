/**
 * Display-safety checks for related-glossary metadata.
 *
 * Placeholder definitions are editorial workflow markers, not learner-facing
 * English meanings. Keep this deliberately narrow: a false positive hides a
 * real definition, so only the known placeholder families are suppressed.
 */
const PLACEHOLDER_PATTERNS = [
  /^reference gloss for\b/i,
  /^(?:tbd|todo|placeholder|definition pending|unknown|n\/?a|not available|no definition)\.?$/i,
  /^(?:generic|temporary|sample) definition\b/i,
];

export function isPlaceholderRelatedGlossaryDefinition(value) {
  const definition = typeof value === 'string' ? value.trim() : '';
  return Boolean(definition && PLACEHOLDER_PATTERNS.some(pattern => pattern.test(definition)));
}

export function getLearnerFacingRelatedGlossaryDefinition(value) {
  const definition = typeof value === 'string' ? value.trim() : '';
  return definition && !isPlaceholderRelatedGlossaryDefinition(definition) ? definition : '';
}
