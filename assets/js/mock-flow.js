/**
 * Time-boxed guided question flow for mock exams.
 * Each section keeps its official section deadline; the available time is
 * distributed across questions using passage/audio context weights.
 */
function countWords(value) {
  return String(value || '').trim().split(/\s+/).filter(Boolean).length;
}

function groupContextWords(group, area) {
  if (area === 'listening') {
    return (group.segments || []).reduce((sum, segment) => sum + countWords(segment.text), 0);
  }
  const docs = Array.isArray(group.documents) ? group.documents : [];
  return docs.length
    ? docs.reduce((sum, doc) => sum + countWords(doc.content), 0)
    : countWords(group.passage);
}

function groupQuestionWeight(group, area) {
  const questions = group.questions || [];
  if (!questions.length) return [];
  const contextWords = groupContextWords(group, area);
  const contextRate = area === 'listening' ? 2.45 : 3.25;
  const contextSeconds = contextWords / contextRate;
  const perQuestionBase = area === 'listening' ? 10 : 17;
  // Reserve time inside the section budget for the audible transition/lead-in before each question.
  const transitionSeconds = 2.4;
  return questions.map((question, index) => {
    const promptWords = countWords(question.question);
    const promptWeight = area === 'reading' ? promptWords * 0.22 : promptWords * 0.12;
    return perQuestionBase + transitionSeconds + promptWeight + (index === 0 ? contextSeconds : 0);
  });
}

/** Return a deterministic schedule whose final slot ends exactly at deadline. */
export function buildMockQuestionSchedule(section, area, startAt, durationSeconds, questionOffset = 0) {
  const groups = Array.isArray(section?.groups) ? section.groups : [];
  const source = [];
  let sectionQuestionNumber = 0;
  for (let groupIndex = 0; groupIndex < groups.length; groupIndex += 1) {
    const group = groups[groupIndex];
    const weights = groupQuestionWeight(group, area);
    for (let questionIndex = 0; questionIndex < (group.questions || []).length; questionIndex += 1) {
      const question = group.questions[questionIndex];
      sectionQuestionNumber += 1;
      source.push({
        questionId: question.id,
        unitId: group.unitId,
        groupIndex,
        questionIndex,
        part: group.part,
        area,
        title: group.title || group.unitId,
        topic: group.topic || '',
        sectionQuestionNumber,
        questionNumber: questionOffset + sectionQuestionNumber,
        questionText: question.question || '',
        weight: Math.max(1, weights[questionIndex] || 1),
      });
    }
  }
  if (!source.length) return [];
  const totalWeight = source.reduce((sum, item) => sum + item.weight, 0);
  const start = Number(startAt);
  const durationMs = Math.max(1000, Number(durationSeconds) * 1000);
  let cursorMs = 0;
  return source.map((item, index) => {
    const startOffsetMs = cursorMs;
    const endOffsetMs = index === source.length - 1
      ? durationMs
      : Math.min(durationMs, Math.round(durationMs * source.slice(0, index + 1).reduce((sum, row) => sum + row.weight, 0) / totalWeight));
    cursorMs = endOffsetMs;
    return {
      ...item,
      index,
      startAt: start + startOffsetMs,
      endAt: start + endOffsetMs,
      allottedMs: endOffsetMs - startOffsetMs,
    };
  });
}

export function getMockScheduledQuestion(schedule, timestamp = Date.now()) {
  if (!Array.isArray(schedule) || !schedule.length) return null;
  const now = Number(timestamp);
  if (!Number.isFinite(now)) return schedule[0];
  let low = 0;
  let high = schedule.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const slot = schedule[mid];
    if (now < slot.startAt) high = mid - 1;
    else if (now >= slot.endAt && mid < schedule.length - 1) low = mid + 1;
    else return slot;
  }
  return now < schedule[0].startAt ? schedule[0] : schedule[schedule.length - 1];
}

export function getMockTransitionLeadIn(previous, current, totalQuestions = 0) {
  if (!current) return '';
  const number = current.sectionQuestionNumber || current.questionNumber || current.index + 1;
  const count = Math.max(0, Number(totalQuestions) || 0);
  const counter = count ? `Question ${number} of ${count}.` : `Question ${number}.`;
  if (!previous) {
    return current.area === 'listening'
      ? `Listening section. ${current.part}. ${counter} Listen carefully.`
      : `Reading section. ${current.part}. ${counter} Read the text and choose the best answer.`;
  }
  const groupChanged = previous.unitId !== current.unitId;
  const partChanged = previous.part !== current.part;
  if (current.area === 'listening') {
    if (groupChanged || partChanged) return `Next group. ${current.part}. ${counter} Listen to the audio and choose your answer.`;
    return `${counter} Continue with the same audio and select your answer.`;
  }
  if (groupChanged || partChanged) return `Next reading group. ${current.part}. ${counter} Read the passage and choose the best answer.`;
  return `${counter} Continue with the same passage and choose your answer.`;
}

export function getMockQuestionTimeRemaining(slot, timestamp = Date.now()) {
  if (!slot) return 0;
  return Math.max(0, Math.ceil((Number(slot.endAt) - Number(timestamp)) / 1000));
}
