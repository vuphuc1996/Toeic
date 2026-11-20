/** Render the non-primary senses and their linked examples on a Flashcard back. */
function escapeFlashcardHtml(value) {
  return String(value ?? '').replace(/[&<>"']/g, char => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
  })[char]);
}

/**
 * Build safe markup for senses after the primary sense.
 * Examples are shown only when their sense_index matches the additional sense.
 */
export function renderAdditionalFlashSenses(word, posDisplayLabel = value => String(value || 'Vocabulary')) {
  const senses = Array.isArray(word?.senses) ? word.senses.slice(1) : [];
  if (!senses.length) return '';

  const examples = Array.isArray(word?.examples) ? word.examples : [];
  const headword = escapeFlashcardHtml(word?.word || '');
  const rows = senses.map((sense, index) => {
    const example = examples.find(item => item && item.sense_index === index + 1);
    const pos = escapeFlashcardHtml(posDisplayLabel(sense?.pos));
    const meaning = escapeFlashcardHtml(sense?.meaning_vi || 'Chưa có nghĩa');
    const exampleMarkup = example
      ? `<p class="flash-additional-example">${escapeFlashcardHtml(example.en || '')}</p>${example.vi ? `<span class="flash-additional-example-vi">${escapeFlashcardHtml(example.vi)}</span>` : ''}`
      : '';
    return `<div class="flash-additional-sense"><span>Nghĩa ${index + 2} · ${pos}</span><strong>${meaning}</strong>${exampleMarkup}</div>`;
  }).join('');

  return `<section class="flash-additional-senses" aria-label="Các nghĩa khác của từ ${headword}"><small>OTHER MEANINGS · ${senses.length}</small>${rows}</section>`;
}
