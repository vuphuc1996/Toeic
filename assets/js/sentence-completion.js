const GRAMMAR_CATEGORIES = new Set([
  'Adjectives and Adverbs', 'Articles and Determiners', 'Conjunctions and Clauses',
  'Gerunds and Infinitives', 'Imperatives and Verb Forms', 'Infinitives and Verb Patterns',
  'Linking Verbs', 'Modal Verbs', 'Participles and Reduced Relative Clauses',
  'Passive Voice', 'Prepositions and Collocations', 'Subject–Verb Agreement',
  'Verb Tense and Aspect', 'Word Forms and Nouns'
]);

const normalize = value => String(value ?? '')
  .normalize('NFD')
  .replace(/[\u0300-\u036f]/g, '')
  .toLocaleLowerCase('en-US')
  .replace(/[’']/g, "'")
  .replace(/\s+/g, ' ')
  .trim();

function shuffledChoices(question, random = Math.random) {
  const indexed = question.choices.map((choice, index) => ({
    choice,
    explanation: question.optionExplanations[index],
    isCorrect: index === question.answerIndex
  }));
  for (let index = indexed.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(random() * (index + 1));
    [indexed[index], indexed[swapIndex]] = [indexed[swapIndex], indexed[index]];
  }
  return indexed;
}

export function validateSentenceCompletionBank(questions, words) {
  const errors = [];
  if (!Array.isArray(questions)) return ['Sentence-completion bank must be an array.'];
  const wordIds = new Set((words || []).map(word => String(word?.id || '')));
  const questionIds = new Set();
  const targetIds = new Set();

  for (const question of questions) {
    const id = String(question?.id || '(missing-id)');
    if (!question?.id || questionIds.has(id)) errors.push(`${id}: missing or duplicate question id.`);
    questionIds.add(id);
    if (!wordIds.has(String(question?.wordId || ''))) errors.push(`${id}: wordId does not resolve to a vocabulary record.`);
    if (targetIds.has(String(question?.wordId || ''))) errors.push(`${id}: target wordId is reused; session weighting expects one item per target word.`);
    targetIds.add(String(question?.wordId || ''));
    if (typeof question?.sentence !== 'string' || (question.sentence.match(/_____/g) || []).length !== 1) errors.push(`${id}: sentence must contain exactly one blank marker (_____).`);
    const choices = question?.choices;
    if (!Array.isArray(choices) || choices.length !== 4 || choices.some(choice => typeof choice !== 'string' || !choice.trim())) errors.push(`${id}: exactly four non-empty text choices are required.`);
    else if (new Set(choices.map(normalize)).size !== 4) errors.push(`${id}: choices must be unique.`);
    if (!Number.isInteger(question?.answerIndex) || question.answerIndex < 0 || question.answerIndex > 3) errors.push(`${id}: answerIndex must be 0..3.`);
    if (!Array.isArray(question?.optionExplanations) || question.optionExplanations.length !== 4 || question.optionExplanations.some(note => typeof note !== 'string' || !note.trim())) errors.push(`${id}: each of the four options needs its own explanation.`);
    for (const field of ['grammarPoint', 'explanation', 'translationVi', 'singleAnswerReason']) {
      if (typeof question?.[field] !== 'string' || !question[field].trim()) errors.push(`${id}: ${field} is required.`);
    }
    if (!GRAMMAR_CATEGORIES.has(String(question?.grammarCategory || ''))) errors.push(`${id}: grammarCategory is missing or unsupported.`);
    if (question?.editorialBatch === '016' && question?.contentBatch !== 'batch-016-part5-grammar-expansion') errors.push(`${id}: Batch 016 contentBatch is missing or inconsistent.`);
    if (question?.contentSource !== 'original-editorial') errors.push(`${id}: contentSource must be original-editorial.`);
    if (question?.editorialStatus !== 'reserve-pending-independent-review') errors.push(`${id}: item must remain pending independent review.`);
    if (question?.reviewNote !== 'internal-author-check; independent-second-review-pending') errors.push(`${id}: independent-review note is missing or inconsistent.`);
  }
  return errors;
}

function reviewWeight(progress = {}) {
  if (!progress.reviewCount) return 3.5;
  if (progress.dueAt && progress.dueAt <= Date.now()) return 7 + Math.min(progress.wrongCount || 0, 4);
  if ((progress.wrongCount || 0) > (progress.correctCount || 0)) return 5.5;
  if ((progress.streak || 0) < 2) return 3.2;
  if ((progress.streak || 0) >= 3) return 1.1;
  return 2;
}

export function chooseSentenceCompletionQuestion(questions, words, progress = {}, seenQuestionIds = [], random = Math.random) {
  const wordMap = new Map((words || []).map(word => [String(word.id), word]));
  const eligible = (questions || []).filter(question => wordMap.has(String(question.wordId)));
  if (!eligible.length) return null;
  const unseen = eligible.filter(question => !seenQuestionIds.includes(question.id));
  const pool = unseen.length ? unseen : eligible;
  const weighted = pool.map(question => ({ question, weight: reviewWeight(progress[question.wordId] || {}) }));
  const total = weighted.reduce((sum, item) => sum + item.weight, 0);
  let point = Math.max(0, Math.min(0.999999999, Number(random()) || 0)) * total;
  let selected = weighted[weighted.length - 1];
  for (const item of weighted) {
    point -= item.weight;
    if (point <= 0) { selected = item; break; }
  }
  const question = selected.question;
  const shuffled = shuffledChoices(question, random);
  const answer = shuffled.find(option => option.isCorrect)?.choice || question.choices[question.answerIndex];
  const targetWord = wordMap.get(String(question.wordId));
  return {
    id: question.id,
    wordId: question.wordId,
    word: targetWord.word,
    mode: 'sentence-completion',
    prompt: 'Chọn từ hoặc dạng từ phù hợp nhất để hoàn thành câu.',
    hint: 'Đọc toàn bộ câu. Xét cấu trúc ngữ pháp, loại từ và ý nghĩa của ngữ cảnh trước khi chọn.',
    sentence: question.sentence,
    choices: shuffled.map(option => option.choice),
    accepted: [answer],
    expectedWord: false,
    expectedDisplay: answer,
    optionExplanations: shuffled.map(option => option.explanation),
    explanation: question.explanation,
    grammarPoint: question.grammarPoint,
    grammarCategory: question.grammarCategory,
    translationVi: question.translationVi,
    singleAnswerReason: question.singleAnswerReason,
    topic: question.topic,
    level: question.level,
    targetAnswer: answer
  };
}
