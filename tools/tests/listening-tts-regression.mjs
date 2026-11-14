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
const speedNode = { value: '0.85' };
const spoken = [];
const gapDurations = [];
let cancelCalls = 0;
let emitCancelEvent = false;
let voices = [];
let currentUtterance = null;
const speechSynthesis = {
  getVoices: () => voices,
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
  state: { settings: { tts: { ...DEFAULT_TTS_SETTINGS } }, listening: [], listeningProgress: {} },
  window: { speechSynthesis },
  SpeechSynthesisUtterance: MockUtterance,
  $: selector => selector === '#listeningSpeed' ? speedNode : statusNode,
  toast: message => { context.toasts.push(message); },
  toasts: [],
  setTimeout(callback, ms) { gapDurations.push(ms); queueMicrotask(callback); return gapDurations.length; },
  clearTimeout() {},
  queueMicrotask,
};
vm.createContext(context);
vm.runInContext(`${appSource.slice(start, end)}
globalThis.__chooseEnglishVoice = chooseEnglishVoice;
globalThis.__recommendedMaleVoice = recommendedMaleVoice;
globalThis.__playListeningAudio = playListeningAudio;
globalThis.__playListeningVocabulary = playListeningVocabulary;
globalThis.__stopSpeech = stopSpeech;
globalThis.__speakText = speakText;`, context, { timeout: 1000 });

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
context.__speakText('A preview sentence.');
assert.equal(spoken.at(-1).text, 'A preview sentence.');
context.__stopSpeech();
assert.equal(context.toasts.length, 0);

console.log('Listening/TTS regression PASS: manual voice priority, Daniel fallback, stable speaker voices, turn pauses, vocabulary pauses, per-lesson rate, safe stop without browser cancel callback, and canceled-preview handling.');

async function waitFor(predicate, message) {
  for (let attempt = 0; attempt < 100; attempt++) {
    if (predicate()) return;
    await new Promise(resolve => setImmediate(resolve));
  }
  assert.fail(`Timed out waiting for ${message}`);
}
function delay(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
