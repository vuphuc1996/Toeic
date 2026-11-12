/**
 * TOEIC Mock Test engine.
 * Pure data selection and scoring helpers; deliberately independent from IndexedDB.
 * Each passage/conversation/talk remains an indivisible block so linked questions
 * are never split across a test form.
 */
export const MOCK_MODES = Object.freeze({
  quick: Object.freeze({
    id: 'quick', label: 'Test nhanh', minutes: 15,
    listeningSeconds: 322, readingSeconds: 578,
    listening: { p1: 1, p2: 2, p3Units: 2, p4Units: 1 },
    reading: { p5: 4, p6Questions: 4, p7Single: 4, p7Multiple: 1 },
  }),
  half: Object.freeze({
    id: 'half', label: 'Thi thử rút gọn', minutes: 60,
    listeningSeconds: 1350, readingSeconds: 2250,
    listening: { p1: 3, p2: [11, 14], p3Units: [6, 7], p4Units: 5 },
    reading: { p5: 15, p6Questions: 8, p7Single: 14, p7Multiple: 13 },
  }),
  full: Object.freeze({
    id: 'full', label: 'Thi TOEIC đầy đủ', minutes: 120,
    listeningSeconds: 2700, readingSeconds: 4500,
    listening: { p1: 6, p2: 25, p3Units: 13, p4Units: 10 },
    reading: { p5: 30, p6Questions: 16, p7Single: 29, p7Multiple: 25 },
  }),
});

const PART_ORDER = Object.freeze({
  listening: ['Part 1', 'Part 2', 'Part 3', 'Part 4'],
  reading: ['Part 5', 'Part 6', 'Part 7'],
});

function randomValue(random) {
  const value = Number(random());
  return Number.isFinite(value) ? Math.min(0.999999999, Math.max(0, value)) : Math.random();
}

function shuffle(items, random = Math.random) {
  const out = [...items];
  for (let i = out.length - 1; i > 0; i -= 1) {
    const j = Math.floor(randomValue(random) * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

function questionId(area, unit, index) {
  return `${area}:${unit.id}:${index + 1}`;
}

function usageCount(historyCounts, id) {
  return Math.max(0, Number(historyCounts?.[id] || 0));
}

function orderByFreshness(items, historyCounts, idOf, random) {
  // Randomize first, then sort by historical use; stable sorting preserves the random tie-break.
  return shuffle(items, random).sort((a, b) => usageCount(historyCounts, idOf(a)) - usageCount(historyCounts, idOf(b)));
}

function pickFresh(items, count, historyCounts, idOf, random = Math.random) {
  if (!Number.isInteger(count) || count < 0 || items.length < count) {
    throw new Error(`Ngân hàng không đủ dữ liệu: cần ${count}, hiện có ${items.length}.`);
  }
  const chosen = orderByFreshness(items, historyCounts, idOf, random).slice(0, count);
  return shuffle(chosen, random);
}

function pickQuestions(units, count, area, historyCounts, random) {
  const pool = [];
  for (const unit of units) {
    (unit.questions || []).forEach((question, index) => pool.push({ unit, question, index, id: questionId(area, unit, index) }));
  }
  return pickFresh(pool, count, historyCounts, item => item.id, random);
}

function groupQuestionPicks(picks, area, part) {
  const byUnit = new Map();
  for (const pick of picks) {
    if (!byUnit.has(pick.unit.id)) byUnit.set(pick.unit.id, { unit: pick.unit, picked: [] });
    byUnit.get(pick.unit.id).picked.push(pick);
  }
  return [...byUnit.values()].map(({ unit, picked }) => makeGroup(area, part, unit, picked));
}

function makeGroup(area, part, unit, picks = null) {
  const questions = (picks || (unit.questions || []).map((question, index) => ({ unit, question, index, id: questionId(area, unit, index) })))
    .map(({ question, index, id }) => ({
      id: id || questionId(area, unit, index),
      sourceUnitId: unit.id,
      sourceIndex: index,
      question: question.question || '',
      choices: Array.isArray(question.choices) ? [...question.choices] : [],
      answerIndex: Number(question.answerIndex),
      explanation: question.explanation || '',
      choiceIds: Array.isArray(question.choiceIds) ? [...question.choiceIds] : [],
    }));
  const docs = Array.isArray(unit.documents) ? unit.documents : [];
  return {
    area,
    part,
    unitId: unit.id,
    title: unit.title || unit.id,
    topic: unit.topic || '',
    level: unit.level || '',
    type: unit.type || '',
    documentType: unit.documentType || '',
    passage: unit.passage || '',
    translation: unit.transcriptTranslation || unit.translation || '',
    documents: docs.map(doc => ({ label: doc.label || '', content: doc.content || '' })),
    photo: unit.photo || '',
    image: unit.image || '',
    imageAlt: unit.imageAlt || unit.title || '',
    segments: (unit.segments || []).map(segment => ({ ...segment })),
    questions,
  };
}

function isMultiplePassage(unit) {
  const docs = Array.isArray(unit.documents) ? unit.documents : [];
  const type = String(unit.documentType || '').toLowerCase();
  return docs.length > 1 || /double|triple|multiple/.test(type);
}

/** Choose indivisible passage blocks whose question counts sum to exactly target. */
function pickBlocksExact(units, target, historyCounts, area, random) {
  const ordered = orderByFreshness(units, historyCounts, unit => questionId(area, unit, 0), random);
  const dp = new Map([[0, []]]);
  for (const unit of ordered) {
    const count = (unit.questions || []).length;
    if (!count) continue;
    const existing = [...dp.entries()].sort((a, b) => b[0] - a[0]);
    for (const [sum, chosen] of existing) {
      const next = sum + count;
      if (next > target || dp.has(next)) continue;
      dp.set(next, [...chosen, unit]);
    }
  }
  if (!dp.has(target)) {
    const available = ordered.reduce((sum, unit) => sum + (unit.questions || []).length, 0);
    throw new Error(`Không thể ghép nguyên cụm đoạn đọc thành đúng ${target} câu (ngân hàng hiện có ${available} câu).`);
  }
  return shuffle(dp.get(target), random);
}

function countPool(list, part) {
  return list.filter(item => item.part === part).reduce((sum, item) => sum + (item.questions || []).length, 0);
}

function addSelectedUsage(groups, counts) {
  for (const group of groups) for (const question of group.questions) counts[question.id] = usageCount(counts, question.id) + 1;
}

function sortGroupsByPart(groups, area, random) {
  return PART_ORDER[area].flatMap(part => shuffle(groups.filter(group => group.part === part), random));
}

function makeListening(mode, data, historyCounts, random) {
  const all = data.filter(item => item.editorialStatus !== 'reserve-pending-independent-review' && ['Part 1', 'Part 2', 'Part 3', 'Part 4'].includes(item.part));
  const spec = mode.listening;
  const halfVariant = mode.id === 'half' && randomValue(random) >= 0.5;
  const groups = [];
  const p1 = pickFresh(all.filter(item => item.part === 'Part 1'), spec.p1, historyCounts, item => questionId('listening', item, 0), random)
    .map(unit => makeGroup('listening', 'Part 1', unit));
  groups.push(...p1); addSelectedUsage(p1, historyCounts);

  const p2Count = Array.isArray(spec.p2) ? spec.p2[halfVariant ? 0 : 1] : spec.p2;
  const p2Picks = pickQuestions(all.filter(item => item.part === 'Part 2'), p2Count, 'listening', historyCounts, random);
  const p2 = groupQuestionPicks(p2Picks, 'listening', 'Part 2');
  groups.push(...p2); addSelectedUsage(p2, historyCounts);

  const p3Count = Array.isArray(spec.p3Units) ? spec.p3Units[halfVariant ? 1 : 0] : spec.p3Units;
  const p3 = pickFresh(all.filter(item => item.part === 'Part 3'), p3Count, historyCounts, item => questionId('listening', item, 0), random)
    .map(unit => makeGroup('listening', 'Part 3', unit));
  groups.push(...p3); addSelectedUsage(p3, historyCounts);

  const p4 = pickFresh(all.filter(item => item.part === 'Part 4'), spec.p4Units, historyCounts, item => questionId('listening', item, 0), random)
    .map(unit => makeGroup('listening', 'Part 4', unit));
  groups.push(...p4); addSelectedUsage(p4, historyCounts);

  const ordered = sortGroupsByPart(groups, 'listening', random);
  const expected = mode.id === 'quick' ? 12 : 50 * (mode.id === 'half' ? 1 : 2);
  const actual = ordered.reduce((sum, group) => sum + group.questions.length, 0);
  if (actual !== expected) throw new Error(`Listening ${mode.id}: cần ${expected} câu, đã ghép ${actual}.`);
  return { id: 'listening', label: 'Listening', seconds: mode.listeningSeconds, groups: ordered };
}

function makeReading(mode, data, historyCounts, random) {
  const all = data.filter(item => item.editorialStatus !== 'reserve-pending-independent-review' && ['Part 5', 'Part 6', 'Part 7'].includes(item.part));
  const spec = mode.reading;
  const groups = [];

  const p5Picks = pickQuestions(all.filter(item => item.part === 'Part 5'), spec.p5, 'reading', historyCounts, random);
  const p5 = groupQuestionPicks(p5Picks, 'reading', 'Part 5');
  groups.push(...p5); addSelectedUsage(p5, historyCounts);

  const p6Units = all.filter(item => item.part === 'Part 6');
  const p6Picked = pickBlocksExact(p6Units, spec.p6Questions, historyCounts, 'reading', random);
  const p6 = p6Picked.map(unit => makeGroup('reading', 'Part 6', unit));
  groups.push(...p6); addSelectedUsage(p6, historyCounts);

  const p7Units = all.filter(item => item.part === 'Part 7');
  const singleUnits = p7Units.filter(unit => !isMultiplePassage(unit));
  const multipleUnits = p7Units.filter(isMultiplePassage);
  const p7Single = pickBlocksExact(singleUnits, spec.p7Single, historyCounts, 'reading', random).map(unit => makeGroup('reading', 'Part 7', unit));
  const p7Multiple = pickBlocksExact(multipleUnits, spec.p7Multiple, historyCounts, 'reading', random).map(unit => makeGroup('reading', 'Part 7', unit));
  const p7 = [...p7Single, ...p7Multiple];
  groups.push(...p7); addSelectedUsage(p7, historyCounts);

  const ordered = sortGroupsByPart(groups, 'reading', random);
  const expected = mode.id === 'quick' ? 13 : 50 * (mode.id === 'half' ? 1 : 2);
  const actual = ordered.reduce((sum, group) => sum + group.questions.length, 0);
  if (actual !== expected) throw new Error(`Reading ${mode.id}: cần ${expected} câu, đã ghép ${actual}.`);
  return { id: 'reading', label: 'Reading', seconds: mode.readingSeconds, groups: ordered };
}

export function createMockExam({ modeId, listening = [], readings = [], history = [], usageCounts = null, random = Math.random, now = Date.now } = {}) {
  const mode = MOCK_MODES[modeId];
  if (!mode) throw new Error('Chế độ thi thử không hợp lệ.');
  const listeningPool = countPool(listening, 'Part 1') + countPool(listening, 'Part 2') + countPool(listening, 'Part 3') + countPool(listening, 'Part 4');
  const readingPool = countPool(readings, 'Part 5') + countPool(readings, 'Part 6') + countPool(readings, 'Part 7');
  if (!listeningPool || !readingPool) throw new Error('Chưa tải đủ ngân hàng Listening và Reading.');

  const historyCounts = Object.create(null);
  if (usageCounts && typeof usageCounts === 'object' && !Array.isArray(usageCounts)) {
    for (const [id, count] of Object.entries(usageCounts)) {
      const n = Number(count);
      if (id && Number.isFinite(n) && n > 0) historyCounts[id] = Math.floor(n);
    }
  } else {
    for (const attempt of (Array.isArray(history) ? history : []).slice(-60)) {
      for (const id of (attempt.questionIds || [])) historyCounts[id] = usageCount(historyCounts, id) + 1;
    }
  }
  const listeningSection = makeListening(mode, listening, historyCounts, random);
  const readingSection = makeReading(mode, readings, historyCounts, random);
  const questionIds = [...listeningSection.groups, ...readingSection.groups].flatMap(group => group.questions.map(question => question.id));
  if (new Set(questionIds).size !== questionIds.length) throw new Error('Bộ tạo đề phát hiện câu hỏi trùng lặp nội bộ.');

  const startedAt = Number(now());
  const listeningDeadlineAt = startedAt + listeningSection.seconds * 1000;
  const totalDeadlineAt = listeningDeadlineAt + readingSection.seconds * 1000;
  return {
    version: 1,
    id: `mock-${startedAt}-${Math.floor(randomValue(random) * 1e6).toString(36)}`,
    modeId,
    modeLabel: mode.label,
    totalMinutes: mode.minutes,
    startedAt,
    listeningDeadlineAt,
    totalDeadlineAt,
    currentSection: 'listening',
    status: 'active',
    answers: {},
    flags: [],
    questionIds,
    sections: { listening: listeningSection, reading: readingSection },
  };
}

export function getExamQuestions(section) {
  return (section?.groups || []).flatMap(group => group.questions.map(question => ({ ...question, part: group.part, unitId: group.unitId, unitTitle: group.title })));
}

export function getMockSectionForTime(exam, timestamp = Date.now()) {
  if (!exam || exam.status !== 'active') return exam?.currentSection || null;
  if (timestamp >= exam.totalDeadlineAt) return 'expired';
  return timestamp >= exam.listeningDeadlineAt ? 'reading' : 'listening';
}

export function scoreMockExam(exam) {
  if (!exam) throw new Error('Không có bài thi để chấm điểm.');
  const summary = { listening: null, reading: null, total: { correct: 0, answered: 0, questions: 0 }, parts: {} };
  for (const area of ['listening', 'reading']) {
    const questions = getExamQuestions(exam.sections[area]);
    const section = { correct: 0, answered: 0, questions: questions.length, accuracy: 0, target75: 0, unanswered: 0 };
    for (const question of questions) {
      const selected = exam.answers?.[question.id];
      const answered = Number.isInteger(selected);
      const correct = answered && selected === question.answerIndex;
      if (answered) section.answered += 1;
      if (correct) section.correct += 1;
      else if (!answered) section.unanswered += 1;
      if (!summary.parts[question.part]) summary.parts[question.part] = { area, correct: 0, answered: 0, questions: 0, accuracy: 0, unanswered: 0 };
      const part = summary.parts[question.part];
      part.questions += 1;
      if (answered) part.answered += 1;
      if (correct) part.correct += 1;
      if (!answered) part.unanswered += 1;
    }
    section.accuracy = section.questions ? Math.round(section.correct / section.questions * 100) : 0;
    section.target75 = Math.max(0, Math.ceil(section.questions * 0.75) - section.correct);
    summary[area] = section;
    summary.total.correct += section.correct;
    summary.total.answered += section.answered;
    summary.total.questions += section.questions;
  }
  summary.total.accuracy = summary.total.questions ? Math.round(summary.total.correct / summary.total.questions * 100) : 0;
  summary.total.unanswered = summary.total.questions - summary.total.answered;
  for (const part of Object.values(summary.parts)) {
    part.accuracy = part.questions ? Math.round(part.correct / part.questions * 100) : 0;
  }
  return summary;
}
