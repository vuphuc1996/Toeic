import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const appSource = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const start = appSource.indexOf('let listeningPlaybackToken=0;');
const end = appSource.indexOf('async function answerListeningQuestion(', start);
assert.notEqual(start, -1, 'Listening/TTS implementation must exist');
assert.notEqual(end, -1, 'TTS implementation boundary must exist');

const DEFAULT_TTS_SETTINGS = {
  accent: 'en-US', defaultGender: 'female', maleVoiceURI: '', femaleVoiceURI: '',
  rate: 0.92, pitch: 1, volume: 1, wordPauseMs: 900, sentencePauseMs: 850, startupDelayMs: 750, part1LeadInPauseMs: 1000, part1OptionPauseMs: 1300,
};
const statusNode = { textContent: '' };
const readingAudioStatus = { textContent: '' };
const voiceStatusNode = { textContent: '' };
function createSelectMock() {
  let values = [];
  return {
    value: '', disabled: false,
    set innerHTML(html) {
      values = [...String(html).matchAll(/<option value=\"([^\"]*)\">/g)].map(match => ({ value: match[1], textContent: '' }));
      this.value = values[0]?.value || '';
    },
    get options() { return values; },
    append(option) { values.push(option); this.value = option.value; },
  };
}
const maleVoiceSelect = createSelectMock();
const femaleVoiceSelect = createSelectMock();
const speedNode = { value: '0.85' };
const spoken = [];
const gapDurations = [];
let cancelCalls = 0;
let emitCancelEvent = false;
let voices = [];
let voicesLoading = false;
let voiceCatalogReads = 0;
let currentUtterance = null;
let holdGapTimers = false;
let nextTimerId = 0;
const pendingGapTimers = new Map();
const speechSynthesis = {
  getVoices() { voiceCatalogReads++; return voicesLoading && voiceCatalogReads === 1 ? [] : voices; },
  speaking: false,
  pending: false,
  speak(utterance) { spoken.push(utterance); currentUtterance = utterance; },
  cancel() {
    cancelCalls++;
    if (emitCancelEvent && currentUtterance?.onerror) currentUtterance.onerror({ error: 'canceled' });
    currentUtterance = null;
  },
  addEventListener() {},
};
class MockUtterance {
  constructor(text) { this.text = text; this.rate = 1; this.pitch = 1; this.volume = 1; this.lang = ''; this.voice = null; }
}
const context = {
  DEFAULT_TTS_SETTINGS,
  PART1_LEAD_IN_TEXT: 'Now, listen to the four statements.',
  state: { settings: { tts: { ...DEFAULT_TTS_SETTINGS } }, listening: [], listeningProgress: {}, readings: [] },
  window: { speechSynthesis },
  SpeechSynthesisUtterance: MockUtterance,
  $: selector => selector === '#listeningSpeed' ? speedNode : selector === '#ttsMaleVoice' ? maleVoiceSelect : selector === '#ttsFemaleVoice' ? femaleVoiceSelect : selector === '#ttsVoiceStatus' ? voiceStatusNode : selector.includes('data-reading-audio-status') ? readingAudioStatus : statusNode,
  document: { createElement: () => ({ value: '', textContent: '' }), querySelectorAll: () => [] },
  escapeHtml: value => String(value ?? '').replaceAll('&', '&amp;').replaceAll('\"', '&quot;').replaceAll('<', '&lt;').replaceAll('>', '&gt;'),
  toast: message => { context.toasts.push(message); },
  toasts: [],
  setTimeout(callback, ms) { gapDurations.push(ms); const id = ++nextTimerId; if (holdGapTimers) pendingGapTimers.set(id, callback); else queueMicrotask(callback); return id; },
  clearTimeout(id) { pendingGapTimers.delete(id); },
  queueMicrotask,
};
vm.createContext(context);
vm.runInContext(`${appSource.slice(start, end)}
globalThis.__chooseEnglishVoice = chooseEnglishVoice;
globalThis.__recommendedMaleVoice = recommendedMaleVoice;
globalThis.__refreshSpeechVoiceSelectors = refreshSpeechVoiceSelectors;
globalThis.__playListeningAudio = playListeningAudio;
globalThis.__playListeningVocabulary = playListeningVocabulary;
globalThis.__stopSpeech = stopSpeech;
globalThis.__speakText = speakText;
globalThis.__prepareSpeechEngine = prepareSpeechEngine;`, context, { timeout: 1000 });

const readingStart = appSource.indexOf('function playReadingText(id){');
const readingEnd = appSource.indexOf('async function answerReadingQuestion(', readingStart);
assert.notEqual(readingStart, -1, 'Reading aloud action must exist');
assert.notEqual(readingEnd, -1, 'Reading aloud action boundary must exist');
vm.runInContext(`${appSource.slice(readingStart, readingEnd)}\nglobalThis.__playReadingText = playReadingText;`, context, { timeout: 1000 });

// The settings UI helper must exist and safely handle an empty, delayed or populated device voice list.
context.__refreshSpeechVoiceSelectors();
assert.equal(maleVoiceSelect.disabled, true, 'voice selectors are disabled while the device has no English voice catalogue');
assert.equal(femaleVoiceSelect.disabled, true);
assert.match(voiceStatusNode.textContent, /chưa cung cấp voice tiếng Anh/);

const femaleUS = { name: 'Ava Enhanced', voiceURI: 'ava-us', lang: 'en-US', localService: true };
const maleUS = { name: 'Microsoft Ryan Online (Natural)', voiceURI: 'ryan-us', lang: 'en-US', localService: false };
const danielUK = { name: 'Daniel', voiceURI: 'daniel-uk', lang: 'en-GB', localService: true };
voices = [femaleUS, maleUS, danielUK];

// A manually selected voice must remain authoritative over automatic suggestions.
context.state.settings.tts.maleVoiceURI = 'ryan-us';
assert.equal(context.__chooseEnglishVoice('en-GB', 'Man', 'male'), maleUS);

// When no male voice has been selected manually, the previously preferred Daniel voice is used when present.
context.state.settings.tts.maleVoiceURI = '';
assert.equal(context.__recommendedMaleVoice(), danielUK);
assert.equal(context.__chooseEnglishVoice('en-US', 'Man', 'male'), danielUK);

// A second male speaker should use another available male voice rather than
// reusing Daniel for every speaker in the same dialogue.
const secondMale = { name: 'Microsoft Ryan Online (Natural)', voiceURI: 'ryan-us', lang: 'en-US', localService: false };
voices = [femaleUS, secondMale, danielUK];
assert.equal(context.__chooseEnglishVoice('en-GB', 'Man 1', 'male', []), danielUK);
assert.equal(context.__chooseEnglishVoice('en-US', 'Man 2', 'male', ['Daniel']), secondMale);
voices = [femaleUS, maleUS, danielUK];
context.state.settings.tts.maleVoiceURI = 'ryan-us';
context.state.settings.tts.femaleVoiceURI = 'missing-female-uri';
context.__refreshSpeechVoiceSelectors();
assert.equal(maleVoiceSelect.disabled, false, 'selectors become enabled after the voice catalogue is published');
assert.equal(maleVoiceSelect.value, 'ryan-us', 'a manually saved male voice remains selected');
assert.equal(femaleVoiceSelect.value, 'missing-female-uri', 'a saved voice missing on this device is preserved instead of silently overwritten');
assert.ok(femaleVoiceSelect.options.some(option => option.value === 'missing-female-uri'));
assert.match(voiceStatusNode.textContent, /3 voice tiếng Anh/);
context.state.settings.tts.femaleVoiceURI = '';

// Stop during the pre-play buffer cancels startup and must not enqueue the first utterance.
context.state.listening = [{ id: 'tts-stop-during-prep', part: 'Part 2', segments: [
  { speaker: 'Narrator', voice: 'female', text: 'This must not be spoken after Stop.' },
] }];
const prepCancelStart = spoken.length;
holdGapTimers = true;
const prepCancelPromise = context.__playListeningAudio('tts-stop-during-prep');
await waitFor(() => pendingGapTimers.size > 0, 'startup preparation delay must be pending before speech');
context.__stopSpeech();
holdGapTimers = false;
await prepCancelPromise;
assert.equal(spoken.length, prepCancelStart, 'Stop during readiness must prevent the first utterance');
assert.equal(pendingGapTimers.size, 0, 'Stop must clear the pending startup timer');

// Multi-speaker playback keeps a stable voice for each named speaker and preserves the configured turn pause.
context.state.settings.tts.sentencePauseMs = 1000;
context.state.settings.tts.maleVoiceURI = 'ryan-us';
context.state.listening = [{
  id: 'tts-two-speaker',
  segments: [
    { speaker: 'Woman', voice: 'female', text: 'Good morning. The meeting starts at nine.' },
    { speaker: 'Man', voice: 'male', text: 'Thank you. I will be there.' },
    { speaker: 'Woman', voice: 'female', text: 'Please bring the updated report.' },
  ],
}];
const audioStart = spoken.length;
const audioPromise = context.__playListeningAudio('tts-two-speaker');
for (let index = 0; index < 3; index++) {
  await waitFor(() => spoken.length > audioStart + index, `utterance ${index + 1} was queued`);
  const utterance = spoken[audioStart + index];
  utterance.onend();
}
await audioPromise;
assert.deepEqual(spoken.slice(audioStart, audioStart + 3).map(item => item.voice?.voiceURI), ['ava-us', 'ryan-us', 'ava-us']);
assert.deepEqual(gapDurations.slice(-2), [1000, 1000]);
assert.equal(spoken[audioStart].rate, 0.85, 'per-lesson playback speed should be applied');
assert.match(statusNode.textContent, /Đã phát xong/);

// Part 1 A-D playback waits for the voice catalogue and startup buffer before the first choice,
// then applies the longer dedicated pause between each of the four descriptions.
context.state.settings.tts.startupDelayMs = 750;
context.state.settings.tts.part1LeadInPauseMs = 1000;
context.state.settings.tts.part1OptionPauseMs = 1300;
context.state.listening = [{ id: 'tts-part1-four-options', part: 'Part 1', segments: [
  { speaker: 'Narrator', voice: 'female', text: 'Passengers are boarding an aircraft by stairs.' },
  { speaker: 'Narrator', voice: 'female', text: 'B. A worker is moving a chair.' },
  { speaker: 'Narrator', voice: 'female', text: 'A worker is cleaning the window.' },
  { speaker: 'Narrator', voice: 'female', text: 'A worker is carrying a box.' },
] }];
const part1Start = spoken.length;
const part1GapStart = gapDurations.length;
voicesLoading = true;
voiceCatalogReads = 0;
const part1Promise = context.__playListeningAudio('tts-part1-four-options');
await waitFor(() => spoken.length > part1Start, 'Part 1 lead-in must start before option A');
assert.equal(spoken[part1Start].text, 'Now, listen to the four statements.');
spoken[part1Start].onend();
await waitFor(() => spoken.length > part1Start + 1, 'Part 1 option A must start after the lead-in pause');
for (let index = 0; index < 4; index++) {
  await waitFor(() => spoken.length > part1Start + 1 + index, `Part 1 option ${String.fromCharCode(65 + index)} must start`);
  const utterance = spoken[part1Start + 1 + index];
  assert.match(utterance.text, new RegExp(`^${String.fromCharCode(65 + index)}\\. `));
  if (index === 0) assert.equal(utterance.text, 'A. Passengers are boarding an aircraft by stairs.');
  if (index === 1) assert.equal(utterance.text, 'B. A worker is moving a chair.', 'an existing option prefix must not be duplicated');
  if (index === 0) assert.ok(voiceCatalogReads >= 2, 'voice catalogue must be checked again when it was initially empty');
  utterance.onend();
}
await part1Promise;
voicesLoading = false;
assert.ok(gapDurations.slice(part1GapStart).includes(750), 'the 750ms voice startup buffer must be applied');
assert.ok(gapDurations.slice(part1GapStart).includes(1000), 'Part 1 must pause 1.0s after the lead-in and before A');
assert.deepEqual(gapDurations.slice(-3), [1300, 1300, 1300], 'Part 1 A-D options need the dedicated 1.3s gap');
assert.match(statusNode.textContent, /câu dẫn và bốn lựa chọn A–D/);

// Stopping after the lead-in but before option A must cancel the transition and never start an option late.
context.state.listening = [{ id: 'tts-part1-stop-after-lead-in', part: 'Part 1', segments: [
  { speaker: 'Narrator', voice: 'female', text: 'One.' },
  { speaker: 'Narrator', voice: 'female', text: 'Two.' },
  { speaker: 'Narrator', voice: 'female', text: 'Three.' },
  { speaker: 'Narrator', voice: 'female', text: 'Four.' },
] }];
const stopAfterLeadStart = spoken.length;
holdGapTimers = false;
const stopAfterLeadPromise = context.__playListeningAudio('tts-part1-stop-after-lead-in');
await waitFor(() => spoken.length === stopAfterLeadStart + 1, 'Part 1 lead-in before cancellable transition');
assert.equal(spoken.at(-1).text, 'Now, listen to the four statements.');
holdGapTimers = true;
spoken.at(-1).onend();
await waitFor(() => pendingGapTimers.size > 0, 'Part 1 lead-in transition pause must be cancellable');
context.__stopSpeech();
holdGapTimers = false;
await stopAfterLeadPromise;
assert.equal(spoken.length, stopAfterLeadStart + 1, 'Stop in the lead-in pause must prevent option A from starting');

// Vocabulary playback uses one utterance per word and the exact configured inter-word pause.
context.state.settings.tts.wordPauseMs = 1200;
context.state.settings.tts.defaultGender = 'female';
context.state.listening = [{ id: 'tts-vocabulary', vocabulary: [{ word: 'invoice' }, { word: 'shipment' }, { word: 'warehouse' }] }];
const vocabStart = spoken.length;
const vocabPromise = context.__playListeningVocabulary('tts-vocabulary');
for (let index = 0; index < 3; index++) {
  await waitFor(() => spoken.length > vocabStart + index, `vocabulary utterance ${index + 1} was queued`);
  spoken[vocabStart + index].onend();
}
await vocabPromise;
assert.deepEqual(spoken.slice(vocabStart, vocabStart + 3).map(item => item.text), ['invoice', 'shipment', 'warehouse']);
assert.deepEqual(gapDurations.slice(-2), [1200, 1200]);
assert.match(statusNode.textContent, /Khoảng nghỉ giữa các từ: 1.2 giây/);

// stopSpeech must resolve the active playback even when the browser emits no cancellation callback.
context.state.settings.tts.sentencePauseMs = 850;
context.state.listening = [{ id: 'tts-cancel', segments: [
  { speaker: 'Woman', voice: 'female', text: 'This utterance will be canceled.' },
  { speaker: 'Man', voice: 'male', text: 'This second utterance must never start.' },
] }];
const cancelStart = spoken.length;
const cancelPromise = context.__playListeningAudio('tts-cancel');
await waitFor(() => spoken.length === cancelStart + 1, 'first utterance for cancellation must start');
const cancelCountBefore = cancelCalls;
context.__stopSpeech();
const cancelResult = await Promise.race([cancelPromise.then(() => 'resolved'), delay(100).then(() => 'timeout')]);
assert.equal(cancelResult, 'resolved', 'stop must not leave playback awaiting a missing browser onerror event');
assert.equal(cancelCalls, cancelCountBefore + 1);
assert.equal(spoken.length, cancelStart + 1, 'playback must not advance after stop');
assert.equal(statusNode.textContent, 'Đã dừng audio.');

// A cancellation error from the browser is not a user-facing voice failure.
context.toasts.length = 0;
const previewPromise = context.__speakText('A preview sentence.');
await waitFor(() => spoken.at(-1)?.text === 'A preview sentence.', 'one-shot speech must wait for voice preparation');
spoken.at(-1).onstart?.();
spoken.at(-1).onend();
assert.equal(await previewPromise, true);
assert.equal(context.toasts.length, 0);

// Reading passage uses the same delayed engine path and exposes accessible playback status.
context.state.readings = [{ id: 'reading-tts', part: 'Part 7', passage: 'The office will remain closed on Monday. Employees may contact the support desk by email.' }];
const readingStartCount = spoken.length;
context.__playReadingText('reading-tts');
await waitFor(() => spoken.length === readingStartCount + 1, 'reading passage TTS must be queued after preparation');
assert.match(spoken.at(-1).text, /office will remain closed/);
spoken.at(-1).onstart?.();
assert.match(readingAudioStatus.textContent, /Đang đọc/);
spoken.at(-1).onend();
await new Promise(resolve => setImmediate(resolve));
assert.match(readingAudioStatus.textContent, /Đã đọc xong/);

// Reading and listening controls are present in source, and every speech route goes through the guarded queue.
assert.match(appSource, /data-reading-speak=/);
assert.equal((appSource.match(/speechSynthesis\.speak\(/g) || []).length, 1, 'all TTS playback must use the shared guarded utterance function');
assert.match(appSource, /prepareSpeechEngine\(playbackToken,cfg\.startupDelayMs\)/);
assert.match(appSource, /Math\.max\(800,Number\(cfg\.part1LeadInPauseMs\)\|\|1000\)/);
assert.match(appSource, /Math\.max\(1000,Number\(cfg\.part1OptionPauseMs\)\|\|1300\)/);
assert.match(appSource, /const speechText=isPart1\?`\$\{letter\}\. \$\{optionText\}`:segment\.text/);

console.log('Listening/TTS regression PASS: voice readiness, Part 1 lead-in, spoken A-D labels, lead-in/options pauses, shared practice/mock playback, stable speaker voices, safe cancellation, vocabulary pacing and Reading read-aloud.');

async function waitFor(predicate, message) {
  for (let attempt = 0; attempt < 100; attempt++) {
    if (predicate()) return;
    await new Promise(resolve => setImmediate(resolve));
  }
  assert.fail(`Timed out waiting for ${message}`);
}
function delay(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
