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
  rate: 0.92, pitch: 1, volume: 1, wordPauseMs: 900, sentencePauseMs: 850,
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
let voiceCatalogThrows = false;
let utteranceConstructorThrows = false;
let voices = [];
let voicesLoading = false;
let voiceCatalogReads = 0;
let resumeCalls = 0;
const timerDurations = new Map();
let currentUtterance = null;
let holdGapTimers = false;
let nextTimerId = 0;
const pendingGapTimers = new Map();
const speechSynthesis = {
  getVoices() { voiceCatalogReads++; if (voiceCatalogThrows) throw new Error('voice catalogue not ready'); return voicesLoading && voiceCatalogReads === 1 ? [] : voices; },
  speaking: false,
  pending: false,
  paused: false,
  resume() { resumeCalls++; this.paused = false; },
  speak(utterance) { spoken.push(utterance); currentUtterance = utterance; },
  cancel() {
    cancelCalls++;
    if (emitCancelEvent && currentUtterance?.onerror) currentUtterance.onerror({ error: 'canceled' });
    currentUtterance = null;
  },
  addEventListener() {},
};
class MockUtterance {
  constructor(text) { if (utteranceConstructorThrows) throw new Error('utterance constructor failed'); this.text = text; this.rate = 1; this.pitch = 1; this.volume = 1; this.lang = ''; this.voice = null; }
}
const context = {
  DEFAULT_TTS_SETTINGS,
  PART1_LEAD_IN_TEXT: 'Now, listen to the four statements.',
  SPEECH_START_TIMEOUT_MS: 10000,
  SPEECH_END_TIMEOUT_MIN_MS: 20000,
  PART1_TITLE_PAUSE_MS: 1000,
  PART1_LEAD_IN_PAUSE_MS: 1000,
  PART1_OPTION_LABEL_PAUSE_MS: 1500,
  PART1_OPTION_GAP_MS: 1300,
  PART_SEQUENCE_PAUSE_MS: 1000,
  PART_OPTION_LABEL_PAUSE_MS: 1000,
  PART_OPTION_GAP_MS: 1000,
  state: { settings: { tts: { ...DEFAULT_TTS_SETTINGS } }, listening: [], listeningProgress: {}, readings: [], foundationListeningClips: [] },
  window: { speechSynthesis },
  SpeechSynthesisUtterance: MockUtterance,
  $: selector => selector === '#listeningSpeed' ? speedNode : selector === '#ttsMaleVoice' ? maleVoiceSelect : selector === '#ttsFemaleVoice' ? femaleVoiceSelect : selector === '#ttsVoiceStatus' ? voiceStatusNode : selector.includes('data-reading-audio-status') ? readingAudioStatus : statusNode,
  document: { createElement: () => ({ value: '', textContent: '' }), querySelectorAll: () => [] },
  escapeHtml: value => String(value ?? '').replaceAll('&', '&amp;').replaceAll('\"', '&quot;').replaceAll('<', '&lt;').replaceAll('>', '&gt;'),
  toast: message => { context.toasts.push(message); },
  toasts: [],
  setTimeout(callback, ms) { if(ms<=2500)gapDurations.push(ms); const id = ++nextTimerId; timerDurations.set(id, ms); if (ms > 2500 || holdGapTimers) pendingGapTimers.set(id, callback); else queueMicrotask(callback); return id; },
  clearTimeout(id) { pendingGapTimers.delete(id); timerDurations.delete(id); },
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

const readingStart = appSource.indexOf('async function playReadingText(id){');
const readingEnd = appSource.indexOf('async function answerReadingQuestion(', readingStart);
assert.notEqual(readingStart, -1, 'Reading aloud action must exist');
assert.notEqual(readingEnd, -1, 'Reading aloud action boundary must exist');
vm.runInContext(`${appSource.slice(readingStart, readingEnd)}\nglobalThis.__playReadingText = playReadingText;`, context, { timeout: 1000 });

const foundationStart = appSource.indexOf('async function playFoundationListening(clipId){');
const foundationEnd = appSource.indexOf('function answerFoundationListening(', foundationStart);
assert.notEqual(foundationStart, -1, 'Foundation dialogue playback must exist');
assert.notEqual(foundationEnd, -1, 'Foundation playback function boundary must exist');
vm.runInContext(`${appSource.slice(foundationStart, foundationEnd)}\nglobalThis.__playFoundationListening = playFoundationListening;`, context, { timeout: 1000 });

// The settings UI helper must exist and safely handle an empty, delayed or populated device voice list.
context.__refreshSpeechVoiceSelectors();
assert.equal(maleVoiceSelect.disabled, true, 'voice selectors are disabled while the device has no English voice catalogue');
assert.equal(femaleVoiceSelect.disabled, true);
assert.match(voiceStatusNode.textContent, /chưa cung cấp danh sách voice tiếng Anh/);

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

// Playback must queue the first utterance in the original tap stack, even when the device voice list is empty.
context.state.listening = [{ id: 'tts-no-voice-catalogue', part: 'Part 2', segments: [
  { speaker: 'Narrator', voice: 'female', text: 'The default device voice should read this sentence.' },
] }];
voices = [];
voiceCatalogReads = 0;
const noVoiceStart = spoken.length;
const noVoicePromise = context.__playListeningAudio('tts-no-voice-catalogue');
assert.equal(spoken.length, noVoiceStart + 1, 'Part title must be queued synchronously before returning to the event loop');
assert.equal(spoken[noVoiceStart].voice, null, 'system default voice is used when no English voice catalogue is published yet');
assert.equal(spoken[noVoiceStart].lang, 'en-US', 'fallback retains the configured English locale');
assert.ok(resumeCalls > 0, 'paused speech synthesis is resumed directly from the user action');
await consumeSpeechSequence(noVoiceStart, ['Part 2: Question–Response','Now, listen to the question and choose the best response.','The default device voice should read this sentence.'], 'No-voice fallback');
await noVoicePromise;
assert.match(statusNode.textContent, /Đã phát xong/);

// Stop during an active utterance resolves playback even when the browser omits cancellation events.
context.state.listening = [{ id: 'tts-stop-during-active', part: 'Part 2', segments: [
  { speaker: 'Narrator', voice: 'female', text: 'This must stop immediately.' },
] }];
voices = [femaleUS, maleUS, danielUK];
const stopActiveStart=spoken.length;
const stopActivePromise=context.__playListeningAudio('tts-stop-during-active');
assert.equal(spoken.length,stopActiveStart+1,'Part title is queued synchronously');
context.__stopSpeech();
await stopActivePromise;
assert.equal(spoken.length,stopActiveStart+1,'stop does not enqueue later utterances');

// Multi-speaker playback keeps a stable voice for each named speaker and preserves the configured turn pause.
context.state.settings.tts.sentencePauseMs = 1000;
context.state.settings.tts.maleVoiceURI = 'ryan-us';
context.state.listening = [{
  id: 'tts-two-speaker', part:'Part 3', topic:'Team Meeting',
  segments: [
    { speaker: 'Woman', voice: 'female', text: 'Good morning. The meeting starts at nine.' },
    { speaker: 'Man', voice: 'male', text: 'Thank you. I will be there.' },
    { speaker: 'Woman', voice: 'female', text: 'Please bring the updated report.' },
  ],
}];
const audioStart = spoken.length;
const audioPromise = context.__playListeningAudio('tts-two-speaker');
await consumeSpeechSequence(audioStart, ['Part 3: Conversations','Now, listen to the conversation and answer the questions.','Good morning. The meeting starts at nine.','Thank you. I will be there.','Please bring the updated report.'], 'Multi-speaker Part 3');
await audioPromise;
assert.deepEqual(spoken.slice(audioStart + 2, audioStart + 5).map(item => item.voice?.voiceURI), ['ava-us', 'ryan-us', 'ava-us']);
assert.deepEqual(gapDurations.slice(-2), [1000, 1000]);
assert.equal(spoken[audioStart].rate, 0.85, 'per-lesson playback speed should be applied');
assert.match(statusNode.textContent, /Đã phát xong/);

// Part 1 uses a fixed and explicit spoken sequence: title, 1s pause,
// lead-in, 1s pause, then each letter label, 1.5s pause, and its description.
context.state.listening = [{ id: 'tts-part1-four-options', part: 'Part 1', topic: 'Warehouse & Shipping', title: 'Organizing warehouse inventory', segments: [
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
await waitFor(() => spoken.length > part1Start, 'Part 1 title must start immediately after synchronous engine preparation');
assert.equal(spoken[part1Start].text, 'Part 1: Warehouse & Shipping');
spoken[part1Start].onend();
await waitFor(() => spoken.length > part1Start + 1, 'Part 1 lead-in must start after the title pause');
assert.equal(spoken[part1Start + 1].text, 'Now, listen to the four statements.');
spoken[part1Start + 1].onend();
let utteranceIndex = part1Start + 2;
for (let index = 0; index < 4; index++) {
  const letter = String.fromCharCode(65 + index);
  await waitFor(() => spoken.length > utteranceIndex, `Part 1 option ${letter} label must be queued`);
  const labelUtterance = spoken[utteranceIndex++];
  assert.equal(labelUtterance.text, `${letter}.`, `Part 1 option ${letter} label is spoken separately`);
  labelUtterance.onend();
  await waitFor(() => spoken.length > utteranceIndex, `Part 1 option ${letter} description must wait for its 1.5s label gap`);
  const descriptionUtterance = spoken[utteranceIndex++];
  const expectedDescriptions = [
    'Passengers are boarding an aircraft by stairs.',
    'A worker is moving a chair.',
    'A worker is cleaning the window.',
    'A worker is carrying a box.',
  ];
  assert.equal(descriptionUtterance.text, expectedDescriptions[index], `Part 1 option ${letter} description follows its label without duplicate prefixes`);
  if (index === 0) assert.ok(voiceCatalogReads >= 1, 'voice catalogue is queried immediately even when initially empty');
  descriptionUtterance.onend();
}
await part1Promise;
voicesLoading = false;
const part1Gaps = gapDurations.slice(part1GapStart);
assert.equal(part1Gaps.some(gap => gap > 2500), false, 'no artificial startup timer delays the first utterance');
assert.ok(part1Gaps.includes(1000), 'Part 1 waits 1.0s after the spoken topic title and after the lead-in');
assert.equal(part1Gaps.filter(gap => gap === 1500).length, 4, 'each A/B/C/D label is followed by a fixed 1.5s pause');
assert.deepEqual(part1Gaps.filter(gap => gap === 1300), [1300, 1300, 1300], 'Part 1 pauses 1.3s between the descriptions');
assert.match(statusNode.textContent, /Part 1:.*câu dẫn, nội dung và bốn lựa chọn A–D/);

// Stopping after the lead-in but before option A must cancel the transition and never start an option late.
context.state.listening = [{ id: 'tts-part1-stop-after-lead-in', part: 'Part 1', topic: 'Office & Facilities', segments: [
  { speaker: 'Narrator', voice: 'female', text: 'One.' },
  { speaker: 'Narrator', voice: 'female', text: 'Two.' },
  { speaker: 'Narrator', voice: 'female', text: 'Three.' },
  { speaker: 'Narrator', voice: 'female', text: 'Four.' },
] }];
const stopAfterLeadStart = spoken.length;
holdGapTimers = false;
const stopAfterLeadPromise = context.__playListeningAudio('tts-part1-stop-after-lead-in');
await waitFor(() => spoken.length === stopAfterLeadStart + 1, 'Part 1 title before lead-in');
assert.equal(spoken.at(-1).text, 'Part 1: Office & Facilities');
spoken.at(-1).onend();
await waitFor(() => spoken.length === stopAfterLeadStart + 2, 'Part 1 lead-in before cancellable transition');
assert.equal(spoken.at(-1).text, 'Now, listen to the four statements.');
holdGapTimers = true;
spoken.at(-1).onend();
await waitFor(() => pendingGapTimers.size > 0, 'Part 1 lead-in transition pause must be cancellable');
context.__stopSpeech();
holdGapTimers = false;
await stopAfterLeadPromise;
assert.equal(spoken.length, stopAfterLeadStart + 2, 'Stop in the lead-in pause must prevent option A from starting');

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

// Foundation A2 dialogues use the saved male/female voice selections and pause between speaker turns.
context.state.settings.tts.maleVoiceURI = 'ryan-us';
context.state.settings.tts.femaleVoiceURI = '';
context.state.settings.tts.sentencePauseMs = 950;
context.state.foundationListeningClips = [{ id: 'a2-foundation-dialogue-test', segments: [
  { speaker: 'Linh', voice: 'female', text: 'Hello. Are you ready?' },
  { speaker: 'Nam', voice: 'male', text: 'Yes. I have the report.' },
  { speaker: 'Linh', voice: 'female', text: 'Please send it now.' },
] }];
const foundationStartIndex = spoken.length;
const foundationGapStart = gapDurations.length;
const foundationPromise = context.__playFoundationListening('a2-foundation-dialogue-test');
for (let index = 0; index < 3; index++) {
  await waitFor(() => spoken.length > foundationStartIndex + index, `Foundation dialogue turn ${index + 1} must be queued`);
  const utterance = spoken[foundationStartIndex + index];
  if (index === 0) assert.equal(utterance.voice?.voiceURI, 'ava-us', 'female turn uses the device female voice');
  if (index === 1) assert.equal(utterance.voice?.voiceURI, 'ryan-us', 'male turn honors the saved male voice');
  utterance.onend();
}
await foundationPromise;
assert.deepEqual(spoken.slice(foundationStartIndex, foundationStartIndex + 3).map(item => item.text), [
  'Hello. Are you ready?', 'Yes. I have the report.', 'Please send it now.',
]);
assert.deepEqual(gapDurations.slice(foundationGapStart).filter(value => value === 950), [950, 950]);
assert.match(statusNode.textContent, /Đã phát xong/);

// Stop during a Foundation turn pause must prevent the next speaker from being queued.
context.state.foundationListeningClips = [{ id: 'a2-foundation-stop-test', segments: [
  { speaker: 'Woman', voice: 'female', text: 'This is the first turn.' },
  { speaker: 'Man', voice: 'male', text: 'This second turn must not play.' },
] }];
holdGapTimers = false;
const foundationStopStart = spoken.length;
const foundationStopPromise = context.__playFoundationListening('a2-foundation-stop-test');
await waitFor(() => spoken.length === foundationStopStart + 1, 'Foundation first turn before stop');
holdGapTimers = true;
spoken.at(-1).onend();
await waitFor(() => pendingGapTimers.size > 0, 'Foundation inter-speaker gap must be cancellable');
context.__stopSpeech();
holdGapTimers = false;
await foundationStopPromise;
assert.equal(spoken.length, foundationStopStart + 1, 'Foundation Stop prevents the next turn');
assert.equal(statusNode.textContent, 'Đã dừng audio.');

// Legacy Pre-A1/A1 clips without explicit speaker segments remain compatible:
// the transcript is split into sentence turns and keeps the configured default voice.
context.state.settings.tts.defaultGender = 'female';
context.state.foundationListeningClips = [{
  id: 'a1-legacy-script-fallback',
  script: 'The office opens at eight. Please speak to the receptionist.',
}];
const legacyFoundationStart = spoken.length;
const legacyFoundationGaps = gapDurations.length;
const legacyFoundationPromise = context.__playFoundationListening('a1-legacy-script-fallback');
for (let index = 0; index < 2; index++) {
  await waitFor(() => spoken.length > legacyFoundationStart + index, `legacy Foundation sentence ${index + 1} must play`);
  const utterance = spoken[legacyFoundationStart + index];
  assert.equal(utterance.voice?.voiceURI, 'ava-us', 'legacy fallback uses configured default female voice');
  utterance.onend();
}
await legacyFoundationPromise;
assert.deepEqual(spoken.slice(legacyFoundationStart, legacyFoundationStart + 2).map(item => item.text), [
  'The office opens at eight.', 'Please speak to the receptionist.',
]);
assert.deepEqual(gapDurations.slice(legacyFoundationGaps).filter(value => value === 950), [950]);
assert.match(statusNode.textContent, /Đã phát xong/);

// A selected device voice that fails is retried once with the system default voice.
// Some mobile engines dispatch a cancellation error when cancel() is called during
// fallback; the fallback path must not cancel the new utterance or accept stale events.
context.state.settings.tts.femaleVoiceURI='ava-us';
emitCancelEvent=true;
const fallbackStart=spoken.length;
const fallbackPromise=context.__speakText('Use the fallback voice if the selected one fails.');
const cancelBeforeFallback=cancelCalls;
let fallbackSettled=false;fallbackPromise.then(()=>{fallbackSettled=true;});
assert.equal(spoken.length,fallbackStart+1,'selected voice is queued immediately');
const selectedUtterance=spoken[fallbackStart];
selectedUtterance.onerror?.({error:'voice-unavailable'});
assert.equal(spoken.length,fallbackStart+2,'failed named voice is retried with the system voice');
assert.equal(spoken[fallbackStart+1].voice,null);
assert.equal(cancelCalls,cancelBeforeFallback,'fallback must not cancel the queue and trigger a stale cancellation event');
selectedUtterance.onend?.();selectedUtterance.onerror?.({error:'synthesis-failed'});
await Promise.resolve();
assert.equal(fallbackSettled,false,'stale events from the failed voice cannot settle the fallback attempt');
spoken[fallbackStart+1].onstart?.();spoken[fallbackStart+1].onend();
assert.equal(await fallbackPromise,true);
emitCancelEvent=false;
context.state.settings.tts.femaleVoiceURI='';

// A throwing voice catalogue falls back to the system default instead of silently failing.
voiceCatalogThrows=true;
const catalogueThrowStart=spoken.length;
const catalogueThrowPromise=context.__speakText('Use the default voice when the catalogue throws.');
assert.equal(spoken.length,catalogueThrowStart+1,'catalogue failure must not block the first utterance');
assert.equal(spoken[catalogueThrowStart].voice,null);
spoken[catalogueThrowStart].onstart?.();spoken[catalogueThrowStart].onend();
assert.equal(await catalogueThrowPromise,true);
voiceCatalogThrows=false;

// Utterance construction failures are converted into a handled playback failure.
const constructorToastStart=context.toasts.length;
utteranceConstructorThrows=true;
const constructorFailure=await context.__speakText('This utterance cannot be constructed.');
utteranceConstructorThrows=false;
assert.equal(constructorFailure,false);
assert.ok(context.toasts.length>constructorToastStart,'constructor failure must surface a visible error');

// Missing onstart/onend callbacks are surfaced through a bounded watchdog instead of a silent hang.
const timeoutToastStart=context.toasts.length;
const timeoutSpeechPromise=context.__speakText('The browser will not emit a speech event.');
const timeoutSpeechIndex=spoken.length-1;
assert.equal(spoken[timeoutSpeechIndex].text,'The browser will not emit a speech event.');
const startWatchdog=[...timerDurations.entries()].find(([,duration])=>duration===10000);
assert.ok(startWatchdog,'a ten-second speech-start watchdog must be armed');
const timeoutCallback=pendingGapTimers.get(startWatchdog[0]);
assert.equal(typeof timeoutCallback,'function');
pendingGapTimers.delete(startWatchdog[0]);timerDurations.delete(startWatchdog[0]);
timeoutCallback();
assert.equal(await timeoutSpeechPromise,false,'a missing browser start event must resolve as a failure, not hang');
assert.ok(context.toasts.length>timeoutToastStart);
assert.match(context.toasts.at(-1),/10 giây/);

// A cancellation error from the browser is not a user-facing voice failure.
context.toasts.length = 0;
const previewPromise = context.__speakText('A preview sentence.');
assert.equal(spoken.at(-1)?.text, 'A preview sentence.', 'one-shot speech queues immediately from the click handler');
spoken.at(-1).onstart?.();
spoken.at(-1).onend();
assert.equal(await previewPromise, true);
assert.equal(context.toasts.length, 0);

// Parts 2–4 all announce the Part and lead-in, then read content and lettered answers.
async function consumeSpeechSequence(start, expectedTexts, label) {
  for (let index = 0; index < expectedTexts.length; index++) {
    await waitFor(() => spoken.length > start + index, `${label} utterance ${index + 1}`);
    const utterance = spoken[start + index];
    assert.equal(utterance.text, expectedTexts[index], `${label} speech order at ${index + 1}`);
    utterance.onstart?.();
    utterance.onend?.();
  }
}
function assertOneSecondOptionCadence(choiceCount, label) {
  // One pause before the option set, one after every spoken A/B/C/D label,
  // and one between the end of an option and the next label.
  const expectedGapCount = 1 + choiceCount + Math.max(0, choiceCount - 1);
  assert.deepEqual(gapDurations.slice(-expectedGapCount), Array(expectedGapCount).fill(1000),
    `${label}: question/option labels and answer text must be separated by exactly 1 second`);
}
voices = [femaleUS, maleUS, danielUK];
context.state.settings.tts.sentencePauseMs = 850;
context.state.listening = [{ id: 'tts-part2-sequence', part: 'Part 2', topic: 'Questions', segments: [
  { speaker: 'Speaker', voice: 'female', text: 'When will the manager return?' },
], questions: [{ question: 'Choose the most appropriate response.', choices: ['At three o’clock.', 'In the main office.', 'The new manager.'] }] }];
let sequenceStart = spoken.length;
let sequencePromise = context.__playListeningAudio('tts-part2-sequence');
await consumeSpeechSequence(sequenceStart, [
  'Part 2: Question–Response',
  'Now, listen to the question and choose the best response.',
  'When will the manager return?',
  'A.', 'At three o’clock.', 'B.', 'In the main office.', 'C.', 'The new manager.',
], 'Part 2');
await sequencePromise;
assertOneSecondOptionCadence(3, 'Listening Part 2');
assert.match(statusNode.textContent, /Đã phát xong Part 2/);

context.state.listening = [{ id: 'tts-part3-sequence', part: 'Part 3', topic: 'Conversation', segments: [
  { speaker: 'Woman', voice: 'female', text: 'I need to change my appointment.' },
  { speaker: 'Man', voice: 'male', text: 'I can move it to Friday.' },
], questions: [{ question: 'What does the woman want to do?', choices: ['Cancel an order', 'Change an appointment', 'Reserve a room', 'Request a refund'] }] }];
sequenceStart = spoken.length;
sequencePromise = context.__playListeningAudio('tts-part3-sequence');
await consumeSpeechSequence(sequenceStart, [
  'Part 3: Conversations',
  'Now, listen to the conversation and answer the questions.',
  'I need to change my appointment.',
  'I can move it to Friday.',
  'Question 1. What does the woman want to do?',
  'A.', 'Cancel an order', 'B.', 'Change an appointment', 'C.', 'Reserve a room', 'D.', 'Request a refund',
], 'Part 3');
await sequencePromise;
assertOneSecondOptionCadence(4, 'Listening Part 3');

context.state.listening = [{ id: 'tts-part4-sequence', part: 'Part 4', topic: 'Announcement', segments: [
  { speaker: 'Announcer', voice: 'male', text: 'The west entrance will close at noon for repairs.' },
], questions: [{ question: 'When will the entrance close?', choices: ['At noon', 'At two', 'Tomorrow morning', 'On Friday'] }] }];
sequenceStart = spoken.length;
sequencePromise = context.__playListeningAudio('tts-part4-sequence');
await consumeSpeechSequence(sequenceStart, [
  'Part 4: Short Talks',
  'Now, listen to the talk and answer the questions.',
  'The west entrance will close at noon for repairs.',
  'Question 1. When will the entrance close?',
  'A.', 'At noon', 'B.', 'At two', 'C.', 'Tomorrow morning', 'D.', 'On Friday',
], 'Part 4');
await sequencePromise;
assertOneSecondOptionCadence(4, 'Listening Part 4');
assert.ok(gapDurations.slice(-30).includes(1000), 'Part headers, lead-ins, question/answer and letter labels use one-second pauses');

// Reading Parts 5–7 announce their Part, then read text/questions/options in order.
context.state.readings = [{ id: 'reading-tts', part: 'Part 7', title: 'Office Notice', passage: 'The office will remain closed on Monday. Employees may contact the support desk by email.', questions: [{ question: 'How can employees contact the support desk?', choices: ['By telephone', 'By email', 'In person', 'By regular mail'] }] }];
const readingStartCount = spoken.length;
const readingPromise = context.__playReadingText('reading-tts');
await consumeSpeechSequence(readingStartCount, [
  'Part 7: Reading Comprehension',
  'Now, read the passage and answer the questions.',
  'The office will remain closed on Monday. Employees may contact the support desk by email.',
  'Question 1. How can employees contact the support desk?',
  'A.', 'By telephone', 'B.', 'By email', 'C.', 'In person', 'D.', 'By regular mail',
], 'Reading Part 7');
await readingPromise;
assertOneSecondOptionCadence(4, 'Reading Part 7');
assert.match(readingAudioStatus.textContent, /Đã đọc xong/);

context.state.readings = [{ id: 'reading-part5-tts', part: 'Part 5', title: 'Incomplete Sentences', questions: [{ question: 'The team ___ the proposal yesterday.', choices: ['finish', 'finished', 'finishing', 'finishes'] }] }];
const readingPart5Start = spoken.length;
const readingPart5Promise = context.__playReadingText('reading-part5-tts');
await consumeSpeechSequence(readingPart5Start, [
  'Part 5: Incomplete Sentences',
  'Now, complete each sentence with the best answer.',
  'Question 1. The team ___ the proposal yesterday.',
  'A.', 'finish', 'B.', 'finished', 'C.', 'finishing', 'D.', 'finishes',
], 'Reading Part 5');
await readingPart5Promise;
assertOneSecondOptionCadence(4, 'Reading Part 5');
assert.match(readingAudioStatus.textContent, /Đã đọc xong/);

// Reading Part 6 must announce its own title and instruction before the text.
context.state.readings = [{ id: 'reading-part6-tts', part: 'Part 6', title: 'Text Completion', passage: 'The annual meeting has been moved to Friday. Employees should confirm attendance by Wednesday.', questions: [{ question: 'By when should employees confirm?', choices: ['Monday', 'Wednesday', 'Friday', 'Saturday'] }] }];
const readingPart6Start = spoken.length;
const readingPart6Promise = context.__playReadingText('reading-part6-tts');
await consumeSpeechSequence(readingPart6Start, [
  'Part 6: Text Completion',
  'Now, read the text and choose the best answer for each blank.',
  'The annual meeting has been moved to Friday. Employees should confirm attendance by Wednesday.',
  'Question 1. By when should employees confirm?',
  'A.', 'Monday', 'B.', 'Wednesday', 'C.', 'Friday', 'D.', 'Saturday',
], 'Reading Part 6');
await readingPart6Promise;
assertOneSecondOptionCadence(4, 'Reading Part 6');

// Mock transitions announce the heading/lead-in outside this player. The shared
// player must honor skipLeadIn and begin with the dialogue, not repeat either.
context.state.listening = [{ id: 'tts-mock-skip-leadin', part: 'Part 3', topic: 'Project Update', segments: [
  { speaker: 'Woman', voice: 'female', text: 'The project review starts at ten.' },
  { speaker: 'Man', voice: 'male', text: 'I will bring the revised schedule.' },
], questions: [{ question: 'When does the review start?', choices: ['At nine', 'At ten', 'At eleven', 'At noon'] }] }];
const mockSkipStart = spoken.length;
const mockSkipPromise = context.__playListeningAudio('tts-mock-skip-leadin', { skipLeadIn: true });
assert.equal(spoken[mockSkipStart]?.text, 'The project review starts at ten.', 'skipLeadIn starts directly with the listening content');
await consumeSpeechSequence(mockSkipStart, [
  'The project review starts at ten.',
  'I will bring the revised schedule.',
  'Question 1. When does the review start?',
  'A.', 'At nine', 'B.', 'At ten', 'C.', 'At eleven', 'D.', 'At noon',
], 'Mock Listening skipLeadIn');
await mockSkipPromise;
assertOneSecondOptionCadence(4, 'Guided Mock Listening');
assert.doesNotMatch(spoken.slice(mockSkipStart).map(item => item.text).join(' | '), /Part 3: Conversations|Now, listen to the conversation/,
  'Mock does not repeat the Part title or lead-in after its own transition');

// Reading and listening controls are present in source, and every speech route goes through the guarded queue.
assert.match(appSource, /data-reading-speak=/);
assert.equal((appSource.match(/\bsynth\.speak\(utterance\)/g) || []).length, 1, 'all TTS playback must use the shared guarded utterance function');
assert.match(appSource, /const SPEECH_START_TIMEOUT_MS = 10000/);
assert.match(appSource, /const SPEECH_END_TIMEOUT_MIN_MS = 20000/);
assert.doesNotMatch(appSource, /TTS_PREPARATION_DELAY_MS/);
assert.equal((appSource.match(/function\s+speakText\s*\(/g)||[]).length,1,'only one single-utterance route implementation may exist');
assert.equal((appSource.match(/function\s+speakUtterance\s*\(/g)||[]).length,1,'only one shared utterance guard may exist');
assert.match(appSource, /const PART1_TITLE_PAUSE_MS = 1000/);
assert.match(appSource, /const PART1_LEAD_IN_PAUSE_MS = 1000/);
assert.match(appSource, /const PART1_OPTION_LABEL_PAUSE_MS = 1500/);
assert.match(appSource, /const PART_OPTION_LABEL_PAUSE_MS = 1000/);
assert.match(appSource, /const PART_OPTION_GAP_MS = 1000/);
assert.match(appSource, /prepareSpeechEngine\(playbackToken\)/);
assert.match(appSource, /say\(isPart1\?/);
assert.match(appSource, /speakUtterance\(value,\{accent:segment\?\.accent\|\|cfg\.accent/);
assert.match(appSource, /'Part 2':\{name:'Question–Response'/);
assert.match(appSource, /PART_OPTION_LABEL_PAUSE_MS,playbackToken/);

console.log('Listening/TTS regression PASS: Parts 1–4 title/lead-in/content/question/lettered-choice sequence, Reading Parts 5–7, immediate gesture-stack playback, voice fallbacks, stale-event guard, speech watchdog, speaker pacing and safe cancellation.');

async function waitFor(predicate, message) {
  for (let attempt = 0; attempt < 100; attempt++) {
    if (predicate()) return;
    await new Promise(resolve => setImmediate(resolve));
  }
  assert.fail(`Timed out waiting for ${message}`);
}
function delay(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
