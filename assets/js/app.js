import { LocalNotificationProvider } from './notification-provider.js?__release=2.95.73';
import { buildRobotLearningInsights } from './robot-learning-insights.js?__release=2.95.73';
import { MOCK_MODES, createMockExam, getExamQuestions, getMockSectionForTime, scoreMockExam } from './mock-engine.js?__release=2.95.73';
import { buildMockScoreReadiness } from './mock-score-readiness.js?__release=2.95.73';
import { archiveAllPracticeAnswersForRetry, archivePracticeAnswerForRetry, countAttemptedPracticeQuestions, ensurePracticeProgress, getPracticeAttemptCount, getPracticeAttemptHistory, recordPracticeAnswer, summarizePracticeProgress, stagePracticeChoice, getPracticeDraftChoice, getPracticeDraftEntries, isPracticeDraftSetComplete, summarizePracticeDraftSet, commitPracticeDraftSet } from './practice-progress.js?__release=2.95.73';
import { chooseSentenceCompletionQuestion, validateSentenceCompletionBank } from './sentence-completion.js?__release=2.95.73';
import { buildObjectiveResourceIndex, ensureObjectiveProgress, recordObjectiveAttempt, recordExplanationRubric, summarizeAllObjectives, listDueRecallItems } from './learning-outcome-progress.js?__release=2.95.73';
import { recordFoundationAttempt, summarizeFoundationLesson, recordFoundationApplicationAttempt, summarizeFoundationApplication, recordFoundationRecallAttempt, listDueFoundationRecallItems, recordFoundationProductionAttempt, recordFoundationProductionRevision, summarizeFoundationOutcomeProgress, summarizeFoundationProductionPortfolio, buildFoundationProductionPortfolioMarkdown } from './foundation-evidence.js?__release=2.95.73';
import { recordFoundationReadingAttempt, summarizeFoundationReading } from './foundation-reading-evidence.js?__release=2.95.73';
import { recordFoundationListeningAttempt, summarizeFoundationListening } from './foundation-listening-evidence.js?__release=2.95.73';
import { recordAlphabetSoundPractice, summarizeAlphabetSoundProgress } from './alphabet-sound-progress.js?__release=2.95.73';
import { buildMockQuestionSchedule, getMockScheduledQuestion, getMockTransitionLeadIn, getMockQuestionTimeRemaining } from './mock-flow.js?__release=2.95.73';
import { detectLegacyReleaseAdditionRepair } from './vocabulary-release-integrity.js?__release=2.95.73';
import { createRobotBuddy } from './robot-buddy.js?__release=2.95.73';
import { renderAdditionalFlashSenses } from './flashcard-senses.js?__release=2.95.73';
import { getLearnerFacingRelatedGlossaryDefinition } from './related-glossary-quality.js?__release=2.95.73';
import { createLearnerBackup, validateLearnerBackup } from './learner-data-backup.js?__release=2.95.73';

// Keep this release marker synchronized with data/manifest.json and sw.js.
const APP_RELEASE_VERSION = '2.95.73';
function releaseDataUrl(path, version = APP_RELEASE_VERSION) {
  const url = new URL(path, document.baseURI);
  url.searchParams.set('__release', version);
  // Legacy workers strip __release but preserve __shell, forcing a fresh release-specific cache key.
  url.searchParams.set('__shell', version);
  return url.toString();
}
const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const icon = (name, cls='ui-icon') => `<svg class="${cls}" aria-hidden="true"><use href="#icon-${name}"></use></svg>`;

let learningFocusState = { active:false, kind:'', nodes:[] };
let assessmentResultFocusState = null;
function setLearningFocusHeader(title,subtitle='',eyebrow='FOCUSED LEARNING'){
  const titleNode=$('#learningFocusTitle'),subNode=$('#learningFocusSubtitle'),eyeNode=$('#learningFocusEyebrow');
  if(titleNode)titleNode.textContent=title||'Không gian học tập';
  if(subNode)subNode.textContent=subtitle||'Tập trung vào nội dung đang học.';
  if(eyeNode)eyeNode.textContent=eyebrow;
}
function showModalLayer(){
  const root=$('#learningFocusBackdrop'),layer=$('#modalLayer'),focusDialog=$('#learningFocusDialog');
  if(!root||!layer)return;
  if(!learningFocusState.active)root.classList.add('is-modal-only');
  root.hidden=false;
  layer.hidden=false;
  layer.setAttribute('aria-hidden','false');
  focusDialog?.setAttribute('aria-hidden','true');
  document.body.classList.add('has-modal-overlay');
}
function hideModalLayer(){
  const root=$('#learningFocusBackdrop'),layer=$('#modalLayer'),focusDialog=$('#learningFocusDialog');
  if(layer){layer.hidden=true;layer.setAttribute('aria-hidden','true');}
  document.body.classList.remove('has-modal-overlay');
  if(root?.classList.contains('is-modal-only')){
    root.classList.remove('is-modal-only');
    root.hidden=true;
  }
  focusDialog?.setAttribute('aria-hidden','false');
}
function openLearningFocus({kind='study',title,subtitle,eyebrow,elements=[]}={}){
  const backdrop=$('#learningFocusBackdrop'),host=$('#learningFocusContent');if(!backdrop||!host)return;
  if(!learningFocusState.active){learningFocusState={active:true,kind,nodes:[]};}
  else if(kind)learningFocusState.kind=kind;
  setLearningFocusHeader(title,subtitle,eyebrow);
  for(const selector of elements){
    const node=typeof selector==='string'?$(selector):selector;
    if(!node||learningFocusState.nodes.some(x=>x.node===node))continue;
    const placeholder=document.createComment(`learning-focus:${node.id||node.className||'panel'}`);
    node.parentNode?.insertBefore(placeholder,node);
    learningFocusState.nodes.push({node,placeholder});
    host.append(node);
  }
  backdrop.classList.remove('is-modal-only');
  backdrop.hidden=false;
  document.body.classList.add('has-learning-focus');
  requestAnimationFrame(()=>$('#learningFocusClose')?.focus({preventScroll:true}));
}
function openLearningDetail({kind='learning-detail',title,subtitle='Học theo cùng một không gian; nội dung dài sẽ cuộn trong khung chung.',eyebrow='TOEIC LEARNING',content}={}){
  const node=$('#modalContent');if(!node)return;
  stopSpeech();
  node.innerHTML=`<div class="learning-detail-surface">${content||''}</div>`;
  hideModalLayer();
  $('#modalLayer').classList.remove('is-learning-detail');
  openLearningFocus({kind,title,subtitle,eyebrow,elements:[node]});
}
function closeLearningFocus(){
  if(assessmentResultFocusState){void confirmPendingAssessmentResult({openReviewForSingle:false});return;}
  if($('#modalLayer')&&!$('#modalLayer').hidden){closeModal();return;}
  if(state.practiceReviewPending||state.autoAdvanceWaiting||state.pendingPracticeBatch||state.pendingFoundationAssessment||state.pendingSinglePractice||state.pendingFlashQuizResult||state.pendingPlacementResult||state.pendingMockResult){toast('Hãy hoàn tất hoặc đóng an toàn bước kết quả hiện tại trước khi rời phần đang làm.','error');return;}
  if(!learningFocusState.active)return;
  const kind=learningFocusState.kind;
  for(const entry of [...learningFocusState.nodes].reverse()){
    const {node,placeholder}=entry;
    if(placeholder?.parentNode){placeholder.parentNode.insertBefore(node,placeholder);placeholder.remove();}
  }
  learningFocusState={active:false,kind:'',nodes:[]};
  $('#learningFocusBackdrop').hidden=true;
  document.body.classList.remove('has-learning-focus');
  if(kind==='flashcards'){
    ['#flashSession','#flashQuiz','#flashResult'].forEach(sel=>{const el=$(sel);if(el)el.hidden=true;});
    state.flashSession=null;state.flashQuizAnswers=[];state.flashQuizIndex=0;renderFlashHome();
  }
  if(kind==='practice'){
    pauseAutoAdvance();const panel=$('.quiz-panel');if(panel)panel.hidden=true;
  }
  if(kind==='learning-detail'){
    stopSpeech();
    const content=$('#modalContent');if(content)content.innerHTML='';
    state.activeGrammarLesson=null;state.activeReading=null;state.activeListening=null;
  }
}
function syncPracticeModeSelection(mode){
  const select=$('#practiceMode');if(select&&mode)select.value=mode;
  $$('[data-practice-mode]').forEach(button=>{const selected=button.dataset.practiceMode===mode;button.classList.toggle('is-selected',selected);button.setAttribute('aria-pressed',String(selected));});
}
function updatePracticeFocusHeader(mode){
  const sentenceMode=mode==='sentence-completion';
  setLearningFocusHeader(sentenceMode?'Ôn tập TOEIC Part 5':'Ôn tập từ vựng',sentenceMode?'Đọc câu, xét ngữ pháp và ngữ cảnh, rồi chọn một phương án A–D.':'Một câu hỏi mỗi lần. Hoàn thành đáp án để xem giải thích và tiến độ.',sentenceMode?'TOEIC PART 5 · INCOMPLETE SENTENCES':'SMART REVIEW · FOCUSED SESSION');
}
function startPracticeFocus(forcedItemId=null){
  if(state.practiceReviewPending||state.autoAdvanceWaiting){toast('Hãy hoàn tất phần giải thích của câu hiện tại trước.','error');return;}
  const panel=$('.quiz-panel');if(!panel)return;
  const mode=$('#practiceMode')?.value||'random';
  panel.hidden=false;
  nextQuestion(mode,forcedItemId).then(started=>{
    if(!started){panel.hidden=true;return;}
    const actualMode=state.currentQuestion?.mode||mode;
    updatePracticeFocusHeader(actualMode);
    openLearningFocus({kind:'practice',title:actualMode==='sentence-completion'?'Ôn tập TOEIC Part 5':'Ôn tập từ vựng',subtitle:actualMode==='sentence-completion'?'Đọc câu, xét ngữ pháp và ngữ cảnh, rồi chọn một phương án A–D.':'Một câu hỏi mỗi lần. Hoàn thành đáp án để xem giải thích và tiến độ.',eyebrow:actualMode==='sentence-completion'?'TOEIC PART 5 · INCOMPLETE SENTENCES':'SMART REVIEW · FOCUSED SESSION',elements:[panel]});
  });
}
const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const DB_NAME = 'toeic-vocabulary-phase1';
const DB_STORE = 'workspace';
const DEFAULT_TTS_SETTINGS = { accent: 'en-US', defaultGender: 'female', maleVoiceURI: '', femaleVoiceURI: '', rate: 0.92, pitch: 1, volume: 1, wordPauseMs: 900, sentencePauseMs: 850 };
const SPEECH_START_TIMEOUT_MS = 10000;
const SPEECH_END_TIMEOUT_MIN_MS = 20000;
const PART1_TITLE_PAUSE_MS = 1000;
const PART1_LEAD_IN_PAUSE_MS = 1000;
const PART1_OPTION_LABEL_PAUSE_MS = 1500;
const PART1_OPTION_GAP_MS = 1300;
const PART_SEQUENCE_PAUSE_MS = 1000;
const PART_OPTION_LABEL_PAUSE_MS = 1000;
const PART_OPTION_GAP_MS = 1000;
const PART1_LEAD_IN_TEXT = 'Now, listen to the four statements.';
const state = { words: [], baseWords: [], dataManifest: null, vocabularyMigrationRestoredCount: 0, categories: [], sentenceCompletionItems: [], sentenceCompletionSeenIds: [], relatedTerms: new Map(), personalVocabulary: { schemaVersion: 3, additions: [], overrides: {}, overrideBaseSigs: {}, deletedBaseIds: [] }, staleOverrideIds: [], wordSources: new Map(), grammarLessons: [], foundationLessons: [], foundationReadingPassages: [], foundationReadingExtendedPassages: [], foundationReadingProgress: {}, foundationListeningClips: [], foundationListeningProgress: {}, foundationOutcomeRegistry: null, alphabetSoundItems: [], alphabetSoundProgress: {}, placementQuestions: [], placementObjectiveMap: null, objectiveResourceMap: null, objectiveResourceIndex: {}, objectiveProgress: {}, placementState: null, foundationProgress: {}, foundationStartLevel: 'ALL', readings: [], listening: [], grammarProgress: {}, readingProgress: {}, listeningProgress: {}, activeListening: null, speechRate: 1, activeGrammarLesson: null, activeReading: null, activeWordId: null, activeFoundationLesson: null, activePage: 'dashboard', activeLetter: '', deferredInstall: null, localWorkspace: false, progress: {}, reminder: null, settings: { autoNextEnabled: true, autoNextDelaySeconds: 3, tts: { ...DEFAULT_TTS_SETTINGS } }, notificationProvider: null, swRegistration: null, currentQuestion: null, questionStartedAt: null, questionAnswered: false, practiceReviewPending: false, sessionSeenIds: [], lastFeedback: null, autoAdvanceTimer: null, autoAdvanceTransitionTimer: null, autoAdvanceAt: null, autoAdvanceRemaining: null, autoAdvanceDuration: 3000, autoAdvanceCancelled: false, autoAdvanceWaiting: false, lastAIPrompt: '', lastGoogleQuery: '', flashProgress: {}, flashSession: null, flashQuizIndex: 0, flashQuizAnswers: [], pendingPracticeBatch: null, pendingFoundationAssessment: null, pendingSinglePractice: null, pendingFlashQuizResult: null, pendingPlacementResult: false, pendingMockResult: null, modalActionInProgress: false, foundationAssessmentDrafts: {}, mockExam: null, mockHistory: [], mockUsageCounts: {}, mockTickTimer: null, lastMockResult: null };

let robotBuddyEngine = null;
let robotIdleTimer = null;
let robotNudgeTimer = null;
let robotIdleStage = 0;
let robotIdleSnoozeUntil = 0;
let robotIdleNoticeTimes = [];
let robotChatInitialized = false;
let robotTypingTimer = null;
let robotSpeakingTimer = null;
let robotStreamState = null;
let robotBuddyMuted = false;
const ROBOT_BUDDY_SETTINGS_KEY = 'toeic:robot-buddy-settings:v1';

function openDB() {
  return new Promise((resolve, reject) => {
    if (!('indexedDB' in window)) return resolve(null);
    const request = indexedDB.open(DB_NAME, 1);
    request.onupgradeneeded = () => request.result.createObjectStore(DB_STORE);
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}
async function dbGet(key) {
  try {
    const db = await openDB();
    if (!db) return JSON.parse(localStorage.getItem(`toeic:${key}`) || 'null');
    return await new Promise((resolve,reject)=>{ const req=db.transaction(DB_STORE,'readonly').objectStore(DB_STORE).get(key); req.onsuccess=()=>resolve(req.result ?? null); req.onerror=()=>reject(req.error); });
  } catch {
    try { return JSON.parse(localStorage.getItem(`toeic:${key}`) || 'null'); } catch { return null; }
  }
}
async function dbSet(key,value) {
  try {
    const db = await openDB();
    if (!db) { localStorage.setItem(`toeic:${key}`, JSON.stringify(value)); return; }
    await new Promise((resolve,reject)=>{ const tx=db.transaction(DB_STORE,'readwrite'); tx.objectStore(DB_STORE).put(value,key); tx.oncomplete=()=>resolve(); tx.onerror=()=>reject(tx.error); });
  } catch { localStorage.setItem(`toeic:${key}`, JSON.stringify(value)); }
}
async function dbDelete(key) {
  try {
    const db = await openDB();
    if (!db) { localStorage.removeItem(`toeic:${key}`); return; }
    await new Promise((resolve,reject)=>{ const tx=db.transaction(DB_STORE,'readwrite'); tx.objectStore(DB_STORE).delete(key); tx.oncomplete=()=>resolve(); tx.onerror=()=>reject(tx.error); });
  } catch { localStorage.removeItem(`toeic:${key}`); }
}
function toast(message, type='success') {
  const el=document.createElement('div'); el.className=`toast ${type==='error'?'error':''}`; el.setAttribute('role',type==='error'?'alert':'status');
  const text=document.createElement('span'); text.className='toast-message'; text.textContent=message;
  const close=document.createElement('button'); close.className='toast-close'; close.type='button'; close.setAttribute('aria-label','Đóng thông báo'); close.title='Đóng thông báo'; close.textContent='×'; close.addEventListener('click',()=>el.remove());
  el.append(text,close); $('#toastRegion').append(el); setTimeout(()=>el.remove(),5000);
}
function normalizeText(value='') { return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/đ/g,'d').trim(); }
function escapeHtml(value='') { return String(value).replace(/[&<>\"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[ch])); }
function choiceIdAt(question,index){return Array.isArray(question?.choiceIds)?String(question.choiceIds[index]||''):'';}
function savedChoiceText(question,saved){
  if(!saved?.answered)return '';
  if(typeof saved.choiceText==='string'&&saved.choiceText.trim())return saved.choiceText;
  const index=Number(saved.choiceIndex);
  if(!Number.isInteger(index)||index<0)return '';
  const legacy=question?.legacyChoices?.[index];
  if(typeof legacy==='string')return legacy;
  return question?.choices?.[index]??'';
}
function savedChoiceIsArchived(question,saved){
  if(!saved?.answered)return false;
  const choiceId=String(saved.choiceId||'');
  if(choiceId&&Array.isArray(question?.choiceIds)&&question.choiceIds.includes(choiceId))return false;
  if(choiceId&&Array.isArray(question?.legacyChoiceIds)&&question.legacyChoiceIds.includes(choiceId))return true;
  const index=Number(saved.choiceIndex),text=savedChoiceText(question,saved);
  return Number.isInteger(index)&&index>=0&&text!==String(question?.choices?.[index]??'');
}
function savedChoiceWrongClass(question,saved,index){
  const choiceId=String(saved?.choiceId||'');
  const selectedIndex=choiceId&&Array.isArray(question?.choiceIds)?question.choiceIds.indexOf(choiceId):Number(saved?.choiceIndex);
  return Boolean(saved?.answered&&!savedChoiceIsArchived(question,saved)&&selectedIndex===index&&index!==question.answerIndex);
}
function savedChoiceHistoryMarkup(question,saved){
  if(!savedChoiceIsArchived(question,saved))return '';
  return `<span class="historical-choice-note">Lựa chọn đã lưu trước lần cập nhật: ${escapeHtml(savedChoiceText(question,saved))}</span>`;
}
function displayWord(value='') { const text=String(value); return text ? text.charAt(0).toLocaleUpperCase('en-US') + text.slice(1) : text; }
function getPrimarySense(item) { return item.senses?.[0] || {pos:'',meaning_vi:'',definition_en:'',synonyms:[],antonyms:[]}; }
function getAllPos(item) { return [...new Set((item.senses||[]).map(s=>s.pos).filter(Boolean))]; }
function topicsMarkup(topics=[]) { return `<div class="topic-list">${topics.slice(0,3).map(t=>`<span class="topic-tag">${escapeHtml(t)}</span>`).join('')}${topics.length>3?`<span class="topic-tag">+${topics.length-3}</span>`:''}</div>`; }
function posMarkup(item) { return getAllPos(item).map(p=>`<span class="pos-tag">${escapeHtml(p)}</span>`).join(' ') || '<span class="pos-tag">—</span>'; }
function sortWords(words) { return [...words].sort((a,b)=>a.word.localeCompare(b.word,'en',{sensitivity:'base'})); }
function normalizeRecord(raw) {
  if (!raw || typeof raw !== 'object') throw new Error('Bản ghi không hợp lệ.');
  const word = String(raw.word || '').trim();
  if (!word) throw new Error('Thiếu trường word.');
  const id = String(raw.id || `${normalizeText(word).replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')}-${Date.now().toString(36)}`).trim();
  let senses = Array.isArray(raw.senses) ? raw.senses : [];
  if (!senses.length && (raw.meaning_vi || raw.pos)) senses=[{pos:String(raw.pos||''),meaning_vi:String(raw.meaning_vi||''),definition_en:String(raw.definition_en||''),synonyms:raw.synonyms||[],antonyms:raw.antonyms||[]}];
  senses=senses.map(s=>({pos:String(s.pos||''),meaning_vi:String(s.meaning_vi||''),definition_en:String(s.definition_en||''),synonyms:Array.isArray(s.synonyms)?s.synonyms:String(s.synonyms||'').split(',').map(x=>x.trim()).filter(Boolean),antonyms:Array.isArray(s.antonyms)?s.antonyms:String(s.antonyms||'').split(',').map(x=>x.trim()).filter(Boolean)}));
  if (!senses.length) throw new Error(`Từ "${word}" cần có ít nhất một nghĩa hoặc loại từ.`);
  const topics=Array.isArray(raw.topics)?raw.topics:String(raw.topics||'').split(',').map(x=>x.trim().toUpperCase()).filter(Boolean);
  const examples=Array.isArray(raw.examples)?raw.examples:[];
  return {id,word,cefr_level:String(raw.cefr_level||raw.level||''),level_basis:String(raw.level_basis||'editorial-estimate'),phonetic:raw.phonetic&&typeof raw.phonetic==='object'?raw.phonetic:{us:String(raw.ipa||'')},senses,topics:[...new Set(topics)],word_family:Array.isArray(raw.word_family)?raw.word_family:[],verb_forms:raw.verb_forms&&typeof raw.verb_forms==='object'?raw.verb_forms:null,examples:examples.map(e=>({en:String(e.en||''),vi:String(e.vi||''),sense_index:Number.isInteger(e.sense_index)&&e.sense_index>=0&&e.sense_index<senses.length?e.sense_index:0})).sort((a,b)=>a.sense_index-b.sense_index),collocations:Array.isArray(raw.collocations)?raw.collocations:String(raw.collocations||'').split(',').map(x=>x.trim()).filter(Boolean)};
}
async function loadData() {
  // A release query is intentional: an older active Service Worker may still be
  // controlling an installed PWA while the new HTML/footer is already visible.
  // A new query key forces that worker to miss its old cache and fetch this release.
  const manifestResponse=await fetch(releaseDataUrl('./data/manifest.json'),{cache:'reload'});
  if(!manifestResponse.ok) throw new Error(`Không đọc được manifest.json (${manifestResponse.status}).`);
  const manifest=await manifestResponse.json();
  if(manifest.version!==APP_RELEASE_VERSION) throw new Error(`Lệch phiên bản dữ liệu: giao diện ${APP_RELEASE_VERSION}, manifest ${manifest.version||'không xác định'}. Hãy cập nhật lại bản phát hành đầy đủ.`);
  if(!Array.isArray(manifest.letters)||!manifest.letters.length) throw new Error('Manifest không có danh sách dữ liệu từ vựng A–Z hợp lệ.');
  const declaredTotal=manifest.letters.reduce((sum,item)=>sum+(Number.isInteger(item.count)?item.count:0),0);
  if(!Number.isInteger(manifest.totalWords)||declaredTotal!==manifest.totalWords) throw new Error(`Manifest không nhất quán: tổng count A–Z là ${declaredTotal}, totalWords là ${manifest.totalWords}.`);
  const fetchReleaseJson=(path)=>fetch(releaseDataUrl(path,manifest.version),{cache:'reload'});
  const [categoryResponse,relatedResponse,grammarResponse,readingResponse,listeningResponse,foundationResponse,foundationReadingResponse,foundationReadingExtendedResponse,foundationListeningResponse,alphabetSoundResponse,placementResponse,placementMapResponse,objectiveMapResponse,objectiveOutcomesResponse,...letterResponses]=await Promise.all([
    fetchReleaseJson(manifest.categories),
    fetchReleaseJson('./data/related-terms.json').catch(()=>null),
    fetchReleaseJson('./data/grammar/lessons.json'),
    fetchReleaseJson('./data/readings/reading-library.json'),
    fetchReleaseJson('./data/listening/listening-library.json'),
    fetchReleaseJson('./data/learning-path/pre-a1-a1.json'),
    fetchReleaseJson('./data/learning-path/foundation-reading.json'),
    fetchReleaseJson('./data/learning-path/foundation-reading-extended.json'),
    fetchReleaseJson('./data/learning-path/foundation-listening.json'),
    fetchReleaseJson('./data/learning-path/alphabet-sounds.json'),
    fetchReleaseJson('./data/learning-path/placement-diagnostic.json'),
    fetchReleaseJson('./data/learning-path/placement-objective-map.json'),
    fetchReleaseJson('./data/learning-path/objective-resource-map.json'),
    fetchReleaseJson('./data/learning-path/objective-outcomes.json'),
    ...manifest.letters.map(x=>fetchReleaseJson(x.file))
  ]);
  if(!categoryResponse.ok) throw new Error('Không đọc được categories.json.');
  if(!grammarResponse.ok) throw new Error('Không đọc được thư viện ngữ pháp.');
  if(!readingResponse.ok) throw new Error('Không đọc được thư viện đọc hiểu.');
  if(!listeningResponse.ok) throw new Error('Không đọc được thư viện nghe hiểu.');
  if(!foundationResponse.ok) throw new Error('Không đọc được lộ trình học từ đầu.');
  if(!foundationReadingResponse.ok) throw new Error('Không đọc được thư viện đọc hiểu Foundation.');
  if(!foundationReadingExtendedResponse.ok) throw new Error('Không đọc được thư viện đọc hiểu A2 mở rộng.');
  if(!foundationListeningResponse.ok) throw new Error('Không đọc được thư viện nghe hiểu Foundation.');
  if(!alphabetSoundResponse.ok) throw new Error('Không đọc được phòng luyện bảng chữ cái.');
  if(!placementResponse.ok) throw new Error('Không đọc được bộ đánh giá trình độ đầu vào.');
  if(!placementMapResponse.ok) throw new Error('Không đọc được bản đồ mục tiêu đánh giá đầu vào.');
  if(!objectiveMapResponse.ok) throw new Error('Không đọc được bản đồ mục tiêu học tập.');
  if(!objectiveOutcomesResponse.ok) throw new Error('Không đọc được khung tiêu chí kết quả học tập.');
  const [categoryData,grammarData,readingData,listeningData,foundationData,foundationReadingData,foundationReadingExtendedData,foundationListeningData,alphabetSoundData,placementData,placementMapData,objectiveMapData,objectiveOutcomesData]=await Promise.all([categoryResponse.json(),grammarResponse.json(),readingResponse.json(),listeningResponse.json(),foundationResponse.json(),foundationReadingResponse.json(),foundationReadingExtendedResponse.json(),foundationListeningResponse.json(),alphabetSoundResponse.json(),placementResponse.json(),placementMapResponse.json(),objectiveMapResponse.json(),objectiveOutcomesResponse.json()]);
  const sentenceCompletionResponse=await fetchReleaseJson('./data/practice/part5-sentence-completion.json');
  if(!sentenceCompletionResponse.ok)throw new Error('Không đọc được ngân hàng TOEIC Part 5.');
  const sentenceCompletionData=await sentenceCompletionResponse.json();
  if(relatedResponse?.ok){const relatedData=await relatedResponse.json();state.relatedTerms=new Map((relatedData.terms||[]).map(item=>[normalizedAnswer(item.term),item]));}else{state.relatedTerms=new Map();}
  const loaded=[];
  for(let i=0;i<letterResponses.length;i++){
    const response=letterResponses[i];
    const entry=manifest.letters[i];
    if(!response.ok) throw new Error(`Không đọc được dữ liệu chữ ${entry.letter} (${response.status}).`);
    const payload=await response.json();
    if(!Array.isArray(payload.words)) throw new Error(`Tệp ${entry.letter}.json không có mảng words.`);
    if(payload.letter!==entry.letter) throw new Error(`Sai dữ liệu chữ ${entry.letter}: payload tự khai báo chữ ${payload.letter||'trống'}.`);
    if(payload.words.length!==entry.count) throw new Error(`Dữ liệu từ vựng chữ ${entry.letter} chưa đồng bộ: manifest yêu cầu ${entry.count}, tải được ${payload.words.length}. Ứng dụng đã dừng để tránh hiển thị số từ sai.`);
    loaded.push(...payload.words.map(normalizeRecord));
  }
  const uniqueIds=new Set(loaded.map(item=>item.id));
  const uniqueWords=new Set(loaded.map(item=>normalizedAnswer(item.word)));
  if(loaded.length!==manifest.totalWords) throw new Error(`Dữ liệu từ vựng chưa đồng bộ: manifest ${manifest.totalWords} từ nhưng tải được ${loaded.length}. Hãy tải lại bản phát hành đầy đủ.`);
  if(uniqueIds.size!==loaded.length||uniqueWords.size!==loaded.length) throw new Error('Dữ liệu từ vựng có ID hoặc từ vựng trùng lặp; ứng dụng đã dừng để tránh tính sai số lượng.');
  state.dataManifest=manifest;
  state.baseWords=sortWords(loaded);
  state.categories=categoryData.categories||[];
  renderTopicShowcase();
  state.grammarLessons=Array.isArray(grammarData.lessons)?grammarData.lessons:[];
  state.readings=Array.isArray(readingData.readings)?readingData.readings:[];
  state.listening=Array.isArray(listeningData.listening)?listeningData.listening:[];
  state.foundationLessons=Array.isArray(foundationData.lessons)?foundationData.lessons:[];
  state.foundationReadingPassages=Array.isArray(foundationReadingData.passages)?foundationReadingData.passages:[];
  state.foundationReadingExtendedPassages=Array.isArray(foundationReadingExtendedData.passages)?foundationReadingExtendedData.passages:[];
  try{const saved=JSON.parse(localStorage.getItem('toeic:foundation-reading-progress:v1')||'{}');state.foundationReadingProgress=saved&&typeof saved==='object'?saved:{};}catch{state.foundationReadingProgress={};}
  state.foundationListeningClips=Array.isArray(foundationListeningData.clips)?foundationListeningData.clips:[];
  try{const saved=JSON.parse(localStorage.getItem('toeic:foundation-listening-progress:v1')||'{}');state.foundationListeningProgress=saved&&typeof saved==='object'?saved:{};}catch{state.foundationListeningProgress={};}
  state.alphabetSoundItems=Array.isArray(alphabetSoundData.letters)?alphabetSoundData.letters:[];
  try{const saved=JSON.parse(localStorage.getItem('toeic:alphabet-sound-progress:v1')||'{}');state.alphabetSoundProgress=saved&&typeof saved==='object'?saved:{};}catch{state.alphabetSoundProgress={};}
  state.placementQuestions=Array.isArray(placementData.questions)?placementData.questions:[];
  state.placementObjectiveMap=placementMapData&&Array.isArray(placementMapData.questionMappings)?placementMapData:null;
  state.objectiveResourceMap=objectiveMapData&&Array.isArray(objectiveMapData.objectives)?objectiveMapData:null;
  state.foundationOutcomeRegistry=objectiveOutcomesData&&Array.isArray(objectiveOutcomesData.objectives)?objectiveOutcomesData:null;
  state.objectiveResourceIndex=buildObjectiveResourceIndex(state.objectiveResourceMap||{});
  try{state.placementState=JSON.parse(localStorage.getItem('toeic:placement-diagnostic:v1')||'null');}catch{state.placementState=null;}
  try{const saved=JSON.parse(localStorage.getItem('toeic:foundation-progress:v1')||'{}');state.foundationProgress=saved&&typeof saved==='object'?saved:{};}catch{state.foundationProgress={};}
  try{const saved=JSON.parse(localStorage.getItem('toeic:foundation-assessment-drafts:v1')||'{}');state.foundationAssessmentDrafts=saved&&typeof saved==='object'?saved:{};}catch{state.foundationAssessmentDrafts={};}
  try{const level=localStorage.getItem('toeic:learning-start-level:v1');if(['ALL','PRE-A1','A1','A2','B1','B2','C1'].includes(level))state.foundationStartLevel=level;}catch{}
  state.sentenceCompletionItems=Array.isArray(sentenceCompletionData.questions)?sentenceCompletionData.questions:[];
  await loadPersonalVocabulary();
  const sentenceErrors=validateSentenceCompletionBank(state.sentenceCompletionItems,state.words);
  if(sentenceErrors.length)throw new Error(`Ngân hàng TOEIC Part 5 không hợp lệ: ${sentenceErrors.slice(0,3).join(' · ')}`);
  state.grammarProgress=await dbGet('grammarProgress')||{};
  state.readingProgress=await dbGet('readingProgress')||{};
  state.listeningProgress=await dbGet('listeningProgress')||{};
  state.objectiveProgress=ensureObjectiveProgress(await dbGet('objectiveProgress')||{});
  await migrateChoiceIdentity();
  state.flashProgress=await dbGet('flashProgress')||{};
  updateOverview(); renderToeicPartInsights(); populateFilters(); renderDictionary(); renderDataTable(); renderGrammarLibrary(); renderReadingLibrary(); renderListeningLibrary(); updateStorageLabel();
}
async function migrateChoiceIdentity(){
  const groups=[
    {progress:state.readingProgress,items:state.readings,key:'readingProgress',questionsKey:'questions'},
    {progress:state.listeningProgress,items:state.listening,key:'listeningProgress',questionsKey:'questions'},
    {progress:state.grammarProgress,items:state.grammarLessons,key:'grammarProgress',questionsKey:'exercises'}
  ];
  for(const group of groups){
    let changed=false;
    for(const item of group.items){
      const progress=ensurePracticeProgress(group.progress[item.id]||{});
      const answers=progress.answers;
      const questions=item[group.questionsKey]||[];
      const savedRecords=[...Object.entries(answers),...Object.entries(progress.attemptHistory).flatMap(([index,history])=>(Array.isArray(history)?history:[]).map(saved=>[index,saved]))];
      for(const [rawIndex,saved] of savedRecords){
        if(!saved?.answered)continue;
        const question=questions[Number(rawIndex)];
        if(!question)continue;
        const currentIds=Array.isArray(question.choiceIds)?question.choiceIds:[];
        const storedId=String(saved.choiceId||'');
        if(storedId){
          const currentIndex=currentIds.indexOf(storedId);
          if(currentIndex>=0){
            const oldIndex=Number(saved.choiceIndex);
            if(Number.isInteger(oldIndex)&&oldIndex>=0&&oldIndex!==currentIndex&&saved.previousChoiceIndex===undefined){saved.previousChoiceIndex=oldIndex;changed=true;}
            if(oldIndex!==currentIndex){saved.choiceIndex=currentIndex;changed=true;}
          }
          continue;
        }
        const oldIndex=Number(saved.choiceIndex);
        if(!Number.isInteger(oldIndex)||oldIndex<0)continue;
        const previousIds=Array.isArray(question.previousChoiceIds)?question.previousChoiceIds:[];
        const previousChoices=Array.isArray(question.previousChoices)?question.previousChoices:[];
        const legacyIds=Array.isArray(question.legacyChoiceIds)?question.legacyChoiceIds:[];
        const legacyChoices=Array.isArray(question.legacyChoices)?question.legacyChoices:[];
        if(oldIndex>=(previousIds.length||question.choices?.length||0))continue;
        let choiceId='',historicalText='';
        if(previousIds[oldIndex]){
          const legacyText=legacyChoices[oldIndex],previousText=previousChoices[oldIndex];
          const archivedLegacy=Boolean(legacyIds[oldIndex]&&typeof legacyText==='string'&&legacyText!==previousText&&(!saved.choiceText||saved.choiceText===legacyText));
          if(archivedLegacy){choiceId=String(legacyIds[oldIndex]);historicalText=legacyText;}
          else{choiceId=String(previousIds[oldIndex]);historicalText=typeof previousText==='string'?previousText:'';}
        }else{
          const savedText=typeof saved.choiceText==='string'?saved.choiceText.trim():'';
          const currentTextIndex=savedText?(question.choices||[]).findIndex(choice=>String(choice)===savedText):-1;
          const legacyText=legacyChoices[oldIndex];
          const hasLegacySnapshot=Boolean(legacyIds[oldIndex]&&typeof legacyText==='string'&&legacyText!==question.choices?.[oldIndex]);
          if(hasLegacySnapshot&&(!savedText||savedText===legacyText)){
            choiceId=String(legacyIds[oldIndex]);historicalText=legacyText;
          }else if(currentTextIndex>=0){
            choiceId=choiceIdAt(question,currentTextIndex);historicalText=savedText;
          }else if(savedText){
            // A non-matching stored text is ambiguous; preserve the record rather than guess its identity.
            continue;
          }else{
            choiceId=choiceIdAt(question,oldIndex);
            historicalText=String(question.choices?.[oldIndex]??'');
          }
        }
        if(!choiceId)continue;
        saved.choiceId=choiceId;changed=true;
        if(saved.previousChoiceIndex===undefined){saved.previousChoiceIndex=oldIndex;changed=true;}
        if((typeof saved.choiceText!=='string'||!saved.choiceText.trim())&&historicalText){saved.choiceText=historicalText;changed=true;}
        const currentIndex=currentIds.indexOf(choiceId);
        if(currentIndex>=0&&currentIndex!==oldIndex){saved.choiceIndex=currentIndex;changed=true;}
      }
    }
    if(changed)await dbSet(group.key,group.progress);
  }
}

function emptyPersonalVocabulary(){return {schemaVersion:3,additions:[],overrides:{},overrideBaseSigs:{},deletedBaseIds:[]};}
function recordSignature(record){return JSON.stringify(normalizeRecord(record));}
async function loadPersonalVocabulary(){
  const saved=await dbGet('personalVocabulary');
  if(saved&&typeof saved==='object'&&Array.isArray(saved.additions)&&saved.overrides&&Array.isArray(saved.deletedBaseIds)){
    const overrides=Object.fromEntries(Object.entries(saved.overrides).map(([id,record])=>[id,normalizeRecord(record)]));
    const overrideBaseSigs={...(saved.overrideBaseSigs||{})};
    let baseSignatureMigrationNeeded=Number(saved.schemaVersion||2)<3||!saved.overrideBaseSigs;
    // v2.10.0 migration: attach a base signature to every existing override without changing its content.
    for(const id of Object.keys(overrides)){
      if(!overrideBaseSigs[id]){
        const base=state.baseWords.find(w=>w.id===id);
        if(base){overrideBaseSigs[id]=recordSignature(base);baseSignatureMigrationNeeded=true;}
      }
    }
    state.personalVocabulary={schemaVersion:3,additions:saved.additions.map(normalizeRecord),overrides,overrideBaseSigs,deletedBaseIds:[...new Set(saved.deletedBaseIds.map(String))]};
    // Repair exact legacy 979/992-word migration artifacts without clearing
    // any other user-hidden words or personal overrides.
    const legacySnapshot=await dbGet('workspace');
    const repairIds=detectLegacyReleaseAdditionRepair({
      deletedBaseIds:state.personalVocabulary.deletedBaseIds,
      legacyRecords:legacySnapshot,
      baseWords:state.baseWords,
      releaseAdditionIds:state.dataManifest?.releaseAdditionIds||[],
      previousTotalWords:state.dataManifest?.previousReleaseTotalWords,
      releaseRepairProfiles:state.dataManifest?.releaseRepairProfiles||[],
      currentTotalWords:state.dataManifest?.totalWords
    });
    if(repairIds.length){
      const repairSet=new Set(repairIds);
      state.personalVocabulary.deletedBaseIds=state.personalVocabulary.deletedBaseIds.filter(id=>!repairSet.has(id));
      state.vocabularyMigrationRestoredCount=repairIds.length;
      baseSignatureMigrationNeeded=true;
    }
    if(baseSignatureMigrationNeeded){await dbSet('personalVocabulary',state.personalVocabulary);}
  } else {
    // One-time migration from older workspace format, preserving the source data as a recovery copy.
    const legacy=await dbGet('workspace');
    const personal=emptyPersonalVocabulary();
    if(Array.isArray(legacy)){
      const baseById=new Map(state.baseWords.map(w=>[w.id,w]));
      const baseByWord=new Map(state.baseWords.map(w=>[normalizedAnswer(w.word),w]));
      for(const raw of legacy){
        let record; try{record=normalizeRecord(raw);}catch{continue;}
        const base=baseById.get(record.id)||baseByWord.get(normalizedAnswer(record.word));
        if(base){
          record.id=base.id;
          if(recordSignature(record)!==recordSignature(base)){personal.overrides[base.id]=record;personal.overrideBaseSigs[base.id]=recordSignature(base);}
        } else personal.additions.push(record);
      }
      // An older workspace is a snapshot, not an explicit deletion ledger.
      // Missing IDs may simply have been added in a newer GitHub release; never
      // infer user deletion from absence during migration.
      personal.deletedBaseIds=[];
      await dbSet('personalVocabulary',personal);
    }
    state.personalVocabulary=personal;
  }
  rebuildEffectiveWords();
}
function rebuildEffectiveWords(){
  const personal=state.personalVocabulary||emptyPersonalVocabulary();
  const deleted=new Set(personal.deletedBaseIds||[]);
  const overrides=personal.overrides||{};
  const used=new Set();
  const merged=[];
  state.wordSources=new Map();
  state.staleOverrideIds=[];
  for(const base of state.baseWords){
    if(deleted.has(base.id))continue;
    const override=overrides[base.id];
    const item=override?normalizeRecord(override):base;
    if(override){
      const savedSig=personal.overrideBaseSigs?.[base.id];
      if(savedSig&&savedSig!==recordSignature(base))state.staleOverrideIds.push(base.id);
    }
    merged.push(item); used.add(item.id);
    state.wordSources.set(item.id,override?'personal-edit':'base');
  }
  for(const raw of personal.additions||[]){
    const item=normalizeRecord(raw);
    if(used.has(item.id))continue;
    if(merged.some(w=>normalizedAnswer(w.word)===normalizedAnswer(item.word)))continue;
    merged.push(item); used.add(item.id); state.wordSources.set(item.id,'personal-add');
  }
  state.words=sortWords(merged);
  state.localWorkspace=Object.keys(personal.overrides||{}).length>0||(personal.additions||[]).length>0||(personal.deletedBaseIds||[]).length>0;
  const staleNote=$('#staleOverrideNote');
  if(staleNote){staleNote.hidden=!state.staleOverrideIds.length;staleNote.textContent=state.staleOverrideIds.length?`${state.staleOverrideIds.length} bản ghi cá nhân đang dựa trên phiên bản từ điển gốc cũ. Nội dung cá nhân vẫn được giữ nguyên; hãy mở từng từ để đối chiếu trước khi khôi phục bản gốc.`:'';}
}
function getWordSource(id){return state.wordSources.get(id)||'base';}
function sourceBadgeMarkup(id){
  const source=getWordSource(id);
  const label=source==='base'?'TỪ ĐIỂN GỐC':source==='personal-edit'?'BẢN CÁ NHÂN':'TỪ CÁ NHÂN';
  return `<span class="source-badge ${source}">${label}</span>`;
}
function personalRecordCount(){return (state.personalVocabulary.additions||[]).length+Object.keys(state.personalVocabulary.overrides||{}).length+(state.personalVocabulary.deletedBaseIds||[]).length;}

function collectToeicPartStats(items,progressMap,parts){
  return parts.map(part=>{
    const subset=items.filter(item=>item.part===part);
    const total=subset.reduce((sum,item)=>sum+(item.questions||[]).length,0);
    let answered=0,correct=0,totalAttempts=0;
    subset.forEach(item=>{
      const progress=ensurePracticeProgress(progressMap[item.id]||{});
      const summary=summarizePracticeProgress(progress,(item.questions||[]).length);
      answered+=summary.attempted;correct+=summary.correct;totalAttempts+=summary.totalAttempts;
    });
    return {part,total,answered,correct,totalAttempts,accuracy:answered?Math.round(correct/answered*100):null,coverage:total?Math.round(answered/total*100):0};
  });
}
function renderPartStatCards(hostId,stats,area){
  const host=$(`#${hostId}`);if(!host)return;
  host.innerHTML=stats.map(stat=>`<button type="button" class="toeic-part-card" data-toeic-area="${area}" data-toeic-part="${stat.part}"><span class="toeic-part-name">${stat.part}</span><strong>${stat.answered}<small> / ${stat.total} câu</small></strong><span class="toeic-part-track"><i style="width:${stat.coverage}%"></i></span><span class="toeic-part-meta">${stat.accuracy===null?'Chưa có lượt làm':`${stat.accuracy}% đúng`} · ${stat.coverage}% hoàn thành · ${stat.totalAttempts} lượt làm</span></button>`).join('');
}
function renderToeicPartInsights(){
  if(!$('#toeicProgressPanel'))return;
  const listen=collectToeicPartStats(state.listening,state.listeningProgress,['Part 1','Part 2','Part 3','Part 4']);
  const read=collectToeicPartStats(state.readings,state.readingProgress,['Part 5','Part 6','Part 7']);
  renderPartStatCards('toeicListeningParts',listen,'listening');renderPartStatCards('toeicReadingParts',read,'reading');
  const attempted=[...listen,...read].filter(x=>x.answered>0).sort((a,b)=>(a.accuracy??100)-(b.accuracy??100));
  const priority=$('#toeicPriorityText');
  if(priority){
    if(!attempted.length)priority.textContent='Hoàn thành một số câu luyện tập để hệ thống xác định Part cần ưu tiên.';
    else {const weakest=attempted[0];priority.innerHTML=`<strong>Part nên ưu tiên:</strong> ${weakest.part} · ${weakest.accuracy}% đúng sau ${weakest.answered} câu đã làm. Nhấn vào thẻ Part để luyện tập tiếp.`;}
  }
}
function updateOverview(){
  $('#metricWords').textContent=state.baseWords.length.toLocaleString('vi-VN');
  const vocabularyStatus=$('#metricWordsStatus');
  if(vocabularyStatus){
    const baseCount=state.baseWords.length;
    const expected=Number(state.dataManifest?.totalWords||baseCount);
    const personalAdds=(state.personalVocabulary.additions||[]).length;
    const personalEdits=Object.keys(state.personalVocabulary.overrides||{}).length;
    const baseIds=new Set(state.baseWords.map(word=>word.id));
    const hiddenCount=new Set((state.personalVocabulary.deletedBaseIds||[]).filter(id=>baseIds.has(id))).size;
    const repairNote=state.vocabularyMigrationRestoredCount?` · đã khôi phục ${state.vocabularyMigrationRestoredCount} từ mới`:'';
    vocabularyStatus.textContent=`GitHub ${baseCount.toLocaleString('vi-VN')}/${expected.toLocaleString('vi-VN')} · hiện ${state.words.length.toLocaleString('vi-VN')} · ẩn ${hiddenCount}${personalAdds?` · +${personalAdds}`:''}${personalEdits?` · sửa ${personalEdits}`:''} · v${state.dataManifest?.version||APP_RELEASE_VERSION}${repairNote}`;
    vocabularyStatus.dataset.integrity=baseCount===expected?'verified':'mismatch';
  }
  $('#metricTopics').textContent=state.categories.length.toLocaleString('vi-VN');
  const letters=new Set(state.words.map(w=>w.word[0].toUpperCase()));
  $('#metricLetters').textContent=`${letters.size}/26`;
  $('#totalDataFooter').textContent=state.words.length.toLocaleString('vi-VN');
  const dash=$('#dashboardAlphabet');
  dash.innerHTML=ALPHABET.map(l=>{const n=state.words.filter(w=>w.word[0].toUpperCase()===l).length;return `<button class="letter-tile ${n?'has-words':''}" data-letter="${l}"><strong>${l}</strong><small>${n}</small></button>`}).join('');
  if(state.progress) updatePracticeStats();
  renderToeicPartInsights();
  renderLearningObjectiveProgress();
}
function renderTopicShowcase(){
 const host=$('#topicShowcase');if(!host)return;
 const meta={ALL:{label:'Tất cả',sub:'Toàn bộ từ vựng',file:'office.webp'},...Object.fromEntries(state.categories.map(c=>[c.id,{label:c.id.replaceAll('_',' ').toLowerCase().replace(/\b\w/g,x=>x.toUpperCase()),sub:c.label,file:FLASH_TOPIC_META[c.id]?.file||'office.webp'}]))};
 host.innerHTML=Object.entries(meta).map(([id,m])=>`<button class="topic-disc${id==='ALL'?' active':''}" data-topic="${id==='ALL'?'':escapeHtml(id)}"><img loading="lazy" src="./assets/topics/${escapeHtml(m.file)}" alt="${escapeHtml(m.sub)}"><span><strong>${escapeHtml(m.label)}</strong><small>${escapeHtml(m.sub)}</small></span></button>`).join('');
}
function populateFilters(){
  const options=state.categories.map(c=>`<option value="${escapeHtml(c.id)}">${escapeHtml(c.label)}</option>`).join('');
  $('#topicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+options;
  $('#dataTopicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+options;
  $('#dataLetterFilter').innerHTML='<option value="">Tất cả A–Z</option>'+ALPHABET.map(l=>`<option value="${l}">${l}</option>`).join('');
  const grammarCategories=[...new Set(state.grammarLessons.map(x=>x.category).filter(Boolean))].sort();
  const grammarPartFilter=$('#grammarPartFilter');if(grammarPartFilter)grammarPartFilter.innerHTML='<option value="">Tất cả Part</option>'+['Part 5','Part 6'].map(x=>`<option value="${x}">${x==='Part 5'?'Part 5 · Incomplete Sentences':'Part 6 · Text Completion'}</option>`).join('');
  $('#grammarCategoryFilter').innerHTML='<option value="">Tất cả nhóm</option>'+grammarCategories.map(x=>`<option value="${escapeHtml(x)}">${escapeHtml(x)}</option>`).join('');
  const grammarLevels=[...new Set(state.grammarLessons.map(x=>x.level).filter(Boolean))].sort();
  $('#grammarLevelFilter').innerHTML='<option value="">Tất cả cấp độ</option>'+grammarLevels.map(x=>`<option value="${escapeHtml(x)}">${escapeHtml(x)}</option>`).join('');
  const readingParts=[...new Set(state.readings.map(x=>x.part).filter(Boolean))].sort();
  const readingPartFilter=$('#readingPartFilter');if(readingPartFilter)readingPartFilter.innerHTML='<option value="">Tất cả Part</option>'+readingParts.map(x=>`<option value="${escapeHtml(x)}">${escapeHtml(x)}</option>`).join('');
  const readingTopics=[...new Set(state.readings.map(x=>x.topic).filter(Boolean))].sort();
  $('#readingTopicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+readingTopics.map(x=>`<option value="${escapeHtml(x)}">${escapeHtml(x)}</option>`).join('');
  const readingLevels=[...new Set(state.readings.map(x=>x.level).filter(Boolean))].sort();
  $('#readingLevelFilter').innerHTML='<option value="">Tất cả cấp độ</option>'+readingLevels.map(x=>`<option value="${escapeHtml(x)}">${escapeHtml(x)}</option>`).join('');
  const listeningLevels=[...new Set(state.listening.map(x=>x.level).filter(Boolean))].sort();
  $('#listeningLevelFilter').innerHTML='<option value="">Tất cả cấp độ</option>'+listeningLevels.map(x=>`<option value="${escapeHtml(x)}">${escapeHtml(x)}</option>`).join('');
}
function navigate(page){
  if(page!==state.activePage)setQuickHelpOpen(false);
  if(learningFocusState.active&&page!==state.activePage)closeLearningFocus();
  if(state.activePage==='listening'&&page!=='listening') stopSpeech();
  if(state.activePage==='mock'&&page!=='mock'&&state.mockExam?.status==='active') stopSpeech();
  if(state.activePage==='practice'&&page!=='practice') pauseAutoAdvance();
  state.activePage=page;
  $$('.page').forEach(p=>p.classList.toggle('active',p.id===`page-${page}`));
  $$('[data-page]').forEach(b=>b.classList.toggle('active',b.dataset.page===page));
  const titles={dashboard:'Tổng quan',foundation:'Lộ trình học',dictionary:'Từ vựng',flashcards:'Flashcard từ vựng',practice:'Ôn tập',mock:'Thi thử TOEIC',grammar:'Ngữ pháp',reading:'Đọc hiểu',listening:'Nghe hiểu',data:'Từ vựng cá nhân',settings:'Cấu hình'};
  $('#pageTitle').textContent=titles[page]||'Tổng quan';
  if(page==='dictionary') renderDictionary();
  if(page==='flashcards') renderFlashHome();
  if(page==='data') renderDataTable();
  if(page==='practice'){if(!state.currentQuestion)nextQuestion();renderQuestion();updatePracticeStats();resumeAutoAdvance();}
  if(page==='foundation') renderFoundationPath();
  if(page==='grammar') renderGrammarLibrary();
  if(page==='reading') renderReadingLibrary();
  if(page==='listening') renderListeningLibrary();
  if(page==='mock') openMockWorkspace();
  const quickHelpRoot=$('#quickHelp');if(quickHelpRoot)quickHelpRoot.hidden=page==='mock'&&state.mockExam?.status==='active';
  if(page==='settings') renderReminderStatus();
  window.scrollTo({top:0,behavior:'smooth'});
}
function filteredWords(){
  const query=normalizeText($('#dictionarySearch').value); const topic=$('#topicFilter').value; const pos=$('#posFilter').value; const level=$('#cefrFilter')?.value||''; const source=$('#dictionarySourceFilter')?.value||'all';
  return sortWords(state.words.filter(w=>{
    const origin=getWordSource(w.id);
    if(source==='base'&&origin!=='base')return false;
    if(source==='personal'&&!['personal-add','personal-edit'].includes(origin))return false;
    if(state.activeLetter && w.word[0].toUpperCase()!==state.activeLetter) return false;
    if(topic && !w.topics.includes(topic)) return false;
    if(pos && !w.senses.some(s=>s.pos.split('/').includes(pos))) return false;
    if(level && w.cefr_level!==level && !(w.senses||[]).some(s=>s.cefr_level===level)) return false;
    if(query){const search=[w.word,w.phonetic?.us,...w.senses.flatMap(s=>[s.meaning_vi,s.definition_en,...s.synonyms,...s.antonyms]),...w.topics].join(' ');if(!normalizeText(search).includes(query))return false;}
    return true;
  }));
}
function renderDictionary(){
  const alphabetRail=$('#alphabetFilter');
  const alphabetScroll=alphabetRail?.scrollLeft||0;
  alphabetRail.innerHTML=`<button class="alphabet-chip ${!state.activeLetter?'active':''}" data-letter="">ALL</button>`+ALPHABET.map(l=>`<button class="alphabet-chip ${state.activeLetter===l?'active':''}" data-letter="${l}">${l}</button>`).join('');
  alphabetRail.scrollLeft=alphabetScroll;
  const list=filteredWords(); $('#resultCount').textContent=`${list.length} từ vựng`;
  const topic=$('#topicFilter').value, pos=$('#posFilter').value, level=$('#cefrFilter')?.value||'', source=$('#dictionarySourceFilter')?.value||'all';
  const sourceCounts={base:state.words.filter(w=>getWordSource(w.id)==='base').length,personal:state.words.filter(w=>getWordSource(w.id)!=='base').length};
  $('#activeFilters').textContent=[state.activeLetter||'',topic||'',pos||'',level||'',source==='base'?'Từ điển gốc':source==='personal'?'Từ cá nhân':''].filter(Boolean).join(' · ')||`Gốc ${sourceCounts.base} · Cá nhân ${sourceCounts.personal}`;
  $('#wordTableBody').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<tr><td><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(displayWord(w.word))}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span>${sourceBadgeMarkup(w.id)}${w.cefr_level?`<span class="cefr-badge cefr-${escapeHtml(w.cefr_level.toLowerCase())}">${escapeHtml(w.cefr_level)}</span>`:''}</td><td>${posMarkup(w)}</td><td>${escapeHtml(s.meaning_vi||'—')}</td><td>${topicsMarkup(w.topics)}</td><td><button class="row-action" data-detail="${escapeHtml(w.id)}">Chi tiết →</button></td></tr>`}).join('');
  $('#wordCardList').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<article class="word-card"><div class="word-card-head"><div><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(displayWord(w.word))}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span>${sourceBadgeMarkup(w.id)}${w.cefr_level?`<span class="cefr-badge cefr-${escapeHtml(w.cefr_level.toLowerCase())}">${escapeHtml(w.cefr_level)}</span>`:''}</div>${posMarkup(w)}</div><div class="word-meaning">${escapeHtml(s.meaning_vi||'—')}</div>${topicsMarkup(w.topics)}</article>`}).join('');
  $('#dictionaryEmpty').hidden=list.length>0;
}
function renderDataTable(){
  const q=normalizeText($('#dataSearch').value); const letter=$('#dataLetterFilter').value; const topic=$('#dataTopicFilter').value; const pos=$('#dataPosFilter').value; const source=$('#dataSourceFilter')?.value||'all';
  const list=sortWords(state.words.filter(w=>{
    const origin=getWordSource(w.id);
    if(source==='base'&&origin!=='base')return false;
    if(source==='personal'&&!['personal-add','personal-edit'].includes(origin))return false;
    if(source==='overrides'&&origin!=='personal-edit')return false;
    if(letter && w.word[0].toUpperCase()!==letter) return false;
    if(topic && !w.topics.includes(topic)) return false;
    if(pos && !w.senses.some(s=>s.pos.split('/').includes(pos))) return false;
    return !q || normalizeText([w.word,...w.senses.flatMap(s=>[s.meaning_vi,s.definition_en,...s.synonyms,...s.antonyms]),...w.topics].join(' ')).includes(q);
  }));
  const baseCount=state.baseWords.length;
  const addCount=state.personalVocabulary.additions.length;
  const editCount=Object.keys(state.personalVocabulary.overrides).length;
  const levelCounts=['A1','A2','B1','B2'].map(level=>`${level} ${state.words.filter(w=>w.cefr_level===level).length}`).join(' · '); $('#dataCount').textContent=`${list.length} / ${state.words.length} từ đang hiển thị · ${baseCount} gốc · ${addCount} cá nhân mới · ${editCount} bản chỉnh riêng · ${levelCounts}`;
  $('#dataTableBody').innerHTML=list.map(w=>{
    const s=getPrimarySense(w),origin=getWordSource(w.id);
    const sourceLabel=origin==='base'?'GỐC · CHỈ ĐỌC':origin==='personal-edit'?'CÁ NHÂN · BẢN RIÊNG':'CÁ NHÂN · TỰ THÊM';
    const actions=origin==='base'?`<span class="read-only-label">Chỉ đọc</span><button class="row-action" data-edit="${escapeHtml(w.id)}">Tạo bản cá nhân</button>`:`<div class="row-actions"><button class="row-action icon-action" data-edit="${escapeHtml(w.id)}" title="Sửa dữ liệu cá nhân" aria-label="Sửa ${escapeHtml(displayWord(w.word))}">${icon('edit')}</button><button class="row-action icon-action danger-text" data-delete="${escapeHtml(w.id)}" title="Xóa khỏi thiết bị này" aria-label="Xóa ${escapeHtml(displayWord(w.word))}">${icon('trash')}</button></div>`;
    return `<tr><td><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(displayWord(w.word))}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span><span class="source-badge ${origin}">${sourceLabel}</span></td><td>${posMarkup(w)}</td><td>${escapeHtml(s.meaning_vi||'—')}</td><td>${topicsMarkup(w.topics)}</td><td>${actions}</td></tr>`;
  }).join('');
  $('#dataEmpty').hidden=list.length>0;
  updateStorageLabel();
}

function posDisplayLabel(pos=''){
  const labels={n:'Danh từ',v:'Động từ',adj:'Tính từ',adv:'Trạng từ',prep:'Giới từ',pron:'Đại từ',conj:'Liên từ',det:'Từ hạn định',aux:'Trợ động từ',interj:'Thán từ',num:'Số từ'};
  return String(pos||'—').split(/[\/,\s]+/).filter(Boolean).map(code=>labels[code.toLowerCase()]||code.toUpperCase()).join(' / ')||'Chưa phân loại';
}
function posCodes(pos=''){
  return String(pos||'').toLowerCase().split(/[\/,\s]+/).filter(Boolean);
}
function showDetail(id){
  const w=state.words.find(x=>x.id===id); if(!w)return;state.activeWordId=id;
  const origin=getWordSource(id);
  const originLabel=origin==='base'?'Từ vựng gốc · chỉ đọc':origin==='personal-edit'?'Bản cá nhân ghi đè từ gốc':'Từ vựng cá nhân';
  $('#modalEyebrow').textContent='VOCABULARY DETAIL'; $('#modalTitle').textContent='Chi tiết từ vựng';
  const groups=[];
  (w.senses||[]).forEach((sense,index)=>{
    const key=String(sense.pos||'—').trim().toLowerCase();
    let group=groups.find(item=>item.key===key);
    if(!group){group={key,pos:sense.pos||'—',senses:[]};groups.push(group);}
    group.senses.push({sense,index});
  });
  const senseCards=groups.map(group=>{
    const meanings=group.senses.map(({sense,index})=>{
      const related=`${sense.synonyms?.length?`<div class="sense-relations"><span class="sense-relation-label">Gần nghĩa</span><div class="detail-pills">${sense.synonyms.map(x=>`<span class="detail-pill">≈ ${escapeHtml(x)}</span>`).join('')}</div></div>`:''}${sense.antonyms?.length?`<div class="sense-relations"><span class="sense-relation-label">Trái nghĩa</span><div class="detail-pills">${sense.antonyms.map(x=>`<span class="detail-pill">≠ ${escapeHtml(x)}</span>`).join('')}</div></div>`:''}`;
      const examples=(w.examples||[]).filter(example=>Number.isInteger(example.sense_index)?example.sense_index===index:index===0).map(example=>`<div class="example-card"><strong>${escapeHtml(example.en)}</strong><span>${escapeHtml(example.vi)}</span></div>`).join('');
      return `<article class="meaning-entry"><div class="meaning-entry-title">${escapeHtml(sense.meaning_vi||'Chưa có nghĩa')}</div>${sense.definition_en?`<p class="meaning-definition">${escapeHtml(sense.definition_en)}</p>`:''}${related}${examples?`<div class="sense-examples"><span class="sense-example-label">VÍ DỤ NGỮ CẢNH</span>${examples}</div>`:''}</article>`;
    }).join('');
    const includesVerb=group.senses.some(({sense})=>posCodes(sense.pos).includes('v'));
    const verbForms=includesVerb&&w.verb_forms?`<div class="verb-form-block"><span class="sense-example-label">CÁC DẠNG ĐỘNG TỪ</span><div class="detail-pills">${Object.entries({V1:w.verb_forms.v1,'V-s/es':w.verb_forms.vs_es,V2:w.verb_forms.v2,V3:w.verb_forms.v3,'V-ing':w.verb_forms.ving}).filter(x=>x[1]).map(([k,v])=>`<span class="detail-pill"><strong>${k}:</strong> ${escapeHtml(v)}</span>`).join('')}</div></div>`:'';
    return `<section class="pos-detail-card"><header class="pos-detail-header"><strong>${escapeHtml(posDisplayLabel(group.pos))}</strong><span>${escapeHtml(group.pos)}</span></header><div class="pos-detail-body">${meanings}${verbForms}</div></section>`;
  }).join('');
  const family=w.word_family?.length?`<div class="detail-section"><h4>WORD FAMILY</h4><div class="detail-pills">${w.word_family.map(x=>`<span class="detail-pill"><strong>${escapeHtml(displayWord(x.word))}</strong> · ${escapeHtml(x.pos||'')} — ${escapeHtml(x.meaning_vi||'')}</span>`).join('')}</div></div>`:'';
  const editButton=origin==='base'?`<button class="secondary-button" data-edit="${escapeHtml(w.id)}">${icon('edit','ui-icon button-icon')} Tạo bản cá nhân</button>`:`<button class="secondary-button" data-edit="${escapeHtml(w.id)}">${icon('edit','ui-icon button-icon')} Sửa từ cá nhân</button>`;
  $('#modalContent').innerHTML=`<div class="word-origin-note">${escapeHtml(originLabel)} · Không thay đổi dữ liệu gốc trên GitHub.</div><h3 class="detail-word">${escapeHtml(displayWord(w.word))}</h3><div class="detail-ipa">${escapeHtml(w.phonetic?.us||'Chưa có phiên âm')}</div><div class="detail-cefr">${w.cefr_level?`CEFR ${escapeHtml(w.cefr_level)} · mức gợi ý học tập`:'Chưa gắn cấp độ CEFR'}</div><div class="pronunciation-toolbar"><button type="button" class="secondary-button" data-speak-word="${escapeHtml(w.word)}" data-accent="en-US">${icon('volume-2','ui-icon button-icon')} Nghe giọng Mỹ</button><button type="button" class="secondary-button" data-speak-word="${escapeHtml(w.word)}" data-accent="en-GB">${icon('volume-2','ui-icon button-icon')} Nghe giọng Anh</button><button type="button" class="text-button" data-stop-speech>⏹ Dừng</button></div><p class="pronunciation-note">Âm thanh do giọng đọc tiếng Anh có sẵn trên trình duyệt/thiết bị tổng hợp.</p><div class="detail-section pos-groups-section"><h4>NGHĨA THEO TỪ LOẠI</h4><div class="pos-detail-grid">${senseCards||'<p>Chưa có nghĩa.</p>'}</div></div>${family}<div class="detail-section"><h4>TOPICS</h4>${topicsMarkup(w.topics)}</div>${w.collocations?.length?`<div class="detail-section"><h4>COLLOCATIONS</h4><div class="detail-pills">${w.collocations.map(x=>`<span class="detail-pill">${escapeHtml(x)}</span>`).join('')}</div></div>`:''}<div class="modal-actions"><button class="secondary-button" data-ai-word="${escapeHtml(w.id)}">${icon('sparkles','ui-icon button-icon')} Tra cứu Google AI</button>${editButton}</div>`;
  showModalLayer();
}
function openEditor(id=null){
  const old=state.words.find(w=>w.id===id); const s=old?.senses?.[0]||{}; const origin=old?getWordSource(id):'new';
  $('#modalEyebrow').textContent=old?'PERSONAL VOCABULARY · EDIT':'PERSONAL VOCABULARY · NEW';
  $('#modalTitle').textContent=old?(origin==='base'?'Tạo bản cá nhân từ từ gốc':'Chỉnh sửa từ vựng cá nhân'):'Thêm từ vựng cá nhân';
  const topicOptions=state.categories.map(c=>`<option value="${escapeHtml(c.id)}">${escapeHtml(c.id)} · ${escapeHtml(c.label)}</option>`).join('');
  const isBase=origin==='base';
  $('#modalContent').innerHTML=`<div class="personal-editor-note"><strong>${isBase?'Bạn đang tạo một bản ghi cá nhân dựa trên từ gốc.':'Đây là dữ liệu riêng của thiết bị.'}</strong><p>${isBase?'Từ gốc trên GitHub được giữ nguyên. Mọi thay đổi chỉ tạo bản ghi ghi đè cục bộ và có thể khôi phục.':'Thêm/sửa/xóa nội dung này không ảnh hưởng đến kho từ vựng gốc.'}</p></div><form id="wordEditorForm"><div class="editor-grid">
  <label class="field"><span class="field-label">TỪ TIẾNG ANH *</span><input name="word" required value="${escapeHtml(old?displayWord(old.word):'')}" placeholder="Ví dụ: Schedule"></label>
  <label class="field"><span class="field-label">PHIÊN ÂM IPA</span><input name="ipa" value="${escapeHtml(old?.phonetic?.us||'')}" placeholder="/ˈskedʒ.uːl/"></label>
  <label class="field"><span class="field-label">LOẠI TỪ CHÍNH *</span><select name="pos"><option value="n">n – Danh từ</option><option value="v">v – Động từ</option><option value="adj">adj – Tính từ</option><option value="adv">adv – Trạng từ</option><option value="prep">prep – Giới từ</option><option value="conj">conj – Liên từ</option><option value="pron">pron – Đại từ</option><option value="n/v">n/v – Danh từ / Động từ</option></select></label>
  <label class="field"><span class="field-label">CHỦ ĐỀ (CÓ THỂ CHỌN NHIỀU)</span><select name="topics" multiple size="3">${topicOptions}</select></label>
  <label class="field full"><span class="field-label">NGHĨA TIẾNG VIỆT *</span><input name="meaning" required value="${escapeHtml(s.meaning_vi||'')}" placeholder="Nghĩa tiếng Việt"></label>
  <label class="field full"><span class="field-label">GIẢI THÍCH TIẾNG ANH</span><input name="definition" value="${escapeHtml(s.definition_en||'')}" placeholder="English definition"></label>
  <label class="field"><span class="field-label">TỪ ĐỒNG NGHĨA</span><input name="synonyms" value="${escapeHtml((s.synonyms||[]).join(', '))}" placeholder="arrange, plan"></label>
  <label class="field"><span class="field-label">TỪ TRÁI NGHĨA</span><input name="antonyms" value="${escapeHtml((s.antonyms||[]).join(', '))}" placeholder="cancel"></label>
  <label class="field full"><span class="field-label">VÍ DỤ TIẾNG ANH</span><input name="exampleEn" value="${escapeHtml(old?.examples?.[0]?.en||'')}" placeholder="The manager scheduled a meeting."></label>
  <label class="field full"><span class="field-label">DỊCH VÍ DỤ</span><input name="exampleVi" value="${escapeHtml(old?.examples?.[0]?.vi||'')}" placeholder="Quản lý đã lên lịch cuộc họp."></label>
  <label class="field full"><span class="field-label">COLLOCATIONS</span><input name="collocations" value="${escapeHtml((old?.collocations||[]).join(', '))}" placeholder="work schedule, daily schedule"></label>
  </div><p class="editor-help">Các trường có dấu * là bắt buộc. Bản cá nhân được lưu trong IndexedDB của thiết bị này.</p><div class="modal-actions"><button type="submit" class="primary-button">Lưu từ vựng cá nhân</button>${origin==='personal-edit'?`<button type="button" class="secondary-button" id="restoreBaseWord">Khôi phục từ gốc</button>`:''}</div></form>`;
  const form=$('#wordEditorForm'); form.elements.pos.value=s.pos||'n';
  const topics=old?.topics||[]; [...form.elements.topics.options].forEach(o=>o.selected=topics.includes(o.value));
  showModalLayer();
  form.addEventListener('submit',async e=>{
    e.preventDefault(); const fd=new FormData(form); const w=String(fd.get('word')).trim(); const pos=String(fd.get('pos'));
    const record=normalizeRecord({id:old?.id||undefined,word:w,phonetic:{us:String(fd.get('ipa')||'')},senses:[{pos,meaning_vi:String(fd.get('meaning')||''),definition_en:String(fd.get('definition')||''),synonyms:String(fd.get('synonyms')||'').split(',').map(x=>x.trim()).filter(Boolean),antonyms:String(fd.get('antonyms')||'').split(',').map(x=>x.trim()).filter(Boolean)},...(old?.senses?.slice(1)||[])],topics:[...form.elements.topics.selectedOptions].map(o=>o.value),examples:[{en:String(fd.get('exampleEn')||''),vi:String(fd.get('exampleVi')||''),sense_index:0},...(old?.examples?.slice(1)||[])].filter(x=>x.en||x.vi),collocations:String(fd.get('collocations')||'').split(',').map(x=>x.trim()).filter(Boolean),word_family:old?.word_family||[],verb_forms:old?.verb_forms||null});
    const duplicate=state.words.find(x=>x.id!==old?.id&&normalizeText(x.word)===normalizeText(record.word));
    if(duplicate){toast(`Từ này đã tồn tại: ${displayWord(duplicate.word)}. Hãy mở bản ghi đó để tạo bản cá nhân.`, 'error');return;}
    if(old&&state.baseWords.some(x=>x.id===old.id)){state.personalVocabulary.overrides[old.id]=record;const base=state.baseWords.find(x=>x.id===old.id);if(base)state.personalVocabulary.overrideBaseSigs[old.id]=recordSignature(base);}
    else if(old) state.personalVocabulary.additions=state.personalVocabulary.additions.map(x=>x.id===old.id?record:x);
    else state.personalVocabulary.additions.push(record);
    await persistPersonalVocabulary(); closeModal(); updateOverview(); renderDictionary(); renderDataTable(); renderQuestion(); toast(old?'Đã lưu thay đổi trong dữ liệu cá nhân.':'Đã thêm từ vựng cá nhân.');
  });
  $('#restoreBaseWord')?.addEventListener('click',async()=>{delete state.personalVocabulary.overrides[id];delete state.personalVocabulary.overrideBaseSigs[id];await persistPersonalVocabulary();closeModal();updateOverview();renderDictionary();renderDataTable();toast('Đã khôi phục bản gốc từ GitHub.');});
}
async function persistPersonalVocabulary(){
  state.personalVocabulary.additions=sortWords(state.personalVocabulary.additions.map(normalizeRecord));
  state.personalVocabulary.deletedBaseIds=[...new Set(state.personalVocabulary.deletedBaseIds)];
  await dbSet('personalVocabulary',state.personalVocabulary); rebuildEffectiveWords(); updateStorageLabel();
}
function updateStorageLabel(){
  const add=state.personalVocabulary.additions.length, edit=Object.keys(state.personalVocabulary.overrides).length, hidden=state.personalVocabulary.deletedBaseIds.length;
  const label=$('#storageLabel'); if(label)label.textContent=`Dữ liệu cá nhân trên thiết bị: ${add} thêm · ${edit} sửa · ${hidden} ẩn từ gốc (IndexedDB)`;
}
async function deleteWord(id){
  const item=state.words.find(w=>w.id===id); if(!item)return;
  const origin=getWordSource(id); const message=origin==='base'?`Ẩn từ gốc “${displayWord(item.word)}” trên thiết bị này? Dữ liệu gốc trên GitHub không bị xóa.`:`Xóa “${displayWord(item.word)}” khỏi từ vựng cá nhân trên thiết bị này?`;
  if(!confirm(message))return;
  if(state.baseWords.some(w=>w.id===id)){state.personalVocabulary.deletedBaseIds.push(id);delete state.personalVocabulary.overrides[id];delete state.personalVocabulary.overrideBaseSigs[id];}
  else state.personalVocabulary.additions=state.personalVocabulary.additions.filter(w=>w.id!==id);
  await persistPersonalVocabulary(); updateOverview(); renderDictionary(); renderDataTable(); renderQuestion(); toast('Đã cập nhật danh sách từ vựng cá nhân.');
}
function resetModalLayer(){
  const layer=$('#modalLayer');if(!layer)return;
  stopSpeech();
  layer.classList.remove('is-practice-review','is-auto-advance-wait','is-learning-detail');
  delete layer.dataset.modalType;
  $('#closeModal').hidden=false;
  $('#closeModal').setAttribute('aria-label','Đóng cửa sổ');
  $('#closeModal').removeAttribute('title');
  hideModalLayer();
  $('#modalContent').innerHTML='';
}
async function confirmPendingAssessmentResult({openReviewForSingle=false}={}){
  if(state.modalActionInProgress)return;
  state.modalActionInProgress=true;
  try{
    if(state.pendingPracticeBatch)await confirmPracticeBatchResult();
    else if(state.pendingFoundationAssessment)await confirmFoundationAssessmentResult();
    else if(state.pendingSinglePractice)await confirmSinglePracticeResult({openReview:openReviewForSingle});
    else if(state.pendingFlashQuizResult)await confirmFlashQuizResult();
    else if(state.pendingPlacementResult){state.pendingPlacementResult=false;closeAssessmentResultModal();finalizePlacementDiagnostic();}
    else if(state.pendingMockResult)await confirmMockExamResult();
    else closeAssessmentResultModal();
  }catch(error){
    console.error('Không thể hoàn tất bước kết quả:',error);
    toast(`Chưa thể hoàn tất kết quả: ${error?.message||'Lỗi lưu dữ liệu'}. Hãy thử lại.`, 'error');
  }finally{state.modalActionInProgress=false;}
}
async function dismissPracticeReviewModal(){
  if(!state.practiceReviewPending){resetModalLayer();return;}
  clearAutoAdvance();
  state.practiceReviewPending=false;
  state.autoAdvanceWaiting=false;
  state.autoAdvanceCancelled=true;
  resetModalLayer();
  renderQuestion();
  $('#nextQuestionButton').disabled=!state.questionAnswered;
  await savePracticeSession();
  updateAutoAdvanceUI();
  toast('Đã đóng phần giải thích. Kết quả vẫn được giữ; bạn có thể xem lại ngay trên câu hiện tại.');
}
function closeModal(){
  const layer=$('#modalLayer');if(!layer||layer.hidden)return;
  const modalType=layer.dataset.modalType||'';
  if(modalType==='assessment-result'){
    void confirmPendingAssessmentResult({openReviewForSingle:false});
    return;
  }
  if(modalType==='practice-review'){
    void dismissPracticeReviewModal().catch(error=>{console.error(error);toast('Không thể lưu trạng thái câu hỏi. Hãy thử lại.','error');});
    return;
  }
  if(modalType==='practice-wait'){
    void cancelAutoAdvanceWait().catch(error=>{console.error(error);toast('Không thể hủy tự chuyển câu. Hãy thử lại.','error');});
    return;
  }
  if(state.pendingPracticeBatch||state.pendingFoundationAssessment||state.pendingSinglePractice||state.pendingFlashQuizResult||state.pendingPlacementResult||state.pendingMockResult){
    void confirmPendingAssessmentResult({openReviewForSingle:false});
    return;
  }
  if(state.practiceReviewPending){void dismissPracticeReviewModal();return;}
  if(state.autoAdvanceWaiting){void cancelAutoAdvanceWait();return;}
  resetModalLayer();
}
function downloadFile(name,content,type){const blob=new Blob([content],{type});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
async function collectLearnerStorageSnapshot(){
  const db=await openDB();if(!db)throw new Error('IndexedDB không khả dụng; không thể tạo bản sao lưu đầy đủ.');
  try{
    const indexedDBEntries=await new Promise((resolve,reject)=>{const tx=db.transaction(DB_STORE,'readonly');const store=tx.objectStore(DB_STORE);const entries=[];const request=store.openCursor();request.onsuccess=()=>{const cursor=request.result;if(cursor){if(typeof cursor.key!=='string')return reject(new Error('Phát hiện khóa IndexedDB không phải chuỗi; dừng để tránh mất dữ liệu.'));entries.push({key:cursor.key,value:cursor.value});cursor.continue();}else resolve(entries);};request.onerror=()=>reject(request.error);tx.onerror=()=>reject(tx.error);});
    const localStorageEntries=[];for(let i=0;i<localStorage.length;i++){const key=localStorage.key(i);if(key?.startsWith('toeic:'))localStorageEntries.push({key,value:localStorage.getItem(key)});}localStorageEntries.sort((a,b)=>a.key.localeCompare(b.key));
    return {indexedDBEntries,localStorageEntries};
  }finally{db.close();}
}
async function buildFullLearnerBackup(){
  let storagePersistence={supported:!!navigator.storage?.persist,requested:false,granted:null};
  if(navigator.storage?.persist){storagePersistence.requested=true;try{storagePersistence.granted=await navigator.storage.persist();}catch(error){storagePersistence.error=String(error?.message||error);}}
  const snapshot=await collectLearnerStorageSnapshot();return createLearnerBackup({...snapshot,storagePersistence});
}
async function exportLearnerBackup(){
  const button=$('#exportLearnerBackupButton');if(button)button.disabled=true;
  try{const backup=await buildFullLearnerBackup();const json=JSON.stringify(backup,null,2);downloadFile(`toeic-learner-backup-${new Date().toISOString().replace(/[:.]/g,'-')}.json`,json,'application/json;charset=utf-8');const status=$('#learnerBackupStatus');if(status)status.textContent=`Đã tạo bản sao lưu: ${backup.storage.indexedDB.entries.length} khóa IndexedDB và ${backup.storage.localStorage.entries.length} khóa localStorage. SHA-256 đã được đính kèm.`;toast('Đã tạo bản sao lưu toàn bộ dữ liệu học tập.');}
  catch(error){toast(`Sao lưu thất bại: ${error.message}`,'error');}finally{if(button)button.disabled=false;}
}
async function restoreLearnerBackupFile(file){
  const parsed=JSON.parse(await file.text());const validated=await validateLearnerBackup(parsed);
  const summary=`Bản sao lưu ngày ${parsed.exportedAt||'không rõ'} gồm ${validated.indexedDBEntries.length} khóa IndexedDB và ${validated.localStorageEntries.length} khóa localStorage.\n\nKhôi phục sẽ ghi đè các khóa trùng tên, giữ nguyên khóa hiện có không có trong tệp. Ứng dụng sẽ tải lại sau khi hoàn tất. Tiếp tục?`;
  if(!confirm(summary))return;
  const current=await buildFullLearnerBackup();downloadFile(`toeic-learner-backup-before-restore-${new Date().toISOString().replace(/[:.]/g,'-')}.json`,JSON.stringify(current,null,2),'application/json;charset=utf-8');
  const db=await openDB();if(!db)throw new Error('IndexedDB không khả dụng; không thể khôi phục an toàn.');
  const oldLocal=[];for(let i=0;i<localStorage.length;i++){const key=localStorage.key(i);if(key?.startsWith('toeic:'))oldLocal.push([key,localStorage.getItem(key)]);}const importedKeys=new Set(validated.localStorageEntries.map(x=>x.key));
  try{
    await new Promise((resolve,reject)=>{const tx=db.transaction(DB_STORE,'readwrite');const store=tx.objectStore(DB_STORE);for(const entry of validated.indexedDBEntries)store.put(entry.value,entry.key);tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error||new Error('Giao dịch IndexedDB thất bại.'));tx.onabort=()=>reject(tx.error||new Error('Giao dịch IndexedDB bị hủy.'));});
    for(const entry of validated.localStorageEntries)localStorage.setItem(entry.key,entry.value);
  }catch(error){
    for(const entry of oldLocal){try{localStorage.setItem(entry[0],entry[1]);}catch{}}
    for(const entry of validated.localStorageEntries){if(!oldLocal.some(x=>x[0]===entry.key)){try{localStorage.removeItem(entry.key);}catch{}}}
    try{await new Promise((resolve,reject)=>{const tx=db.transaction(DB_STORE,'readwrite');const store=tx.objectStore(DB_STORE);store.clear();for(const entry of current.storage.indexedDB.entries)store.put(entry.value,entry.key);tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error);tx.onabort=()=>reject(tx.error);});}catch(rollbackError){console.error('Learner backup rollback failed:',rollbackError);}
    throw new Error(`Khôi phục chưa hoàn tất. Bản sao lưu hiện trạng đã được tải xuống. Chi tiết: ${error.message}`);
  }finally{db.close();}
  toast('Khôi phục dữ liệu hoàn tất. Đang tải lại ứng dụng…');setTimeout(()=>location.reload(),900);
}

function personalExportRecords(){return sortWords([...state.personalVocabulary.additions,...Object.values(state.personalVocabulary.overrides)]);}
function exportJSON(){const payload={schemaVersion:3,exportedAt:new Date().toISOString(),type:'TOEIC_PERSONAL_VOCABULARY',note:'Chỉ chứa thay đổi cá nhân; không bao gồm dữ liệu từ điển gốc của GitHub.',personalVocabulary:state.personalVocabulary,words:personalExportRecords()};downloadFile('toeic-personal-vocabulary.json',JSON.stringify(payload,null,2),'application/json;charset=utf-8');toast('Đã xuất dữ liệu từ vựng cá nhân.');}
function csvEscape(v){const s=String(v??'');return /[",\r\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s;}
function exportCSV(){const headers=['id','word','ipa','pos','meaning_vi','definition_en','synonyms','antonyms','topics','example_en','example_vi','collocations','source'];const rows=personalExportRecords().map(w=>{const sense=getPrimarySense(w);return [w.id,w.word,w.phonetic?.us||'',sense.pos,sense.meaning_vi,sense.definition_en,(sense.synonyms||[]).join('|'),(sense.antonyms||[]).join('|'),w.topics.join('|'),w.examples?.[0]?.en||'',w.examples?.[0]?.vi||'',w.collocations.join('|'),state.baseWords.some(b=>b.id===w.id)?'override':'personal-add'];});const csv='\uFEFF'+[headers,...rows].map(r=>r.map(csvEscape).join(',')).join('\r\n');downloadFile('toeic-personal-vocabulary.csv',csv,'text/csv;charset=utf-8');toast('Đã xuất tệp từ vựng cá nhân CSV.');}
function parseCSV(text){const rows=[];let row=[],cell='',quoted=false;for(let i=0;i<text.length;i++){const ch=text[i];if(quoted){if(ch==='"'&&text[i+1]==='"'){cell+='"';i++;}else if(ch==='"')quoted=false;else cell+=ch;}else if(ch==='"')quoted=true;else if(ch===','){row.push(cell);cell='';}else if(ch==='\n'){row.push(cell.replace(/\r$/,''));rows.push(row);row=[];cell='';}else cell+=ch;}if(cell.length||row.length){row.push(cell.replace(/\r$/,''));rows.push(row);}const [headers,...items]=rows;return items.filter(r=>r.some(x=>x.trim())).map(r=>Object.fromEntries(headers.map((h,i)=>[h.trim(),r[i]??'']))).map(r=>({id:r.id,word:r.word,phonetic:{us:r.ipa},senses:[{pos:r.pos,meaning_vi:r.meaning_vi,definition_en:r.definition_en,synonyms:String(r.synonyms||'').split('|').filter(Boolean),antonyms:String(r.antonyms||'').split('|').filter(Boolean)}],topics:String(r.topics||'').split('|').filter(Boolean),examples:[{en:r.example_en,vi:r.example_vi}],collocations:String(r.collocations||'').split('|').filter(Boolean)}));}
async function importFile(file){
  const text=await file.text(); let imported; let personalPayload=null;
  if(file.name.toLowerCase().endsWith('.csv')) imported=parseCSV(text.replace(/^\uFEFF/,''));
  else {const parsed=JSON.parse(text); personalPayload=parsed.personalVocabulary||null; imported=Array.isArray(parsed)?parsed:(parsed.words||[]);}
  if(personalPayload&&Array.isArray(personalPayload.additions)&&personalPayload.overrides){
    const merged=emptyPersonalVocabulary();
    const importedBaseSigs=personalPayload.overrideBaseSigs||{};
    for(const raw of personalPayload.additions){const rec=normalizeRecord(raw);const base=state.baseWords.find(b=>b.id===rec.id||normalizedAnswer(b.word)===normalizedAnswer(rec.word));if(base){merged.overrides[base.id]={...rec,id:base.id};merged.overrideBaseSigs[base.id]=importedBaseSigs[rec.id]||recordSignature(base);}else merged.additions.push(rec);}
    for(const [id,raw] of Object.entries(personalPayload.overrides)){const base=state.baseWords.find(b=>b.id===id);if(base){merged.overrides[id]=normalizeRecord({...raw,id});merged.overrideBaseSigs[id]=importedBaseSigs[id]||recordSignature(base);}}
    merged.deletedBaseIds=(personalPayload.deletedBaseIds||[]).filter(id=>state.baseWords.some(b=>b.id===id));
    state.personalVocabulary=merged;
  } else {
    if(!Array.isArray(imported)||!imported.length)throw new Error('Không tìm thấy danh sách từ vựng trong tệp.');
    for(const raw of imported){const rec=normalizeRecord(raw);const base=state.baseWords.find(b=>b.id===rec.id||normalizedAnswer(b.word)===normalizedAnswer(rec.word));if(base){rec.id=base.id;state.personalVocabulary.overrides[base.id]=rec;state.personalVocabulary.overrideBaseSigs[base.id]=recordSignature(base);}else{const old=state.personalVocabulary.additions.findIndex(w=>w.id===rec.id||normalizedAnswer(w.word)===normalizedAnswer(rec.word));if(old>=0)state.personalVocabulary.additions[old]=rec;else state.personalVocabulary.additions.push(rec);}}
  }
  await persistPersonalVocabulary(); updateOverview(); renderDictionary(); renderDataTable(); toast('Import dữ liệu cá nhân hoàn tất. Dữ liệu gốc GitHub không bị thay đổi.');
}
async function resetWorkspace(){if(!confirm('Xóa toàn bộ từ vựng cá nhân trên thiết bị này và hiển thị lại kho gốc GitHub? Dữ liệu học tập không bị xóa.'))return;state.personalVocabulary=emptyPersonalVocabulary();await dbSet('personalVocabulary',state.personalVocabulary);await dbDelete('workspace');rebuildEffectiveWords();updateStorageLabel();updateOverview();renderDictionary();renderDataTable();toast('Đã xóa dữ liệu từ vựng cá nhân; kho gốc được khôi phục.');}
function goToLetter(letter){state.activeLetter=letter||'';$('#dictionarySearch').value='';$('#topicFilter').value='';$('#posFilter').value='';navigate('dictionary');}
// Phase 2 – adaptive practice, per-character feedback and study reminders.
const REVIEW_INTERVALS = [10 * 60 * 1000, 1 * 86400000, 3 * 86400000, 7 * 86400000, 14 * 86400000, 30 * 86400000];
const PRACTICE_DEFAULT_REMINDER = { enabled: false, intervalMinutes: 60, nextAt: null, pendingAnswered: true, lastTriggeredAt: null, pendingWordId: null };
const REMINDER_INTERVAL_OPTIONS = [60, 90, 120, 180];
state.progress = {};
state.reminder = { ...PRACTICE_DEFAULT_REMINDER };
state.currentQuestion = null;
state.questionAnswered = false;
state.sessionSeenIds = [];

function normalizedAnswer(value='') {
  return normalizeText(String(value).replace(/\s+/g, ' ').trim()).replace(/[’']/g, "'");
}
function getWordProgress(id) {
  return state.progress[id] || { reviewCount: 0, correctCount: 0, wrongCount: 0, streak: 0, intervalIndex: -1, dueAt: 0, lastReviewedAt: 0, lastAnswer: '' };
}
function eligibleModes(word) {
  const senses = word.senses || [];
  const modes = ['missing', 'meaning-to-word', 'word-to-meaning', 'pos'];
  if (senses.some(s => (s.synonyms || []).length)) modes.push('synonym');
  if (senses.some(s => (s.antonyms || []).length)) modes.push('antonym');
  if (word.verb_forms && ['vs_es','v2','v3','ving'].some(k => word.verb_forms[k])) modes.push('verb');
  return modes;
}
function wordWeight(word, now=Date.now()) {
  const p = getWordProgress(word.id);
  if (!p.reviewCount) return 3.5;
  if (p.dueAt && p.dueAt <= now) return 7 + Math.min(p.wrongCount || 0, 4);
  if ((p.wrongCount || 0) > (p.correctCount || 0)) return 5.5;
  if ((p.streak || 0) < 2) return 3.2;
  if ((p.streak || 0) >= 3) return 1.1;
  return 2;
}
function getPracticeVocabulary(){
  // Personal hiding/overrides must not break built-in review content. Prefer the
  // effective learner vocabulary, but retain the immutable release vocabulary
  // as a safe source if a local workspace is temporarily empty.
  return Array.isArray(state.words)&&state.words.length?state.words:(Array.isArray(state.baseWords)?state.baseWords:[]);
}
function getSentenceCompletionWordPool(){
  // Part 5 questions are first-party learning resources. A learner may hide a
  // linked headword from their personal dictionary; that must not orphan the
  // question or make the whole review mode appear empty.
  const effective=getPracticeVocabulary();
  const byId=new Map(effective.map(word=>[String(word.id),word]));
  const baseById=new Map((state.baseWords||[]).map(word=>[String(word.id),word]));
  for(const question of state.sentenceCompletionItems||[]){
    const id=String(question.wordId||'');
    if(id&&!byId.has(id)&&baseById.has(id))byId.set(id,baseById.get(id));
  }
  return [...byId.values()];
}
function practiceModeFallbacks(requestedMode){
  const ordered=['random','word-to-meaning','meaning-to-word','missing','pos','verb','synonym','antonym'];
  return ordered.filter(mode=>mode!==requestedMode);
}
function choosePracticeWord(mode='random') {
  const now = Date.now();
  const vocabulary=getPracticeVocabulary();
  let candidates = vocabulary.filter(w => eligibleModes(w).includes(mode) || mode === 'random');
  if (!candidates.length) return null;
  let fresh = candidates.filter(w => !state.sessionSeenIds.includes(w.id));
  if (!fresh.length) { state.sessionSeenIds = []; fresh = candidates; }
  const weighted = fresh.map(word => ({ word, weight: wordWeight(word, now) }));
  const total = weighted.reduce((sum, item) => sum + item.weight, 0);
  let point = Math.random() * total;
  for (const item of weighted) { point -= item.weight; if (point <= 0) return item.word; }
  return weighted[weighted.length - 1].word;
}
function shuffle(items) {
  const list = [...items];
  for (let i=list.length-1;i>0;i--) { const j=Math.floor(Math.random()*(i+1)); [list[i],list[j]]=[list[j],list[i]]; }
  return list;
}
function uniqueValues(values) { return [...new Map(values.filter(Boolean).map(v=>[normalizedAnswer(v),String(v)])).values()]; }
function makeChoices(correctValues, distractors, count=4) {
  const valid = uniqueValues(correctValues);
  const answer = valid[Math.floor(Math.random()*valid.length)] || '';
  const options = uniqueValues([...distractors]).filter(v=>!valid.some(c=>normalizedAnswer(c)===normalizedAnswer(v)));
  return shuffle([answer, ...shuffle(options).slice(0, Math.max(0,count-1))]);
}
function maskWord(word) {
  const chars = [...word];
  if (chars.length <= 2) return chars.map((ch,i)=>i===0?ch:'_').join(' ');
  const reveal = new Set([0, chars.length-1]);
  if (chars.length >= 6) reveal.add(Math.floor(chars.length/2));
  return chars.map((ch,i)=>reveal.has(i)?ch:'_').join(' ');
}
function makeQuestion(mode='random', forcedWordId=null) {
  if(mode==='sentence-completion')return chooseSentenceCompletionQuestion(state.sentenceCompletionItems,getSentenceCompletionWordPool(),state.progress,state.sentenceCompletionSeenIds,Math.random,forcedWordId);
  const vocabulary=getPracticeVocabulary();
  const chosen = forcedWordId ? vocabulary.find(w => w.id === forcedWordId) : choosePracticeWord(mode);
  if (!chosen) return null;
  const supported = eligibleModes(chosen);
  const actualMode = mode === 'random' ? supported[Math.floor(Math.random()*supported.length)] : mode;
  const allSenses = chosen.senses || [];
  const sense = actualMode === 'synonym' ? (allSenses.find(s => (s.synonyms || []).length) || getPrimarySense(chosen))
    : actualMode === 'antonym' ? (allSenses.find(s => (s.antonyms || []).length) || getPrimarySense(chosen))
    : getPrimarySense(chosen);
  let q = { wordId: chosen.id, mode: actualMode, word: chosen.word, prompt: '', hint: '', choices: [], accepted: [], expectedWord: false, answerLabel: 'CÂU TRẢ LỜI', expectedDisplay: '' };
  if (actualMode === 'missing') {
    q.prompt = `Hoàn thành từ: ${maskWord(displayWord(chosen.word))}`; q.hint = sense.meaning_vi || 'Điền đầy đủ chữ cái còn thiếu.';
    q.accepted = [chosen.word]; q.expectedWord = true; q.expectedDisplay = displayWord(chosen.word);
  } else if (actualMode === 'meaning-to-word') {
    const selected = allSenses[Math.floor(Math.random()*allSenses.length)] || sense;
    q.prompt = `Từ tiếng Anh nào có nghĩa: “${selected.meaning_vi}”?`; q.hint = selected.definition_en || 'Nhập từ tiếng Anh tương ứng.';
    q.accepted = [chosen.word]; q.expectedWord = true; q.expectedDisplay = displayWord(chosen.word);
  } else if (actualMode === 'word-to-meaning') {
    q.prompt = `“${displayWord(chosen.word)}” có nghĩa là gì?`; q.hint = chosen.phonetic?.us || 'Chọn nghĩa tiếng Việt phù hợp.';
    q.accepted = allSenses.map(s=>s.meaning_vi).filter(Boolean); q.expectedDisplay = q.accepted[0] || '';
    const distractors = getPracticeVocabulary().filter(w=>w.id!==chosen.id).map(w=>getPrimarySense(w).meaning_vi).filter(Boolean);
    q.choices = makeChoices(q.accepted, distractors);
  } else if (actualMode === 'pos') {
    const options = allSenses.map(s=>s.pos).filter(Boolean);
    q.prompt = `“${displayWord(chosen.word)}” thuộc loại từ nào?`; q.hint = 'Chọn ký hiệu loại từ phù hợp với nghĩa chính.';
    q.accepted = options; q.expectedDisplay = options.join(' / ');
    q.choices = shuffle(['n','v','adj','adv','prep','conj','pron','n/v'].filter(x=>!options.includes(x)).slice(0,Math.max(0,4-options.length)).concat(options));
  } else if (actualMode === 'synonym' || actualMode === 'antonym') {
    const key = actualMode === 'synonym' ? 'synonyms' : 'antonyms';
    q.accepted = sense[key] || [];
    q.prompt = actualMode === 'synonym' ? `Từ nào đồng nghĩa gần nhất với “${displayWord(chosen.word)}”?` : `Từ nào trái nghĩa với “${displayWord(chosen.word)}”?`;
    q.hint = sense.meaning_vi || 'Chọn một từ phù hợp.'; q.expectedDisplay = q.accepted.join(', ');
    const distractors = getPracticeVocabulary().filter(w=>w.id!==chosen.id).flatMap(w=>(getPrimarySense(w)[key]||[]));
    q.choices = makeChoices(q.accepted, distractors);
  } else if (actualMode === 'verb') {
    const forms = chosen.verb_forms || {};
    const candidates = [['V-s/es',forms.vs_es],['V2',forms.v2],['V3',forms.v3],['V-ing',forms.ving]].filter(x=>x[1]);
    const chosenForm = candidates[Math.floor(Math.random()*candidates.length)];
    if (!chosenForm) return makeQuestion('meaning-to-word');
    q.verbLabel = chosenForm[0]; q.prompt = `Dạng ${chosenForm[0]} của động từ “${displayWord(forms.v1 || chosen.word)}” là gì?`;
    q.hint = 'Chú ý quy tắc chia động từ hoặc dạng bất quy tắc.'; q.accepted=[chosenForm[1]]; q.expectedWord=true; q.expectedDisplay=displayWord(chosenForm[1]);
  }
  q.prompt = q.prompt || `Hãy ôn từ “${displayWord(chosen.word)}”.`;
  return q;
}
async function savePracticeSession() {
  await dbSet('practiceSession', { currentQuestion: state.currentQuestion, questionAnswered: state.questionAnswered, practiceReviewPending: state.practiceReviewPending, pendingSinglePractice: state.pendingSinglePractice, sessionSeenIds: state.sessionSeenIds, sentenceCompletionSeenIds: state.sentenceCompletionSeenIds, lastFeedback: state.lastFeedback, autoAdvanceCancelled: state.autoAdvanceCancelled, autoAdvanceWaiting: state.autoAdvanceWaiting });
}
function progressPriorityLabel(wordId) {
  const p = getWordProgress(wordId);
  if (!p.reviewCount) return 'Từ mới';
  if (p.dueAt && p.dueAt <= Date.now()) return 'Đến hạn ôn';
  if (p.wrongCount > p.correctCount || p.streak === 0) return 'Cần củng cố';
  if (p.streak >= 3) return 'Đã ghi nhớ';
  return 'Đang học';
}
function renderQuestion() {
  const q = state.currentQuestion;
  if (!q) {
    $('#questionType').textContent='SẴN SÀNG'; $('#questionPrompt').textContent='Chọn “Câu hỏi mới” để bắt đầu.';
    const sentenceDisplay=$('#sentenceCompletionDisplay');if(sentenceDisplay){sentenceDisplay.hidden=true;sentenceDisplay.innerHTML='';}
    $('#questionHint').textContent='Câu hỏi được chọn từ kho từ vựng và ưu tiên từ bạn chưa thuộc.';
    $('#choiceList').hidden=true; $('#answerForm').hidden=false; $('#answerInput').value='';
    $('#nextQuestionButton').disabled=true; $('#answerFeedback').hidden=true; $('#choiceReview').hidden=true; return;
  }
  const names = {missing:'MISSING LETTERS', 'meaning-to-word':'VIETNAMESE → ENGLISH', 'word-to-meaning':'ENGLISH → VIETNAMESE', pos:'PART OF SPEECH', synonym:'SYNONYM', antonym:'ANTONYM', verb:'VERB FORMS', 'sentence-completion':'TOEIC PART 5 · INCOMPLETE SENTENCES'};
  $('#questionType').textContent = names[q.mode] || 'PRACTICE';
  $('#questionPrompt').textContent=q.prompt; $('#questionHint').textContent=q.hint || '';
  const sentenceDisplay=$('#sentenceCompletionDisplay');
  if(sentenceDisplay){const active=q.mode==='sentence-completion';sentenceDisplay.hidden=!active;sentenceDisplay.innerHTML=active?`<span class="sentence-context-label">HOÀN THÀNH CÂU</span>${q.grammarCategory?`<span class="sentence-category-label">${escapeHtml(q.grammarCategory)}</span>`:''}<p>${escapeHtml(q.sentence).replace('_____', '<span class="sentence-blank">__________</span>')}</p>`:'';}
  $('#questionCounter').textContent=q.mode==='sentence-completion'?`${state.sentenceCompletionSeenIds.length} câu đã gặp trong lượt này`:`${state.sessionSeenIds.length} từ đã gặp trong lượt này`;
  $('#questionPriority').textContent=progressPriorityLabel(q.wordId);
  const isChoice=q.choices?.length>0;
  $('#choiceList').hidden=!isChoice;
  $('#choiceList').innerHTML=isChoice?q.choices.map((choice,i)=>{
    const picked=state.questionAnswered&&state.lastFeedback&&normalizedAnswer(state.lastFeedback.input)===normalizedAnswer(choice);
    const isRight=q.accepted.some(a=>normalizedAnswer(a)===normalizedAnswer(choice));
    const revealFeedback=state.questionAnswered&&!state.pendingSinglePractice;
    const cls=revealFeedback&&isRight?' correct-choice':revealFeedback&&picked?' wrong-choice':'';
    return `<button type="button" class="choice-option${picked?' selected':''}${cls}" data-choice="${escapeHtml(choice)}" ${state.questionAnswered?'disabled':''}><span>${String.fromCharCode(65+i)}</span>${escapeHtml(choice)}</button>`;
  }).join(''):'';
  $('#answerForm').hidden=isChoice;
  $('#answerInput').value=''; $('#answerInput').disabled=state.questionAnswered;
  $('#answerLabel').textContent=q.expectedWord?'NHẬP TỪ TIẾNG ANH':'CÂU TRẢ LỜI';
  $('#answerInput').placeholder=q.mode==='verb'?'Nhập dạng động từ...':q.mode==='missing'?'Điền từ hoàn chỉnh...':'Nhập câu trả lời...';
  $('#checkAnswerButton').disabled=state.questionAnswered;
  const revealFeedback=state.questionAnswered&&!state.pendingSinglePractice;
  $('#answerFeedback').hidden=!revealFeedback;
  $('#nextQuestionButton').disabled=!state.questionAnswered||state.practiceReviewPending;
  $('#skipQuestionButton').disabled=state.questionAnswered;
  if (revealFeedback && state.lastFeedback) renderFeedback(state.lastFeedback);
  else { $('#answerReference').hidden=true;$('#choiceReview').hidden=true;$('#characterFeedback').hidden=true;$('#autoAdvanceRow').hidden=true; }
}
function alignCharacters(expected, actual) {
  const a=[...expected], b=[...actual]; const dp=Array.from({length:a.length+1},()=>Array(b.length+1).fill(0));
  for(let i=0;i<=a.length;i++)dp[i][0]=i;
  for(let j=0;j<=b.length;j++)dp[0][j]=j;
  for(let i=1;i<=a.length;i++)for(let j=1;j<=b.length;j++){
    const cost=a[i-1].toLowerCase()===b[j-1].toLowerCase()?0:1;
    dp[i][j]=Math.min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+cost);
  }
  const cells=[]; let i=a.length,j=b.length;
  while(i>0||j>0){
    if(i>0&&j>0&&a[i-1].toLowerCase()===b[j-1].toLowerCase()&&dp[i][j]===dp[i-1][j-1]){cells.push({expected:a[i-1],actual:b[j-1],status:'correct'});i--;j--;continue;}
    if(i>0&&j>0&&dp[i][j]===dp[i-1][j-1]+1){cells.push({expected:a[i-1],actual:b[j-1],status:'wrong'});i--;j--;continue;}
    if(i>0&&dp[i][j]===dp[i-1][j]+1){cells.push({expected:a[i-1],actual:'',status:'wrong'});i--;continue;}
    cells.push({expected:'',actual:b[j-1],status:'wrong extra'});j--;
  }
  return cells.reverse();
}
const POS_EXPLANATIONS = {
  n:'Danh từ – chỉ người, vật, sự việc, khái niệm hoặc địa điểm.',
  v:'Động từ – diễn tả hành động, trạng thái hoặc quá trình.',
  adj:'Tính từ – bổ nghĩa cho danh từ hoặc đứng sau một số động từ nối.',
  adv:'Trạng từ – bổ nghĩa cho động từ, tính từ, trạng từ hoặc cả câu.',
  prep:'Giới từ – thể hiện quan hệ về thời gian, địa điểm, phương thức...',
  conj:'Liên từ – nối từ, cụm từ hoặc mệnh đề.',
  pron:'Đại từ – thay thế cho danh từ hoặc cụm danh từ.',
  'n/v':'Có thể dùng như danh từ hoặc động từ tùy ngữ cảnh.'
};
function lookupWord(term) {
  const needle=normalizedAnswer(term);
  return state.words.find(w=>normalizedAnswer(w.word)===needle)
    || state.words.find(w=>(w.word_family||[]).some(f=>normalizedAnswer(f.word)===needle))
    || null;
}
function findRelatedSources(term, relationKey=null) {
  const needle=normalizedAnswer(term);
  return state.words.filter(w=>(w.senses||[]).some(s=>{
    const keys=relationKey?[relationKey]:['synonyms','antonyms'];
    return keys.some(k=>(s[k]||[]).some(x=>normalizedAnswer(x)===needle));
  })).slice(0,3);
}
function getChoiceExplanation(q, choice, isCorrect) {
  if(q.mode==='sentence-completion'){const index=(q.choices||[]).findIndex(option=>normalizedAnswer(option)===normalizedAnswer(choice));return q.optionExplanations?.[index]|| (isCorrect?q.explanation:'Phương án này không phù hợp với cấu trúc hoặc ý nghĩa của câu.');}
  if(q.mode==='pos') return POS_EXPLANATIONS[choice] || 'Ký hiệu loại từ trong tiếng Anh.';
  if(q.mode==='word-to-meaning') {
    const sources=state.words.filter(w=>(w.senses||[]).some(s=>normalizedAnswer(s.meaning_vi)===normalizedAnswer(choice)));
    if(sources.length) return `Nghĩa này được dùng cho: ${sources.slice(0,3).map(w=>`${displayWord(w.word)} (${getAllPos(w).join('/')||'—'})`).join(', ')}.`;
    return 'Đây là một phương án diễn đạt nghĩa tiếng Việt khác; hãy đối chiếu với nghĩa chính của từ trong câu hỏi.';
  }
  if(q.mode==='synonym'||q.mode==='antonym') {
    const exact=lookupWord(choice);
    if(exact) {
      const senses=(exact.senses||[]).map(s=>`${s.pos||'—'}: ${s.meaning_vi||'chưa có nghĩa'}${s.definition_en?` (${s.definition_en})`:''}`).join('; ');
      return `Nghĩa của ${displayWord(exact.word)}: ${senses||'Chưa có nghĩa tiếng Việt.'}`;
    }
    const alias=state.relatedTerms?.get(normalizedAnswer(choice));
    const relationKey=q.mode==='synonym'?'synonyms':'antonyms';
    const relation=q.mode==='synonym'?'đồng nghĩa với':'trái nghĩa với';
    const source=state.words.find(w=>w.id===q.wordId);
    // Keep explanatory context relation-specific; an antonym reference must not be
    // presented as evidence for a synonym (or vice versa).
    const refs=findRelatedSources(choice,relationKey);
    if(alias) {
      const learnerDefinition=getLearnerFacingRelatedGlossaryDefinition(alias.definition_en);
      const details=[alias.pos?`Loại từ: ${alias.pos}`:'',learnerDefinition?`English: ${learnerDefinition}`:''].filter(Boolean).join(' · ');
      const context=refs.length?` Có liên hệ ${relationKey==='synonyms'?'đồng nghĩa':'trái nghĩa'} trong dữ liệu với: ${refs.map(w=>`${displayWord(w.word)} (${getPrimarySense(w).meaning_vi})`).join('; ')}.`:'';
      return `Nghĩa tiếng Việt: ${alias.meaning_vi}.${details?` ${details}.`:''} Đây là phương án ${relation} ${displayWord(q.word)} trong câu hỏi hiện tại.${context}`;
    }
    if(isCorrect) {
      const meaning=source?getPrimarySense(source).meaning_vi:'';
      return `Phương án này được lưu là ${relation} ${displayWord(q.word)}. Nghĩa riêng của lựa chọn chưa có trong bảng tham chiếu; nghĩa từ gốc: ${meaning||'xem từ điển gốc'}.`;
    }
    if(refs.length) return `Được dùng trong nhóm từ liên hệ của ${refs.map(w=>`${displayWord(w.word)} – ${getPrimarySense(w).meaning_vi}`).join('; ')}. Chưa có nghĩa độc lập đã kiểm chứng trong bảng tham chiếu.`;
    return 'Chưa có nghĩa riêng trong bảng tham chiếu hiện tại. Hãy đối chiếu với từ điển gốc hoặc thêm nguồn tham khảo đã kiểm chứng.';
  }
  const exact=lookupWord(choice);
  if(exact) return `${getAllPos(exact).join('/')} · ${(exact.senses||[]).map(s=>s.meaning_vi).filter(Boolean).join('; ')}`;
  return isCorrect?'Đáp án khớp với dạng cần điền.':'So sánh với đáp án chuẩn và thông tin từ vựng bên dưới.';
}
function renderChoiceReview(q, feedback) {
  const host=$('#choiceReview');
  if(!q?.choices?.length){host.hidden=true;host.innerHTML='';return;}
  host.hidden=false;
  host.innerHTML=`<div class="choice-review-title"><strong>Giải nghĩa toàn bộ lựa chọn</strong><span>A–D</span></div><div class="choice-review-list">${q.choices.map((choice,i)=>{
    const correct=q.accepted.some(x=>normalizedAnswer(x)===normalizedAnswer(choice));
    const selected=normalizedAnswer(feedback.input)===normalizedAnswer(choice);
    const badge=correct?(q.mode==='synonym'?'ĐÚNG · ĐỒNG NGHĨA':q.mode==='antonym'?'ĐÚNG · TRÁI NGHĨA':'ĐÁP ÁN ĐÚNG'):selected?'BẠN ĐÃ CHỌN · SAI':'PHƯƠNG ÁN KHÔNG ĐÚNG';
    const cls=correct?'is-correct':selected?'is-selected-wrong':'is-neutral';
    return `<article class="choice-review-item ${cls}"><div class="choice-review-head"><span class="choice-review-letter">${String.fromCharCode(65+i)}</span><strong>${escapeHtml(choice)}</strong><em>${badge}</em></div><p>${escapeHtml(getChoiceExplanation(q,choice,correct))}</p></article>`;
  }).join('')}</div>`;
}
function renderWordReference(w,q,feedback) {
  if(!w)return '';
  const sentenceReview=q?.mode==='sentence-completion'?`<section class="sentence-answer-review"><h3>Câu hoàn chỉnh</h3><p class="sentence-completed-text">${escapeHtml(q.sentence||'').replace('_____',`<strong>${escapeHtml(q.accepted?.[0]||'')}</strong>`)}</p><p><b>Dịch nghĩa:</b> ${escapeHtml(q.translationVi||'')}</p><p><b>Nhóm ngữ pháp:</b> ${escapeHtml(q.grammarCategory||'')}</p><p><b>Trọng tâm ngữ pháp:</b> ${escapeHtml(q.grammarPoint||'')}</p><p><b>Vì sao chỉ có một đáp án:</b> ${escapeHtml(q.singleAnswerReason||'')}</p></section>`:'';
  const senses=(w.senses||[]).map(s=>`<div class="reference-sense"><span class="meaning-pos">${escapeHtml(s.pos||'')}</span><strong>${escapeHtml(s.meaning_vi||'')}</strong>${s.definition_en?`<small>${escapeHtml(s.definition_en)}</small>`:''}${s.synonyms?.length?`<p><b>Đồng nghĩa:</b> ${s.synonyms.map(escapeHtml).join(', ')}</p>`:''}${s.antonyms?.length?`<p><b>Trái nghĩa:</b> ${s.antonyms.map(escapeHtml).join(', ')}</p>`:''}</div>`).join('');
  const examples=(w.examples||[]).map(e=>`<small class="reference-example">${escapeHtml(e.en)}${e.vi?` — ${escapeHtml(e.vi)}`:''}</small>`).join('');
  const family=(w.word_family||[]).length?`<p><b>Word family:</b> ${w.word_family.map(f=>`${escapeHtml(displayWord(f.word))} (${escapeHtml(f.pos||'')}) – ${escapeHtml(f.meaning_vi||'')}`).join('; ')}</p>`:'';
  const forms=w.verb_forms?`<p><b>Verb forms:</b> ${Object.entries({V1:w.verb_forms.v1,'V-s/es':w.verb_forms.vs_es,V2:w.verb_forms.v2,V3:w.verb_forms.v3,'V-ing':w.verb_forms.ving}).filter(([,v])=>v).map(([k,v])=>`${k}: ${escapeHtml(v)}`).join(' · ')}</p>`:'';
  const selected=feedback.correct?'Bạn đã trả lời đúng.':`Bạn nhập/chọn: ${escapeHtml(feedback.input)} · Đáp án: ${escapeHtml(feedback.expected)}`;
  return `${sentenceReview}<div class="reference-title-row"><strong>${escapeHtml(displayWord(w.word))}</strong><span>${escapeHtml(w.phonetic?.us||'')}</span></div><p class="reference-overview">${escapeHtml(selected)}</p>${senses}${family}${forms}${w.collocations?.length?`<p><b>Collocations:</b> ${w.collocations.map(escapeHtml).join(', ')}</p>`:''}${examples}${w.topics?.length?`<p><b>Chủ đề:</b> ${w.topics.map(escapeHtml).join(', ')}</p>`:''}`;
}
function renderFeedback(feedback) {
  $('#answerFeedback').hidden=false;$('#answerFeedback').classList.remove('is-compact');
  $('#answerReference').hidden=false;
  $('#feedbackHeading').textContent=feedback.correct?'Chính xác! Bạn làm tốt lắm.':'Chưa chính xác – hãy ghi nhớ vị trí cần sửa.';
  $('#feedbackHeading').className=`feedback-heading ${feedback.correct?'is-correct':'is-wrong'}`;
  const q=state.currentQuestion;
  $('#feedbackExplanation').textContent=q?.mode==='sentence-completion'?(q.explanation||'Hãy đối chiếu cấu trúc và ngữ cảnh của câu.'):feedback.correct?'Đáp án đã được ghi nhận. Hãy xem nghĩa của tất cả lựa chọn bên dưới.':`Đáp án đúng: ${feedback.expected}. Bạn có thể xem lại từng lựa chọn để ghi nhớ.`;
  if(q?.expectedWord){
    const cells=alignCharacters(q.expectedDisplay,feedback.input||'');
    $('#characterFeedback').hidden=false;
    $('#characterFeedback').innerHTML=cells.map(c=>`<span class="char-cell ${c.status}"><b>${escapeHtml(c.actual||'·')}</b><small>${escapeHtml(c.expected||'thừa')}</small></span>`).join('');
  } else { $('#characterFeedback').hidden=true; $('#characterFeedback').innerHTML=''; }
  const w=state.words.find(x=>x.id===q?.wordId);
  $('#answerReference').innerHTML=renderWordReference(w,q,feedback);
  renderChoiceReview(q,feedback);
  updateAutoAdvanceUI();
}
function compactInlinePracticeFeedback(){
  const host=$('#answerFeedback');if(!host)return;
  host.classList.add('is-compact');
  const ref=$('#answerReference'),review=$('#choiceReview');
  if(ref)ref.hidden=true;if(review)review.hidden=true;
}
function openPracticeReviewModal(feedback){
  if(!state.currentQuestion||!feedback)return;
  renderFeedback(feedback);
  const q=state.currentQuestion,w=state.words.find(x=>x.id===q.wordId);
  const title=feedback.correct?'Bạn đã trả lời chính xác':'Cùng xem lại đáp án';
  const result=feedback.correct?'Chính xác':'Chưa chính xác';
  const inputLabel=q.choices?.length?'Phương án bạn đã chọn':'Câu trả lời của bạn';
  const detail=$('#answerReference').innerHTML;
  const choices=$('#choiceReview').hidden?'':$('#choiceReview').innerHTML;
  const chars=$('#characterFeedback').hidden?'':`<section class="review-detail-section"><h3>Đối chiếu từng ký tự</h3><div class="character-feedback">${$('#characterFeedback').innerHTML}</div></section>`;
  $('#modalLayer').classList.remove('is-auto-advance-wait','is-learning-detail');
  $('#modalLayer').classList.add('is-practice-review');
  $('#modalLayer').dataset.modalType='practice-review';
  $('#closeModal').hidden=false;
  $('#closeModal').setAttribute('aria-label','Đóng giải thích và giữ câu hiện tại');
  $('#closeModal').title='Đóng giải thích, giữ câu hiện tại';
  $('#modalEyebrow').textContent='SMART REVIEW · GIẢI THÍCH ĐÁP ÁN';
  $('#modalTitle').textContent=title;
  $('#modalContent').innerHTML=`<div class="practice-review-result ${feedback.correct?'is-correct':'is-wrong'}"><span class="practice-review-status">${result}</span><strong>${escapeHtml(displayWord(q.word))}</strong><p>${escapeHtml(q.prompt)}</p><div class="practice-review-answer-grid"><div><small>${inputLabel}</small><b>${escapeHtml(feedback.input)}</b></div><div><small>ĐÁP ÁN CHUẨN</small><b>${escapeHtml(feedback.expected||q.accepted[0]||'—')}</b></div></div></div><p class="practice-review-explanation">${q.mode==='sentence-completion'?escapeHtml(q.explanation||''):feedback.correct?'Bạn đã chọn đúng. Hãy xem thêm nghĩa và cách dùng để ghi nhớ lâu hơn.':`Đáp án đúng là ${escapeHtml(feedback.expected||q.accepted[0]||'—')}. Đọc phần giải thích để hiểu điểm khác biệt.`}</p>${chars}<section class="review-detail-section"><h3>Giải nghĩa từ vựng</h3>${detail||'<p>Chưa có thông tin giải thích chi tiết.</p>'}</section>${choices?`<section class="review-detail-section"><h3>Phân tích từng lựa chọn</h3>${choices}</section>`:''}${q.mode==='sentence-completion'?`<section class="review-detail-section explanation-rubric" aria-label="Tự đánh giá khả năng giải thích"><h3>Tự kiểm tra cách bạn hiểu câu hỏi</h3><p>Đọc phần giải thích rồi tự đánh giá. Đây là ghi nhận do bạn tự chọn, không phải chấm tự động hay xác nhận độc lập.</p>${[['clue','Tôi xác định được dấu hiệu ngữ pháp hoặc từ vựng quyết định.'],['fit','Tôi giải thích được vì sao đáp án đúng phù hợp với cấu trúc và ngữ cảnh.'],['distractor','Tôi chỉ ra được ít nhất một lý do phương án nhiễu không phù hợp.']].map(([key,label],i)=>`<fieldset class="explanation-rubric-item"><legend>${i+1}. ${label}</legend><label><input type="radio" name="rubric-${key}" value="yes" data-explanation-rubric="${key}"> Làm được</label><label><input type="radio" name="rubric-${key}" value="no" data-explanation-rubric="${key}"> Chưa làm được</label></fieldset>`).join('')}<button type="button" class="secondary-button" data-save-explanation-rubric>Lưu tự đánh giá (0–3)</button><small class="explanation-rubric-status" data-explanation-rubric-status>Chưa có tự đánh giá cho câu này.</small></section>`:''}<div class="practice-review-footer"><button type="button" class="secondary-button" data-practice-review-ai>Phân tích thêm bằng Google AI</button><button type="button" class="primary-button" data-practice-review-ok>OK · Tiếp tục</button></div>`;
  $('#answerFeedback').hidden=false;compactInlinePracticeFeedback();
  showModalLayer();
  $('#modalContent [data-practice-review-ok]')?.focus();
}
function closeAutoAdvanceWaitModal(){
  const layer=$('#modalLayer');
  if(layer?.dataset.modalType!=='practice-wait')return;
  resetModalLayer();
}
function showAutoAdvanceWaitModal(){
  const layer=$('#modalLayer');
  layer.classList.remove('is-practice-review','is-learning-detail');
  layer.classList.add('is-auto-advance-wait');
  layer.dataset.modalType='practice-wait';
  $('#closeModal').hidden=false;
  $('#closeModal').setAttribute('aria-label','Hủy tự chuyển câu');
  $('#closeModal').title='Hủy tự chuyển câu';
  $('#modalEyebrow').textContent='SMART REVIEW · CHUẨN BỊ CÂU TIẾP THEO';
  $('#modalTitle').textContent='Đang chuẩn bị câu hỏi mới';
  $('#modalContent').innerHTML=`<div class="auto-next-wait-card" role="status" aria-live="polite"><div class="auto-next-wait-loader" aria-hidden="true"><span></span></div><p class="auto-next-wait-kicker">BẠN ĐÃ HOÀN THÀNH CÂU HỎI</p><h3 id="autoAdvanceWaitStatus">Đang chuẩn bị câu tiếp theo</h3><p id="autoAdvanceWaitHint">Bạn có thể xem thời gian chờ hoặc giữ câu hiện tại để chuyển thủ công.</p><div class="auto-next-wait-meter"><div class="auto-next-wait-ring" id="autoAdvanceWaitRing"><strong id="autoAdvanceWaitCountdown">${Number(state.settings.autoNextDelaySeconds)||3}</strong><small>GIÂY</small></div><div class="auto-next-wait-progress"><span id="autoAdvanceWaitProgress"></span></div><div class="auto-next-wait-stage" id="autoAdvanceWaitStage">Đang chọn nội dung phù hợp với tiến độ học.</div></div><button type="button" class="secondary-button" data-auto-advance-cancel>Giữ câu này · Chuyển thủ công</button></div>`;
  showModalLayer();
  updateAutoAdvanceUI();
  $('#closeModal').focus();
}
async function cancelAutoAdvanceWait(){
  if(!state.autoAdvanceWaiting){closeAutoAdvanceWaitModal();return;}
  clearAutoAdvance();
  state.autoAdvanceWaiting=false;
  state.autoAdvanceCancelled=true;
  closeAutoAdvanceWaitModal();
  $('#nextQuestionButton').disabled=false;
  await savePracticeSession();
  updateAutoAdvanceUI();
  toast('Đã giữ câu hiện tại. Bạn có thể tự chuyển sang câu tiếp theo.');
}
async function acknowledgePracticeReview(){
  if(!state.practiceReviewPending)return;
  state.practiceReviewPending=false;
  if(state.settings.autoNextEnabled&&!state.autoAdvanceCancelled){
    state.autoAdvanceWaiting=true;
    await savePracticeSession();
    $('#nextQuestionButton').disabled=true;
    showAutoAdvanceWaitModal();
    scheduleAutoAdvance();
    return;
  }
  state.autoAdvanceWaiting=false;
  $('#modalLayer').classList.remove('is-practice-review');delete $('#modalLayer').dataset.modalType;
  $('#closeModal').hidden=false;hideModalLayer();$('#modalContent').innerHTML='';
  await savePracticeSession();
  $('#nextQuestionButton').disabled=false;
  clearAutoAdvance();
  updateAutoAdvanceUI();
}

async function updatePracticeProgress(wordId, correct, input) {
  const now=Date.now(); const p=getWordProgress(wordId);
  p.reviewCount=(p.reviewCount||0)+1; p.lastReviewedAt=now; p.lastAnswer=String(input||'');
  if(correct){
    p.correctCount=(p.correctCount||0)+1; p.streak=(p.streak||0)+1;
    p.intervalIndex=Math.min((p.intervalIndex ?? -1)+1, REVIEW_INTERVALS.length-1);
  } else {
    p.wrongCount=(p.wrongCount||0)+1; p.streak=0; p.intervalIndex=0;
  }
  p.dueAt=now+REVIEW_INTERVALS[Math.max(0,p.intervalIndex)];
  state.progress[wordId]=p;
  await dbSet('studyProgress',state.progress);
  updatePracticeStats();
}
function updatePracticeStats() {
  const validIds=new Set(state.words.map(w=>w.id));
  const entries=Object.entries(state.progress).filter(([id])=>validIds.has(id)).map(([,p])=>p);
  const reviewed=entries.reduce((sum,p)=>sum+(p.reviewCount||0),0);
  const correct=entries.reduce((sum,p)=>sum+(p.correctCount||0),0);
  const due=state.words.filter(w=>{const p=getWordProgress(w.id);return !p.reviewCount || (p.dueAt&&p.dueAt<=Date.now()) || (p.wrongCount>p.correctCount);}).length;
  const mastered=entries.filter(p=>(p.streak||0)>=3).length;
  $('#practiceReviewed').textContent=reviewed.toLocaleString('vi-VN');
  $('#homeReviewed').textContent=reviewed.toLocaleString('vi-VN');
  $('#homeAccuracy').textContent=`${reviewed?Math.round(correct/reviewed*100):0}%`;
  $('#homeDue').textContent=due.toLocaleString('vi-VN');
  $('#practiceAccuracy').textContent=`${reviewed?Math.round(correct/reviewed*100):0}%`;
  $('#practiceDue').textContent=due.toLocaleString('vi-VN');
  $('#practiceMastered').textContent=mastered.toLocaleString('vi-VN');
  const levelLabel=$('#learningLevelLabel'),levelDetail=$('#learningLevelDetail'),levelBar=$('#learningLevelProgress');
  if(levelLabel&&levelDetail&&levelBar){const coverage=state.words.length?mastered/state.words.length:0;const accuracyRate=reviewed?correct/reviewed:0;const index=Math.min(100,Math.round(coverage*75+accuracyRate*25));const band=index>=72?'B2':index>=48?'B1':index>=24?'A2':'A1';levelLabel.textContent=reviewed?`Mức tham chiếu ${band}`:'Chưa đủ dữ liệu';levelDetail.textContent=reviewed?`${mastered} từ đã ghi nhớ · độ chính xác ${Math.round(accuracyRate*100)}% · chỉ số ${index}/100`:'Hãy trả lời ít nhất một số câu hỏi để bắt đầu đo tiến độ.';levelBar.style.width=`${index}%`;}
  const weak=state.words.filter(w=>{const p=getWordProgress(w.id);return p.reviewCount && (p.wrongCount>0 || (p.dueAt&&p.dueAt<=Date.now()));})
    .sort((a,b)=>{const pa=getWordProgress(a.id),pb=getWordProgress(b.id);const sa=(pb.wrongCount*3)-(pa.wrongCount*3)+(pa.dueAt||0)-(pb.dueAt||0);return sa;}).slice(0,6);
  $('#weakWordList').innerHTML=weak.length?weak.map(w=>{const p=getWordProgress(w.id);return `<button class="weak-word-item" data-weak-word="${escapeHtml(w.id)}"><span><strong>${escapeHtml(displayWord(w.word))}</strong><small>${escapeHtml(getPrimarySense(w).meaning_vi||'')}</small></span><em>${p.wrongCount} lỗi</em></button>`;}).join(''):'<p class="muted">Bạn chưa có từ sai. Hãy bắt đầu luyện tập để tạo dữ liệu ưu tiên.</p>';
}
async function submitAnswer(value) {
  const q=state.currentQuestion; if(!q||state.questionAnswered||state.pendingSinglePractice)return;
  const input=String(value??'').trim(); if(!input){toast('Hãy nhập hoặc chọn câu trả lời trước.','error');return;}
  const correct=q.accepted.some(answer=>normalizedAnswer(answer)===normalizedAnswer(input));
  const answeredAt=Date.now();
  const responseDurationMs=Number.isFinite(state.questionStartedAt)?Math.max(0,answeredAt-state.questionStartedAt):null;
  state.questionAnswered=true;state.practiceReviewPending=true;
  state.lastFeedback={correct,input,expected:q.expectedDisplay||q.accepted[0]||''};
  state.pendingSinglePractice={wordId:q.wordId,questionId:q.id,mode:q.mode,correct,input,answeredAt,responseDurationMs};
  await savePracticeSession();renderQuestion();
  $('#nextQuestionButton').disabled=true;$('#skipQuestionButton').disabled=true;
  showSinglePracticeResult();
}
function showSinglePracticeResult(){
  const pending=state.pendingSinglePractice;if(!pending)return;
  showAssessmentResultModal({eyebrow:pending.mode==='sentence-completion'?'TOEIC PART 5 · COMPLETE':'SMART REVIEW · COMPLETE',title:'Bạn đã hoàn thành câu hỏi',correct:pending.correct?1:0,incorrect:pending.correct?0:1,total:1,description:'Lựa chọn đã được ghi nhận. Hãy xác nhận để lưu kết quả học tập và mở phần giải thích.'});
}
async function confirmSinglePracticeResult({openReview=true}={}){
  const pending=state.pendingSinglePractice,q=state.currentQuestion;if(!pending||!q)return;
  await updatePracticeProgress(pending.wordId,pending.correct,pending.input);
  if(q.mode==='sentence-completion'){
    if(!state.sentenceCompletionSeenIds.includes(q.id))state.sentenceCompletionSeenIds.push(q.id);
    trackObjectivePractice(q.id,{id:q.id,choiceIds:[`part5:${q.id}`]},pending.correct,pending.answeredAt,pending.responseDurationMs);
    await saveObjectivePractice();
  }else if(!state.sessionSeenIds.includes(q.wordId))state.sessionSeenIds.push(q.wordId);
  if(state.reminder.enabled){state.reminder.pendingAnswered=true;state.reminder.pendingWordId=null;state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;await dbSet('reminderSettings',state.reminder);}
  state.pendingSinglePractice=null;
  if(!openReview){state.practiceReviewPending=false;state.autoAdvanceWaiting=false;state.autoAdvanceCancelled=true;clearAutoAdvance();}
  await savePracticeSession();closeAssessmentResultModal();renderReminderStatus();
  if(openReview)openPracticeReviewModal(state.lastFeedback);
  else{renderQuestion();$('#nextQuestionButton').disabled=!state.questionAnswered;updateAutoAdvanceUI();}
const savedWordProgress=state.progress[pending.wordId];if(pending.correct&&savedWordProgress?.streak===3)
  toast(pending.correct?'Đã ghi nhận câu trả lời đúng.':'Đã lưu kết quả. Từ này sẽ được ưu tiên ôn lại.');
}
async function nextQuestion(modeOverride=null, forcedItemId=null) {
  clearAutoAdvance();
  state.autoAdvanceWaiting=false;
  closeAutoAdvanceWaitModal();
  state.autoAdvanceCancelled=false;
  const requestedMode=modeOverride||$('#practiceMode')?.value||'random';
  let actualMode=requestedMode;
  let q=makeQuestion(requestedMode,forcedItemId);
  // Recall links may outlive a content refresh. Retry the selected mode without
  // the stale item key before deciding that the requested mode has no content.
  if(!q&&forcedItemId)q=makeQuestion(requestedMode,null);
  if(!q){
    for(const candidate of practiceModeFallbacks(requestedMode)){
      q=makeQuestion(candidate,null);
      if(q){actualMode=candidate;break;}
    }
  }
  if(!q){
    const sentenceBankEmpty=requestedMode==='sentence-completion'&&!state.sentenceCompletionItems?.length;
    const vocabularyEmpty=!getPracticeVocabulary().length;
    toast(vocabularyEmpty?'Chưa tải được dữ liệu từ vựng. Hãy tải lại ứng dụng khi có kết nối.':sentenceBankEmpty?'Ngân hàng TOEIC Part 5 chưa tải được. Hãy kiểm tra dữ liệu ứng dụng và thử lại.':'Chưa tìm được câu hỏi hợp lệ. Hãy tải lại dữ liệu học tập rồi thử lại.','error');
    return false;
  }
  if(actualMode!==requestedMode){
    syncPracticeModeSelection(actualMode);
    const requestedLabel=requestedMode==='sentence-completion'?'TOEIC Part 5':requestedMode;
    const fallbackLabel=actualMode==='word-to-meaning'?'Từ → Nghĩa':actualMode==='meaning-to-word'?'Nghĩa → Từ':actualMode==='missing'?'Điền chữ thiếu':'Ôn tập thông minh';
    toast(`Dạng ${requestedLabel} chưa có câu phù hợp. Đã chuyển sang ${fallbackLabel} để bạn tiếp tục học.`);
  }
  state.currentQuestion=q; state.questionStartedAt=null; state.questionAnswered=false; state.practiceReviewPending=false; state.lastFeedback=null;
  await savePracticeSession(); state.questionStartedAt=Date.now(); renderQuestion();return true;
}
async function skipQuestion() {
  if(!state.currentQuestion||state.questionAnswered)return;
  if(state.currentQuestion.mode==='sentence-completion')state.sentenceCompletionSeenIds.push(state.currentQuestion.id);else state.sessionSeenIds.push(state.currentQuestion.wordId);
  await nextQuestion($('#practiceMode').value);
}
function clearAutoAdvance() {
  if(state.autoAdvanceTimer){clearInterval(state.autoAdvanceTimer);state.autoAdvanceTimer=null;}
  if(state.autoAdvanceTransitionTimer){clearTimeout(state.autoAdvanceTransitionTimer);state.autoAdvanceTransitionTimer=null;}
  state.autoAdvanceAt=null;
  state.autoAdvanceRemaining=null;
  $('#autoAdvanceRow')?.classList.remove('is-loading');
}
function updateAutoAdvanceUI() {
  const row=$('#autoAdvanceRow');
  if(row)row.hidden=true; // Countdown is presented in a focused waiting modal, not below the answer content.
  const active=!!state.autoAdvanceWaiting && !!state.questionAnswered && !state.practiceReviewPending && !!state.settings.autoNextEnabled && !state.autoAdvanceCancelled;
  const layer=$('#modalLayer');
  if(!active){
    if(layer?.dataset.modalType==='practice-wait')closeAutoAdvanceWaitModal();
    return;
  }
  const remaining=state.autoAdvanceAt ? state.autoAdvanceAt-Date.now() : (state.autoAdvanceRemaining??((Number(state.settings.autoNextDelaySeconds)||3)*1000));
  const seconds=Math.max(0,Math.ceil(remaining/1000));
  const duration=Math.max(1000,state.autoAdvanceDuration||((Number(state.settings.autoNextDelaySeconds)||3)*1000));
  const elapsed=Math.min(1,Math.max(0,1-Math.max(0,remaining)/duration));
  const count=$('#autoAdvanceWaitCountdown'),status=$('#autoAdvanceWaitStatus'),hint=$('#autoAdvanceWaitHint');
  const progress=$('#autoAdvanceWaitProgress'),ring=$('#autoAdvanceWaitRing'),stage=$('#autoAdvanceWaitStage');
  if(count){const next=String(seconds||'✓');if(count.textContent!==next){count.textContent=next;count.classList.remove('count-tick');void count.offsetWidth;count.classList.add('count-tick');}}
  if(progress)progress.style.width=`${Math.round(elapsed*100)}%`;
  if(ring){ring.style.setProperty('--ring-progress',`${Math.round(elapsed*100)}%`);ring.classList.toggle('is-final',seconds<=1);}
  if(status)status.textContent=seconds>0?'Đang chuẩn bị câu tiếp theo':'Đang tải câu hỏi mới…';
  if(hint)hint.textContent=seconds>0?'Hệ thống đang chọn từ phù hợp với lịch sử ôn tập của bạn.':'Một chút nữa thôi, câu hỏi tiếp theo đang được mở.';
  if(stage)stage.textContent=seconds>0?`Còn ${seconds} giây · Bạn có thể giữ câu để chuyển thủ công.`:'Đang hoàn tất chuyển câu…';
}

function pauseAutoAdvance() {
  if(state.autoAdvanceAt) state.autoAdvanceRemaining=Math.max(0,state.autoAdvanceAt-Date.now());
  if(state.autoAdvanceTimer){clearInterval(state.autoAdvanceTimer);state.autoAdvanceTimer=null;}
  state.autoAdvanceAt=null;
  if(state.questionAnswered) updateAutoAdvanceUI();
}
function resumeAutoAdvance() {
  if(!state.questionAnswered||state.practiceReviewPending||!state.autoAdvanceWaiting||!state.settings.autoNextEnabled||state.autoAdvanceCancelled||state.activePage!=='practice'||document.hidden)return;
  if(state.autoAdvanceTimer||state.autoAdvanceTransitionTimer)return;
  const delay=state.autoAdvanceRemaining ?? ((Number(state.settings.autoNextDelaySeconds)||3)*1000);
  state.autoAdvanceRemaining=null;
  state.autoAdvanceAt=Date.now()+Math.max(0,delay);
  state.autoAdvanceTimer=setInterval(()=>{
    if(state.activePage!=='practice'||document.hidden)return;
    const remaining=state.autoAdvanceAt-Date.now();
    updateAutoAdvanceUI();
    if(remaining<=0){
      clearInterval(state.autoAdvanceTimer);state.autoAdvanceTimer=null;state.autoAdvanceAt=null;
      const row=$('#autoAdvanceRow');row?.classList.add('is-loading');
      const countdown=$('#autoAdvanceCountdown');const status=$('#autoAdvanceStatus');
      if(countdown)countdown.textContent='…';
      if(status)status.textContent='Đang tải câu hỏi tiếp theo…';
      state.autoAdvanceTransitionTimer=setTimeout(async()=>{state.autoAdvanceTransitionTimer=null;if(state.activePage==='practice'&&!document.hidden){state.autoAdvanceWaiting=false;closeAutoAdvanceWaitModal();await nextQuestion();}},520);
    }
  },100);
  updateAutoAdvanceUI();
}
function scheduleAutoAdvance() {
  clearAutoAdvance();
  state.autoAdvanceCancelled=false;
  if(!state.settings.autoNextEnabled||!state.questionAnswered||state.practiceReviewPending||!state.autoAdvanceWaiting){updateAutoAdvanceUI();return;}
  state.autoAdvanceRemaining=(Number(state.settings.autoNextDelaySeconds)||3)*1000;
  state.autoAdvanceDuration=state.autoAdvanceRemaining;
  resumeAutoAdvance();
  savePracticeSession();
}
async function holdCurrentQuestion() {
  clearAutoAdvance();
  state.autoAdvanceWaiting=false;
  state.autoAdvanceCancelled=true;
  closeAutoAdvanceWaitModal();
  await savePracticeSession();
  updateAutoAdvanceUI();
  toast('Đã giữ câu hỏi. Bạn có thể xem kỹ đáp án và giải nghĩa.');
}
function setAutoNextSettings(enabled, seconds) {
  state.settings.autoNextEnabled=!!enabled;
  state.settings.autoNextDelaySeconds=[3,5,10].includes(Number(seconds))?Number(seconds):3;
  dbSet('appSettings',state.settings).catch(err=>console.warn('Không lưu được cấu hình tự chuyển:',err));
  if(!state.settings.autoNextEnabled){clearAutoAdvance();state.autoAdvanceWaiting=false;closeAutoAdvanceWaitModal();$('#nextQuestionButton').disabled=!state.questionAnswered||state.practiceReviewPending;}
  else if(state.questionAnswered&&!state.practiceReviewPending&&!state.autoAdvanceCancelled){state.autoAdvanceWaiting=true;showAutoAdvanceWaitModal();scheduleAutoAdvance();}
  updateAutoAdvanceUI();
}
function formatRemaining(ms) {
  if(ms<=0)return 'đã đến giờ nhắc';
  const total=Math.ceil(ms/1000), h=Math.floor(total/3600), m=Math.floor((total%3600)/60), s=total%60;
  return h?`${h} giờ ${m} phút`:`${m} phút ${s} giây`;
}
function isStandaloneApp() {
  return window.matchMedia?.('(display-mode: standalone)').matches || window.navigator.standalone === true;
}
function isAppleMobile() {
  return /iPhone|iPad|iPod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
}
const INSTALL_INVITE_KEY = 'toeic:pwa-install-invite:v1';
function isAndroidDevice() { return /Android/i.test(navigator.userAgent || ''); }
function isMobileOrTabletDevice() {
  const ua = navigator.userAgent || '';
  const appleTouch = /iPhone|iPad|iPod/i.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const mobileOrTabletUA = /Android|Mobile|Tablet|iPhone|iPad|iPod/i.test(ua) || navigator.userAgentData?.mobile === true;
  const compactTouchDevice = !!(navigator.maxTouchPoints > 0 && window.matchMedia?.('(max-width: 1100px)').matches && window.matchMedia?.('(pointer: coarse)').matches);
  return appleTouch || mobileOrTabletUA || compactTouchDevice;
}
function installInviteWasDismissed() {
  try { return localStorage.getItem(INSTALL_INVITE_KEY) === 'dismissed'; } catch { return false; }
}
function markInstallInviteDismissed() {
  try { localStorage.setItem(INSTALL_INVITE_KEY, 'dismissed'); } catch { /* Local storage may be disabled; the app remains usable. */ }
}
function syncInstallButton() {
  const button = $('#installButton');
  if (!button) return;
  const show = !isStandaloneApp() && (isMobileOrTabletDevice() || !!state.deferredInstall);
  button.hidden = !show;
  button.title = isMobileOrTabletDevice() ? 'Hướng dẫn thêm vào màn hình chính' : 'Cài đặt TOEIC Dictionary';
  button.setAttribute('aria-label', button.title);
}
function closeInstallInvite(remember = true) {
  state.installGuideOpen = false;
  $('#installInviteBackdrop').hidden = true;
  document.body.classList.remove('install-invite-open');
  if (remember) markInstallInviteDismissed();
}
function openInstallInvite(view = 'welcome') {
  if (!isMobileOrTabletDevice() || isStandaloneApp()) return;
  state.installGuideOpen = view === 'guide';
  const content = $('#installInviteContent');
  if (view === 'guide') {
    const apple = isAppleMobile();
    const android = isAndroidDevice();
    let platformTitle = 'Thêm ứng dụng vào Màn hình chính';
    let platformIntro = 'Tên mục có thể hơi khác nhau tùy trình duyệt và phiên bản hệ điều hành.';
    let steps = '';
    if (apple) {
      platformTitle = 'Hướng dẫn cho iPhone / iPad';
      platformIntro = 'Thao tác bằng Safari. Trình duyệt khác trên iPhone/iPad có thể không hiển thị đủ tùy chọn.';
      steps = `<ol class="install-steps"><li>Mở địa chỉ TOEIC Dictionary bằng <strong>Safari</strong>.</li><li>Nhấn nút <strong>Chia sẻ</strong> (biểu tượng hình vuông có mũi tên hướng lên) ở thanh công cụ.</li><li>Kéo danh sách xuống và chọn <strong>Thêm vào Màn hình chính (Add to Home Screen)</strong>.</li><li>Nếu thấy tùy chọn <strong>Open as Web App</strong>, hãy bật để mở như ứng dụng; giữ tên <strong>TOEIC Dictionary</strong>, sau đó nhấn <strong>Thêm (Add)</strong>.</li><li>Thoát Safari và mở TOEIC Dictionary từ biểu tượng quyển sách trên Màn hình chính.</li></ol>`;
    } else if (android) {
      platformTitle = 'Hướng dẫn cho Android / máy tính bảng';
      platformIntro = 'Khuyến nghị Chrome hoặc Edge. Nếu trình duyệt hiện hộp cài đặt, bạn có thể dùng nút cài ngay bên dưới.';
      steps = `<ol class="install-steps"><li>Mở TOEIC Dictionary bằng <strong>Chrome</strong> hoặc <strong>Edge</strong>.</li><li>Nhấn menu <strong>⋮</strong> cạnh thanh địa chỉ.</li><li>Chọn <strong>Install and create shortcut</strong> hoặc mục tương đương như <strong>Install app / Add to Home screen</strong> tùy phiên bản Chrome/Edge.</li><li>Chọn <strong>Cài đặt (Install)</strong> hoặc <strong>Thêm (Add)</strong> để xác nhận.</li><li>Quay về Màn hình chính và mở biểu tượng <strong>TOEIC Dictionary</strong>.</li></ol>`;
    } else {
      platformTitle = 'Hướng dẫn cho máy tính bảng';
      steps = `<ol class="install-steps"><li>Mở website bằng trình duyệt hiện đại.</li><li>Mở menu trình duyệt và tìm <strong>Install app</strong> hoặc <strong>Add to Home Screen</strong>.</li><li>Xác nhận thêm/cài đặt ứng dụng.</li><li>Mở TOEIC Dictionary từ biểu tượng vừa tạo.</li></ol>`;
    }
    const nativeButton = state.deferredInstall && !apple ? `<button type="button" class="primary-button" data-install-action="install">Cài đặt ngay <svg class="ui-icon button-icon"><use href="#icon-download"></use></svg></button>` : '';
    content.innerHTML = `<p class="eyebrow">HƯỚNG DẪN THEO THIẾT BỊ</p><h2 id="installInviteTitle">${platformTitle}</h2><p id="installInviteDescription">${platformIntro}</p>${steps}<div class="install-invite-actions">${nativeButton}<button type="button" class="secondary-button" data-install-action="back">Quay lại</button><button type="button" class="text-button install-web-continue" data-install-action="dismiss">Đã hiểu, tiếp tục</button></div><p class="install-invite-footnote">Bạn phải tự xác nhận thao tác trong menu chia sẻ/cài đặt của thiết bị. Website không tự mở được menu Chia sẻ của iOS.</p>`;
  } else {
    content.innerHTML = `<p class="eyebrow">TOEIC DICTIONARY · MOBILE EXPERIENCE</p><h2 id="installInviteTitle">Thêm từ điển vào Màn hình chính?</h2><p id="installInviteDescription">Bạn có thể mở TOEIC Dictionary nhanh như một ứng dụng, học tập thuận tiện hơn và dễ quay lại mỗi ngày.</p><div class="install-benefits"><span>${icon('check-circle')} Mở nhanh từ biểu tượng ứng dụng</span><span>${icon('check-circle')} Giao diện gọn, gần giống ứng dụng riêng</span><span>${icon('check-circle')} Vẫn dùng được khi offline với dữ liệu đã cache</span></div><div class="install-invite-actions"><button type="button" class="primary-button" data-install-action="guide">Hướng dẫn thêm vào màn hình chính ${icon('arrow-right','ui-icon button-icon')}</button><button type="button" class="secondary-button" data-install-action="dismiss">Để sau, tiếp tục dùng trên web</button></div><p class="install-invite-footnote">Đây là lựa chọn tự nguyện. Chọn “Để sau, tiếp tục dùng trên web” để bỏ qua và sử dụng website bình thường.</p>`;
  }
  $('#installInviteBackdrop').hidden = false;
  document.body.classList.add('install-invite-open');
}
async function runNativeInstall() {
  if (!state.deferredInstall) return;
  const promptEvent = state.deferredInstall;
  state.deferredInstall = null;
  try {
    await promptEvent.prompt();
    const choice = await promptEvent.userChoice;
    if (choice?.outcome === 'accepted') {
      markInstallInviteDismissed();
      closeInstallInvite(false);
      toast('Đã bắt đầu cài đặt TOEIC Dictionary.');
    } else {
      toast('Bạn có thể tiếp tục dùng website hoặc cài đặt sau.');
    }
  } catch (error) {
    toast('Không mở được hộp cài đặt. Hãy dùng hướng dẫn thủ công bên dưới.', 'error');
  }
  syncInstallButton();
}
function initializeInstallInvite() {
  syncInstallButton();
  if (!isMobileOrTabletDevice() || isStandaloneApp() || installInviteWasDismissed()) return;
  window.setTimeout(() => {
    if (!isStandaloneApp() && !installInviteWasDismissed()) openInstallInvite('welcome');
  }, 850);
}


function renderReminderStatus() {
  const enabled=!!state.reminder.enabled;
  const toggle=$('#reminderEnabled'); if(toggle)toggle.checked=enabled;
  const interval=$('#reminderInterval');
  if(interval){const selected=String(state.reminder.intervalMinutes||60);interval.value=REMINDER_INTERVAL_OPTIONS.map(String).includes(selected)?selected:'60';}
  const dot=$('#reminderStatusDot'); if(dot)dot.classList.toggle('enabled',enabled);
  const supported=('Notification' in window)&&('serviceWorker' in navigator);
  const permission=supported?Notification.permission:'unsupported';
  const permissionButton=$('#notificationPermissionButton');
  if(permissionButton){
    const label=permission==='granted'?'Thông báo đã được cấp quyền':permission==='denied'?'Thông báo đang bị chặn':permission==='unsupported'?'Không hỗ trợ thông báo':'Cho phép thông báo';
    permissionButton.innerHTML=`${icon('bell','ui-icon button-icon')}${label}`;
    permissionButton.disabled=permission==='granted'||permission==='unsupported'||permission==='denied';
  }
  const info=$('#reminderInfo');
  if(info){
    if(!enabled)info.textContent='Nhắc nhở đang tắt. Bật để bắt đầu chu kỳ.';
    else if(permission==='unsupported')info.textContent='Thiết bị/trình duyệt không hỗ trợ thông báo hệ thống. Popup trong website vẫn hoạt động khi trang đang mở.';
    else if(permission==='denied')info.textContent='Bạn đã chặn thông báo. Hãy cho phép Notifications trong cài đặt của trình duyệt hoặc thiết bị.';
    else if(permission!=='granted')info.textContent='Bộ đếm cục bộ đã bật. Cấp quyền Notifications để hiển thị thông báo hệ thống khi ứng dụng còn hoạt động.';
    else info.textContent=`Đã cấp quyền thông báo hệ thống. ${state.reminder.nextAt?`Lượt nhắc tiếp theo: ${formatRemaining(state.reminder.nextAt-Date.now())}.`:'Đang chuẩn bị chu kỳ nhắc.'}`;
  }
  const help=$('#notificationPlatformHelp');
  if(help){
    if(isAppleMobile()&&!isStandaloneApp())help.textContent='iPhone/iPad: để hiện thông báo hệ thống, hãy thêm website vào Màn hình chính bằng Safari, mở từ biểu tượng TOEIC Dictionary rồi mới cấp quyền Notifications.';
    else if(isAppleMobile())help.textContent='iPhone/iPad: bạn đang dùng PWA. Cho phép Notifications và kiểm tra Cài đặt iOS → Thông báo → TOEIC Dictionary.';
    else if(/Android/i.test(navigator.userAgent))help.textContent='Android: dùng Chrome/Edge, cấp quyền Notifications cho website/PWA và kiểm tra cài đặt thông báo của hệ điều hành.';
    else help.textContent='PC/laptop: cấp quyền Notifications cho website trong trình duyệt và cài đặt thông báo Windows/macOS.';
  }
}
async function setReminderEnabled(enabled) {
  state.reminder.enabled=!!enabled;
  state.reminder.intervalMinutes=Number($('#reminderInterval').value)||60;
  state.reminder.nextAt=enabled?Date.now()+state.reminder.intervalMinutes*60000:null;
  state.reminder.pendingAnswered=true; state.reminder.pendingWordId=null;
  await dbSet('reminderSettings',state.reminder);
  renderReminderStatus();
  toast(enabled?'Đã bật nhắc nhở cục bộ.':'Đã tắt nhắc nhở học tập.');
}
async function requestNotificationPermission() {
  if(isAppleMobile()&&!isStandaloneApp()){toast('Trên iPhone/iPad, hãy thêm website vào Màn hình chính và mở từ biểu tượng TOEIC Dictionary trước khi xin quyền thông báo.','error');renderReminderStatus();return;}
  if(!('Notification' in window)){toast('Trình duyệt này không hỗ trợ thông báo hệ thống.','error');return;}
  if(Notification.permission==='denied'){toast('Thông báo đang bị chặn. Hãy cho phép quyền Notifications trong cài đặt website của trình duyệt.','error');return;}
  try {
    const permission=await state.notificationProvider?.requestPermission?.() || await Notification.requestPermission();
    renderReminderStatus();
    toast(permission==='granted'?'Đã cấp quyền thông báo.':permission==='denied'?'Bạn đã chặn thông báo.':'Chưa cấp quyền thông báo.',permission==='granted'?'success':'error');
  } catch(err){toast('Không thể yêu cầu quyền thông báo trên thiết bị này.','error');}
}
function showReminderPopup(title, body) {
  const host=$('#toastRegion');
  host.querySelectorAll('.reminder-popup').forEach(node=>node.remove());
  const popup=document.createElement('section');
  popup.className='reminder-popup'; popup.setAttribute('role','status');
  popup.innerHTML=`<div class="reminder-popup-head"><span class="reminder-popup-icon">${icon('book-open')}</span><strong>${escapeHtml(title)}</strong><button type="button" data-reminder-close aria-label="Đóng thông báo">×</button></div><p>${escapeHtml(body)}</p><div class="reminder-popup-actions"><button type="button" class="reminder-popup-open" data-reminder-open>Ôn tập ngay</button><span>TOEIC DICTIONARY</span></div>`;
  popup.addEventListener('click',event=>{if(event.target.closest('[data-reminder-close]'))popup.remove();if(event.target.closest('[data-reminder-open]')){popup.remove();navigate('practice');}});
  host.append(popup); window.setTimeout(()=>{if(popup.isConnected)popup.remove();},18000);
}
async function deliverReminder(title, body) {
  let delivered=false;
  if(('Notification'in window)&&Notification.permission==='granted'&&state.notificationProvider){
    try { const result=await state.notificationProvider.sendNotification({title,body,url:new URL('./?open=practice',location.href).href,tag:'toeic-study-reminder'}); delivered=!!result.delivered; }
    catch(err){console.warn('Không thể gửi thông báo hệ thống:',err);}
  }
  if(document.visibilityState==='visible'&&!delivered)showReminderPopup(title,body);
  return delivered || document.visibilityState==='visible';
}
async function checkReminder() {
  if(state.reminderChecking || !state.reminder.enabled || !state.reminder.nextAt || Date.now()<state.reminder.nextAt)return;
  state.reminderChecking=true;
  try {
    let title,body;
    if(state.reminder.pendingAnswered){
      const q=makeQuestion('random');
      if(q){state.currentQuestion=q;state.questionAnswered=false;state.lastFeedback=null;state.reminder.pendingWordId=q.wordId;await savePracticeSession();renderQuestion();}
      title='TOEIC Dictionary – Đến giờ ôn tập';
      body=q?`${q.prompt} Mở ứng dụng để trả lời.`:'Đã đến giờ dành vài phút cho từ vựng TOEIC.';
      state.reminder.pendingAnswered=false;
    } else {
      title='TOEIC Dictionary – Nhắc bạn quay lại';
      body='Bạn chưa trả lời câu hỏi trước đó. Hãy dành 1–2 phút ôn lại từ vựng nhé!';
    }
    state.reminder.lastTriggeredAt=Date.now();
    state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;
    await dbSet('reminderSettings',state.reminder);
    await deliverReminder(title,body);
    renderReminderStatus();
  } catch(err) {
    console.warn('Không thể xử lý nhắc nhở:',err);
  } finally {
    state.reminderChecking=false;
  }
}
async function initializePractice() {
  state.progress=await dbGet('studyProgress')||{};
  const reminder=await dbGet('reminderSettings');
  if(reminder&&typeof reminder==='object')state.reminder={...PRACTICE_DEFAULT_REMINDER,...reminder};
  if(!REMINDER_INTERVAL_OPTIONS.includes(Number(state.reminder.intervalMinutes)))state.reminder.intervalMinutes=60;
  const settings=await dbGet('appSettings');
  if(settings&&typeof settings==='object')state.settings={...state.settings,...settings,tts:{...DEFAULT_TTS_SETTINGS,...(settings.tts||{})}};
  else state.settings.tts={...DEFAULT_TTS_SETTINGS};
  if(![3,5,10].includes(Number(state.settings.autoNextDelaySeconds)))state.settings.autoNextDelaySeconds=3;
  const session=await dbGet('practiceSession');
  if(session){
    state.currentQuestion=session.currentQuestion||null; state.questionAnswered=!!session.questionAnswered; state.practiceReviewPending=!!session.practiceReviewPending; state.pendingSinglePractice=session.pendingSinglePractice||null;
    state.sessionSeenIds=Array.isArray(session.sessionSeenIds)?session.sessionSeenIds:[];
    state.sentenceCompletionSeenIds=Array.isArray(session.sentenceCompletionSeenIds)?session.sentenceCompletionSeenIds:[];
    state.lastFeedback=session.lastFeedback||null;
    state.autoAdvanceCancelled=!!session.autoAdvanceCancelled;
    state.autoAdvanceWaiting=!!session.autoAdvanceWaiting;
    if(state.currentQuestion?.word){const oldWord=String(state.currentQuestion.word);const newWord=displayWord(oldWord);state.currentQuestion.prompt=String(state.currentQuestion.prompt||'').split(oldWord).join(newWord);state.currentQuestion.word=newWord;if(state.currentQuestion.expectedWord&&state.currentQuestion.expectedDisplay)state.currentQuestion.expectedDisplay=displayWord(state.currentQuestion.expectedDisplay);}
  }
  if(state.currentQuestion&&!state.words.some(w=>w.id===state.currentQuestion.wordId)){state.currentQuestion=null;state.questionAnswered=false;}
  updatePracticeStats(); renderQuestion(); renderReminderStatus(); syncSettingsUI();
  if(state.reminder.enabled&&!state.reminder.nextAt){state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;await dbSet('reminderSettings',state.reminder);}
  setInterval(()=>{checkReminder();renderReminderStatus();},15000);
  document.addEventListener('visibilitychange',()=>{if(document.hidden)pauseAutoAdvance();else {checkReminder();resumeAutoAdvance();}});
  window.addEventListener('focus',()=>{checkReminder();resumeAutoAdvance();});
  if(new URLSearchParams(location.search).get('open')==='practice')navigate('practice');
  if(state.pendingSinglePractice&&state.lastFeedback){showSinglePracticeResult();}
  else if(state.questionAnswered&&state.practiceReviewPending&&state.lastFeedback){openPracticeReviewModal(state.lastFeedback);}
  else if(state.questionAnswered&&!state.autoAdvanceCancelled&&state.settings.autoNextEnabled){state.autoAdvanceWaiting=true;state.autoAdvanceRemaining=(Number(state.settings.autoNextDelaySeconds)||3)*1000;state.autoAdvanceDuration=state.autoAdvanceRemaining;showAutoAdvanceWaitModal();resumeAutoAdvance();}
}
function syncSettingsUI(){
  const enabled=$('#autoNextEnabled');if(enabled)enabled.checked=!!state.settings.autoNextEnabled;
  const delay=$('#autoNextDelay');if(delay)delay.value=String([3,5,10].includes(Number(state.settings.autoNextDelaySeconds))?state.settings.autoNextDelaySeconds:3);
  renderReminderStatus();
  const tts={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})};
  const controls={ttsAccent:tts.accent,ttsDefaultGender:tts.defaultGender,ttsRate:String(tts.rate),ttsPitch:String(tts.pitch),ttsVolume:String(tts.volume),ttsWordPause:String(tts.wordPauseMs),ttsSentencePause:String(tts.sentencePauseMs)};
  for(const [id,value] of Object.entries(controls)){const el=$(`#${id}`);if(el)el.value=value;}
  refreshSpeechVoiceSelectors();
}
function bindPracticeEvents() {
  bindTtsSettings();
  $('#newQuestionButton').addEventListener('click',startPracticeFocus);
  $('#practiceModeGrid')?.addEventListener('click',e=>{const b=e.target.closest('[data-practice-mode]');if(!b)return;const select=$('#practiceMode');if(select){select.value=b.dataset.practiceMode;select.dispatchEvent(new Event('change',{bubbles:true}));}$$('[data-practice-mode]').forEach(x=>{const selected=x===b;x.classList.toggle('is-selected',selected);x.setAttribute('aria-pressed',String(selected));});});
  $('#nextQuestionButton').addEventListener('click',()=>nextQuestion());
  $('#skipQuestionButton').addEventListener('click',skipQuestion);
  $('#practiceMode').addEventListener('change',()=>{if(learningFocusState.active&&learningFocusState.kind==='practice'){const mode=$('#practiceMode').value;nextQuestion(mode).then(started=>{if(started)updatePracticeFocusHeader(state.currentQuestion?.mode||mode);});}});
  $('#answerForm').addEventListener('submit',e=>{e.preventDefault();submitAnswer($('#answerInput').value);});
  $('#choiceList').addEventListener('click',e=>{const b=e.target.closest('[data-choice]');if(b&&!state.questionAnswered){$$('.choice-option',$('#choiceList')).forEach(x=>x.classList.remove('selected'));b.classList.add('selected');submitAnswer(b.dataset.choice);}});
  $('#weakWordList').addEventListener('click',e=>{const b=e.target.closest('[data-weak-word]');if(b)showDetail(b.dataset.weakWord);});
  $('#reminderEnabled').addEventListener('change',e=>setReminderEnabled(e.target.checked));
  $('#reminderInterval').addEventListener('change',async()=>{const selected=Number($('#reminderInterval').value);state.reminder.intervalMinutes=REMINDER_INTERVAL_OPTIONS.includes(selected)?selected:60;if(state.reminder.enabled)state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;await dbSet('reminderSettings',state.reminder);renderReminderStatus();toast(`Đã cập nhật chu kỳ ${state.reminder.intervalMinutes} phút.`);});
  $('#notificationPermissionButton').addEventListener('click',requestNotificationPermission);
  $('#autoNextEnabled').addEventListener('change',e=>setAutoNextSettings(e.target.checked,$('#autoNextDelay').value));
  $('#autoNextDelay').addEventListener('change',()=>setAutoNextSettings($('#autoNextEnabled').checked,$('#autoNextDelay').value));
  $('#holdQuestionButton').addEventListener('click',holdCurrentQuestion);
  $('#analyzeAnswerAIButton').addEventListener('click',()=>showAIPromptModal(buildPracticeAIPrompt()));
}

function openMobileGroupMenu(group){
  const menu=$('#mobileGroupMenu'),title=$('#mobileGroupTitle'),options=$('#mobileGroupOptions');if(!menu||!title||!options)return;
  const groups={learning:{title:'Học tập',items:[['foundation','Lộ trình học','Chọn cấp độ bắt đầu phù hợp'],['mock','Thi thử TOEIC','15 phút, 60 phút hoặc Full Test 200 câu'],['flashcards','Flashcard từ vựng','Học theo lượt 10 từ và kiểm tra nhanh'],['grammar','Ngữ pháp','Cấu trúc câu và điểm ngữ pháp'],['reading','Đọc hiểu','Email, thông báo và bài đọc'],['listening','Nghe','Hội thoại và bài nói TOEIC']]},config:{title:'Cấu hình',items:[['settings','Cấu hình','Nhắc học và tùy chỉnh'],['data','Quản lý dữ liệu','Từ vựng cá nhân và sao lưu']]}};
  const data=groups[group];if(!data)return;title.textContent=data.title;options.innerHTML=data.items.map(([page,label,desc])=>`<button type="button" class="mobile-group-option" data-group-page="${page}"><strong>${label}</strong><small>${desc}</small><span>→</span></button>`).join('');menu.hidden=false;
}


const MOCK_HISTORY_KEY = 'toeic:mock-history:v1';
const MOCK_ACTIVE_KEY = 'toeic:mock-active:v1';
const MOCK_RESULT_KEY = 'toeic:mock-last-result:v1';
const MOCK_PENDING_REVIEW_KEY = 'toeic:mock-pending-review:v1';
const MOCK_USAGE_KEY = 'toeic:mock-usage:v1';
const MOCK_PART_TIPS = {
  'Part 1':'Luyện nhận diện người/vật, hành động chính, vị trí và trạng thái trong ảnh. Nghe động từ và cụm giới từ thay vì chỉ bắt danh từ.',
  'Part 2':'Nhận diện từ để hỏi, ý định xác nhận/đề nghị và chọn câu đáp tự nhiên; cảnh giác câu trả lời đúng ngữ pháp nhưng sai ngữ cảnh.',
  'Part 3':'Nghe mục đích cuộc gọi, vai trò người nói, vấn đề, thời gian và bước tiếp theo. Tập ghi nhớ thông tin xuyên suốt cả hội thoại.',
  'Part 4':'Xác định loại thông báo, đối tượng nghe, mốc thời gian, địa điểm và hướng dẫn/hành động tiếp theo.',
  'Part 5':'Ôn từ loại, hòa hợp chủ-vị, thì, dạng động từ, giới từ, liên từ và cấu trúc câu; đọc cả câu trước khi chọn.',
  'Part 6':'Luyện liên kết câu/đoạn, tham chiếu đại từ, từ nối và câu chèn; đọc mạch văn trước và sau chỗ trống.',
  'Part 7':'Đọc câu hỏi để xác định mục tiêu, định vị tên/ngày/số liệu, nhận diện paraphrase và đối chiếu chéo các tài liệu.'
};
function readMockStorage(key, fallback){try{const raw=localStorage.getItem(key);return raw?JSON.parse(raw):fallback;}catch(error){console.warn('Mock storage parse failed:',error);return fallback;}}
function saveMockStorage(){try{localStorage.setItem(MOCK_HISTORY_KEY,JSON.stringify(state.mockHistory.slice(-60)));localStorage.setItem(MOCK_USAGE_KEY,JSON.stringify(state.mockUsageCounts||{}));if(state.mockExam?.status==='active')localStorage.setItem(MOCK_ACTIVE_KEY,JSON.stringify(state.mockExam));else localStorage.removeItem(MOCK_ACTIVE_KEY);if(state.lastMockResult)localStorage.setItem(MOCK_RESULT_KEY,JSON.stringify(state.lastMockResult));else localStorage.removeItem(MOCK_RESULT_KEY);if(state.pendingMockResult)localStorage.setItem(MOCK_PENDING_REVIEW_KEY,JSON.stringify(state.pendingMockResult));else localStorage.removeItem(MOCK_PENDING_REVIEW_KEY);}catch(error){console.warn('Không thể lưu bài thi thử:',error);toast('Không thể lưu tiến trình thi thử trên thiết bị này.','error');}}
function loadMockState(){
  const history=readMockStorage(MOCK_HISTORY_KEY,[]);state.mockHistory=Array.isArray(history)?history.slice(-60):[];
  const storedUsage=readMockStorage(MOCK_USAGE_KEY,null);
  if(storedUsage&&typeof storedUsage==='object'&&!Array.isArray(storedUsage)){state.mockUsageCounts=storedUsage;}
  else{state.mockUsageCounts={};}
  const recentUsage={};for(const attempt of state.mockHistory){for(const id of attempt.questionIds||[])recentUsage[id]=(Number(recentUsage[id])||0)+1;}
  for(const [id,count] of Object.entries(recentUsage))state.mockUsageCounts[id]=Math.max(Number(state.mockUsageCounts[id])||0,count);
  try{localStorage.setItem(MOCK_USAGE_KEY,JSON.stringify(state.mockUsageCounts));}catch(error){console.warn('Không thể khởi tạo lịch sử sử dụng câu hỏi thi thử:',error);}
  const pending=readMockStorage(MOCK_PENDING_REVIEW_KEY,null);state.pendingMockResult=pending?.exam&&pending?.score?pending:null;
  const lastResult=readMockStorage(MOCK_RESULT_KEY,null);state.lastMockResult=!state.pendingMockResult&&lastResult?.exam&&lastResult?.score?lastResult:null;
  const active=readMockStorage(MOCK_ACTIVE_KEY,null);
  if(active&&active.status==='active'&&active.sections?.listening&&active.sections?.reading){state.mockExam=active;}else state.mockExam=null;
}
function mockPoolCount(rows,parts){return (rows||[]).filter(row=>parts.includes(row.part)&&(!row.editorialStatus||['approved-for-mock','internal-editorial-reviewed'].includes(row.editorialStatus))).reduce((sum,row)=>sum+(row.questions||[]).length,0);}
function mockFormatDuration(seconds){const value=Math.max(0,Math.floor(seconds));const h=Math.floor(value/3600),m=Math.floor(value%3600/60),s=value%60;return h?`${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`:`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
function mockModeName(id){return MOCK_MODES[id]?.label||'Thi thử TOEIC';}
function mockResultBand(accuracy){if(accuracy>=85)return 'Tốt';if(accuracy>=75)return 'Khá tốt';if(accuracy>=65)return 'Tiệm cận mục tiêu luyện tập';if(accuracy>=50)return 'Đang hình thành nền tảng';return 'Cần củng cố nền tảng';}
function openMockWorkspace(){
  if(state.pendingMockResult){showPendingMockResult();return;}
  if(state.mockExam?.status==='active'){
    if(getMockSectionForTime(state.mockExam,Date.now())==='expired'){finishMockExam(true);return;}
    renderMockHome();return;
  }
  if(state.lastMockResult){renderMockResult(state.lastMockResult.exam,state.lastMockResult.score);return;}
  renderMockHome();
}
function renderMockHome(){
  $('#mockLanding').hidden=false;$('#mockExamStage').hidden=true;$('#mockResultStage').hidden=true;
  const listening=mockPoolCount(state.listening,['Part 1','Part 2','Part 3','Part 4']);
  const reading=mockPoolCount(state.readings,['Part 5','Part 6','Part 7']);
  const pendingItems=state.listening.filter(item=>item.editorialStatus==='reserve-pending-independent-review');
  const pending=pendingItems.reduce((n,item)=>n+(item.questions||[]).length,0);
  $('#mockPoolStats').innerHTML=`<div class="mock-pool-chip"><strong>${listening}</strong><span>Listening khả dụng</span></div><div class="mock-pool-chip"><strong>${reading}</strong><span>Reading khả dụng</span></div><div class="mock-pool-chip"><strong>${state.listening.length+state.readings.length}</strong><span>Cụm bài nguồn</span></div><div class="mock-pool-chip"><strong>${pending}</strong><span>Câu reserve đang chờ duyệt</span></div>`;
  const listeningParts=['Part 1','Part 2','Part 3','Part 4'];
  const twoFormTargets={'Part 1':12,'Part 2':50,'Part 3':78,'Part 4':60};
  const eligibleByPart=Object.fromEntries(listeningParts.map(part=>[part,state.listening.filter(item=>item.part===part&&(!item.editorialStatus||item.editorialStatus==='approved-for-mock')).reduce((n,item)=>n+(item.questions||[]).length,0)]));
  const pendingByPart=Object.fromEntries(listeningParts.map(part=>[part,pendingItems.filter(item=>item.part===part).reduce((n,item)=>n+(item.questions||[]).length,0)]));
  const projectedByPart=Object.fromEntries(listeningParts.map(part=>[part,eligibleByPart[part]+pendingByPart[part]]));
  const readinessRows=listeningParts.map(part=>`<div class="mock-readiness-row"><strong>${part}</strong><span>Đang dùng: ${eligibleByPart[part]}</span><span>Chờ duyệt: ${pendingByPart[part]}</span><b>${projectedByPart[part]} / ${twoFormTargets[part]}</b></div>`).join('');
  const projectedTotal=listeningParts.reduce((n,part)=>n+projectedByPart[part],0);
  const part1Gap=Math.max(0,twoFormTargets['Part 1']-projectedByPart['Part 1']);const approvedText=`Sau khi được duyệt toàn bộ, ngân hàng dự kiến có ${projectedTotal} câu. Part 1 hiện có ${projectedByPart['Part 1']} câu ảnh JPG đã khai báo nguồn; còn thiếu ${part1Gap} ảnh riêng để đạt 12 vị trí cho hai đề không lặp.`;
  const readiness=$('#mockPoolReadiness');
  if(readiness)readiness.innerHTML=`<div class="mock-readiness-head"><div><strong>Khả năng tạo hai đề Listening 100 câu</strong><small>Chỉ nội dung đã được phê duyệt mới được đưa vào Mock Exam.</small></div><span>${listening} khả dụng · ${pending} chờ duyệt</span></div><div class="mock-readiness-grid">${readinessRows}</div><p>${approvedText}</p>`;
  renderToeicScoreReadiness();
  const resume=$('#mockResumePanel');resume.hidden=state.mockExam?.status!=='active';
  if(!resume.hidden){const exam=state.mockExam,all=getExamQuestions(exam.sections.listening).length+getExamQuestions(exam.sections.reading).length,answered=Object.keys(exam.answers||{}).length;$('#mockResumeTitle').textContent=`${exam.modeLabel} · ${answered}/${all} câu đã trả lời`;
    const remain=Math.max(0,Math.ceil((exam.totalDeadlineAt-Date.now())/60000));$('#mockResumeDescription').textContent=`Bắt đầu ${new Date(exam.startedAt).toLocaleString('vi-VN')} · còn khoảng ${remain} phút. Đồng hồ vẫn chạy khi bạn rời trang.`;}
  $('#mockHistoryCount').textContent=`${state.mockHistory.filter(x=>x.status==='completed').length} lượt`;
  renderMockHistory();
  if(state.mockTickTimer){clearInterval(state.mockTickTimer);state.mockTickTimer=null;}
}

function renderToeicScoreReadiness(){
  const host=$('#toeicScoreReadiness');if(!host)return;
  const snapshot=buildMockScoreReadiness(state.mockHistory);
  if(!snapshot.enough){
    host.innerHTML=`<div class="score-readiness-heading"><div><p class="eyebrow">TOEIC SCORE READINESS · EVIDENCE TRACKER</p><h3>Theo dõi tiến bộ hướng tới mục tiêu</h3></div><span class="score-readiness-status">Chưa đủ dữ liệu</span></div><p>Đã có <strong>${snapshot.count}/3</strong> bài Full Mock hoàn thành đủ 200 câu. Sau 3 bài, hệ thống mới hiển thị xu hướng Listening và Reading qua nhiều lần thi.</p><div class="score-readiness-progress"><span style="width:${Math.min(100,snapshot.count/3*100)}%"></span></div><small>Mục tiêu cá nhân 500+ và chuẩn thiết kế hệ thống 850+ được giữ riêng. Chưa quy đổi tỷ lệ đúng thành điểm ETS.</small>`;
    return;
  }
  const trend=value=>value>5?'Tăng':value< -5?'Giảm':'Ổn định';
  const listeningMetric=snapshot.listeningTrendEnough
    ? `<div><small>Listening · trung bình (${snapshot.listeningDistinctForms} bộ câu hỏi)</small><strong>${snapshot.listeningAverage}%</strong><span>${trend(snapshot.listeningChange)} ${snapshot.listeningChange>0?'+':''}${snapshot.listeningChange} điểm %</span>${snapshot.listeningWarning?`<small class="score-readiness-caveat">${escapeHtml(snapshot.listeningWarning)}</small>`:''}</div>`
    : `<div><small>Listening · xu hướng tạm ẩn</small><strong>Chưa đủ bộ đề độc lập</strong><span>${snapshot.listeningDistinctForms} bộ câu hỏi khác nhau được nhận diện</span><small class="score-readiness-caveat">${escapeHtml(snapshot.listeningWarning)}</small></div>`;
  host.innerHTML=`<div class="score-readiness-heading"><div><p class="eyebrow">TOEIC SCORE READINESS · EVIDENCE TRACKER</p><h3>Xu hướng qua 3 bài Full Mock gần nhất</h3></div><span class="score-readiness-status">Đủ dữ liệu bài thi</span></div><div class="score-readiness-metrics">${listeningMetric}<div><small>Reading · trung bình</small><strong>${snapshot.readingAverage}%</strong><span>${trend(snapshot.readingChange)} ${snapshot.readingChange>0?'+':''}${snapshot.readingChange} điểm %</span></div></div><p>Đây là tỷ lệ đúng trung bình của 3 bài Full Mock gần nhất. Listening chỉ mở xu hướng khi xác nhận ít nhất hai bộ câu hỏi khác nhau; độ trùng lặp cao vẫn được cảnh báo. Không phải điểm TOEIC /495 hoặc /990, không dự báo chắc chắn khả năng đạt 500+ hay 850+.</p><small>Điểm ETS cần được hiệu chuẩn theo đề thi tương đương và phương pháp quy đổi của ETS. Kết quả học tập cá nhân vẫn cần đối chiếu với bài thi chính thức.</small>`;
}

function renderMockHistory(){
  const rows=state.mockHistory.filter(x=>x.status==='completed').slice(-5).reverse();
  $('#mockHistoryList').innerHTML=rows.length?rows.map(item=>`<div class="mock-history-row"><strong>${escapeHtml(mockModeName(item.modeId))}</strong><span>${new Date(item.completedAt).toLocaleString('vi-VN')}</span><b>${Number(item.correct||0)}/${Number(item.questions||0)} · ${Number(item.accuracy||0)}%</b><small>Listening ${Number(item.listeningAccuracy||0)}% · Reading ${Number(item.readingAccuracy||0)}%</small></div>`).join(''):'<p class="muted">Bạn chưa hoàn thành bài thi nào.</p>';
}
function startMockExam(modeId){
  const quickHelpRoot=$('#quickHelp');if(quickHelpRoot)quickHelpRoot.hidden=true;
  if(state.mockExam?.status==='active'&&!window.confirm('Bạn đang có bài thi chưa hoàn tất. Bỏ bài hiện tại để tạo đề mới?'))return;
  if(state.mockExam?.status==='active')markMockAttemptAbandoned();
  try{
    const used=state.mockUsageCounts||{};
    const exam=createMockExam({modeId,listening:state.listening,readings:state.readings,usageCounts:used});
    exam.reusedQuestionCount=exam.questionIds.filter(id=>(Number(used[id])||0)>0).length;
    for(const id of exam.questionIds)state.mockUsageCounts[id]=(Number(state.mockUsageCounts[id])||0)+1;
    state.mockExam=exam;state.lastMockResult=null;
    state.mockHistory.push({attemptId:exam.id,modeId,status:'in-progress',startedAt:exam.startedAt,questionIds:[...exam.questionIds]});
    state.mockHistory=state.mockHistory.slice(-60);saveMockStorage();if(exam.reusedQuestionCount)toast(`Đề mới có ${exam.reusedQuestionCount} câu từng xuất hiện trước đó; ngân hàng chưa đủ để tạo đề hoàn toàn mới ở mọi Part.`,'error');renderMockExam();
  }catch(error){console.error(error);toast(error.message||'Không thể tạo đề thi thử.','error');}
}
function markMockAttemptAbandoned(){
  const exam=state.mockExam;if(!exam)return;stopSpeech();if(state.mockTickTimer){clearInterval(state.mockTickTimer);state.mockTickTimer=null;}
  const record=state.mockHistory.find(item=>item.attemptId===exam.id);if(record){record.status='abandoned';record.abandonedAt=Date.now();}
  state.mockExam=null;saveMockStorage();
}
function resumeMockExam(){if(!state.mockExam)return;if(getMockSectionForTime(state.mockExam,Date.now())==='expired'){finishMockExam(true);return;}renderMockExam();}
function discardMockExam(){if(!state.mockExam)return;if(!window.confirm('Bỏ bài thi đang làm? Các câu trả lời trong bài này sẽ bị xóa.'))return;markMockAttemptAbandoned();renderMockHome();}
function getMockVisibleQuestions(){
  const exam=state.mockExam;if(!exam)return[];
  const area=exam.currentSection==='reading'?'reading':'listening';
  const offset=area==='reading'?getExamQuestions(exam.sections.listening).length:0;
  const rows=[];let number=offset;
  for(const group of exam.sections[area].groups){for(const question of group.questions){number++;rows.push({group,question,number,area});}}
  return rows;
}
function mockChoicesMarkup(group,question){
  const isPart1=group.part==='Part 1';const choices=isPart1?['A','B','C','D']:question.choices;
  return `<div class="mock-choice-grid">${choices.map((choice,index)=>`<button type="button" class="mock-choice-button ${state.mockExam.answers?.[question.id]===index?'is-selected':''}" data-mock-answer="${escapeHtml(question.id)}" data-choice-index="${index}" aria-pressed="${state.mockExam.answers?.[question.id]===index}"><strong>${String.fromCharCode(65+index)}</strong><span>${isPart1?'':escapeHtml(choice)}</span></button>`).join('')}</div>`;
}
function mockQuestionMarkup(group,question,number){
  const flagged=(state.mockExam.flags||[]).includes(question.id);
  return `<article class="mock-question-card" id="mock-question-${escapeHtml(question.id)}" data-mock-question-id="${escapeHtml(question.id)}"><div class="mock-question-line"><span class="mock-question-number">QUESTION ${number}</span><h4>${escapeHtml(question.question)}</h4><button type="button" class="mock-flag-button ${flagged?'is-flagged':''}" data-mock-flag="${escapeHtml(question.id)}" aria-pressed="${flagged}">${flagged?'★ Đã đánh dấu':'☆ Đánh dấu'}</button></div>${mockChoicesMarkup(group,question)}</article>`;
}
function mockGroupMarkup(group,numberById){
  const first=group.questions[0],start=numberById.get(first?.id)||0;
  const title=group.title||group.unitId;
  const isListening=group.area==='listening';
  let media='';
  if(isListening){
    const audioLabel=group.part==='Part 1'?`Part 1: ${group.topic||title} → câu dẫn → nhãn A/B/C/D (nghỉ 1,5 giây) → mô tả`:group.part==='Part 2'?'Nghe câu hỏi và chọn phản hồi':'Nghe toàn bộ nội dung trước khi trả lời';
    media=`<div class="mock-group-audio"><button type="button" class="mock-audio-button" data-mock-audio="${escapeHtml(group.unitId)}">▶ Phát audio / TTS</button><small id="mock-audio-status-${escapeHtml(group.unitId)}">${audioLabel} · Transcript chỉ mở sau khi nộp bài.</small></div>`;
    if(group.part==='Part 1'){media+=`<figure class="mock-part1-frame"><img class="mock-part1-image" data-photo-id="${escapeHtml(group.unitId)}" src="${escapeHtml(group.photo)}" alt="${escapeHtml(group.imageAlt)}" loading="lazy"><figcaption>PHOTOGRAPH · ${escapeHtml(title)}</figcaption></figure>`;}
  }else if(group.part!=='Part 5'){
    const docs=group.documents||[];
    if(docs.length)media=`<div class="mock-reading-passage">${docs.map(doc=>`<div class="reading-document-card"><span class="reading-passage-label">${escapeHtml(doc.label||'DOCUMENT')}</span><pre>${escapeHtml(doc.content||'')}</pre></div>`).join('')}</div>`;
    else if(group.passage)media=`<div class="mock-reading-passage"><span class="reading-passage-label">${escapeHtml(group.documentType||group.part)}</span><pre>${escapeHtml(group.passage)}</pre></div>`;
  }
  const tip=group.part==='Part 2'?'Mỗi câu hỏi có một phản hồi phù hợp nhất.':group.part==='Part 3'||group.part==='Part 4'?'Nghe hết hội thoại/bài nói; các câu hỏi trong cùng nhóm được giữ nguyên thứ tự.':group.part==='Part 1'?'Nghe tên chủ đề Part 1, câu dẫn, từng nhãn A–D; mỗi nhãn nghỉ 1,5 giây trước khi đọc mô tả. Quan sát ảnh và chọn câu mô tả đúng nhất.':'';
  return `<section class="mock-question-group" data-mock-group="${escapeHtml(group.unitId)}"><header class="mock-group-header"><div><h3>${escapeHtml(title)}</h3><p>${escapeHtml(group.topic||tip)}</p></div><span class="mock-group-part">${escapeHtml(group.part)}</span></header>${media}${group.questions.map(question=>mockQuestionMarkup(group,question,numberById.get(question.id)||0)).join('')}</section>`;
}

function ensureMockGuidedFlow(exam){
 if(!exam.flow||typeof exam.flow!=='object')exam.flow={enabled:true,voiceEnabled:true,activeQuestionIds:{listening:null,reading:null},lastAnnouncedIds:{listening:null,reading:null},schedules:{}};
 exam.flow.activeQuestionIds=exam.flow.activeQuestionIds||{listening:null,reading:null};
 exam.flow.lastAnnouncedIds=exam.flow.lastAnnouncedIds||{listening:null,reading:null};
 exam.flow.schedules=exam.flow.schedules||{};
 if(!Array.isArray(exam.flow.schedules.listening))exam.flow.schedules.listening=buildMockQuestionSchedule(exam.sections.listening,'listening',exam.startedAt,(exam.listeningDeadlineAt-exam.startedAt)/1000,0);
 if(!Array.isArray(exam.flow.schedules.reading))exam.flow.schedules.reading=buildMockQuestionSchedule(exam.sections.reading,'reading',exam.listeningDeadlineAt,(exam.totalDeadlineAt-exam.listeningDeadlineAt)/1000,getExamQuestions(exam.sections.listening).length);
 return exam.flow;
}
function updateMockGuidedFlow(timestamp=Date.now()){
 const exam=state.mockExam;if(!exam||exam.status!=='active')return;
 const area=exam.currentSection==='reading'?'reading':'listening',flow=ensureMockGuidedFlow(exam),schedule=flow.schedules[area]||[];
 const slot=getMockScheduledQuestion(schedule,timestamp);if(!slot)return;
 const sectionQuestions=getExamQuestions(exam.sections[area]);
 const previous=slot.index>0?schedule[slot.index-1]:null;
 const group=exam.sections[area].groups.find(item=>item.unitId===slot.unitId);
 const changed=flow.activeQuestionIds[area]!==slot.questionId;
 if(changed){
   flow.activeQuestionIds[area]=slot.questionId;flow.lastAnnouncedIds[area]=slot.questionId;saveMockStorage();
   const leadIn=group?.part==='Part 1'?`Part 1: ${group.topic||group.title||'Photographs'}. ${PART1_LEAD_IN_TEXT}`:getMockTransitionLeadIn(previous,slot,sectionQuestions.length);
   const label=`${area==='listening'?'Listening':'Reading'} · ${slot.part} · Câu ${slot.questionNumber}`;
   const copy=$('#mockFlowQuestionLabel'),lead=$('#mockFlowLeadIn'),status=$('#mockFlowStatus');
   if(copy)copy.textContent=label;if(lead)lead.textContent=leadIn;if(status)status.textContent=area==='listening'?'Đang chuẩn bị nội dung nghe':'Đang chuyển câu đọc';
   $$('#mockQuestionGroups .mock-question-card').forEach(card=>card.classList.toggle('is-current',card.dataset.mockQuestionId===slot.questionId));
   $$('#mockQuestionGroups .mock-question-group').forEach(card=>card.classList.toggle('is-current-group',card.dataset.mockGroup===slot.unitId));
   $$('#mockQuestionMap [data-mock-jump]').forEach(button=>button.classList.toggle('is-current',button.dataset.mockJump===slot.questionId));
   document.getElementById(`mock-question-${slot.questionId}`)?.scrollIntoView({behavior:'smooth',block:'center'});
   if(flow.voiceEnabled){
     const previousGroupChanged=!previous||previous.unitId!==slot.unitId;
     if(area==='listening'&&group&&previousGroupChanged){
       const statusElement=document.getElementById(`mock-audio-status-${group.unitId}`);
       if(group.part==='Part 1'){
         // Part 1 owns its full title → lead-in → A/B/C/D script in the shared player.
         playListeningAudio(group.unitId,{statusElement});
       }else{
         speakText(leadIn,null,'',state.settings.tts?.defaultGender||'female',{onStart:()=>{if(status)status.textContent='Đang đọc câu dẫn';},onEnd:()=>{if(state.mockExam?.id===exam.id&&state.mockExam.currentSection==='listening')playListeningAudio(group.unitId,{statusElement,skipLeadIn:true});}});
       }
     }else{
       speakText(leadIn,null,'',state.settings.tts?.defaultGender||'female',{onStart:()=>{if(status)status.textContent='Đang đọc câu dẫn';},onEnd:()=>{if(status)status.textContent=area==='listening'?'Tiếp tục cùng audio hiện tại':'Đã chuyển đến câu hiện tại';}});
     }
   }
 }
 const remaining=getMockQuestionTimeRemaining(slot,timestamp),duration=Math.max(1,slot.allottedMs||1000),elapsed=Math.max(0,Math.min(duration,timestamp-slot.startAt));
 const countdown=$('#mockFlowCountdown'),progress=$('#mockFlowProgress'),status=$('#mockFlowStatus'),copy=$('#mockFlowQuestionLabel');
 if(countdown)countdown.textContent=mockFormatDuration(remaining);
 if(progress)progress.style.width=`${Math.min(100,Math.max(0,elapsed/duration*100))}%`;
 if(copy)copy.textContent=`${area==='listening'?'Listening':'Reading'} · ${slot.part} · Câu ${slot.questionNumber}`;
 if(status&&remaining>0)status.textContent=area==='listening'?'Thời gian cho câu/cụm nghe':'Thời gian cho câu/cụm đọc';
 $('#mockBottomProgress').textContent=`Câu ${slot.questionNumber} · ${slot.part} · ${Number.isInteger(exam.answers?.[slot.questionId])?'Đã chọn':'Chưa chọn'} · ${sectionQuestions.length} câu trong phần`;
}
function renderMockExam(){
  const exam=state.mockExam;if(!exam)return;ensureMockGuidedFlow(exam);
  $('#mockLanding').hidden=true;$('#mockResultStage').hidden=true;$('#mockExamStage').hidden=false;
  const area=exam.currentSection==='reading'?'reading':'listening';const section=exam.sections[area];
  const rows=getMockVisibleQuestions();const numberById=new Map(rows.map(row=>[row.question.id,row.number]));
  const answered=rows.filter(row=>Number.isInteger(exam.answers?.[row.question.id])).length;
  const flagged=(exam.flags||[]).filter(id=>rows.some(row=>row.question.id===id)).length;
  $('#mockExamModeLabel').textContent=`${exam.modeLabel.toUpperCase()} · ${rows.length} CÂU TRONG PHẦN NÀY`;
  $('#mockSectionEyebrow').textContent=area==='listening'?'SECTION I · LISTENING':'SECTION II · READING';
  $('#mockSectionTitle').textContent=area==='listening'?'Listening Comprehension':'Reading Comprehension';
  $('#mockSectionDescription').textContent=`${rows.length} câu hỏi · ${mockFormatDuration(section.seconds)} phút · ${section.groups.length} cụm bài`;
  $('#mockAnsweredCount').textContent=`${answered} / ${rows.length}`;$('#mockAnsweredBar').style.width=`${rows.length?answered/rows.length*100:0}%`;
  $('#mockMapCount').textContent=`${answered}/${rows.length} · ${flagged} đánh dấu`;
  $('#mockQuestionMap').innerHTML=rows.map(row=>`<button type="button" class="mock-map-button ${Number.isInteger(exam.answers?.[row.question.id])?'is-answered':''} ${(exam.flags||[]).includes(row.question.id)?'is-flagged':''}" data-mock-jump="${escapeHtml(row.question.id)}" aria-label="Đến câu ${row.number}">${row.number}</button>`).join('');
  $('#mockQuestionGroups').innerHTML=section.groups.map(group=>mockGroupMarkup(group,numberById)).join('');
  $('#mockFlowQuestionLabel').textContent='Đang chuẩn bị câu đầu tiên';$('#mockFlowLeadIn').textContent='Hệ thống tự chuyển đến câu tiếp theo theo thời gian đã phân bổ.';
  $('#mockBottomProgress').textContent=`Đang hiển thị ${rows.length} câu · ${answered} đã chọn`;
  $('#mockFinishSectionButton').hidden=true;$('#mockTestRules').innerHTML=area==='listening'?'<strong>Listening:</strong> hệ thống tự chuyển câu/cụm theo thời gian, đọc câu dẫn và phát nội dung nghe khi sang nhóm mới. Question Map chỉ dùng để quay lại câu cần kiểm tra; transcript và đáp án chỉ mở sau khi nộp bài. Hết giờ tự chuyển sang Reading.':'<strong>Reading:</strong> hệ thống tự phân bổ thời gian theo đoạn đọc và số câu, đọc câu dẫn mỗi khi chuyển vị trí. Có thể dùng Question Map để quay lại câu; hết giờ tự nộp bài.';
  updateMockTimer();
  if(state.mockTickTimer)clearInterval(state.mockTickTimer);
  state.mockTickTimer=setInterval(updateMockTimer,1000);
}
function updateMockTimer(){
  const exam=state.mockExam;if(!exam||exam.status!=='active'){if(state.mockTickTimer){clearInterval(state.mockTickTimer);state.mockTickTimer=null;}return;}
  const phase=getMockSectionForTime(exam,Date.now());
  if(phase==='expired'){finishMockExam(true);return;}
  if(phase!==exam.currentSection){exam.currentSection=phase;stopSpeech();saveMockStorage();toast('Đã hết giờ Listening. Hệ thống chuyển sang Reading.');renderMockExam();return;}
  const end=phase==='listening'?exam.listeningDeadlineAt:exam.totalDeadlineAt;
  const left=Math.max(0,Math.ceil((end-Date.now())/1000));
  $('#mockTimerLabel').textContent=phase==='listening'?'LISTENING REMAINING':'READING REMAINING';
  $('#mockTimerValue').textContent=mockFormatDuration(left);
  $('#mockTimerHint').textContent=phase==='listening'?'Tự chuyển sang Reading khi hết giờ':'Tự nộp bài khi hết 120/60/15 phút';
  $('#mockTimerValue').classList.toggle('is-urgent',left<=300);
  updateMockGuidedFlow(Date.now());
}
function setMockAnswer(questionId,choiceIndex){
  const exam=state.mockExam;if(!exam||exam.status!=='active')return;
  const livePhase=getMockSectionForTime(exam,Date.now());if(livePhase==='expired'||livePhase!==exam.currentSection){updateMockTimer();return;}
  const rows=getMockVisibleQuestions();if(!rows.some(row=>row.question.id===questionId))return;
  const row=rows.find(item=>item.question.id===questionId);if(!Number.isInteger(choiceIndex)||choiceIndex<0||choiceIndex>=row.question.choices.length)return;
  exam.answers[questionId]=choiceIndex;saveMockStorage();renderMockExam();
  document.getElementById(`mock-question-${questionId}`)?.scrollIntoView({block:'nearest',behavior:'smooth'});
}
function toggleMockFlag(questionId){const exam=state.mockExam;if(!exam||exam.status!=='active')return;const flags=new Set(exam.flags||[]);flags.has(questionId)?flags.delete(questionId):flags.add(questionId);exam.flags=[...flags];saveMockStorage();renderMockExam();}
function submitMockExam(){if(!state.mockExam||state.mockExam.status!=='active')return;const livePhase=getMockSectionForTime(state.mockExam,Date.now());if(livePhase==='expired'){finishMockExam(true);return;}if(livePhase!==state.mockExam.currentSection){updateMockTimer();return;}const score=scoreMockExam(state.mockExam);const left=score.total.questions-score.total.answered;if(!window.confirm(`Bạn đã trả lời ${score.total.answered}/${score.total.questions} câu. ${left?`${left} câu đang bỏ trống và sẽ tính là chưa đúng. `:''}Nộp bài và xem kết quả?`))return;finishMockExam(false);}
function finishMockExam(timedOut=false){
  const exam=state.mockExam;if(!exam||exam.status!=='active')return;
  stopSpeech();if(state.mockTickTimer){clearInterval(state.mockTickTimer);state.mockTickTimer=null;}
  exam.status='submitted-pending-review';exam.completedAt=Date.now();exam.timedOut=Boolean(timedOut);const score=scoreMockExam(exam);exam.score=score;
  const record=state.mockHistory.find(item=>item.attemptId===exam.id);
  if(record)Object.assign(record,{status:'submitted-pending-review',submittedAt:exam.completedAt,timedOut:Boolean(timedOut)});
  state.pendingMockResult={exam,score};state.mockExam=null;state.lastMockResult=null;saveMockStorage();showPendingMockResult();
}
function showPendingMockResult(){
 const pending=state.pendingMockResult;if(!pending)return;
 const {score,exam}=pending;
 showAssessmentResultModal({eyebrow:'MOCK EXAM · COMPLETED',title:'Bạn đã hoàn thành bài thi',correct:score.total.correct,incorrect:score.total.questions-score.total.correct,total:score.total.questions,description:`${exam.modeLabel||'Bài thi TOEIC'} · ${exam.timedOut?'Đã hết thời gian.':'Đã nộp bài.'} Kết quả tổng hợp đã sẵn sàng; transcript, đáp án và giải thích chỉ mở sau khi xác nhận.`});
}
function confirmMockExamResult(){
 const pending=state.pendingMockResult;if(!pending)return;
 const {exam,score}=pending,record=state.mockHistory.find(item=>item.attemptId===exam.id);
 if(record)Object.assign(record,{status:'completed',completedAt:exam.completedAt,correct:score.total.correct,questions:score.total.questions,accuracy:score.total.accuracy,listeningAccuracy:score.listening.accuracy,readingAccuracy:score.reading.accuracy});
 state.lastMockResult={exam,score};state.pendingMockResult=null;saveMockStorage();closeAssessmentResultModal();renderMockResult(exam,score);
}
function mockSectionScoreMarkup(label,data,detail){
  const title=label==='LISTENING'?'LISTENING · PART 1–4':'READING · PART 5–7';
  const status=data.accuracy>=85?'Nền tảng tốt':data.accuracy>=75?'Đã đạt mốc luyện tập':data.accuracy>=50?'Cần tăng độ chính xác':'Cần củng cố ưu tiên';
  const next=data.target75?`Cần thêm ${data.target75} câu đúng ở một bài cùng quy mô để chạm mốc 75%.`:'Bạn đã đạt mốc nội bộ 75%; bước tiếp theo là hướng tới 85%.';
  return `<article class="mock-score-card"><div class="mock-score-head"><div><small>SECTION SCORE</small><strong>${title}</strong></div><span>${status}</span></div><div class="mock-score-body"><div class="mock-score-dial" style="--score-value:${data.accuracy}%"><div><strong>${data.accuracy}%</strong><small>CHÍNH XÁC</small></div></div><div class="mock-score-details"><div class="mock-score-raw"><strong>${data.correct}</strong><span>/ ${data.questions} câu đúng</span></div><p>${detail}</p><div class="mock-score-target"><strong>MỤC TIÊU 75%</strong><span>${next}</span></div><div class="mock-score-next">${data.unanswered?`${data.unanswered} câu bỏ trống cũng cần được xử lý.`:'Hãy tiếp tục giữ tốc độ và độ chính xác ở phần này.'}</div></div></div></article>`;
}
function mockReviewGroupMarkup(group,numberById,exam){
  const listeningTranscript=group.area==='listening'&&(group.segments||[]).length?`<details class="mock-review-transcript"><summary>Transcript sau khi thi</summary><div>${group.segments.map(segment=>`<p><strong>${escapeHtml(segment.speaker||'Speaker')}:</strong> ${escapeHtml(segment.text||'')}</p>`).join('')}${group.translation?`<p class="mock-review-translation">${escapeHtml(group.translation)}</p>`:''}</div></details>`:'';
  const readingText=(group.documents||[]).length?group.documents.map(doc=>`<div class="reading-document-card"><strong>${escapeHtml(doc.label||'DOCUMENT')}</strong><pre>${escapeHtml(doc.content||'')}</pre></div>`).join(''):group.passage?`<pre>${escapeHtml(group.passage)}</pre>`:'';
  const readingContext=group.area==='reading'&&readingText?`<details class="mock-review-transcript"><summary>Xem lại đoạn đọc / tài liệu</summary><div>${readingText}</div></details>`:'';
  return `<div class="mock-review-part"><h3>${escapeHtml(group.part)} · ${escapeHtml(group.title)}</h3>${listeningTranscript}${readingContext}${group.questions.map(question=>{
    const selected=Number.isInteger(exam.answers?.[question.id])?exam.answers[question.id]:null;const correct=selected===question.answerIndex;const isP1=group.part==='Part 1';
    const answerText=isP1?`(${String.fromCharCode(65+question.answerIndex)}) ${group.segments?.[question.answerIndex]?.text||''}`:`(${String.fromCharCode(65+question.answerIndex)}) ${question.choices[question.answerIndex]||''}`;
    const selectedText=selected===null?'Chưa trả lời':isP1?String.fromCharCode(65+selected):`(${String.fromCharCode(65+selected)}) ${question.choices[selected]||''}`;
    return `<article class="mock-review-question"><h4>Câu ${numberById.get(question.id)||''} · ${correct?'Đúng':selected===null?'Bỏ trống':'Chưa đúng'}</h4><div class="mock-review-answer">Bạn chọn: <strong class="${correct?'':'is-wrong'}">${escapeHtml(selectedText)}</strong><br>Đáp án: <strong>${escapeHtml(answerText)}</strong></div><p>${escapeHtml(question.explanation||'Chưa có giải thích biên tập cho câu này.')}</p></article>`;
  }).join('')}</div>`;
}
function renderMockResult(exam,score){
  if(state.mockTickTimer){clearInterval(state.mockTickTimer);state.mockTickTimer=null;}
  $('#mockLanding').hidden=true;$('#mockExamStage').hidden=true;const stage=$('#mockResultStage');stage.hidden=false;
  const used=Math.max(0,Math.min(exam.totalMinutes*60,Math.round(((exam.completedAt||Date.now())-exam.startedAt)/1000)));
  const listeningAccuracy=score.listening.accuracy,readingAccuracy=score.reading.accuracy;
  const partRows=Object.entries(score.parts).sort((a,b)=>Number(a[0].replace('Part ',''))-Number(b[0].replace('Part ','')));
  const weakest=partRows.filter(([,item])=>item.accuracy<75).sort((a,b)=>a[1].accuracy-b[1].accuracy);
  const recs=weakest.length?weakest.slice(0,4).map(([part,item],index)=>`<div class="mock-recommendation"><strong>${index===0?'ƯU TIÊN CAO':'CẦN CỦNG CỐ'} · ${escapeHtml(part)} · ${item.accuracy}% (${item.correct}/${item.questions})</strong><p>${escapeHtml(MOCK_PART_TIPS[part])} Sau khi ôn, hãy làm lại một nhóm câu mới cùng Part và đặt mục tiêu tối thiểu 75%.</p></div>`).join(''):'<div class="mock-recommendation"><strong>Tiếp tục duy trì</strong><p>Độ chính xác ở cả các Part đã đạt từ 75% trở lên. Hãy luyện đề mới để kiểm tra khả năng duy trì kết quả với câu hỏi chưa gặp và nâng dần mục tiêu lên 85%.</p></div>';
  const lqs=getExamQuestions(exam.sections.listening),rqs=getExamQuestions(exam.sections.reading);const numberById=new Map([...lqs,...rqs].map((q,index)=>[q.id,index+1]));
  const review=[...exam.sections.listening.groups,...exam.sections.reading.groups].map(group=>mockReviewGroupMarkup(group,numberById,exam)).join('');
  const reused=Number(exam.reusedQuestionCount||0);
  stage.innerHTML=`<div class="mock-result-hero"><div><p class="eyebrow">${escapeHtml(exam.modeLabel.toUpperCase())} · KẾT QUẢ LUYỆN TẬP</p><h1>${score.total.accuracy>=75?'Bạn đã đạt mốc luyện tập 75%!': 'Đã hoàn thành bài thi'}</h1><p>${new Date(exam.completedAt).toLocaleString('vi-VN')} · Thời gian thực tế ${mockFormatDuration(used)} ${exam.timedOut?'· Tự động nộp khi hết giờ':''}</p></div><div class="mock-result-total"><strong>${score.total.correct}/${score.total.questions}</strong><span>TỔNG CÂU ĐÚNG · ${score.total.accuracy}%</span></div></div>
    <section class="mock-result-skills"><div class="mock-result-section-heading"><div><p class="eyebrow">YOUR TOEIC PRACTICE REPORT</p><h2>Kết quả theo hai kỹ năng</h2><p>Điểm số hiện tại theo số câu đúng và tỷ lệ chính xác của bài thi này.</p></div><span class="mock-result-target-chip">Mục tiêu nội bộ: ≥ 75%</span></div><div class="mock-result-score-grid">${mockSectionScoreMarkup('LISTENING',score.listening,`${score.listening.answered} đã trả lời · ${score.listening.unanswered} bỏ trống`)}${mockSectionScoreMarkup('READING',score.reading,`${score.reading.answered} đã trả lời · ${score.reading.unanswered} bỏ trống`)}</div></section>
    <div class="mock-result-note"><strong>${escapeHtml(mockResultBand(score.total.accuracy))}.</strong> Đây là điểm luyện tập theo số câu đúng, chưa phải điểm TOEIC quy đổi. ETS báo Listening và Reading riêng trên thang 5–495, nhưng quy đổi số câu đúng bằng phương pháp equating theo từng đề; ứng dụng chưa có dữ liệu hiệu chuẩn tương ứng nên không tự tạo điểm /495 hoặc /990. Ngân hàng hiện tại được ưu tiên câu chưa dùng gần đây; lần này có ${reused} câu từng xuất hiện trong lịch sử cục bộ.</div>
    <section class="panel"><div class="panel-header"><div><h3>Phân tích theo từng Part</h3><p class="muted">Mục tiêu luyện tập nội bộ: từ 75% đúng trở lên.</p></div></div><div class="mock-part-grid">${partRows.map(([part,item])=>`<div class="mock-part-result"><strong>${escapeHtml(part)}</strong><span>${item.correct}/${item.questions} đúng</span><b>${item.accuracy}%</b><div class="mock-part-track"><i style="width:${item.accuracy}%"></i></div></div>`).join('')}</div></section>
    <section class="panel"><div class="panel-header"><div><h3>Bạn nên cố gắng ở đâu?</h3><p class="muted">Ưu tiên những Part có tỷ lệ chính xác thấp nhất.</p></div></div><div class="mock-recommendation-list">${recs}</div></section>
    <div class="mock-result-actions"><button type="button" class="primary-button" data-mock-new="${escapeHtml(exam.modeId)}">Làm đề mới cùng chế độ</button><button type="button" class="secondary-button" data-mock-home>Về danh sách thi thử</button></div>
    <details class="mock-review-details"><summary>Xem lại toàn bộ ${score.total.questions} câu, đáp án và giải thích</summary><div class="mock-review-body">${review}</div></details>`;
}


const FLASH_TOPIC_META={ALL:{label:'Học tổng hợp',file:'office.webp',emoji:'🎯',desc:'Trộn từ nhiều chủ đề'},TIME:{label:'Thời gian',file:'time.webp',emoji:'⏰'},OFFICE:{label:'Văn phòng',file:'office.webp',emoji:'💼'},BUSINESS:{label:'Kinh doanh',file:'meeting.webp',emoji:'📈'},MEETING:{label:'Cuộc họp',file:'meeting.webp',emoji:'🤝'},TRAVEL:{label:'Du lịch',file:'travel.webp',emoji:'✈️'},TRANSPORT:{label:'Giao thông',file:'travel.webp',emoji:'🚆'},HR:{label:'Nhân sự',file:'office.webp',emoji:'🧑‍💼'},FINANCE:{label:'Tài chính',file:'finance.webp',emoji:'💳'},PURCHASING:{label:'Mua hàng',file:'shopping.svg',emoji:'🛒'},CUSTOMER:{label:'Khách hàng',file:'customer.webp',emoji:'💬'},SHIPPING:{label:'Vận chuyển',file:'shipping.webp',emoji:'📦'},TECHNOLOGY:{label:'Công nghệ',file:'technology.webp',emoji:'💻'},MARKETING:{label:'Tiếp thị',file:'meeting.webp',emoji:'📣'},FACILITY:{label:'Cơ sở vật chất',file:'construction.svg',emoji:'🏢'},QUALITY:{label:'Chất lượng',file:'technology.webp',emoji:'⭐'},DAILY:{label:'Thông dụng',file:'time.webp',emoji:'🌱'},LEGAL:{label:'Pháp lý',file:'legal.svg',emoji:'⚖️'},HEALTH:{label:'Sức khỏe & an toàn',file:'health.svg',emoji:'🦺'},ENVIRONMENT:{label:'Môi trường',file:'environment.svg',emoji:'🌿'},EDUCATION:{label:'Giáo dục',file:'education.svg',emoji:'🎓'},FOOD:{label:'Ẩm thực & nhà hàng',file:'food.svg',emoji:'🍽️'},HOTEL:{label:'Khách sạn',file:'hotel.svg',emoji:'🏨'},EVENT:{label:'Sự kiện',file:'event.svg',emoji:'🎤'},COMMUNICATION:{label:'Giao tiếp',file:'communication.svg',emoji:'💬'},CONSTRUCTION:{label:'Xây dựng',file:'construction.svg',emoji:'🏗️'},SHOPPING:{label:'Mua sắm',file:'shopping.svg',emoji:'🛍️'},BANKING:{label:'Ngân hàng',file:'banking.svg',emoji:'💳'},CAREER:{label:'Nghề nghiệp',file:'career.svg',emoji:'🚀'},WEATHER:{label:'Thời tiết',file:'weather.svg',emoji:'🌤️'},HEALTHCARE:{label:'Y tế',file:'healthcare.svg',emoji:'🩺'},AIRPORT:{label:'Sân bay',file:'airport.svg',emoji:'🛫'},REAL_ESTATE:{label:'Bất động sản',file:'real_estate.svg',emoji:'🏙️'}};
const FLASH_TOPIC_GROUPS=[
 {id:'SALES',label:'Bán hàng & doanh số',description:'Sales, doanh số, khách hàng và tiếp thị',file:'finance.webp',emoji:'💹',sources:['BUSINESS','MARKETING','CUSTOMER']},
 {id:'SUPPLY_CHAIN',label:'Chuỗi cung ứng',description:'Mua hàng, kho vận, giao nhận và vận tải',file:'shipping.webp',emoji:'🚚',sources:['SHIPPING','TRANSPORT','PURCHASING']},
 {id:'INSURANCE',label:'Bảo hiểm',description:'Hợp đồng, quyền lợi, rủi ro và thanh toán',file:'healthcare.svg',emoji:'🛡️',sources:['FINANCE','HEALTHCARE','HR','LEGAL']},
 {id:'MANUFACTURING',label:'Sản xuất',description:'Nhà máy, quy trình, chất lượng và thiết bị',file:'construction.svg',emoji:'🏭',sources:['QUALITY','FACILITY','BUSINESS','TECHNOLOGY']},
 {id:'COMPLAINTS',label:'Khiếu nại khách hàng',description:'Phản hồi, xử lý vấn đề và dịch vụ',file:'customer.webp',emoji:'🧾',sources:['CUSTOMER','COMMUNICATION','QUALITY']},
 {id:'PUBLIC_RELATIONS',label:'Quan hệ công chúng',description:'Truyền thông, sự kiện và hình ảnh thương hiệu',file:'event.svg',emoji:'📣',sources:['MARKETING','COMMUNICATION','EVENT']},
 {id:'RESEARCH',label:'Nghiên cứu & phát triển',description:'Nghiên cứu, thử nghiệm và cải tiến',file:'technology.webp',emoji:'🔬',sources:['TECHNOLOGY','EDUCATION','QUALITY']},
 {id:'ENERGY',label:'Năng lượng & tiện ích',description:'Điện, nước, năng lượng và vận hành cơ sở',file:'environment.svg',emoji:'⚡',sources:['ENVIRONMENT','FACILITY','TECHNOLOGY']},
 {id:'SAFETY',label:'An ninh & an toàn',description:'An toàn lao động, quy định và bảo vệ',file:'health.svg',emoji:'🦺',sources:['HEALTH','FACILITY','LEGAL']},
 {id:'PUBLIC_SERVICE',label:'Dịch vụ công',description:'Cơ quan, thủ tục, dịch vụ và thông báo',file:'legal.svg',emoji:'🏛️',sources:['LEGAL','COMMUNICATION','BUSINESS']},
 {id:'MEDIA',label:'Truyền thông & giải trí',description:'Nội dung, quảng bá, sự kiện và phương tiện',file:'event.svg',emoji:'🎬',sources:['MARKETING','COMMUNICATION','EVENT']},
 {id:'PROJECT',label:'Quản lý dự án',description:'Kế hoạch, tiến độ, cuộc họp và nguồn lực',file:'meeting.webp',emoji:'🗂️',sources:['BUSINESS','MEETING','TIME','FACILITY']}
];
function flashTopicMatches(word,topic){if(topic==='ALL')return true;const group=FLASH_TOPIC_GROUPS.find(x=>x.id===topic);return group?group.sources.some(id=>(word.topics||[]).includes(id)):(word.topics||[]).includes(topic);}
function flashRecord(id){return state.words.find(w=>w.id===id)||null;}
function flashStats(){const vals=Object.values(state.flashProgress);return {known:vals.filter(x=>(x.interval||0)>=3).length,due:vals.filter(x=>(x.dueAt||0)<=Date.now()&&(x.reps||0)>0).length,today:vals.filter(x=>x.lastSeen&&new Date(x.lastSeen).toDateString()===new Date().toDateString()).length};}
function renderFlashHome(){
 const stats=flashStats();$('#flashKnownCount').textContent=stats.known;$('#flashDueCount').textContent=stats.due;$('#flashStreakCount').textContent=stats.today;$('#flashcardMasteryLabel').textContent=`${stats.known} từ đã ghi nhớ`;
 const cats=[{id:'ALL',label:'Học tổng hợp',description:'Trộn từ theo mức độ ghi nhớ',file:'office.webp',emoji:'🎯'},...state.categories.map(c=>({id:c.id,label:c.label,description:c.description,file:FLASH_TOPIC_META[c.id]?.file||'office.webp',emoji:FLASH_TOPIC_META[c.id]?.emoji||'📚'})),...FLASH_TOPIC_GROUPS];
 const query=normalizeText($('#flashTopicSearch')?.value||'');
 $('#flashTopicGrid').innerHTML=cats.filter(c=>!query||normalizeText(`${c.label} ${c.description||''} ${c.id}`).includes(query)).map(c=>{const count=state.words.filter(w=>flashTopicMatches(w,c.id)).length;const meta=FLASH_TOPIC_META[c.id]||c;return `<button class="flash-topic-card" data-flash-topic="${escapeHtml(c.id)}" ${count<1?'disabled':''}><span class="flash-topic-image"><img loading="lazy" src="./assets/topics/${escapeHtml(meta.file||c.file||'office.webp')}" alt="Minh họa ${escapeHtml(c.label)}" decoding="async"></span><span class="flash-topic-copy"><strong><span class="flash-topic-title-icon" aria-hidden="true">${escapeHtml(meta.emoji||c.emoji||'📚')}</span>${escapeHtml(c.label)}</strong><small>${count} từ · ${escapeHtml(c.description||meta.desc||'')}</small></span><span class="flash-topic-arrow">→</span></button>`}).join('');
}
function flashShuffle(a){const x=[...a];for(let i=x.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[x[i],x[j]]=[x[j],x[i]];}return x;}
function flashPickBatch(topic,size,exclude=[]){const now=Date.now(),pool=state.words.filter(w=>flashTopicMatches(w,topic)&&!exclude.includes(w.id));const due=pool.filter(w=>(state.flashProgress[w.id]?.dueAt||0)<=now);const ranked=flashShuffle(pool).sort((a,b)=>{const pa=state.flashProgress[a.id]||{},pb=state.flashProgress[b.id]||{};const score=x=>{const p=state.flashProgress[x.id]||{};return (p.lapses||0)*4+(p.dueAt&&p.dueAt<=now?8:0)-(p.interval||0)*.25;};return score(b)-score(a);});const dueRank=flashShuffle(due);const combined=[...dueRank,...ranked.filter(w=>!dueRank.some(d=>d.id===w.id))];return flashShuffle(combined.slice(0,Math.min(size,pool.length)));}
function startFlashSession(topic='ALL',includeIds=[]){const reviewIds=includeIds.slice(0,10);const words=reviewIds.map(flashRecord).filter(Boolean);const selected=words.length?words:flashPickBatch(topic,10);if(!selected.length){toast('Chủ đề này chưa có từ vựng.','error');return;}state.flashSession={topic,size:selected.length,words:selected,index:0,flipped:false,reviewIds};$('#flashQuiz').hidden=true;$('#flashResult').hidden=true;$('#flashSession').hidden=false;const topicLabel=FLASH_TOPIC_META[topic]?.label||FLASH_TOPIC_GROUPS.find(x=>x.id===topic)?.label||'Học tổng hợp';$('#flashSessionTitle').textContent=`${topicLabel} · ${selected.length} từ`;$('#flashSessionEyebrow').textContent=reviewIds.length?'REVIEW · ÔN TỪ CHƯA NHỚ':'VOCABULARY QUEST';renderFlashCard();openLearningFocus({kind:'flashcards',title:topicLabel,subtitle:'Chạm vào thẻ để lật xem nghĩa; chạm lần nữa để chuyển sang từ tiếp theo.',eyebrow:'FLASHCARD · FOCUSED LEARNING',elements:['#flashSession','#flashQuiz','#flashResult']});}
function advanceFlashCard(){const ss=state.flashSession;if(!ss)return;if(!ss.flipped){ss.flipped=true;renderFlashCard();return;}ss.index++;ss.flipped=false;if(ss.index>=ss.words.length)finishFlashLearning();else renderFlashCard();}
function renderFlashCard(){
 const ss=state.flashSession;if(!ss)return;const w=ss.words[ss.index];if(!w)return;
 const sense=getPrimarySense(w),example=w.examples?.[0]||{},topic=w.topics?.[0]||'OFFICE',meta=FLASH_TOPIC_META[topic]||FLASH_TOPIC_META.ALL;
 const imagePath=typeof w.image==='string'&&w.image.startsWith('./assets/vocabulary/')&&!w.image.includes('..')&&/\.(webp|avif|jpe?g|png)$/i.test(w.image)&&w.imageAlt&&w.imageStatus==='approved'?w.image:'';
 const imageMarkup=imagePath?`<div class="flashcard-art"><img loading="lazy" decoding="async" src="${escapeHtml(imagePath)}" alt="${escapeHtml(w.imageAlt)}"></div>`:'';
 const additionalSensesMarkup=renderAdditionalFlashSenses(w,posDisplayLabel);
 $('#flashProgressText').textContent=`${ss.index+1} / ${ss.words.length}`;$('#flashProgressBar').style.width=`${(ss.index+1)/ss.words.length*100}%`;
 const detailsMarkup=ss.flipped?`<section class="flashcard-details-panel" aria-live="polite"><div class="flashcard-detail-heading"><span class="flash-kicker">MEANING & USAGE</span><span class="flash-detail-status">Mặt sau · ${ss.index+1}/${ss.words.length}</span></div><h3>${escapeHtml(sense.meaning_vi||'Chưa có nghĩa')}</h3><p class="flash-definition">${escapeHtml(sense.definition_en||'')}</p>${additionalSensesMarkup}<div class="flash-example"><small>IN CONTEXT</small><p>${escapeHtml(example.en||'Chưa có ví dụ.')}</p><span>${escapeHtml(example.vi||'')}</span></div>${(w.collocations||[]).length?`<div class="flash-detail-section"><small>COLLOCATIONS</small><div class="flash-collocations">${w.collocations.slice(0,4).map(x=>`<span>${escapeHtml(x)}</span>`).join('')}</div></div>`:''}<div class="flash-related-grid"><div><small>ĐỒNG NGHĨA</small><p>${(sense.synonyms||[]).slice(0,3).map(escapeHtml).join(' · ')||'Đang cập nhật'}</p></div><div><small>TRÁI NGHĨA</small><p>${(sense.antonyms||[]).slice(0,3).map(escapeHtml).join(' · ')||'Đang cập nhật'}</p></div></div>${w.verb_forms?`<div class="flash-verb-forms"><span>V1 <b>${escapeHtml(w.verb_forms.v1||w.word)}</b></span><span>V2 <b>${escapeHtml(w.verb_forms.v2||'—')}</b></span><span>V3 <b>${escapeHtml(w.verb_forms.v3||'—')}</b></span><span>V-ing <b>${escapeHtml(w.verb_forms.ving||'—')}</b></span></div>`:''}</section>`:'';
 $('#flashcardStage').innerHTML=`<article class="flashcard-stack ${imageMarkup?'has-approved-art':''} ${ss.flipped?'is-revealed':''}"><section class="flashcard-front-panel" data-flash-card tabindex="0" role="button" aria-label="${ss.flipped?'Chuyển sang từ tiếp theo':'Lật thẻ để xem nghĩa'}"><div class="flashcard-front-meta"><span class="flash-topic-pill">${escapeHtml(meta.label||topic)}</span><span class="flash-card-count">${ss.index+1}/${ss.words.length}</span></div><div class="flashcard-front-layout">${imageMarkup}<div class="flashcard-front-copy"><span class="flash-kicker">${ss.flipped?'WORD REVIEW':'GUESS THE WORD'}</span><h2>${escapeHtml(displayWord(w.word))}</h2><p class="flash-ipa">${escapeHtml(w.phonetic?.us||'Chưa có IPA')} · ${escapeHtml(getAllPos(w).join(' / ')||'Vocabulary')}</p><p class="flash-tap-hint">${ss.flipped?'Từ đã được lật · xem phần giải nghĩa bên dưới':'Hãy thử đoán nghĩa và cách dùng trước khi lật thẻ.'}</p></div></div></section>${detailsMarkup}<div class="flashcard-buttons"><button class="secondary-button" data-flash-speak="${escapeHtml(w.word)}">🔊 Nghe phát âm</button><button class="primary-button" data-flash-flip>${ss.flipped?'Từ tiếp theo':'Lật thẻ xem nghĩa'} ${ss.flipped?'→':'↻'}</button></div></article>`;
 $('#flashSessionActions').innerHTML=`<button class="text-button" data-flash-exit>Thoát lượt học</button><span class="muted">${ss.flipped?'Đọc ví dụ và nghe phát âm trước khi tiếp tục.':'Hãy thử đoán nghĩa trước khi lật thẻ.'}</span>`;
}

function finishFlashLearning(){const ss=state.flashSession;if(!ss)return;ss.words.forEach(w=>{const p=state.flashProgress[w.id]||{};p.lastSeen=Date.now();p.reps=(p.reps||0)+1;p.dueAt=Date.now()+Math.max(1,p.interval||1)*86400000;state.flashProgress[w.id]=p;});dbSet('flashProgress',state.flashProgress);ss.quiz=flashShuffle(ss.words);state.flashQuizIndex=0;state.flashQuizAnswers=[];$('#flashSession').hidden=true;$('#flashQuiz').hidden=false;renderFlashQuiz();$('#flashQuiz').scrollIntoView({behavior:'smooth',block:'start'});}
function renderFlashQuiz(){const ss=state.flashSession;if(!ss?.quiz)return;const i=state.flashQuizIndex;if(i>=ss.quiz.length){finishFlashQuiz();return;}const w=ss.quiz[i],correct=getPrimarySense(w).meaning_vi||'';const pool=flashShuffle(state.words.filter(x=>x.id!==w.id).map(x=>getPrimarySense(x).meaning_vi).filter(x=>x&&x!==correct));const choices=flashShuffle([correct,...[...new Set(pool)].slice(0,3)]);$('#flashQuizProgress').textContent=`${i+1} / ${ss.quiz.length}`;$('#flashQuizStage').innerHTML=`<div class="flash-quiz-question"><span class="flash-kicker">QUESTION ${i+1}</span><h2>${escapeHtml(displayWord(w.word))}</h2><p>${escapeHtml(w.phonetic?.us||'')} · Chọn nghĩa chính xác nhất</p><div class="flash-quiz-choices">${choices.map((c,j)=>`<button class="flash-quiz-choice" data-flash-answer="${encodeURIComponent(c)}"><b>${String.fromCharCode(65+j)}</b>${escapeHtml(c)}</button>`).join('')}</div></div>`;$('#flashQuizActions').innerHTML='<span class="muted">Chọn một đáp án để tiếp tục.</span>';
}
async function answerFlashQuiz(encoded){
 const ss=state.flashSession,w=ss?.quiz?.[state.flashQuizIndex];if(!w)return;
 const answer=decodeURIComponent(encoded),correct=getPrimarySense(w).meaning_vi||'',ok=normalizeText(answer)===normalizeText(correct);
 if(state.flashQuizAnswers.some(entry=>entry.id===w.id))return;
 state.flashQuizAnswers.push({id:w.id,choice:answer,correct:ok,answeredAt:Date.now()});
 const buttons=$$('#flashQuizStage [data-flash-answer]');buttons.forEach(button=>{button.disabled=true;if(decodeURIComponent(button.dataset.flashAnswer)===answer)button.classList.add('is-selected');});
 if(state.flashQuizIndex<ss.quiz.length-1){
   $('#flashQuizActions').innerHTML='<p class="assessment-draft-note">Đã ghi nhận lựa chọn. Đáp án sẽ được chấm sau khi hoàn thành toàn bộ lượt.</p><button type="button" class="primary-button" data-flash-quiz-next>Câu tiếp theo →</button>';
 }else{
   await finishFlashQuiz();
 }
}

async function finishFlashQuiz(){
 const ss=state.flashSession;if(!ss||state.flashQuizAnswers.length!==ss.quiz.length||state.pendingFlashQuizResult)return;
 const answers=state.flashQuizAnswers.map(item=>({...item}));
 const correct=answers.filter(item=>item.correct).length;
 state.pendingFlashQuizResult={answers,total:ss.quiz.length,completedAt:Date.now()};
 showAssessmentResultModal({eyebrow:'FLASH QUIZ · SESSION COMPLETE',title:'Bạn đã hoàn thành lượt kiểm tra',correct,incorrect:answers.length-correct,total:answers.length,description:'Toàn bộ lựa chọn đã được ghi nhận. Xác nhận để cập nhật lịch ôn và xem đáp án từng câu.'});
}
async function confirmFlashQuizResult(){
 const pending=state.pendingFlashQuizResult,ss=state.flashSession;if(!pending||!ss)return;
 for(const answer of pending.answers){const p=state.flashProgress[answer.id]||{};if(answer.correct){p.correct=(p.correct||0)+1;p.interval=Math.min(30,Math.max(1,(p.interval||0)*2||2));p.lapses=Math.max(0,(p.lapses||0)-1);}else{p.lapses=(p.lapses||0)+1;p.interval=0;p.dueAt=Date.now()+60000;}p.lastQuiz=answer.answeredAt||Date.now();state.flashProgress[answer.id]=p;}
 await dbSet('flashProgress',state.flashProgress);
 const good=pending.answers.filter(x=>x.correct),wrong=pending.answers.filter(x=>!x.correct),pct=Math.round(good.length/ss.quiz.length*100),wrongIds=wrong.map(x=>x.id);
 const nextSize=10;
 ss.pendingWrongIds=wrongIds;ss.recommendedNextSize=nextSize;state.pendingFlashQuizResult=null;closeAssessmentResultModal();
 $('#flashQuiz').hidden=true;$('#flashResult').hidden=false;setLearningFocusHeader('Hoàn thành lượt học','Xem kết quả và đối chiếu từng câu trước khi chọn lượt tiếp theo.','FLASHCARD · SESSION REVIEW');
 const nextLabel=`Học tiếp ${nextSize} từ mới`;
 const reviewCount=Math.min(10,wrong.length),reviewLabel=wrong.length?`Ôn ${reviewCount} từ sai + từ mới (tối đa 10 từ)`:'';
 const reviewRows=pending.answers.map((answer,index)=>{const word=ss.quiz.find(item=>item.id===answer.id);const correctMeaning=getPrimarySense(word||{}).meaning_vi||'Chưa có nghĩa';return `<article class="flash-quiz-review-row ${answer.correct?'is-correct':'is-wrong'}"><div><strong>${index+1}. ${escapeHtml(displayWord(word?.word||answer.id))}</strong><span>${answer.correct?'Đúng':'Chưa đúng'}</span></div><p>Bạn chọn: ${escapeHtml(answer.choice)}</p><p>Đáp án: ${escapeHtml(correctMeaning)}</p></article>`;}).join('');
 $('#flashResult').innerHTML=`<div class="flash-result-emoji">${pct>=80?'🏆':pct>=60?'✨':'💪'}</div><span class="flash-kicker">SESSION COMPLETE</span><h2>${pct>=80?'Quá tốt! Bạn đang tiến bộ.':pct>=60?'Làm tốt! Hãy củng cố thêm.':'Đừng lo, sai là một phần của việc ghi nhớ.'}</h2><div class="flash-score"><strong>${good.length}/${ss.quiz.length}</strong><span>${pct}% chính xác · ${wrong.length} câu cần củng cố</span></div><div class="flash-result-bar"><span style="width:${pct}%"></span></div><section class="flash-quiz-review"><h3>Đối chiếu câu trả lời</h3>${reviewRows}</section><p>${wrong.length?`Có ${wrong.length} từ cần ôn lại. Những từ này sẽ được ưu tiên ở lượt tiếp theo.`:'Bạn đã hoàn thành lượt này rất tốt. Lượt tiếp theo sẽ mở thêm từ mới.'}</p><div class="flash-result-actions">${wrong.length?`<button class="primary-button" data-flash-review-wrong>${reviewLabel}</button>`:`<button class="primary-button" data-flash-next-batch>${nextLabel}</button>`}<button class="secondary-button" data-flash-next-batch>${wrong.length?'Chỉ học từ mới':nextLabel}</button><button class="text-button" data-flash-home>Về chọn chủ đề</button></div>`;
 renderFlashHome();
}

async function handleAssessmentResultSurfaceAction(e){
  const confirmAssessment=e.target.closest?.('[data-assessment-confirm]');
  if(confirmAssessment){await confirmPendingAssessmentResult({openReviewForSingle:true});return true;}
  return false;
}

function bindEvents(){
  bindPracticeEvents();
  $('#quickHelpLauncher')?.addEventListener('click',toggleQuickHelp);
  $('#quickHelpClose')?.addEventListener('click',()=>setQuickHelpOpen(false));
  $('#robotChatForm')?.addEventListener('submit',handleRobotInput);
  $('#robotMuteToggle')?.addEventListener('click',toggleRobotMute);
  $('#robotInsightsToggle')?.addEventListener('click',toggleRobotInsights);
  $('#robotIdleNeedHelp')?.addEventListener('click',()=>{hideRobotIdleNudge();setQuickHelpOpen(true);});
  $('#robotIdleDismiss')?.addEventListener('click',()=>{hideRobotIdleNudge();robotIdleSnoozeUntil=Date.now()+600000;scheduleRobotIdle(600000);});
  $('#quickHelp')?.addEventListener('click',event=>{
    const choice=event.target.closest('[data-robot-choice]');
    if(choice){handleRobotChoice(choice.dataset.robotChoice);return;}
    const prompt=event.target.closest('[data-robot-prompt]');
    if(prompt){sendRobotMessage(prompt.dataset.robotPrompt);return;}
    const command=event.target.closest('[data-robot-command],[data-robot-page]');
    if(command){handleRobotCommand(command.dataset.robotCommand||'',command.dataset.robotPage||'');return;}
  });

  document.addEventListener('visibilitychange',()=>{if(!document.hidden)renderRecallQueue();});
  window.addEventListener('focus',renderRecallQueue);
  document.addEventListener('error',event=>{
    const image=event.target;
    if(image instanceof HTMLImageElement&&image.matches('.flash-topic-image img,.flashcard-art img')){
      image.hidden=true;
      image.parentElement?.classList.add('image-missing');
    }
  },true);
  $$('[data-page]').forEach(b=>b.addEventListener('click',()=>navigate(b.dataset.page)));
  $$('[data-menu-toggle]').forEach(b=>b.addEventListener('click',()=>openMobileGroupMenu(b.dataset.menuToggle)));
  $('#mobileGroupMenu')?.addEventListener('click',e=>{if(e.target.closest('[data-group-close]'))$('#mobileGroupMenu').hidden=true;const item=e.target.closest('[data-group-page]');if(item){$('#mobileGroupMenu').hidden=true;navigate(item.dataset.groupPage);}});
  $$('[data-go]').forEach(b=>b.addEventListener('click',()=>navigate(b.dataset.go)));
  $('#learningRecallQueue')?.addEventListener('click',e=>{const button=e.target.closest('[data-recall-open]');if(button)openRecallItem(button.dataset.recallOpen,button.dataset.recallItem);});
  $('#toeicProgressPanel')?.addEventListener('click',e=>{const btn=e.target.closest('[data-toeic-part]');if(!btn)return;const area=btn.dataset.toeicArea,part=btn.dataset.toeicPart;navigate(area);const filter=area==='listening'?$('#listeningPartFilter'):$('#readingPartFilter');if(filter){filter.value=part;if(area==='listening')renderListeningLibrary();else renderReadingLibrary();}});
  $('#dashboardAlphabet').addEventListener('click',e=>{const b=e.target.closest('[data-letter]');if(b)goToLetter(b.dataset.letter);});
  $('#alphabetFilter').addEventListener('click',e=>{const b=e.target.closest('[data-letter]');if(b){state.activeLetter=b.dataset.letter;renderDictionary();}});
  $('#topicShowcase')?.addEventListener('click',e=>{const b=e.target.closest('[data-topic]');if(!b)return;$('#topicFilter').value=b.dataset.topic;$$('[data-topic]', $('#topicShowcase')).forEach(x=>x.classList.toggle('active',x===b));state.activeLetter='';renderDictionary();});
  ['dictionarySearch','topicFilter','posFilter','cefrFilter','dictionarySourceFilter'].forEach(id=>$('#'+id).addEventListener('input',()=>{if(id==='topicFilter')$$('[data-topic]', $('#topicShowcase')).forEach(x=>x.classList.toggle('active',x.dataset.topic===$('#topicFilter').value));renderDictionary();}));
  $('#dictionarySourceFilter').addEventListener('change',renderDictionary);
  $('#resetFilters').addEventListener('click',()=>{state.activeLetter='';$('#dictionarySearch').value='';$('#topicFilter').value='';$('#posFilter').value='';$('#cefrFilter').value='';$('#dictionarySourceFilter').value='all';$$('[data-topic]', $('#topicShowcase')).forEach(x=>x.classList.toggle('active',x.dataset.topic===''));renderDictionary();});
  $('#wordTableBody').addEventListener('click',e=>{const b=e.target.closest('[data-detail]');if(b)showDetail(b.dataset.detail);});
  $('#wordCardList').addEventListener('click',e=>{const b=e.target.closest('[data-detail]');if(b)showDetail(b.dataset.detail);});
  $('#dataTableBody').addEventListener('click',e=>{const detail=e.target.closest('[data-detail]');if(detail){showDetail(detail.dataset.detail);return;}const edit=e.target.closest('[data-edit]'),del=e.target.closest('[data-delete]');if(edit){openEditor(edit.dataset.edit);return;}if(del)deleteWord(del.dataset.delete);});
  $('#dataSearch').addEventListener('input',renderDataTable);
  $('#grammarSearch').addEventListener('input',renderGrammarLibrary); $('#grammarCategoryFilter').addEventListener('change',renderGrammarLibrary); $('#grammarLevelFilter').addEventListener('change',renderGrammarLibrary); $('#grammarPartFilter')?.addEventListener('change',renderGrammarLibrary);
  $('#readingSearch').addEventListener('input',renderReadingLibrary); $('#readingPartFilter')?.addEventListener('change',renderReadingLibrary); $('#readingTopicFilter').addEventListener('change',renderReadingLibrary); $('#readingLevelFilter').addEventListener('change',renderReadingLibrary);
  $('#listeningSearch').addEventListener('input',renderListeningLibrary); $('#listeningPartFilter').addEventListener('change',renderListeningLibrary); $('#listeningLevelFilter').addEventListener('change',renderListeningLibrary);
  $('#page-mock')?.addEventListener('click',e=>{
    const start=e.target.closest('[data-mock-start]');if(start){startMockExam(start.dataset.mockStart);return;}
    const answer=e.target.closest('[data-mock-answer]');if(answer){setMockAnswer(answer.dataset.mockAnswer,Number(answer.dataset.choiceIndex));return;}
    const flag=e.target.closest('[data-mock-flag]');if(flag){toggleMockFlag(flag.dataset.mockFlag);return;}
    const audio=e.target.closest('[data-mock-audio]');if(audio){playListeningAudio(audio.dataset.mockAudio,{statusElement:document.getElementById(`mock-audio-status-${audio.dataset.mockAudio}`)});return;}
    const jump=e.target.closest('[data-mock-jump]');if(jump){document.getElementById(`mock-question-${jump.dataset.mockJump}`)?.scrollIntoView({behavior:'smooth',block:'center'});$$('#mockQuestionMap [data-mock-jump]').forEach(button=>button.classList.toggle('is-current',button===jump));return;}
    if(e.target.closest('#mockResumeButton')){resumeMockExam();return;}
    if(e.target.closest('#mockDiscardButton')){discardMockExam();return;}
    if(e.target.closest('#mockSubmitButton')){submitMockExam();return;}
    if(e.target.closest('#mockClearFlagsButton')){if(state.mockExam){state.mockExam.flags=[];saveMockStorage();renderMockExam();}return;}
    const newExam=e.target.closest('[data-mock-new]');if(newExam){state.lastMockResult=null;renderMockHome();startMockExam(newExam.dataset.mockNew);return;}
    if(e.target.closest('[data-mock-home]')){state.lastMockResult=null;saveMockStorage();renderMockHome();return;}
  });
  document.addEventListener('error',event=>{
    const image=event.target;if(!(image instanceof HTMLImageElement))return;
    if(image.matches('.mock-part1-image')&&!image.dataset.fallbackApplied){const fallback=image.dataset.fallbackSrc;if(fallback&&image.src!==new URL(fallback,document.baseURI).href){image.dataset.fallbackApplied='1';image.src=fallback;return;}image.closest('.mock-part1-frame')?.classList.add('image-missing');}
  },true);
  $('#flashTopicGrid')?.addEventListener('click',e=>{const b=e.target.closest('[data-flash-topic]');if(b)startFlashSession(b.dataset.flashTopic);});
  $('#flashTopicSearch')?.addEventListener('input',renderFlashHome);
  $('#flashcardStage')?.addEventListener('click',e=>{const speak=e.target.closest('[data-flash-speak]');if(speak){e.stopPropagation();speakText(speak.dataset.flashSpeak,null,'',state.settings.tts?.defaultGender||'female');return;}if(e.target.closest('[data-flash-flip]')||e.target.closest('[data-flash-card]'))advanceFlashCard();});
  $('#flashcardStage')?.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target.matches('[data-flash-card]')){e.preventDefault();advanceFlashCard();}});
  $('#flashSessionActions')?.addEventListener('click',e=>{if(e.target.closest('[data-flash-exit]'))closeLearningFocus();});
  $('#flashQuizStage')?.addEventListener('click',e=>{const b=e.target.closest('[data-flash-answer]');if(b)answerFlashQuiz(b.dataset.flashAnswer);});
  $('#flashQuizActions')?.addEventListener('click',e=>{const b=e.target.closest('[data-flash-quiz-speak]');if(b)speakText(b.dataset.flashQuizSpeak,null,'',state.settings.tts?.defaultGender||'female');});
  $('#flashQuizActions')?.addEventListener('click',e=>{if(e.target.closest('[data-flash-quiz-next]')){state.flashQuizIndex++;renderFlashQuiz();}});
  $('#flashResult')?.addEventListener('click',e=>{if(e.target.closest('[data-flash-next-batch]'))startFlashSession(state.flashSession?.topic||'ALL');if(e.target.closest('[data-flash-review-wrong]')){const topic=state.flashSession?.topic||'ALL';const allWrong=state.flashSession?.pendingWrongIds||state.flashQuizAnswers.filter(x=>!x.correct).map(x=>x.id);const ids=allWrong.slice(0,10);const fresh=flashPickBatch(topic,Math.max(0,10-ids.length),ids).map(x=>x.id);startFlashSession(topic,[...ids,...fresh]);}if(e.target.closest('[data-flash-home]'))closeLearningFocus();});
  $('#grammarCardList').addEventListener('click',e=>{const b=e.target.closest('[data-grammar-open]');if(b)openGrammarLesson(b.dataset.grammarOpen);});
  $('#readingCardList').addEventListener('click',e=>{const b=e.target.closest('[data-reading-open]');if(b)openReadingDetail(b.dataset.readingOpen);});
  $('#listeningCardList').addEventListener('click',e=>{const b=e.target.closest('[data-listening-open]');if(b)openListeningDetail(b.dataset.listeningOpen);});
  $('#dataLetterFilter').addEventListener('change',renderDataTable); $('#dataTopicFilter').addEventListener('change',renderDataTable); $('#dataPosFilter').addEventListener('change',renderDataTable); $('#dataSourceFilter').addEventListener('change',renderDataTable);
  $('#resetDataFilters').addEventListener('click',()=>{$('#dataSearch').value='';$('#dataLetterFilter').value='';$('#dataTopicFilter').value='';$('#dataPosFilter').value='';$('#dataSourceFilter').value='all';renderDataTable();});
  $('#addWordButton').addEventListener('click',()=>openEditor());
  $('#importButton').addEventListener('click',()=>$('#importFile').click());
  $('#importFile').addEventListener('change',async e=>{const file=e.target.files?.[0];if(!file)return;try{await importFile(file);}catch(err){toast(`Import thất bại: ${err.message}`,'error');}finally{e.target.value='';}});
  $('#exportJsonButton').addEventListener('click',exportJSON);$('#exportCsvButton').addEventListener('click',exportCSV);$('#resetLocalButton').addEventListener('click',resetWorkspace);
  $('#exportLearnerBackupButton')?.addEventListener('click',exportLearnerBackup);$('#restoreLearnerBackupButton')?.addEventListener('click',()=>$('#learnerBackupFile')?.click());$('#learnerBackupFile')?.addEventListener('change',async e=>{const file=e.target.files?.[0];if(!file)return;try{await restoreLearnerBackupFile(file);}catch(error){toast(`Khôi phục thất bại: ${error.message}`,'error');}finally{e.target.value='';}});
  $('#closeModal').addEventListener('click',closeModal);
  $('#learningFocusClose')?.addEventListener('click',closeLearningFocus);
  $('#learningFocusContent')?.addEventListener('click',handleAssessmentResultSurfaceAction);
  $('#foundationLessonList')?.addEventListener('click',e=>{const b=e.target.closest('[data-foundation-open]');if(b)openFoundationLesson(b.dataset.foundationOpen);});
  $('#startPlacementDiagnostic')?.addEventListener('click',startPlacementDiagnostic);
  document.addEventListener('click',e=>{const answer=e.target.closest('[data-placement-answer]');if(answer){answerPlacementQuestion(answer);return;}if(e.target.closest('[data-placement-next]')){if(state.placementState){state.placementState.index++;renderPlacementQuestion();}return;}const apply=e.target.closest('[data-placement-apply]');if(apply){applyPlacementLevel(apply.dataset.placementApply);return;}if(e.target.closest('[data-placement-retry]')){startPlacementDiagnostic();}});
  $('#foundationStartLevel')?.addEventListener('change',e=>{const level=e.target.value;state.foundationStartLevel=['ALL','PRE-A1','A1','A2','B1','B2','C1'].includes(level)?level:'ALL';try{localStorage.setItem('toeic:learning-start-level:v1',state.foundationStartLevel);}catch{}renderFoundationPath();});
  $('#learningFocusBackdrop')?.addEventListener('click',e=>{if(e.target.id==='learningFocusBackdrop')return;});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&learningFocusState.active&&$('#modalLayer')?.hidden!==false)closeLearningFocus();});$('#modalLayer')?.addEventListener('click',e=>{if(e.target.id==='modalLayer'&&(state.practiceReviewPending||state.autoAdvanceWaiting||state.pendingPracticeBatch||state.pendingFoundationAssessment||state.pendingSinglePractice||state.pendingFlashQuizResult||state.pendingPlacementResult||state.pendingMockResult))return;if(e.target.id==='modalLayer')closeModal();});
  $('#closeGoogleSearch').addEventListener('click',closeGoogleSearchPanel);
  $('#googleSearchBackdrop').addEventListener('click',e=>{if(e.target.id==='googleSearchBackdrop')closeGoogleSearchPanel();});
  $('#runGoogleAIButton').addEventListener('click',openGoogleSearch);
  $('#modalContent').addEventListener('click',e=>{if(e.target.closest('[data-foundation-production-export]'))exportFoundationProductionPortfolio();});
  $('#modalContent').addEventListener('click',async e=>{if(await handleAssessmentResultSurfaceAction(e))return;const practiceBatchResult=e.target.closest('[data-practice-batch-result]');if(practiceBatchResult){maybeShowPracticeBatchResult(practiceBatchResult.dataset.practiceBatchResult,practiceBatchResult.dataset.resourceId);return;}const foundationBatchResult=e.target.closest('[data-foundation-batch-result]');if(foundationBatchResult){const kind=foundationBatchResult.dataset.foundationBatchResult,lessonId=foundationBatchResult.dataset.lessonId,scopeId=foundationBatchResult.dataset.foundationScope||'';const questions=kind==='foundation-recognition'?(state.foundationLessons.find(x=>x.id===lessonId)?.questionBank||[]):kind==='foundation-application'?[{...state.foundationLessons.find(x=>x.id===lessonId)?.applicationTask,id:state.foundationLessons.find(x=>x.id===lessonId)?.applicationTask?.id}]:kind==='foundation-reading'?(scopeId==='reading2'?state.foundationReadingExtendedPassages:state.foundationReadingPassages).find(x=>x.lessonId===lessonId)?.questions||[]:(state.foundationListeningClips.find(x=>x.lessonId===lessonId&&(scopeId==='listening2'?x.evidenceScope==='listening2':!x.supplementary))?.questions||[]);showFoundationAssessmentResult(kind,lessonId,questions,scopeId);return;}const alphabetPlay=e.target.closest('[data-alphabet-play]');if(alphabetPlay){playAlphabetSound(alphabetPlay);return;}const foundationListening=e.target.closest('[data-foundation-listening-answer]');if(foundationListening){answerFoundationListening(foundationListening);return;}const foundationListenPlay=e.target.closest('[data-foundation-listening-play]');if(foundationListenPlay){playFoundationListening(foundationListenPlay.dataset.foundationListeningPlay);return;}const foundationListenStop=e.target.closest('[data-foundation-listening-stop]');if(foundationListenStop){stopSpeech();return;}const foundationTranscriptToggle=e.target.closest('[data-foundation-listening-transcript-toggle]');if(foundationTranscriptToggle){const transcript=foundationTranscriptToggle.closest('[data-foundation-listening]')?.querySelector('[data-foundation-listening-transcript]');if(transcript){transcript.hidden=!transcript.hidden;foundationTranscriptToggle.textContent=transcript.hidden?'Hiện transcript':'Ẩn transcript';}return;}const foundationReading=e.target.closest('[data-foundation-reading-answer]');if(foundationReading){answerFoundationReading(foundationReading);return;}const foundationApplication=e.target.closest('[data-foundation-application-answer]');if(foundationApplication){answerFoundationApplication(foundationApplication);return;}const foundationRecall=e.target.closest('[data-foundation-recall-answer]');if(foundationRecall){answerFoundationRecall(foundationRecall);return;}const foundationProduction=e.target.closest('[data-foundation-production-save]');if(foundationProduction){saveFoundationProduction(foundationProduction);return;}const foundationProductionRevision=e.target.closest('[data-foundation-production-revision-save]');if(foundationProductionRevision){saveFoundationProductionRevision(foundationProductionRevision);return;}const foundationAnswer=e.target.closest('[data-foundation-answer]');if(foundationAnswer){answerFoundationQuestion(foundationAnswer);return;}const edit=e.target.closest('[data-edit]');const ai=e.target.closest('[data-ai-word]');const grammarAI=e.target.closest('[data-ai-lesson]');const readingAI=e.target.closest('[data-ai-reading]');const listeningAI=e.target.closest('[data-ai-listening]');const reviewAI=e.target.closest('[data-practice-review-ai]');const grammarChoice=e.target.closest('[data-grammar-choice]');const readingChoice=e.target.closest('[data-reading-choice]');const readingSpeak=e.target.closest('[data-reading-speak]');const lookup=e.target.closest('[data-lookup-term]');const listeningChoice=e.target.closest('[data-listening-choice]');const speak=e.target.closest('[data-speak-word]');const stop=e.target.closest('[data-stop-speech]');const play=e.target.closest('[data-listening-play]');const stopListening=e.target.closest('[data-listening-stop]');const vocabPlay=e.target.closest('[data-listening-vocab-play]');const reviewOk=e.target.closest('[data-practice-review-ok]');const saveRubric=e.target.closest('[data-save-explanation-rubric]');const retry=e.target.closest('[data-practice-retry]');const retryAll=e.target.closest('[data-practice-retry-all]');const waitCancel=e.target.closest('[data-auto-advance-cancel]');if(retry){retryPracticeQuestion(retry);return;}if(retryAll){retryAllPracticeQuestions(retryAll);return;}if(waitCancel){cancelAutoAdvanceWait();return;}if(reviewOk){acknowledgePracticeReview();return;}if(saveRubric){const keys=['clue','fit','distractor'];const ratings=keys.map(key=>{const selected=$(`#modalContent [data-explanation-rubric="${key}"]:checked`);return selected?selected.value==='yes':null;});if(ratings.some(value=>value===null)){toast('Hãy tự đánh giá đủ cả 3 tiêu chí trước khi lưu.','error');return;}const q=state.currentQuestion;const objectiveIds=state.objectiveResourceIndex?.[q?.id]||[];state.objectiveProgress=recordExplanationRubric(state.objectiveProgress,objectiveIds,q?.id,ratings,Date.now());await saveObjectivePractice();const score=ratings.filter(Boolean).length;const status=$('#modalContent [data-explanation-rubric-status]');if(status)status.textContent=`Đã lưu tự đánh giá ${score}/3. Đây là tự báo cáo, không phải điểm mastery.`;saveRubric.disabled=true;saveRubric.textContent=`Đã lưu · ${score}/3`;return;}if(reviewAI){showAIPromptModal(buildPracticeAIPrompt(),'Phân tích câu trả lời ôn tập hiện tại');return;}if(edit)openEditor(edit.dataset.edit);if(ai){const w=state.words.find(x=>x.id===ai.dataset.aiWord);if(w)showAIPromptModal(buildWordAIPrompt(w),`Giải thích từ ${displayWord(w.word)} theo ngữ cảnh TOEIC`);}if(grammarChoice)answerGrammarExercise(grammarChoice);if(readingChoice)answerReadingQuestion(readingChoice);if(readingSpeak){playReadingText(readingSpeak.dataset.readingSpeak);return;}if(lookup)openLookupTerm(lookup.dataset.lookupTerm);if(grammarAI){const lesson=state.grammarLessons.find(x=>x.id===grammarAI.dataset.aiLesson);if(lesson)showAIPromptModal(buildGrammarAIPrompt(lesson),`Phân tích ngữ pháp ${lesson.title}`);}if(readingAI){const reading=state.readings.find(x=>x.id===readingAI.dataset.aiReading);if(reading)showAIPromptModal(buildReadingAIPrompt(reading),`Phân tích bài đọc TOEIC ${reading.title}`);}if(listeningChoice)answerListeningQuestion(listeningChoice);if(listeningAI){const item=state.listening.find(x=>x.id===listeningAI.dataset.aiListening);if(item)showAIPromptModal(buildListeningAIPrompt(item),`Phân tích bài nghe TOEIC ${item.title}`);}if(speak)speakText(speak.dataset.speakWord,speak.dataset.accent||null,'',state.settings.tts?.defaultGender||'female');if(stop)stopSpeech();if(play)playListeningAudio(play.dataset.listeningPlay);if(vocabPlay)playListeningVocabulary(vocabPlay.dataset.listeningVocabPlay);if(stopListening)stopSpeech();});
  $('#globalSearch').addEventListener('keydown',e=>{if(e.key==='Enter'){navigate('dictionary');$('#dictionarySearch').value=e.target.value;renderDictionary();}});
  $('#modalContent').addEventListener('input',e=>{const field=e.target.closest('[data-foundation-production-text],[data-foundation-revision-text]');if(!field)return;const panel=field.closest('[data-foundation-production]'),revision=field.hasAttribute('data-foundation-revision-text'),counter=panel?.querySelector(revision?'[data-foundation-revision-count]':'[data-foundation-production-count]');if(!counter)return;const count=field.value.trim().split(/\s+/).filter(Boolean).length,minimum=Number(panel.dataset.minimumWords)||3;counter.textContent=`${count}/${minimum} từ tối thiểu${count>=minimum?' · Đủ độ dài':''}`;counter.classList.toggle('is-ready',count>=minimum);});
  $('#globalSearch').addEventListener('input',e=>{if(e.target.value.length>=2){navigate('dictionary');$('#dictionarySearch').value=e.target.value;renderDictionary();}});
  document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();$('#globalSearch').focus();}if(e.key==='Escape'){if($('#googleSearchBackdrop')&&!$('#googleSearchBackdrop').hidden)closeGoogleSearchPanel();else if($('#modalLayer')&&!$('#modalLayer').hidden){e.preventDefault();closeModal();}else if($('#quickHelpPanel')&&!$('#quickHelpPanel').hidden)setQuickHelpOpen(false);else if($('#installInviteBackdrop').hidden)closeModal();}});
  window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();state.deferredInstall=e;syncInstallButton();if(state.installGuideOpen)openInstallInvite('guide');});
  window.addEventListener('appinstalled',()=>{markInstallInviteDismissed();closeInstallInvite(false);syncInstallButton();toast('TOEIC Dictionary đã được thêm vào thiết bị.');});
  $('#installButton').addEventListener('click',()=>{if(isMobileOrTabletDevice())openInstallInvite('guide');else if(state.deferredInstall)runNativeInstall();});
  $('#installInviteBackdrop').addEventListener('click',e=>{
    const action=e.target.closest('[data-install-action]')?.dataset.installAction;
    if(action==='dismiss')closeInstallInvite(true);
    else if(action==='guide')openInstallInvite('guide');
    else if(action==='back')openInstallInvite('welcome');
    else if(action==='install')runNativeInstall();
  });
  window.addEventListener('pageshow',syncInstallButton);
}
function practiceAttemptHistoryMarkup(progress,index){
  const history=getPracticeAttemptHistory(progress,index);
  if(!history.length)return '';
  const rows=history.map((attempt,i)=>`<li><div class="attempt-history-line"><span>Lần ${Number(attempt.attemptNumber)||i+1}</span><strong class="${attempt.correct?'attempt-history-correct':'attempt-history-wrong'}">${attempt.correct?'Đúng':'Sai'}</strong><span>Đã chọn: ${escapeHtml(attempt.choiceText||'Chưa lưu lựa chọn')}</span></div>${attempt.correctChoiceText?`<small>Đáp án đúng: ${escapeHtml(attempt.correctChoiceText)}</small>`:''}${attempt.explanation?`<p>${escapeHtml(attempt.explanation)}</p>`:''}</li>`).join('');
  return `<details class="practice-attempt-history"><summary>Lịch sử ${history.length} lần trước</summary><ol>${rows}</ol></details>`;
}
function practiceRetryActionMarkup(kind,id,index,progress,saved){
  if(!saved?.answered)return '';
  const attempts=getPracticeAttemptCount(progress,index);
  return `<div class="exercise-retry-row"><span>Lần làm ${attempts}</span><button type="button" class="text-button practice-retry-button" data-practice-retry="${kind}" data-practice-id="${escapeHtml(id)}" data-question-index="${index}">↻ Làm lại câu này</button></div>${practiceAttemptHistoryMarkup(progress,index)}`;
}
function practiceRetryAllToolbar(kind,id,progress,questions){
  const activeAnswers=Object.values(ensurePracticeProgress(progress).answers).filter(answer=>answer?.answered).length;
  if(!activeAnswers)return '';
  const attempted=countAttemptedPracticeQuestions(progress,questions.length);
  return `<div class="learning-attempt-toolbar"><div><strong>${attempted}/${questions.length} câu đã thử · ${activeAnswers} câu có kết quả hiện tại</strong><small>Lịch sử các lần trả lời được giữ lại khi làm lại.</small></div><button type="button" class="secondary-button" data-practice-retry-all="${kind}" data-practice-id="${escapeHtml(id)}">↻ Làm lại toàn bộ bài</button></div>`;
}
async function retryPracticeQuestion(button){
  const kind=button.dataset.practiceRetry,id=button.dataset.practiceId,index=Number(button.dataset.questionIndex);
  const key=({reading:'readingProgress',listening:'listeningProgress',grammar:'grammarProgress'})[kind];
  const map=kind==='reading'?state.readingProgress:kind==='listening'?state.listeningProgress:kind==='grammar'?state.grammarProgress:null;
  const renderer=kind==='reading'?openReadingDetail:kind==='listening'?openListeningDetail:kind==='grammar'?openGrammarLesson:null;
  if(!key||!map||!renderer||!id||!Number.isInteger(index)||index<0)return;
  const progress=ensurePracticeProgress(map[id]||{});
  if(!archivePracticeAnswerForRetry(progress,index))return;
  map[id]=progress;await dbSet(key,map);
  const host=$('#learningFocusContent'),previousScroll=host?.scrollTop||0;
  renderer(id);requestAnimationFrame(()=>{if(host)host.scrollTop=previousScroll;});
  if(kind==='reading')renderReadingLibrary();else if(kind==='listening')renderListeningLibrary();else renderGrammarLibrary();
  renderToeicPartInsights();toast('Đã mở lại câu hỏi. Lịch sử lần trước vẫn được lưu.');
}
async function retryAllPracticeQuestions(button){
  const kind=button.dataset.practiceRetryAll,id=button.dataset.practiceId;
  const key=({reading:'readingProgress',listening:'listeningProgress',grammar:'grammarProgress'})[kind];
  const map=kind==='reading'?state.readingProgress:kind==='listening'?state.listeningProgress:kind==='grammar'?state.grammarProgress:null;
  const items=kind==='reading'?state.readings:kind==='listening'?state.listening:kind==='grammar'?state.grammarLessons:[];
  const renderer=kind==='reading'?openReadingDetail:kind==='listening'?openListeningDetail:kind==='grammar'?openGrammarLesson:null;
  if(!key||!map||!renderer||!id)return;
  const item=items.find(x=>x.id===id);if(!item)return;
  const progress=ensurePracticeProgress(map[id]||{}),questions=item.questions||item.exercises||[],count=Object.values(progress.answers).filter(answer=>answer?.answered).length;
  if(!count)return;
  if(!window.confirm(`Mở khóa lại ${count} câu trong “${item.title}”? Lịch sử trả lời cũ sẽ được giữ lại.`))return;
  const archived=archiveAllPracticeAnswersForRetry(progress);
  if(!archived){toast('Không có câu trả lời mới cần mở khóa.','error');return;}
  map[id]=progress;await dbSet(key,map);
  const host=$('#learningFocusContent'),previousScroll=host?.scrollTop||0;
  renderer(id);requestAnimationFrame(()=>{if(host)host.scrollTop=previousScroll;});
  if(kind==='reading')renderReadingLibrary();else if(kind==='listening')renderListeningLibrary();else renderGrammarLibrary();
  renderToeicPartInsights();toast(`Đã mở khóa ${archived} câu. Lịch sử được bảo toàn.`);
}

const PLACEMENT_LEVELS=['PRE-A1','A1','A2','B1'];
function startPlacementDiagnostic(){
 const qs=state.placementQuestions||[];if(!qs.length){toast('Chưa tải được bộ câu hỏi đánh giá.','error');return;}
 const session={answers:{},index:0,startedAt:Date.now()};
 state.placementState=session;renderPlacementQuestion();
}
function renderPlacementQuestion(){
 const s=state.placementState,qs=state.placementQuestions||[];if(!s)return;
 if(s.index>=qs.length){finishPlacementDiagnostic();return;}
 const q=qs[s.index],n=s.index+1;
 const mapped=(state.placementObjectiveMap?.questionMappings||[]).find(x=>x.questionId===q.id),domainLabel=mapped?.domainLabel||'Nội dung tổng hợp';
 const choices=q.choices.map((c,i)=>`<button type="button" class="foundation-choice" data-placement-answer="${i}">${String.fromCharCode(65+i)}. ${escapeHtml(c)}</button>`).join('');
 openLearningDetail({kind:'learning-detail',title:'Đánh giá điểm bắt đầu',subtitle:`Câu ${n}/${qs.length} · ${q.level}`,eyebrow:'PLACEMENT CHECK · PRACTICE ESTIMATE',content:`<div class="placement-progress"><div class="foundation-progress-track"><span style="width:${Math.round(n/qs.length*100)}%"></span></div><small>${n} / ${qs.length}</small></div><section class="foundation-question" data-placement-question><span class="foundation-level detail-pill">${q.level}</span><small class="placement-domain-label">Nhóm nội dung: ${escapeHtml(domainLabel)}</small><h3>${escapeHtml(q.prompt)}</h3><div class="foundation-choices">${choices}</div><p class="foundation-feedback" data-placement-feedback hidden></p></section><p class="placement-disclaimer">Bài đánh giá ngắn để gợi ý điểm bắt đầu, không phải chứng chỉ CEFR hoặc điểm ETS. Chưa đo kỹ năng nghe, nói và viết.</p>`});
}
function answerPlacementQuestion(button){
 const s=state.placementState,qs=state.placementQuestions||[],q=qs[s?.index];if(!s||!q||s.answers[q.id]!==undefined)return;
 const selected=Number(button.dataset.placementAnswer);if(!Number.isInteger(selected)||selected<0||selected>3)return;
 s.answers[q.id]=selected;const host=button.closest('[data-placement-question]');
 host?.querySelectorAll('[data-placement-answer]').forEach(b=>{b.disabled=true;if(Number(b.dataset.placementAnswer)===selected)b.classList.add('is-selected');});
 if(s.index===qs.length-1){finishPlacementDiagnostic();return;}
 const next=document.createElement('button');next.type='button';next.className='primary-button';next.textContent='Câu tiếp theo →';next.dataset.placementNext='true';host?.append(next);
}
function finishPlacementDiagnostic(){
 const s=state.placementState,qs=state.placementQuestions||[];if(!s)return;
 const counts={};for(const lv of PLACEMENT_LEVELS)counts[lv]={correct:0,total:0};
 qs.forEach(q=>{counts[q.level].total++;if(s.answers[q.id]===q.answerIndex)counts[q.level].correct++;});
 const correctTotal=qs.filter(q=>s.answers[q.id]===q.answerIndex).length;state.pendingPlacementResult=true;
 showAssessmentResultModal({eyebrow:'PLACEMENT CHECK · COMPLETE',title:'Bạn đã hoàn thành bài đánh giá',correct:correctTotal,incorrect:qs.length-correctTotal,total:qs.length,description:'Đã nhận đủ câu trả lời. Xác nhận để xem phân tích điểm bắt đầu và từng câu đã làm.'});return;
}
function finalizePlacementDiagnostic(){
 const s=state.placementState,qs=state.placementQuestions||[];if(!s)return;
 const counts={};for(const lv of PLACEMENT_LEVELS)counts[lv]={correct:0,total:0};
 qs.forEach(q=>{counts[q.level].total++;if(s.answers[q.id]===q.answerIndex)counts[q.level].correct++;});
 const passed=PLACEMENT_LEVELS.filter(lv=>counts[lv].total>=3&&counts[lv].correct>=3),recommended=passed.at(-1)||'PRE-A1';
 const domainCounts={};(state.placementObjectiveMap?.questionMappings||[]).forEach(m=>{const q=qs.find(x=>x.id===m.questionId);if(!q)return;const d=domainCounts[m.domain]||(domainCounts[m.domain]={label:m.domainLabel,correct:0,total:0});d.total++;if(s.answers[q.id]===q.answerIndex)d.correct++;});
 const result={recommended,counts,completedAt:Date.now(),answers:s.answers,questionCount:qs.length};
 try{localStorage.setItem('toeic:placement-diagnostic:v1',JSON.stringify(result));}catch{}
 state.placementState=null;
 const rows=PLACEMENT_LEVELS.map(lv=>`<div class="placement-result-row"><strong>${lv}</strong><span>${counts[lv].correct}/${counts[lv].total} câu đúng</span></div>`).join('');
 const domainRows=Object.values(domainCounts).map(d=>`<div class="placement-result-row"><strong>${escapeHtml(d.label)}</strong><span>${d.correct}/${d.total} câu đúng</span></div>`).join('');
 openLearningDetail({kind:'learning-detail',title:'Kết quả đánh giá điểm bắt đầu',subtitle:'Kết quả tham khảo từ bài kiểm tra ngắn',eyebrow:'YOUR PERSONAL START POINT',content:`<section class="foundation-question"><p class="foundation-kicker">ĐỀ XUẤT ĐIỂM BẮT ĐẦU</p><h2>${recommended}</h2><p>${recommended==='PRE-A1'?'Nên bắt đầu từ nền tảng và điều chỉnh sau khi học thêm.':`Bạn có thể bắt đầu từ ${recommended}; không cần hoàn thành các chặng thấp hơn trước.`}</p></section><section class="detail-section"><h3>Kết quả theo cấp độ</h3>${rows}</section><section class="detail-section"><h3>Kết quả theo nhóm nội dung</h3>${domainRows||'<p>Chưa có bản đồ nội dung để phân tích.</p>'}<p class="placement-disclaimer">Nhóm nội dung chỉ phản ánh các câu đã làm trong bài kiểm tra này, không phải điểm kỹ năng toàn diện.</p></section><section class="detail-section placement-question-review"><h3>Xem lại từng câu và đáp án</h3>${qs.map((q,i)=>{const selected=s.answers[q.id],ok=selected===q.answerIndex;return `<article class="mock-review-question"><h4>Câu ${i+1} · ${ok?'Đúng':'Chưa đúng'}</h4><p>${escapeHtml(q.prompt)}</p><p>Bạn chọn: <strong>${escapeHtml(q.choices[selected]||'Chưa trả lời')}</strong></p><p>Đáp án: <strong>${escapeHtml(q.choices[q.answerIndex]||'')}</strong></p><p>${escapeHtml(q.rationale||'')}</p></article>`;}).join('')}</section><p class="placement-disclaimer">Ngưỡng gợi ý: ít nhất 3/4 câu đúng ở cấp độ đó. Đây chỉ là mẫu trắc nghiệm ngắn về từ vựng, ngữ pháp và đọc hiểu; chưa đánh giá nghe, nói, viết, tốc độ xử lý hay toàn bộ năng lực CEFR/TOEIC.</p><button type="button" class="primary-button" data-placement-apply="${recommended}">Áp dụng ${recommended} làm điểm bắt đầu</button><button type="button" class="secondary-button" data-placement-retry>Làm lại bài đánh giá</button>`});
}
function applyPlacementLevel(level){if(!['PRE-A1','A1','A2','B1'].includes(level))return;state.foundationStartLevel=level;try{localStorage.setItem('toeic:learning-start-level:v1',level);}catch{}closeLearningFocus();renderFoundationPath();toast(`Đã đặt điểm bắt đầu ${level}.`);}

function foundationProductionTasks(lesson){
 const tasks=[lesson?.productionTask,...(Array.isArray(lesson?.additionalProductionTasks)?lesson.additionalProductionTasks:[])].filter(task=>task&&typeof task==='object'&&String(task.id||'').trim());
 const unique=[...new Map(tasks.map(task=>[String(task.id),task])).values()];
 return unique.length?unique:(lesson?.applicationTask?[lesson.applicationTask]:[]);
}
function foundationProductionFieldKey(lessonId,taskId){
 return `foundation-production-${String(lessonId||'').replace(/[^a-zA-Z0-9_-]/g,'-')}-${String(taskId||'').replace(/[^a-zA-Z0-9_-]/g,'-')}`;
}

function renderFoundationPath(){
 const rank={'PRE-A1':0,'A1':1,'A2':2,'B1':3,'B2':4,'C1':5};
 const selector=$('#foundationStartLevel');if(selector)selector.value=state.foundationStartLevel||'ALL';
 const all=state.foundationLessons||[],selected=state.foundationStartLevel||'ALL';
 const rows=selected==='ALL'?all:all.filter(x=>(rank[x.level]??99)>=(rank[selected]??0));
 const done=rows.filter(lesson=>summarizeFoundationLesson(state.foundationProgress,lesson.id).status==='practice_threshold_met').length;
 const pct=rows.length?Math.round(done/rows.length*100):0;
 const label=$('#foundationProgressLabel'),percent=$('#foundationProgressPercent'),bar=$('#foundationProgressBar'),hint=$('#foundationProgressHint'),list=$('#foundationLessonList'),note=$('#foundationPathNote'),meter=$('#foundationProgressMeter'),outcomeDashboard=$('#foundationOutcomeDashboard');
 if(!label||!percent||!bar||!hint||!list||!note)return;
 label.textContent=`${done} / ${rows.length} bài đạt ngưỡng`;
 percent.textContent=`${pct}%`;
 bar.style.width=`${pct}%`;
 meter?.setAttribute('aria-valuenow',String(pct));
 const dueRecallTotal=listDueFoundationRecallItems(state.foundationProgress,all).length;
 hint.textContent=rows.length?(done?`${done} bài đạt ngưỡng nhận biết/hiểu dựa trên câu hỏi độc lập.`:'Chỉ tính bằng chứng nhận biết/hiểu từ câu hỏi độc lập.')+` ${dueRecallTotal} câu ôn tập cách quãng đang đến hạn; vận dụng/sản sinh được tự đánh giá riêng.`:'Chưa có bài học được phát hành ở cấp độ này.';
 if(outcomeDashboard)outcomeDashboard.innerHTML=renderFoundationOutcomeDashboard(selected,all); 
 const levelName=selected==='ALL'?'tất cả cấp độ':selected;
 note.textContent=selected==='ALL'?'Bạn đang xem toàn bộ bài học hiện có.':`Bạn đang bắt đầu từ ${levelName}. Các cấp độ thấp hơn chỉ được ẩn khỏi lộ trình, không bị xóa và có thể mở lại bằng cách đổi lựa chọn. ${rows.length?'':'Nội dung '+levelName+' trở lên chưa được phát hành đầy đủ; bạn vẫn có thể dùng từ điển và các thư viện luyện tập hiện có.'}`;
 list.innerHTML=rows.length?rows.map((lesson,index)=>{
   const evidence=summarizeFoundationLesson(state.foundationProgress,lesson.id);
   const application=summarizeFoundationApplication(state.foundationProgress,lesson.id);
   const readingResource=(state.foundationReadingPassages||[]).find(item=>item.lessonId===lesson.id);
   const extendedReadingResource=(state.foundationReadingExtendedPassages||[]).find(item=>item.lessonId===lesson.id);
   const extendedReadingProgressId=extendedReadingResource?`${lesson.id}::reading2`:'';
   const extendedReading=extendedReadingResource?summarizeFoundationReading(state.foundationReadingProgress,extendedReadingProgressId,{minimumUniqueQuestions:extendedReadingResource.minimumUniqueQuestions||3,practiceAccuracyThreshold:extendedReadingResource.practiceAccuracyThreshold||0.67}):null;
   const listeningResource=(state.foundationListeningClips||[]).find(item=>item.lessonId===lesson.id&&!item.supplementary);
   const extendedListeningResource=(state.foundationListeningClips||[]).find(item=>item.lessonId===lesson.id&&item.supplementary&&item.evidenceScope==='listening2');
   const extendedListening=summarizeFoundationListening(state.foundationListeningProgress,extendedListeningResource?`${lesson.id}::listening2`:'',{minimumUniqueQuestions:extendedListeningResource?.minimumUniqueQuestions||3,practiceAccuracyThreshold:extendedListeningResource?.practiceAccuracyThreshold||0.67});
   const reading=summarizeFoundationReading(state.foundationReadingProgress,lesson.id,{minimumUniqueQuestions:readingResource?.minimumUniqueQuestions||2,practiceAccuracyThreshold:readingResource?.practiceAccuracyThreshold||0.8});
   const listening=summarizeFoundationListening(state.foundationListeningProgress,lesson.id,{minimumUniqueQuestions:listeningResource?.minimumUniqueQuestions||2,practiceAccuracyThreshold:listeningResource?.practiceAccuracyThreshold||0.8});
   const readingTarget=readingResource?.questions?.length||2,listeningTarget=listeningResource?.questions?.length||2;
   const recognitionStatus=evidence.status==='practice_threshold_met'?`Nhận biết: đạt · ${evidence.accuracyPercent}%`:evidence.uniqueQuestions?`Nhận biết: ${evidence.uniqueQuestions}/3 câu`:'Nhận biết: chưa có bằng chứng';
   const applicationStatus=application.uniqueTasks?`Vận dụng: ${application.accuracyPercent}% đúng gần nhất`:'Vận dụng: chưa thực hiện';
   const readingBaseStatus=reading.uniqueQuestions?`${reading.uniqueQuestions}/${readingTarget} câu · ${reading.accuracyPercent}%`:'chưa thực hiện';
   const readingExtendedStatus=extendedReading?`Mở rộng · chờ duyệt ${extendedReading.uniqueQuestions}/${extendedReadingResource.questions.length} câu${extendedReading.accuracyPercent===null?'':` · ${extendedReading.accuracyPercent}%`}`:'';
   const readingStatus=`Đọc hiểu: ${readingBaseStatus}${readingExtendedStatus?` · ${readingExtendedStatus}`:''}`;
   const listeningBaseStatus=listening.uniqueQuestions?`${listening.uniqueQuestions}/${listeningTarget} câu · ${listening.accuracyPercent}%`:'chưa thực hiện';
   const listeningExtendedStatus=extendedListeningResource?`Mở rộng · chờ duyệt ${extendedListening.uniqueQuestions}/${extendedListeningResource.questions.length} câu${extendedListening.accuracyPercent===null?'':` · ${extendedListening.accuracyPercent}%`}`:'';
   const listeningStatus=`Nghe hiểu: ${listeningBaseStatus}${listeningExtendedStatus?` · ${listeningExtendedStatus}`:''}`;
   const productionTasks=foundationProductionTasks(lesson);
   const completedProductionTasks=productionTasks.filter(task=>Number.isFinite(Number(state.foundationProgress[lesson.id]?.productionEvidence?.[task.id]?.latestScore))).length;
   const productionStatus=productionTasks.length?`Tự tạo câu: ${completedProductionTasks}/${productionTasks.length} nhiệm vụ có tự đánh giá`:'Tự tạo câu: chưa có nhiệm vụ';
   const recallDue=listDueFoundationRecallItems(state.foundationProgress,[lesson]).length;
   const recallStatus=recallDue?`Ôn lại: ${recallDue} câu đến hạn`:'Ôn lại: theo lịch';
   return `<article class="learning-card foundation-card"><div class="learning-card-top"><span class="learning-category">Bài ${String(index+1).padStart(2,'0')}</span><span class="learning-level">${escapeHtml(lesson.level)}</span></div><h3>${escapeHtml(lesson.title)}</h3><p>${escapeHtml(lesson.objective)}</p><div class="foundation-card-evidence"><span>${recognitionStatus}</span><span>${applicationStatus}</span><span>${readingStatus}</span><span>${listeningStatus}</span><span>${productionStatus}</span><span>${recallStatus}</span></div><div class="learning-card-footer foundation-card-footer"><small>${evidence.uniqueQuestions} câu nhận biết độc lập</small><button type="button" class="secondary-button" data-foundation-open="${escapeHtml(lesson.id)}">${evidence.uniqueQuestions?'Tiếp tục ôn':'Bắt đầu học'} →</button></div></article>`;
 }).join(''):`<article class="learning-card foundation-card foundation-empty"><div class="learning-card-top"><span class="learning-category">${escapeHtml(selected)}</span><span class="learning-level">Đang xây dựng</span></div><h3>Chặng ${escapeHtml(selected)} chưa được phát hành</h3><p>Không tự động đưa bạn quay về Pre-A1/A1. Bạn vẫn có thể tiếp tục với từ điển, Ngữ pháp, Đọc hiểu, Nghe và Thi thử hiện có.</p><div class="learning-card-footer"><small>Nội dung sẽ được bổ sung theo lộ trình.</small><button type="button" class="secondary-button" data-go="dictionary">Mở từ điển →</button></div></article>`;
}
function renderFoundationOutcomeDashboard(selected, lessons) {
 const stageOrder={'PRE-A1':0,'A1':1,'A2':2};
 const hostLevels=selected==='ALL'?Object.keys(stageOrder):Object.keys(stageOrder).filter(level=>stageOrder[level]>=(stageOrder[selected]??0));
 const outcomes=summarizeFoundationOutcomeProgress(state.foundationProgress,lessons,state.foundationOutcomeRegistry||{},Date.now());
 const groups=[
  {objectiveId:'foundation-pre-a1-a1',title:'Pre-A1 / A1',levels:['PRE-A1','A1']},
  {objectiveId:'foundation-a2',title:'A2',levels:['A2']}
 ].filter(group=>group.levels.some(level=>hostLevels.includes(level)));
 const cards=groups.map(group=>{
  const rows=outcomes.filter(row=>row.objectiveId===group.objectiveId);
  const names={recognition:'Nhận biết',production:'Tự tạo câu · tự đánh giá',retention:'Ghi nhớ cách quãng'};
  return `<section class="foundation-outcome-group"><h4>${group.title}</h4><div class="foundation-outcome-metrics">${rows.map(row=>`<article class="foundation-outcome-metric"><strong>${names[row.kind]||row.title}</strong><span>${row.uniqueItems}/${row.minimumUniqueItems} mục độc lập</span><span>${row.accuracyPercent===null?'Chưa có kết quả':`${row.accuracyPercent}%`}</span><small>${row.kind==='production'?'Tự báo cáo của người học':row.kind==='retention'?'Chỉ tính câu đã ôn sau thời điểm đến hạn':'Kết quả mới nhất theo ID câu hỏi'}</small></article>`).join('')}</div></section>`;
 }).join('');
 const due=listDueFoundationRecallItems(state.foundationProgress,lessons).length;
 const showA2Portfolio=groups.some(group=>group.objectiveId==='foundation-a2');
 const a2Portfolio=showA2Portfolio?renderFoundationProductionPortfolio(lessons.filter(lesson=>lesson.level==='A2')):'';
 return `<section class="foundation-outcome-dashboard-inner"><div class="foundation-outcome-heading"><div><h3>Bằng chứng kết quả học tập</h3><p>Ba loại bằng chứng được theo dõi riêng; số lượng bài có sẵn không đồng nghĩa với mastery.</p></div><span class="foundation-outcome-due">${due} câu ôn đến hạn</span></div>${cards}${a2Portfolio}<p class="placement-disclaimer">Ngưỡng tham khảo: tối thiểu 10 mục độc lập và 80%. Tự đánh giá sản sinh không phải chấm điểm ngôn ngữ độc lập; ôn tập cách quãng không phải bảo đảm ghi nhớ lâu dài hoặc chứng nhận CEFR.</p></section>`;
}


function exportFoundationProductionPortfolio(){
 const lessons=(state.foundationLessons||[]).filter(lesson=>lesson.level==='A2');
 const summary=summarizeFoundationProductionPortfolio(state.foundationProgress,lessons,{level:'A2'});
 if(!summary.startedTasks){toast('Chưa có bài viết A2 nào được lưu để xuất.','error');return;}
 const markdown=buildFoundationProductionPortfolioMarkdown(state.foundationProgress,lessons,Date.now());
 const now=new Date(),stamp=[now.getFullYear(),String(now.getMonth()+1).padStart(2,'0'),String(now.getDate()).padStart(2,'0')].join('-');
 downloadFile(`toeic-foundation-a2-writing-portfolio-${stamp}.md`,markdown,'text/markdown;charset=utf-8');
 toast(`Đã xuất nhật ký ${summary.startedTasks} bài viết A2. Tệp chỉ chứa dữ liệu bạn đã lưu trên thiết bị.`);
}

function renderFoundationProductionPortfolio(lessons){
 const summary=summarizeFoundationProductionPortfolio(state.foundationProgress,lessons,{level:'A2'});
 const recordRows=summary.records.map(item=>{
  const ratingRows=item.rubric.map((label,index)=>`<li><span>${escapeHtml(label)}</span><strong>${item.latestRatings[index]===true?'Đã xác nhận':item.latestRatings[index]===false?'Cần rà lại':'Chưa có dữ liệu'}</strong></li>`).join('');
  const trendLabel=item.trend==='not_revised'?'Chưa viết lại':item.trend==='self_report_up'?'Tự đánh giá tăng':item.trend==='self_report_down'?'Tự đánh giá giảm':'Tự đánh giá không đổi';
  return `<details class="foundation-portfolio-row"><summary><span><strong>${escapeHtml(item.title)}</strong><small>${item.attemptCount} lượt tự đánh giá · ${item.revisionCount} lần viết lại</small></span><span class="foundation-portfolio-scores"><strong>${item.initialScore}/3 <i>→</i> ${item.latestScore}/3</strong><small>${trendLabel}</small></span></summary><div class="foundation-portfolio-row-detail"><ul>${ratingRows}</ul><button type="button" class="text-button" data-foundation-open="${escapeHtml(item.lessonId)}">Mở bài học để tiếp tục →</button></div></details>`;
 }).join('');
 const compareCount=summary.selfReportedImproved+summary.selfReportedUnchanged+summary.selfReportedReduced;
 return `<details class="foundation-production-portfolio"><summary><span><strong>Nhật ký viết A2</strong><small>${summary.startedTasks}/${summary.totalTasks} bài có dữ liệu · ${summary.revisedTasks} bài đã viết lại</small></span><span class="foundation-portfolio-toggle">Xem tổng kết</span></summary><div class="foundation-portfolio-content"><div class="foundation-portfolio-export"><div><strong>Xuất bài viết đã lưu</strong><small>Tải về Markdown gồm tình huống, câu trả lời ban đầu, các lần viết lại và phần tự đánh giá.</small></div><button type="button" class="secondary-button" data-foundation-production-export ${summary.startedTasks?'':'disabled'}>Xuất nhật ký (.md)</button></div><div class="foundation-portfolio-metrics"><article><small>Bài đã bắt đầu</small><strong>${summary.startedTasks}/${summary.totalTasks}</strong></article><article><small>Bài đã viết lại</small><strong>${summary.revisedTasks}</strong></article><article><small>Tổng lượt tự đánh giá</small><strong>${summary.totalAttempts}</strong></article></div><section class="foundation-portfolio-trend"><h4>Thay đổi tự đánh giá sau khi viết lại</h4><div class="foundation-portfolio-trend-counts"><span>${summary.selfReportedImproved} tăng</span><span>${summary.selfReportedUnchanged} không đổi</span><span>${summary.selfReportedReduced} giảm</span></div><p>${compareCount?`Đối chiếu ${compareCount} bài có ít nhất một lần viết lại. So sánh chỉ thực hiện trong từng bài theo bộ tiêu chí riêng của bài đó; đây là tự đánh giá, không phải chấm điểm ngôn ngữ độc lập.`:'Khi bạn viết lại và tự đánh giá, ứng dụng sẽ đối chiếu từng bài với bộ tiêu chí riêng của bài đó.'}</p></section><section class="foundation-portfolio-records"><h4>Chi tiết theo bài học</h4>${recordRows||'<p class="foundation-portfolio-empty">Chưa có bài viết A2 được lưu. Hãy mở một bài A2 và hoàn thành phần Tự tạo câu để bắt đầu nhật ký.</p>'}</section><p class="foundation-portfolio-disclaimer">Dữ liệu đọc từ tiến độ hiện có trên thiết bị. Điểm là tự đánh giá của người học trên thang 0–3; ứng dụng không tự chấm ngữ pháp, không suy ra năng lực CEFR và không gửi bài viết ra ngoài thiết bị.</p></div></details>`;
}

function renderAlphabetSoundLab(){
 const items=state.alphabetSoundItems||[];
 const summary=summarizeAlphabetSoundProgress(state.alphabetSoundProgress,items.length);
 const cards=items.map(item=>{
  const saved=state.alphabetSoundProgress?.letters?.[item.id]||{};
  const nameCount=Math.max(0,Number(saved.letterName?.count)||0),wordCount=Math.max(0,Number(saved.exampleWord?.count)||0);
  return `<article class="alphabet-sound-card" data-alphabet-card="${escapeHtml(item.id)}"><div class="alphabet-sound-card-head"><strong>${escapeHtml(item.letter)} <span>${escapeHtml(item.lowercase)}</span></strong><span class="alphabet-sound-letter-tag">${escapeHtml(item.letterNameIpa)}</span></div><div class="alphabet-sound-example"><strong>${escapeHtml(item.exampleWord)}</strong><span>${escapeHtml(item.exampleIpa)} · ${escapeHtml(item.exampleMeaning)}</span></div><div class="alphabet-sound-focus"><span>Âm tiêu biểu</span><strong>${escapeHtml(item.focusSound)}</strong><small>${escapeHtml(item.note)}</small></div><div class="alphabet-sound-actions"><button type="button" class="secondary-button" data-alphabet-play="${escapeHtml(item.id)}" data-alphabet-kind="letterName" aria-label="Nghe tên chữ ${escapeHtml(item.letter)}">${nameCount?'Nghe lại tên chữ':'Nghe tên chữ'}</button><button type="button" class="secondary-button" data-alphabet-play="${escapeHtml(item.id)}" data-alphabet-kind="exampleWord" aria-label="Nghe từ ví dụ ${escapeHtml(item.exampleWord)}">${wordCount?'Nghe lại từ mẫu':'Nghe từ mẫu'}</button></div><small class="alphabet-sound-status">Tên chữ: ${nameCount} lượt · Từ mẫu: ${wordCount} lượt</small></article>`;
 }).join('');
 return `<section class="detail-section alphabet-sound-lab" data-alphabet-sound-lab><div class="alphabet-sound-lab-heading"><div><h4>PHÒNG LUYỆN TÊN CHỮ VÀ ÂM ĐẦU</h4><p>Luyện đủ 26 chữ A–Z. Nghe tên chữ cái riêng, sau đó nghe từ mẫu để nhận biết một âm thường gặp.</p></div><div class="alphabet-sound-progress" data-alphabet-summary>${summary.practicedLetters}/${summary.expectedLetters} chữ đã luyện · ${summary.completedPairs}/${summary.expectedLetters} cặp đã chọn nghe đủ</div></div><div class="alphabet-sound-grid">${cards}</div><p class="alphabet-sound-disclaimer">Âm hiển thị là ví dụ nhập môn, không phải quy tắc phát âm đầy đủ. Một chữ có thể biểu thị nhiều âm tùy từ. Giọng đọc dùng TTS của thiết bị; số lượt chỉ ghi nhận thao tác phát, không đánh giá độ chính xác phát âm.</p></section>`;
}
function playAlphabetSound(button){
 const id=String(button.dataset.alphabetPlay||'').toUpperCase(),kind=button.dataset.alphabetKind;
 const item=state.alphabetSoundItems.find(entry=>entry.id===id);if(!item||!['letterName','exampleWord'].includes(kind))return;
 if(!('speechSynthesis'in window)||typeof SpeechSynthesisUtterance==='undefined'){toast('Thiết bị chưa hỗ trợ đọc phát âm.','error');return;}
 speakText(kind==='letterName'?item.letter:item.exampleWord,null,'',state.settings.tts?.defaultGender||'female');
 state.alphabetSoundProgress=recordAlphabetSoundPractice(state.alphabetSoundProgress,id,kind,Date.now());
 try{localStorage.setItem('toeic:alphabet-sound-progress:v1',JSON.stringify(state.alphabetSoundProgress));}catch(error){console.warn('Không lưu được tiến độ luyện bảng chữ cái:',error);}
 const card=button.closest('[data-alphabet-card]'),saved=state.alphabetSoundProgress.letters[id]||{};
 const nameCount=Number(saved.letterName?.count)||0,wordCount=Number(saved.exampleWord?.count)||0;
 const status=card?.querySelector('.alphabet-sound-status');if(status)status.textContent=`Tên chữ: ${nameCount} lượt · Từ mẫu: ${wordCount} lượt`;
 const nameButton=card?.querySelector('[data-alphabet-kind="letterName"]'),wordButton=card?.querySelector('[data-alphabet-kind="exampleWord"]');
 if(nameButton)nameButton.textContent=nameCount?'Nghe lại tên chữ':'Nghe tên chữ';
 if(wordButton)wordButton.textContent=wordCount?'Nghe lại từ mẫu':'Nghe từ mẫu';
 const summary=summarizeAlphabetSoundProgress(state.alphabetSoundProgress,state.alphabetSoundItems.length),summaryNode=$('[data-alphabet-summary]',button.closest('[data-alphabet-sound-lab]'));
 if(summaryNode)summaryNode.textContent=`${summary.practicedLetters}/${summary.expectedLetters} chữ đã luyện · ${summary.completedPairs}/${summary.expectedLetters} cặp đã chọn nghe đủ`;
}

function renderFoundationProductionSection(lesson, application, saved, legacySaved=null, taskOverride=null, taskIndex=0){
 if(!application)return '';
 const task=taskOverride||lesson.productionTask||null,taskId=task?.id||application.id;
 const minimumWords=Math.max(3,Number(task?.minimumWords)||3);
 const fieldKey=foundationProductionFieldKey(lesson.id,taskId);
 const responseId=`${fieldKey}-response`,revisionResponseId=`${fieldKey}-revision-response`;
 const rubric=Array.isArray(task?.rubric)&&task.rubric.length===3?task.rubric:[
  'Tôi giải thích được vì sao cấu trúc phù hợp với ý định',
  'Tôi chỉ ra được vì sao cách diễn đạt khác không phù hợp',
  'Tôi tự tạo được câu mới phù hợp tình huống'
 ];
 const requirements=(task?.requirements||[]).map(item=>`<li>${escapeHtml(item)}</li>`).join('');
 const contextHtml=task?`<div class="foundation-production-context"><div><strong>Bối cảnh</strong><p>${escapeHtml(task.scenario)}</p></div><div><strong>Nhiệm vụ</strong><p>${escapeHtml(task.instruction)}</p></div>${requirements?`<div><strong>Yêu cầu cần có</strong><ul>${requirements}</ul></div>`:''}${task.sentenceFrame?`<div class="foundation-production-frame"><strong>Khung gợi ý</strong><p>${escapeHtml(task.sentenceFrame)}</p></div>`:''}${task.modelAnswer?`<details class="foundation-production-model"><summary>Gợi ý tham khảo (chỉ mở sau khi bạn tự viết)</summary><p>${escapeHtml(task.modelAnswer)}</p><small>${escapeHtml(task.modelAnswerNote||'Đây là ví dụ tham khảo, không phải đáp án duy nhất.')}</small></details>`:''}</div>`:'';
 const initialResponse=String(saved?.initialResponse||saved?.attempts?.[0]?.response||saved?.latestResponse||'');
 const latestResponse=String(saved?.latestResponse||initialResponse);
 const initialAttempt=(saved?.attempts||[]).find(item=>item?.response===initialResponse)||saved?.attempts?.[0]||null;
 const initialRatings=Array.isArray(initialAttempt?.ratings)&&initialAttempt.ratings.length===3?initialAttempt.ratings:(saved?.latestRatings||[]);
 const count=initialResponse.trim().split(/\s+/).filter(Boolean).length;
 const latestCount=latestResponse.trim().split(/\s+/).filter(Boolean).length;
 const legacyNotice=taskIndex===0&&task&&legacySaved&&!saved?'<p class="placement-disclaimer">Bài tự tạo từ phiên bản trước vẫn được giữ trong dữ liệu học tập trên thiết bị. Bài tập theo tình huống A2 này có mã ghi nhận riêng nên cần thực hiện lại để được tính vào bằng chứng mới.</p>':'';
 const rubricHtml=rubric.map((label,index)=>`<div class="foundation-production-rubric-row"><strong>${index+1}. ${escapeHtml(label)}</strong><label><input type="radio" name="${fieldKey}-self-${index}" value="yes" ${initialRatings?.[index]===true?'checked':''}> Có</label><label><input type="radio" name="${fieldKey}-self-${index}" value="no" ${initialRatings?.[index]===false?'checked':''}> Chưa chắc</label></div>`).join('');
 const revisionChecklist=Array.isArray(task?.revisionChecklist)&&task.revisionChecklist.length===3?task.revisionChecklist:[];
 const revisionChecksHtml=revisionChecklist.map((label,index)=>`<label class="foundation-revision-check"><input type="checkbox" data-foundation-revision-check value="${index}" ${saved?.latestRevisionChecks?.[index]===true?'checked':''}><span><strong>${escapeHtml(label)}</strong><small>Đã tự đối chiếu yêu cầu này</small></span></label>`).join('');
 const revisionRubricHtml=rubric.map((label,index)=>`<div class="foundation-production-rubric-row"><strong>${index+1}. ${escapeHtml(label)}</strong><label><input type="radio" name="${fieldKey}-revision-${index}" value="yes" ${saved?.latestRatings?.[index]===true?'checked':''}> Có</label><label><input type="radio" name="${fieldKey}-revision-${index}" value="no" ${saved?.latestRatings?.[index]===false?'checked':''}> Chưa chắc</label></div>`).join('');
 const previousRevisionSource=saved?.lastRevisionSource||saved?.initialResponse||saved?.latestResponse||'';
 const revisionHtml=saved&&revisionChecklist.length?`<details class="foundation-revision-workspace" open><summary>Rà soát và viết lại <span>${Number(saved.revisionCount)||0} lượt sửa</span></summary><div class="foundation-revision-body"><div class="foundation-revision-previous"><strong>Bản trước để đối chiếu</strong><p>${escapeHtml(previousRevisionSource)}</p></div><div class="foundation-revision-checklist"><strong>Tự rà soát từng yêu cầu</strong>${revisionChecksHtml}</div><div class="foundation-revision-hint"><strong>Gợi ý sửa theo chủ điểm</strong><p>${escapeHtml(task.revisionHint||'Đối chiếu từng yêu cầu với câu trả lời rồi viết lại cho rõ nghĩa.')}</p></div><label class="foundation-production-label" for="${revisionResponseId}">Bản viết lại của bạn</label><textarea id="${revisionResponseId}" class="foundation-production-textarea" maxlength="500" rows="4" data-foundation-revision-text placeholder="Rewrite your response here...">${escapeHtml(latestResponse)}</textarea><p class="foundation-production-word-count" data-foundation-revision-count>${latestCount}/${minimumWords} từ tối thiểu${latestCount>=minimumWords?' · Đủ độ dài':''}</p><div class="foundation-production-rubric"><strong class="foundation-production-rubric-title">Tự đánh giá bản viết lại</strong>${revisionRubricHtml}</div><button type="button" class="primary-button" data-foundation-production-revision-save data-foundation-id="${escapeHtml(lesson.id)}" data-foundation-task-id="${escapeHtml(taskId)}">Lưu bản viết lại</button><p class="placement-disclaimer">Mỗi lần sửa được lưu thành một lượt riêng, gồm bản dựa trên, bản viết lại và tự đánh giá. Ứng dụng không tự chấm đúng/sai về ngôn ngữ.</p></div></details>`:'';
 const heading=taskIndex===0?'TỰ TẠO CÂU / SẢN SINH NGÔN NGỮ':'THỬ THÁCH VIẾT MỞ RỘNG';
 const title=task?.title?`<h5 class="foundation-production-task-title">${escapeHtml(task.title)}</h5>`:'';
 return `<section class="detail-section foundation-production ${taskIndex>0?'foundation-production-extended':''}" data-foundation-production="${escapeHtml(taskId)}" data-minimum-words="${minimumWords}"><h4>${heading}</h4>${title}${legacyNotice}<p>${taskIndex===0?'Viết câu trả lời theo tình huống và tự kiểm tra ba tiêu chí.':'Bài viết mở rộng giúp bạn kết hợp nhiều câu và vận dụng cấu trúc vào tình huống gần thực tế hơn.'} ${saved?'Bản đầu tiên được giữ riêng để đối chiếu; dùng khu vực viết lại bên dưới để lưu phiên bản mới. ':''}Ứng dụng không tự chấm ngữ pháp; câu trả lời và tự đánh giá chỉ được lưu trên thiết bị này.</p>${contextHtml}<label class="foundation-production-label" for="${responseId}">${saved?'Bản trả lời đầu tiên':'Câu trả lời tiếng Anh của bạn'}</label><textarea id="${responseId}" class="foundation-production-textarea" maxlength="500" rows="4" data-foundation-production-text placeholder="Write your own response in English...">${escapeHtml(initialResponse)}</textarea><p class="foundation-production-word-count" data-foundation-production-count>${count}/${minimumWords} từ tối thiểu${count>=minimumWords?' · Đủ độ dài':''}</p><div class="foundation-production-rubric"><strong class="foundation-production-rubric-title">Tự kiểm tra trước khi lưu</strong>${rubricHtml}</div><button type="button" class="secondary-button" data-foundation-production-save data-foundation-id="${escapeHtml(lesson.id)}" data-foundation-task-id="${escapeHtml(taskId)}">Lưu câu và tự đánh giá</button><p class="placement-disclaimer" data-foundation-production-summary>${saved?`Lần gần nhất: ${saved.latestScore}/3 tiêu chí · ${saved.latestWordCount} từ · ${saved.attempts?.length||1} lượt · ${Number(saved.revisionCount)||0} lần viết lại. Đây là tự đánh giá, không phải kết quả chấm tự động.`:`Tối thiểu ${minimumWords} từ. Hệ thống giữ câu mới nhất và lịch sử tự đánh giá; không gửi câu trả lời lên máy chủ.`}</p>${revisionHtml}</section>`;
}

function renderFoundationReadingPanel(passage,lessonId,scopeId=''){
 const progressId=scopeId?`${lessonId}::${scopeId}`:lessonId;
 const draftKey=foundationDraftKey('foundation-reading',lessonId,scopeId);
 const summary=summarizeFoundationReading(state.foundationReadingProgress,progressId,{minimumUniqueQuestions:passage?.minimumUniqueQuestions||2,practiceAccuracyThreshold:passage?.practiceAccuracyThreshold||0.8});
 if(!passage)return '';
 const heading=scopeId?'ĐỌC HIỂU MỞ RỘNG · BÀI ĐỌC A2':'ĐỌC HIỂU · '+(passage.level==='A2'?'ĐOẠN VĂN NỀN TẢNG':'ĐOẠN NGẮN');
 const questions=(passage.questions||[]).map((q,i)=>{
  const saved=state.foundationReadingProgress[progressId]?.evidence?.[q.id],hasDraft=Number.isInteger(state.foundationAssessmentDrafts[draftKey]?.answers?.[q.id]);
  return `<section class="foundation-question" data-foundation-reading-question="${escapeHtml(q.id)}"><h3>Câu đọc hiểu ${i+1}/${passage.questions.length}</h3><p>${escapeHtml(q.prompt)}</p><div class="foundation-choices">${q.choices.map((choice,j)=>`<button type="button" class="foundation-choice ${state.foundationAssessmentDrafts[draftKey]?.answers?.[q.id]===j?'is-selected':''}" data-foundation-reading-answer="${j}" data-foundation-reading-lesson="${escapeHtml(lessonId)}" data-foundation-reading-scope="${escapeHtml(scopeId)}" data-foundation-reading-question-id="${escapeHtml(q.id)}">${String.fromCharCode(65+j)}. ${escapeHtml(choice)}</button>`).join('')}</div>${foundationDraftToolbar('foundation-reading',lessonId,passage.questions,scopeId)}<p class="foundation-feedback" data-foundation-reading-feedback ${saved&&!hasDraft?'':'hidden'}>${saved&&!hasDraft?`${saved.latestCorrect?'Đúng ở lượt gần nhất.':'Cần đọc lại và ôn tập.'} · ${saved.attempts?.length||1} lượt.`:''}</p></section>`;
 }).join('');
 return `<section class="detail-section foundation-reading" data-foundation-reading="${escapeHtml(passage.id)}"><h4>${heading}</h4><p class="placement-disclaimer">Đọc toàn bộ nội dung trước, sau đó trả lời ba câu hỏi. Bạn có thể đọc lại văn bản khi cần.</p><h3>${escapeHtml(passage.title)}</h3><p class="foundation-reading-format">${escapeHtml(passage.format||'Bài đọc')} · ${passage.text.trim().split(/\s+/).length} từ</p><div class="foundation-reading-text">${escapeHtml(passage.text)}</div>${questions}<p class="placement-disclaimer" data-foundation-reading-summary>${summary.uniqueQuestions}/${passage.questions.length} câu độc lập · ${summary.accuracyPercent===null?'Chưa có kết quả':`${summary.accuracyPercent}% đúng gần nhất`}. Ngưỡng luyện tập: ${summary.minimumUniqueQuestions} câu độc lập và ${Math.round(summary.threshold*100)}% đúng. Đây không phải chứng nhận CEFR.</p></section>`;
}

function renderFoundationListeningPanel(clip,lessonId,scopeId=''){
 const progressId=scopeId?`${lessonId}::${scopeId}`:lessonId;
 const draftKey=foundationDraftKey('foundation-listening',lessonId,scopeId);
 const summary=summarizeFoundationListening(state.foundationListeningProgress,progressId,{minimumUniqueQuestions:clip?.minimumUniqueQuestions||2,practiceAccuracyThreshold:clip?.practiceAccuracyThreshold||0.8});
 const statusId=`foundationListeningStatus-${String(clip.id).replace(/[^a-zA-Z0-9_-]/g,'-')}`;
 const questions=(clip.questions||[]).map((q,i)=>{
  const saved=state.foundationListeningProgress[progressId]?.evidence?.[q.id];
  const hasDraft=Number.isInteger(state.foundationAssessmentDrafts[draftKey]?.answers?.[q.id]);
  return `<section class="foundation-question" data-foundation-listening-question="${escapeHtml(q.id)}"><h3>Câu nghe hiểu ${i+1}/${clip.questions.length}</h3><p>${escapeHtml(q.prompt)}</p><div class="foundation-choices">${q.choices.map((choice,j)=>`<button type="button" class="foundation-choice ${state.foundationAssessmentDrafts[draftKey]?.answers?.[q.id]===j?'is-selected':''}" data-foundation-listening-answer="${j}" data-foundation-listening-lesson="${escapeHtml(lessonId)}" data-foundation-listening-scope="${escapeHtml(scopeId)}" data-foundation-listening-question-id="${escapeHtml(q.id)}">${String.fromCharCode(65+j)}. ${escapeHtml(choice)}</button>`).join('')}</div>${foundationDraftToolbar('foundation-listening',lessonId,clip.questions,scopeId)}<p class="foundation-feedback" data-foundation-listening-feedback ${saved&&!hasDraft?'':'hidden'}>${saved&&!hasDraft?`${saved.latestCorrect?'Đúng ở lượt gần nhất.':'Cần nghe lại và ôn tập.'} · ${saved.attempts?.length||1} lượt.`:''}</p></section>`;
 }).join('');
 return `<section class="detail-section foundation-listening" data-foundation-listening="${escapeHtml(clip.id)}"><h4>${clip.segments?.length?'NGHE HIỂU HỘI THOẠI':'NGHE HIỂU ĐOẠN NGẮN'}${scopeId?' · MỞ RỘNG':''}</h4>${scopeId?'<p class="foundation-reading-review-note">Bài nghe bổ sung đang chờ kiểm duyệt độc lập. Kết quả chỉ dùng để luyện tập riêng, chưa cộng vào kết quả A2 chính thức hoặc kết luận năng lực CEFR.</p>':''}<p class="placement-disclaimer">Nghe bằng voice tiếng Anh trên thiết bị. Hội thoại A2 dùng voice nam/nữ đã cấu hình và nghỉ giữa các lượt theo mục Cấu hình → Giọng đọc. Đây là TTS của trình duyệt, không phải audio thu âm ETS.</p><h3>${escapeHtml(clip.title)}</h3><div class="foundation-listening-actions"><button type="button" class="secondary-button" data-foundation-listening-play="${escapeHtml(clip.id)}">▶ ${clip.segments?.length?'Phát hội thoại':'Phát đoạn nghe'}</button><button type="button" class="text-button" data-foundation-listening-stop>⏹ Dừng</button><button type="button" class="text-button" data-foundation-listening-transcript-toggle>Hiện transcript</button></div><p class="placement-disclaimer" id="${statusId}" aria-live="polite">Sẵn sàng phát · Có thể dừng bất cứ lúc nào.</p><div class="foundation-listening-transcript" data-foundation-listening-transcript hidden><strong>Transcript</strong>${clip.segments?.length?`<div class="foundation-listening-transcript-turns">${clip.segments.map(segment=>`<div><strong>${escapeHtml(segment.speaker)}</strong><p>${escapeHtml(segment.text)}</p></div>`).join('')}</div>`:`<p>${escapeHtml(clip.script)}</p>`}</div>${questions}<p class="placement-disclaimer" data-foundation-listening-summary>${summary.uniqueQuestions}/${clip.questions.length} câu độc lập · ${summary.accuracyPercent===null?'Chưa có kết quả':`${summary.accuracyPercent}% đúng gần nhất`}. Ngưỡng luyện tập: ${summary.minimumUniqueQuestions} câu độc lập và ${Math.round(summary.threshold*100)}% đúng; không phải chứng nhận CEFR.</p></section>`;
}

function openFoundationLesson(id){
 const x=state.foundationLessons.find(item=>item.id===id);if(!x)return;state.activeFoundationLesson=id;
 const openExtensionIds=new Set(Array.from($('#modalContent')?.querySelectorAll('details[data-foundation-extension][open]')||[]).map(item=>item.dataset.foundationExtension));
 const lessonDenominator=x.level==='A2'?13:10;
 const examples=(x.examples||[]).map(e=>`<div class="example-card"><strong>${escapeHtml(e.en)}</strong><span>${escapeHtml(e.vi)}</span></div>`).join('');
 const bank=Array.isArray(x.questionBank)&&x.questionBank.length?x.questionBank:[{id:`${x.id}::q1`,question:x.question,choices:x.choices,answerIndex:x.answerIndex,rationale:x.rationale}];
 const evidence=summarizeFoundationLesson(state.foundationProgress,id);
 const application=x.applicationTask;const applicationSaved=application?state.foundationProgress[id]?.applicationEvidence?.[application.id]:null;const applicationSummary=summarizeFoundationApplication(state.foundationProgress,id);
 const applicationHtml=application?`<section class="detail-section foundation-application" data-foundation-application="${escapeHtml(application.id)}"><h4>VẬN DỤNG TRONG NGỮ CẢNH</h4><p>${escapeHtml(application.focus||'Áp dụng kiến thức vào tình huống thực tế.')}</p><h3>${escapeHtml(application.prompt)}</h3><div class="foundation-choices">${application.choices.map((choice,index)=>`<button type="button" class="foundation-choice ${state.foundationAssessmentDrafts[foundationDraftKey('foundation-application',id)]?.answers?.[application.id]===index?'is-selected':''}" data-foundation-application-answer="${index}" data-foundation-id="${escapeHtml(x.id)}" data-foundation-task-id="${escapeHtml(application.id)}">${String.fromCharCode(65+index)}. ${escapeHtml(choice)}</button>`).join('')}</div>${foundationDraftToolbar('foundation-application',id,[{id:application.id}])}<p class="foundation-feedback" data-foundation-application-feedback ${applicationSaved?'':'hidden'}>${applicationSaved?`${applicationSaved.latestCorrect?'Đạt ở lượt gần nhất.':'Cần luyện thêm.'} ${escapeHtml(application.rationale)} · ${applicationSaved.attempts?.length||1} lượt.`:''}</p><p class="placement-disclaimer" data-foundation-application-summary>${applicationSummary.uniqueTasks} tình huống đã thực hiện · ${applicationSummary.accuracyPercent===null?'Chưa có kết quả':`${applicationSummary.accuracyPercent}% đúng gần nhất`}. Bằng chứng vận dụng được theo dõi riêng, không cộng vào câu hỏi nhận biết.</p></section>`:'';
 const productionTasks=foundationProductionTasks(x);
 const legacyProductionSaved=x.productionTask&&application?state.foundationProgress[id]?.productionEvidence?.[application.id]:null;
 const productionHtml=productionTasks.map((task,index)=>{
   const productionSaved=state.foundationProgress[id]?.productionEvidence?.[task.id]||null;
   const section=renderFoundationProductionSection(x,application,productionSaved,index===0?legacyProductionSaved:null,task,index);
   return index===0?section:`<details class="foundation-production-extension" data-foundation-extension="${escapeHtml(task.id)}"><summary><span><strong>${escapeHtml(task.title||'Thử thách viết mở rộng')}</strong><small>Thử thách bổ sung · tối thiểu ${Math.max(3,Number(task.minimumWords)||3)} từ</small></span><span class="foundation-portfolio-toggle">Mở bài viết</span></summary>${section}</details>`;
 }).join('');
 const dueRecall=listDueFoundationRecallItems(state.foundationProgress,[x]);
 const recallScheduled=bank.filter(q=>Number(state.foundationProgress[id]?.evidence?.[q.id]?.recallDueAt)>0).length;
 const recallHtml=dueRecall.length?`<section class="detail-section foundation-recall"><h4>ÔN TẬP CÁCH QUÃNG · ${dueRecall.length} CÂU ĐẾN HẠN</h4><p>Trả lời lại trước khi xem đáp án. Đúng sẽ lên lịch sau 3 ngày; chưa đúng sẽ được nhắc lại sau 1 ngày.</p>${dueRecall.map(item=>`<article class="foundation-recall-card"><h3>${escapeHtml(item.question)}</h3><div class="foundation-choices">${item.choices.map((choice,index)=>`<button type="button" class="foundation-choice" data-foundation-recall-answer="${index}" data-foundation-recall-lesson="${escapeHtml(id)}" data-foundation-recall-question="${escapeHtml(item.questionId)}">${String.fromCharCode(65+index)}. ${escapeHtml(choice)}</button>`).join('')}</div><small>Đến hạn từ ${new Date(item.dueAt).toLocaleString('vi-VN')}</small></article>`).join('')}</section>`:`<section class="detail-section foundation-recall"><h4>ÔN TẬP CÁCH QUÃNG</h4><p>${recallScheduled?`${recallScheduled} câu đã được lên lịch ôn. Câu đầu tiên sẽ đến hạn sau 24 giờ; sau mỗi lượt ôn, lịch tiếp theo là 1 hoặc 3 ngày tùy kết quả.`:'Sau khi bạn trả lời câu nhận biết, hệ thống sẽ tự lên lịch ôn lại sau 24 giờ.'} ${dueRecall.length?'':'Chưa có câu đến hạn.'}</p></section>`;
 const questions=bank.map((q,i)=>{const saved=state.foundationProgress[id]?.evidence?.[q.id],hasDraft=Number.isInteger(state.foundationAssessmentDrafts[foundationDraftKey('foundation-recognition',id)]?.answers?.[q.id]);return `<section class="foundation-question" data-foundation-question="${escapeHtml(x.id)}" data-foundation-question-id="${escapeHtml(q.id)}"><h3>Tự kiểm tra ${i+1}/${bank.length}</h3><p>${escapeHtml(q.question)}</p><div class="foundation-choices">${q.choices.map((c,j)=>`<button type="button" class="foundation-choice ${state.foundationAssessmentDrafts[foundationDraftKey('foundation-recognition',id)]?.answers?.[q.id]===j?'is-selected':''}" data-foundation-answer="${j}" data-foundation-id="${escapeHtml(x.id)}" data-foundation-question-id="${escapeHtml(q.id)}">${String.fromCharCode(65+j)}. ${escapeHtml(c)}</button>`).join('')}</div>${foundationDraftToolbar('foundation-recognition',id,bank)}<p class="foundation-feedback" data-foundation-feedback ${saved&&!hasDraft?'':'hidden'}>${saved&&!hasDraft?`${saved.latestCorrect?'Đã trả lời đúng gần nhất.':'Cần ôn lại.'} · ${saved.attempts?.length||1} lượt.`:''}</p></section>`}).join('');
 const readingPassage=state.foundationReadingPassages.find(item=>item.lessonId===id);const readingHtml=readingPassage?renderFoundationReadingPanel(readingPassage,id):'';
 const extendedReadingPassage=state.foundationReadingExtendedPassages.find(item=>item.lessonId===id);const extendedReadingSummary=extendedReadingPassage?summarizeFoundationReading(state.foundationReadingProgress,`${id}::reading2`,{minimumUniqueQuestions:extendedReadingPassage.minimumUniqueQuestions||3,practiceAccuracyThreshold:extendedReadingPassage.practiceAccuracyThreshold||0.67}):null;const extendedReadingHtml=extendedReadingPassage?`<details class="foundation-reading-extension" data-foundation-extension="reading2"><summary><span><strong>Đọc hiểu mở rộng · ${escapeHtml(extendedReadingPassage.format||'Bài đọc')}</strong><small>${extendedReadingSummary.uniqueQuestions}/${extendedReadingPassage.questions.length} câu đã có bằng chứng · khoảng ${extendedReadingPassage.text.trim().split(/\s+/).length} từ</small></span><span class="foundation-portfolio-toggle">Mở bài đọc</span></summary><p class="foundation-reading-review-note">Nội dung bổ sung đang chờ kiểm duyệt độc lập. Tiến độ ở đây chỉ dùng để luyện tập riêng, chưa cộng vào kết quả A2 chính thức hoặc kết luận năng lực CEFR.</p>${renderFoundationReadingPanel(extendedReadingPassage,id,'reading2')}</details>`:'';
 const listeningClip=state.foundationListeningClips.find(item=>item.lessonId===id&&!item.supplementary);const extendedListeningClip=state.foundationListeningClips.find(item=>item.lessonId===id&&item.supplementary&&item.evidenceScope==='listening2');const listeningHtml=listeningClip?renderFoundationListeningPanel(listeningClip,id):'';const extendedListeningSummary=extendedListeningClip?summarizeFoundationListening(state.foundationListeningProgress,`${id}::listening2`,{minimumUniqueQuestions:extendedListeningClip.minimumUniqueQuestions||3,practiceAccuracyThreshold:extendedListeningClip.practiceAccuracyThreshold||0.67}):null;const extendedListeningHtml=extendedListeningClip?`<details class="foundation-reading-extension foundation-listening-extension" data-foundation-extension="listening2"><summary><span><strong>Nghe hiểu mở rộng · ${escapeHtml(extendedListeningClip.format||'Tình huống nghe')}</strong><small>${extendedListeningSummary.uniqueQuestions}/${extendedListeningClip.questions.length} câu đã có bằng chứng · 6 lượt thoại · ${escapeHtml(extendedListeningClip.title)}</small></span><span class="foundation-portfolio-toggle">Mở bài nghe</span></summary>${renderFoundationListeningPanel(extendedListeningClip,id,'listening2')}</details>`:'';
 const alphabetHtml=id==='pa1-alphabet'?renderAlphabetSoundLab():'';
 const content=`<p class="foundation-level detail-pill">${escapeHtml(x.level)} · MỤC TIÊU ${x.order}/${lessonDenominator}</p>${alphabetHtml}<section class="detail-section"><h4>SAU BÀI NÀY, BẠN CÓ THỂ</h4><p>${escapeHtml(x.objective)}</p></section><section class="detail-section"><h4>GIẢI THÍCH</h4><p>${escapeHtml(x.explanation)}</p><div class="foundation-focus">${escapeHtml(x.focus)}</div></section><section class="detail-section"><h4>VÍ DỤ SONG NGỮ</h4>${examples}</section><section class="detail-section"><h4>MẸO GHI NHỚ</h4><p>${escapeHtml(x.tip)}</p></section><section class="detail-section"><h4>BẰNG CHỨNG LUYỆN TẬP</h4><p data-foundation-evidence-summary>${evidence.uniqueQuestions}/3 câu độc lập · ${evidence.accuracyPercent===null?'Chưa có kết quả':`${evidence.accuracyPercent}% đúng gần nhất`}. Cần ít nhất 3 câu độc lập và 80% đúng để đạt ngưỡng luyện tập. Đây không phải chứng nhận CEFR.</p></section>${questions}${recallHtml}${applicationHtml}${productionHtml}${readingHtml}${extendedReadingHtml}${listeningHtml}${extendedListeningHtml}<p class="placement-disclaimer">Câu hỏi tự kiểm tra đo nhận biết/hiểu; tình huống vận dụng, đọc hiểu, nghe hiểu và lượt luyện tên chữ/từ mẫu được theo dõi riêng. TTS không đánh giá độ chính xác phát âm; bài học chưa đánh giá nói/viết tự do hoặc giao tiếp tự nhiên.</p>`;
 openLearningDetail({kind:'learning-detail',title:x.title,subtitle:'Học theo từng bước · nghe, đọc, xem ví dụ, vận dụng và tự kiểm tra.',eyebrow:'FOUNDATION PATH · '+x.level,content});
 for(const detail of Array.from($('#modalContent')?.querySelectorAll('details[data-foundation-extension]')||[])){if(openExtensionIds.has(detail.dataset.foundationExtension))detail.open=true;}
 const candidates=[['foundation-recognition',bank,''],...(application? [['foundation-application',[{...application,id:application.id}], '']]:[]),...(readingPassage?[['foundation-reading',readingPassage.questions,'']]:[]),...(extendedReadingPassage?[['foundation-reading',extendedReadingPassage.questions,'reading2']]:[]),...(listeningClip?[['foundation-listening',listeningClip.questions,'']]:[]),...(extendedListeningClip?[['foundation-listening',extendedListeningClip.questions,'listening2']]:[])];
 for(const [kind,items,scopeId] of candidates){if(showFoundationAssessmentResult(kind,id,items,scopeId))break;}
}

async function playFoundationListening(clipId){
 const clip=state.foundationListeningClips.find(item=>item.id===clipId);if(!clip)return;
 if(!('speechSynthesis'in window)||typeof SpeechSynthesisUtterance==='undefined'){toast('Thiết bị chưa hỗ trợ đọc đoạn nghe. Hãy dùng Cấu hình để kiểm tra giọng đọc.','error');return;}
 const cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})};
 const segments=Array.isArray(clip.segments)&&clip.segments.length?clip.segments:String(clip.script||'').match(/[^.!?]+[.!?]+|[^.!?]+$/g)?.map((text,index)=>({speaker:'Narrator',voice:cfg.defaultGender,text:text.trim(),accent:cfg.accent}))||[];
 if(!segments.length){toast('Bài nghe chưa có nội dung để phát.','error');return;}
 stopSpeech();const playbackToken=++listeningPlaybackToken;const status=$(`[id="foundationListeningStatus-${String(clipId).replace(/[^a-zA-Z0-9_-]/g,'-')}"]`);
 if(status)status.textContent='Đang khởi động giọng đọc…';
 if(!prepareSpeechEngine(playbackToken)||playbackToken!==listeningPlaybackToken)return;
 const speakerVoices=new Map();const usedVoiceNames={female:[],male:[]};
 const resolveVoice=segment=>{
   const speaker=String(segment.speaker||'Narrator').trim(),key=speaker.toLowerCase();
   if(speakerVoices.has(key))return speakerVoices.get(key);
   const gender=classifyVoiceHint(segment.voice||speaker)||cfg.defaultGender;
   const voice=chooseEnglishVoice(segment.accent||cfg.accent,speaker,gender,usedVoiceNames[gender]||[]);
   if(voice){speakerVoices.set(key,voice);(usedVoiceNames[gender]||[]).push(voice.name);}
   return voice;
 };
 for(let index=0;index<segments.length;index++){
   if(playbackToken!==listeningPlaybackToken)return;
   const segment=segments[index],speaker=segment.speaker||`Lượt lời ${index+1}`;
   const gender=classifyVoiceHint(segment.voice||speaker)||cfg.defaultGender;
   const voice=resolveVoice(segment);
   if(status)status.textContent=`Đang nghe ${speaker} (${index+1}/${segments.length})…`;
   const played=await speakUtterance(segment.text,{accent:segment.accent||cfg.accent,gender,voice,rate:cfg.rate,onStart:()=>{if(status)status.textContent=`${speaker} đang nói…`; }},playbackToken);
   if(playbackToken!==listeningPlaybackToken)return;
   if(!played){if(status)status.textContent=speechFailureMessage();toast(speechFailureMessage(),'error');return;}
   if(index<segments.length-1){
     const gap=Math.max(500,Number(cfg.sentencePauseMs)||850);
     if(status)status.textContent=`Đã hết lượt ${speaker} · nghỉ ${(gap/1000).toFixed(2)} giây…`;
     if(!await waitSpeechGap(gap,playbackToken))return;
   }
 }
 if(playbackToken===listeningPlaybackToken&&status)status.textContent='Đã phát xong. Bạn có thể nghe lại hoặc mở transcript.';
}

function answerFoundationListening(button){
 const lessonId=button.dataset.foundationListeningLesson,scopeId=button.dataset.foundationListeningScope||'',questionId=button.dataset.foundationListeningQuestionId,index=Number(button.dataset.foundationListeningAnswer);
 const clip=state.foundationListeningClips.find(item=>item.lessonId===lessonId&&(scopeId==='listening2'?item.evidenceScope==='listening2':!item.supplementary));if(!clip)return;
 stageFoundationAssessment('foundation-listening',lessonId,questionId,index,clip.questions||[],scopeId);
}

function answerFoundationReading(button){
 const lessonId=button.dataset.foundationReadingLesson,questionId=button.dataset.foundationReadingQuestionId,index=Number(button.dataset.foundationReadingAnswer),scopeId=button.dataset.foundationReadingScope||'';
 const source=scopeId==='reading2'?state.foundationReadingExtendedPassages:state.foundationReadingPassages;
 const passage=source.find(item=>item.lessonId===lessonId);if(!passage)return;
 stageFoundationAssessment('foundation-reading',lessonId,questionId,index,passage.questions||[],scopeId);
}

function answerFoundationRecall(button){
 const lessonId=button.dataset.foundationRecallLesson,questionId=button.dataset.foundationRecallQuestion,index=Number(button.dataset.foundationRecallAnswer);
 const lesson=state.foundationLessons.find(item=>item.id===lessonId),question=lesson?.questionBank?.find(item=>item.id===questionId);if(!lesson||!question||!Number.isInteger(index))return;
 const saved=state.foundationProgress?.[lessonId]?.evidence?.[questionId],dueAt=Number(saved?.recallDueAt)||0;
 if(!dueAt||Date.now()<dueAt){toast('Câu hỏi chưa đến thời điểm ôn tập cách quãng.','error');return;}
 const correct=index===Number(question.answerIndex);
 const next=recordFoundationRecallAttempt(state.foundationProgress,lessonId,questionId,correct,Date.now());
 if(next===state.foundationProgress){toast('Không thể ghi nhận lượt ôn tập. Hãy thử mở lại bài học.','error');return;}
 state.foundationProgress=next;
 try{localStorage.setItem('toeic:foundation-progress:v1',JSON.stringify(state.foundationProgress));}catch(error){console.warn('Không thể lưu lượt ôn Foundation:',error);}
 openFoundationLesson(lessonId);renderFoundationPath();toast(correct?`Đúng. Đã hẹn ôn lại sau 3 ngày. ${question.rationale||''}`:`Chưa đúng. Đã hẹn ôn lại sau 1 ngày. ${question.rationale||''}`,correct?'success':'error');
}

function findFoundationProductionTask(lesson,taskId){
 return foundationProductionTasks(lesson).find(task=>String(task.id)===String(taskId))||null;
}

function saveFoundationProduction(button){
 const lessonId=button.dataset.foundationId,taskId=button.dataset.foundationTaskId,lesson=state.foundationLessons.find(item=>item.id===lessonId);
 const task=findFoundationProductionTask(lesson,taskId);if(!lesson?.applicationTask||!task)return;
 const panel=button.closest('[data-foundation-production]'),response=$('[data-foundation-production-text]',panel)?.value||'';
 const minimumWords=Math.max(3,Number(task.minimumWords)||3),fieldKey=foundationProductionFieldKey(lessonId,taskId);
 const ratings=[0,1,2].map(index=>{const selected=$(`input[name="${fieldKey}-self-${index}"]:checked`,panel);return selected?selected.value==='yes':null;});
 if(response.trim().split(/\s+/).filter(Boolean).length<minimumWords){toast(`Hãy viết câu trả lời có ít nhất ${minimumWords} từ theo tình huống.`,'error');return;}
 if(ratings.some(value=>value===null)){toast('Hãy tự đánh giá đủ 3 tiêu chí trước khi lưu.','error');return;}
 const nextProgress=recordFoundationProductionAttempt(state.foundationProgress,lessonId,taskId,response,ratings,Date.now(),minimumWords);
 try{localStorage.setItem('toeic:foundation-progress:v1',JSON.stringify(nextProgress));state.foundationProgress=nextProgress;}catch(error){console.warn('Không thể lưu tự đánh giá Foundation:',error);toast('Không thể lưu bằng chứng trên thiết bị này.','error');return;}
 openFoundationLesson(lessonId);renderFoundationPath();const saved=state.foundationProgress[lessonId]?.productionEvidence?.[taskId];toast(`Đã lưu câu tự tạo và tự đánh giá ${saved?.latestScore||0}/3. Không có chấm điểm tự động.`);
}

function saveFoundationProductionRevision(button){
 const lessonId=button.dataset.foundationId,taskId=button.dataset.foundationTaskId,lesson=state.foundationLessons.find(item=>item.id===lessonId);
 const task=findFoundationProductionTask(lesson,taskId);if(!lesson?.applicationTask||!task)return;
 const panel=button.closest('[data-foundation-production]'),response=$('[data-foundation-revision-text]',panel)?.value||'';
 const minimumWords=Math.max(3,Number(task.minimumWords)||8),fieldKey=foundationProductionFieldKey(lessonId,taskId);
 const reviewChecks=$$('[data-foundation-revision-check]',panel).map(field=>field.checked);
 const ratings=[0,1,2].map(index=>{const selected=$(`input[name="${fieldKey}-revision-${index}"]:checked`,panel);return selected?selected.value==='yes':null;});
 if(response.trim().split(/\s+/).filter(Boolean).length<minimumWords){toast(`Hãy viết lại câu trả lời có ít nhất ${minimumWords} từ.`,'error');return;}
 if(reviewChecks.length!==3||reviewChecks.some(value=>!value)){toast('Hãy xác nhận đã rà soát đủ 3 yêu cầu trước khi lưu bản viết lại.','error');return;}
 if(ratings.some(value=>value===null)){toast('Hãy tự đánh giá đủ 3 tiêu chí cho bản viết lại.','error');return;}
 const nextProgress=recordFoundationProductionRevision(state.foundationProgress,lessonId,taskId,response,ratings,reviewChecks,Date.now(),minimumWords);
 if(nextProgress===state.foundationProgress){toast('Bản viết lại cần khác bản trước và có đủ dữ liệu kiểm tra.','error');return;}
 try{localStorage.setItem('toeic:foundation-progress:v1',JSON.stringify(nextProgress));state.foundationProgress=nextProgress;}catch(error){console.warn('Không thể lưu bản viết lại Foundation:',error);toast('Không thể lưu bản viết lại trên thiết bị này.','error');return;}
 openFoundationLesson(lessonId);renderFoundationPath();const saved=state.foundationProgress[lessonId]?.productionEvidence?.[taskId];toast(`Đã lưu bản viết lại lần ${saved?.revisionCount||1} cùng lịch sử đối chiếu. Không có chấm điểm tự động.`);
}

function answerFoundationApplication(button){
 const lessonId=button.dataset.foundationId,taskId=button.dataset.foundationTaskId,index=Number(button.dataset.foundationApplicationAnswer);
 const task=state.foundationLessons.find(item=>item.id===lessonId)?.applicationTask;if(!task||task.id!==taskId)return;
 stageFoundationAssessment('foundation-application',lessonId,taskId,index,[{...task,id:task.id}]);
}

function answerFoundationQuestion(button){
 const id=button.dataset.foundationId,questionId=button.dataset.foundationQuestionId,index=Number(button.dataset.foundationAnswer),lesson=state.foundationLessons.find(item=>item.id===id);if(!lesson||!questionId)return;
 const bank=Array.isArray(lesson.questionBank)&&lesson.questionBank.length?lesson.questionBank:[{id:`${lesson.id}::q1`,question:lesson.question,choices:lesson.choices,answerIndex:lesson.answerIndex,rationale:lesson.rationale}];
 stageFoundationAssessment('foundation-recognition',id,questionId,index,bank);
}


function renderGrammarLibrary(){
  const q=normalizeText($('#grammarSearch').value), category=$('#grammarCategoryFilter').value, level=$('#grammarLevelFilter').value, part=$('#grammarPartFilter')?.value||'';
  const list=state.grammarLessons.filter(item=>{
    if(category&&item.category!==category)return false;
    if(level&&item.level!==level)return false;
    const parts=Array.isArray(item.parts)?item.parts:(item.partFocus?[item.partFocus]:[]);
    if(part&&!parts.includes(part))return false;
    return !q||normalizeText([item.title,item.category,item.summary,item.formula,item.explanation,parts.join(' ')].join(' ')).includes(q);
  });
  $('#grammarCount').textContent=`${list.length} / ${state.grammarLessons.length} bài học`;
  $('#grammarCardList').innerHTML=list.map(item=>{
    const progress=ensurePracticeProgress(state.grammarProgress[item.id]||{});
    const done=countAttemptedPracticeQuestions(progress,(item.exercises||[]).length);
    const partLabel=(item.parts|| (item.partFocus?[item.partFocus]:[])).join(' · ');
    return `<article class="learning-card"><div class="learning-card-top"><span class="learning-category">${escapeHtml(item.category)}${partLabel?` · ${escapeHtml(partLabel)}`:''}</span><span class="learning-level">${escapeHtml(item.level)}</span></div><h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(item.summary)}</p><div class="learning-formula">${escapeHtml(item.formula)}</div><div class="learning-card-footer"><small>${done}/${(item.exercises||[]).length} câu đã làm</small><button class="secondary-button" data-grammar-open="${escapeHtml(item.id)}">Học bài <span>→</span></button></div></article>`;
  }).join('');
  $('#grammarEmpty').hidden=list.length>0;
}
function openGrammarLesson(id){
  const lesson=state.grammarLessons.find(x=>x.id===id);if(!lesson)return;
  state.activeGrammarLesson=id;
  const examples=(lesson.examples||[]).map(ex=>`<article class="lesson-example"><strong>${escapeHtml(ex.en)}</strong><span>${escapeHtml(ex.vi)}</span>${(ex.breakdown||[]).length?`<div class="sentence-breakdown">${ex.breakdown.map(part=>`<div><small>${escapeHtml(part.part)}</small><b>${escapeHtml(part.text)}</b><span>${escapeHtml(part.meaning)}</span></div>`).join('')}</div>`:''}</article>`).join('');
  const tips=(lesson.tips||[]).map(t=>`<li>${escapeHtml(t)}</li>`).join('');
  const prog=ensurePracticeProgress(state.grammarProgress[id]||{});
  const exercises=(lesson.exercises||[]).map((ex,i)=>{
    const saved=prog.answers?.[i],draftChoice=getPracticeDraftChoice(prog,i),history=getPracticeAttemptHistory(prog,i);
    const attemptLabel=history.length&&!saved?` · LÀM LẠI LẦN ${history.length+1}`:'';
    const feedback=saved?.answered?`<p class="exercise-feedback visible">${escapeHtml(`${saved.correct?'Chính xác.':'Chưa chính xác.'} ${ex.explanation}`)}</p>${practiceRetryActionMarkup('grammar',id,i,prog,saved)}`:`<p class="exercise-feedback" hidden></p>${history.length?`<small class="practice-retry-hint">Đã lưu ${history.length} lần trước. Bạn đang làm lại câu này.</small>${practiceAttemptHistoryMarkup(prog,i)}`:''}`;
    return `<article class="lesson-exercise" data-started-at="${Date.now()}" data-grammar-exercise="${i}"><div class="exercise-kicker">BÀI TẬP ${i+1}${attemptLabel}</div><h4>${escapeHtml(ex.question)}</h4><div class="exercise-choice-grid">${ex.choices.map((choice,j)=>`<button type="button" class="exercise-choice ${saved?.answered&&j===ex.answerIndex?'is-correct':''} ${saved?.answered&&saved.choiceIndex===j&&j!==ex.answerIndex?'is-wrong':''} ${!saved?.answered&&draftChoice===j?'is-selected':''}" data-grammar-choice data-lesson-id="${escapeHtml(id)}" data-exercise-index="${i}" data-choice-index="${j}" data-choice-id="${escapeHtml(choiceIdAt(ex,j))}" ${saved?.answered?'disabled':''}><span>${String.fromCharCode(65+j)}</span>${escapeHtml(choice)}</button>`).join('')}</div>${feedback}</article>`;
  }).join('');
  const retryToolbar=practiceRetryAllToolbar('grammar',id,prog,lesson.exercises||[])+practiceDraftToolbar('grammar',id,prog,lesson.exercises||[]);
  const content=`<div class="lesson-intro"><p>${escapeHtml(lesson.summary)}</p><div class="lesson-formula">${escapeHtml(lesson.formula)}</div></div><section class="detail-section"><h4>GIẢI THÍCH</h4><p class="lesson-explanation">${escapeHtml(lesson.explanation)}</p></section><section class="detail-section"><h4>VÍ DỤ VÀ PHÂN TÍCH</h4>${examples}</section><section class="detail-section"><h4>MẸO GHI NHỚ</h4><ul class="lesson-tips">${tips}</ul></section><section class="detail-section"><h4>LUYỆN TẬP</h4>${retryToolbar}<div class="lesson-exercises">${exercises}</div></section><div class="modal-actions"><button class="primary-button" data-ai-lesson="${escapeHtml(id)}">${icon('sparkles','ui-icon button-icon')} Tra cứu Google AI</button></div>`;
  openLearningDetail({title:lesson.title,subtitle:lesson.summary,eyebrow:`GRAMMAR · ${(lesson.parts||[]).join(' / ')} · ${lesson.category} · ${lesson.level}`,content});
  maybeShowPracticeBatchResult('grammar',id);
}
function trackObjectivePractice(resourceId, question, correct, answeredAt = Date.now(), durationMs = null) {
  if (!resourceId || !question) return;
  const objectiveIds = state.objectiveResourceIndex?.[resourceId] || [];
  if (!objectiveIds.length) return;
  const stableChoiceIds = Array.isArray(question.choiceIds) ? question.choiceIds.join('|') : '';
  const itemId = question.id || `${resourceId}::index:${question.__index ?? 'unknown'}::${stableChoiceIds}`;
  state.objectiveProgress = recordObjectiveAttempt(state.objectiveProgress, objectiveIds, itemId, correct, answeredAt, durationMs);
}
async function saveObjectivePractice() {
  state.objectiveProgress = ensureObjectiveProgress(state.objectiveProgress);
  await dbSet('objectiveProgress', state.objectiveProgress);
  renderLearningObjectiveProgress();
}

const ASSESSMENT_DRAFT_STORAGE_KEY = 'toeic:foundation-assessment-drafts:v1';
function assessmentConfettiMarkup(){
  return `<div class="assessment-result-confetti" aria-hidden="true">${Array.from({length:22},(_,i)=>`<i style="--confetti-index:${i};--confetti-x:${(i*37)%100}%;--confetti-delay:${(i%7)*.08}s;--confetti-rotation:${(i*41)%360}deg"></i>`).join('')}</div>`;
}
function assessmentResultBodyMarkup({correct=0,incorrect=0,total=0,description='Bạn đã trả lời hết câu hỏi trong lượt này.'}={}){
  return `${assessmentConfettiMarkup()}<p>${escapeHtml(description)}</p><div class="assessment-result-stats"><article><strong>${correct}</strong><span>Đúng</span></article><article><strong>${incorrect}</strong><span>Chưa đúng</span></article><article><strong>${total}</strong><span>Tổng câu</span></article></div><p class="assessment-result-note">Đáp án và phần giải thích chỉ mở sau khi bạn xác nhận.</p><div class="assessment-result-actions"><button type="button" class="primary-button" data-assessment-confirm>Xác nhận &amp; xem đáp án</button></div>`;
}
function showAssessmentResultInLearningFocus({eyebrow,title,bodyMarkup}={}){
  const backdrop=$('#learningFocusBackdrop'),dialog=$('#learningFocusDialog'),host=$('#learningFocusContent'),close=$('#learningFocusClose');
  if(!learningFocusState.active||!backdrop||backdrop.hidden||!dialog||!host)return false;
  hideModalLayer();
  if(!assessmentResultFocusState){
    const titleNode=$('#learningFocusTitle'),subtitleNode=$('#learningFocusSubtitle'),eyebrowNode=$('#learningFocusEyebrow');
    assessmentResultFocusState={
      header:{title:titleNode?.textContent||'Không gian học tập',subtitle:subtitleNode?.textContent||'Tập trung vào nội dung đang học.',eyebrow:eyebrowNode?.textContent||'FOCUSED LEARNING'},
      close:{ariaLabel:close?.getAttribute('aria-label'),title:close?.getAttribute('title')},
      children:[...host.children].map(node=>({node,hidden:node.hidden,inert:node.inert,ariaHidden:node.getAttribute('aria-hidden')})),
      panel:null,
    };
    for(const entry of assessmentResultFocusState.children){entry.node.hidden=true;entry.node.inert=true;entry.node.setAttribute('aria-hidden','true');}
  }else assessmentResultFocusState.panel?.remove();
  const panel=document.createElement('section');
  panel.className='assessment-result-modal assessment-result-inline';
  panel.innerHTML=bodyMarkup;
  host.append(panel);
  assessmentResultFocusState.panel=panel;
  setLearningFocusHeader(title,'Kết quả đã sẵn sàng. Xác nhận để xem đáp án và phần giải thích.',eyebrow);
  close?.setAttribute('aria-label','Xác nhận kết quả');
  close?.removeAttribute('title');
  dialog.setAttribute('aria-hidden','false');
  host.scrollTop=0;
  panel.querySelector('[data-assessment-confirm]')?.focus();
  return true;
}
function restoreAssessmentResultLearningFocus(){
  const snapshot=assessmentResultFocusState;if(!snapshot)return false;
  snapshot.panel?.remove();
  for(const entry of snapshot.children){
    entry.node.hidden=entry.hidden;
    entry.node.inert=entry.inert;
    if(entry.ariaHidden===null)entry.node.removeAttribute('aria-hidden');
    else entry.node.setAttribute('aria-hidden',entry.ariaHidden);
  }
  setLearningFocusHeader(snapshot.header.title,snapshot.header.subtitle,snapshot.header.eyebrow);
  const close=$('#learningFocusClose');
  if(close){
    if(snapshot.close.ariaLabel===null)close.removeAttribute('aria-label');else close.setAttribute('aria-label',snapshot.close.ariaLabel);
    if(snapshot.close.title===null)close.removeAttribute('title');else close.setAttribute('title',snapshot.close.title);
  }
  assessmentResultFocusState=null;
  return true;
}
function showAssessmentResultModal({eyebrow='SESSION COMPLETE',title='Bạn đã hoàn thành',correct=0,incorrect=0,total=0,description='Bạn đã trả lời hết câu hỏi trong lượt này.'}={}){
  const bodyMarkup=assessmentResultBodyMarkup({correct,incorrect,total,description});
  if(showAssessmentResultInLearningFocus({eyebrow,title,bodyMarkup}))return;
  $('#modalEyebrow').textContent=eyebrow;
  $('#modalTitle').textContent=title;
  $('#modalLayer').classList.remove('is-practice-review','is-auto-advance-wait','is-learning-detail');
  $('#closeModal').hidden=false;
  $('#modalLayer').dataset.modalType='assessment-result';
  $('#modalContent').innerHTML=`<section class="assessment-result-modal">${bodyMarkup}</section>`;
  showModalLayer();
  $('#closeModal').focus();
}
function closeAssessmentResultModal(){
  if(restoreAssessmentResultLearningFocus())return;
  resetModalLayer();
}
function getPracticeBatch(kind,id){
  const config={
    grammar:{items:state.grammarLessons,store:state.grammarProgress,key:'grammarProgress',questionsKey:'exercises',render:openGrammarLesson},
    reading:{items:state.readings,store:state.readingProgress,key:'readingProgress',questionsKey:'questions',render:openReadingDetail},
    listening:{items:state.listening,store:state.listeningProgress,key:'listeningProgress',questionsKey:'questions',render:openListeningDetail},
  }[kind];
  const item=config?.items.find(row=>row.id===id);if(!item)return null;
  const questions=item[config.questionsKey]||[];
  const progress=ensurePracticeProgress(config.store[id]||{});
  config.store[id]=progress;
  return {...config,kind,id,item,questions,progress};
}
function practiceDraftToolbar(kind,id,progress,questions){
  const drafts=getPracticeDraftEntries(progress).filter(entry=>entry.index<questions.length);
  if(!drafts.length)return '';
  const complete=isPracticeDraftSetComplete(progress,questions.length);
  return `<div class="assessment-draft-toolbar"><span>Đã chọn tạm ${drafts.length}/${questions.length} câu · chưa hiển thị đúng/sai</span>${complete?`<button type="button" class="secondary-button" data-practice-batch-result="${kind}" data-resource-id="${escapeHtml(id)}">Xem bảng hoàn thành</button>`:''}</div>`;
}
function refreshPracticeDetail(kind,id){
  const host=$('#learningFocusContent'),previousScroll=host?.scrollTop||0;
  const config={grammar:openGrammarLesson,reading:openReadingDetail,listening:openListeningDetail}[kind];
  config?.(id);requestAnimationFrame(()=>{if(host)host.scrollTop=previousScroll;});
  ({grammar:renderGrammarLibrary,reading:renderReadingLibrary,listening:renderListeningLibrary}[kind])?.();
}
function maybeShowPracticeBatchResult(kind,id){
  const batch=getPracticeBatch(kind,id);if(!batch||!isPracticeDraftSetComplete(batch.progress,batch.questions.length))return false;
  const summary=summarizePracticeDraftSet(batch.progress,batch.questions);if(!summary.answered)return false;
  state.pendingPracticeBatch={kind,id};
  showAssessmentResultModal({eyebrow:`${kind.toUpperCase()} · SESSION COMPLETE`,title:'Bạn đã hoàn thành lượt học',correct:summary.correct,incorrect:summary.incorrect,total:summary.total,description:'Tất cả câu hỏi trong lượt này đã được chọn. Kết quả được giữ kín cho đến khi bạn xác nhận.'});
  return true;
}
async function stagePracticeBatchAnswer(kind,id,index,choiceIndex,button){
  const batch=getPracticeBatch(kind,id),question=batch?.questions[index];
  if(!batch||!question||!Number.isInteger(choiceIndex)||choiceIndex<0||choiceIndex>=question.choices.length||batch.progress.answers[String(index)]?.answered)return;
  const now=Date.now();const startedAt=Number(button?.closest?.('[data-started-at]')?.dataset.startedAt)||now;
  if(!stagePracticeChoice(batch.progress,index,choiceIndex,now,startedAt))return;
  batch.store[id]=batch.progress;await dbSet(batch.key,batch.store);
  refreshPracticeDetail(kind,id);
  maybeShowPracticeBatchResult(kind,id);
}
async function confirmPracticeBatchResult(){
  const pending=state.pendingPracticeBatch;if(!pending)return;
  const batch=getPracticeBatch(pending.kind,pending.id);if(!batch)return;
  const result=commitPracticeDraftSet(batch.progress,batch.questions,({question,index,choiceIndex,correct,draft})=>({
    choiceIndex,choiceId:choiceIdAt(question,choiceIndex),choiceText:question.choices[choiceIndex],
    correctChoiceText:question.choices[question.answerIndex],explanation:question.explanation,correct,
    answeredAt:Number(draft.answeredAt)||Date.now(),
  }));
  if(!result.complete){toast('Chưa đủ lựa chọn. Hãy hoàn thành tất cả câu trước khi xem đáp án.','error');return;}
  for(const row of result.records){const question=batch.questions[row.index];if(batch.kind==='listening'&&batch.item.editorialStatus==='reserve-pending-independent-review')continue;trackObjectivePractice(batch.id,{...question,__index:row.index},row.correct,row.answeredAt,Math.max(0,row.answeredAt-row.startedAt));}
  batch.store[batch.id]=batch.progress;await dbSet(batch.key,batch.store);await saveObjectivePractice();
  state.pendingPracticeBatch=null;closeAssessmentResultModal();batch.render(batch.id);renderToeicPartInsights();
  const correct=result.records.filter(row=>row.correct).length,accuracy=Math.round(correct/Math.max(1,result.records.length)*100);
  toast(`Đã chấm ${result.committed} câu. Đáp án và giải thích đã mở.`);
}
function saveFoundationAssessmentDrafts(){try{localStorage.setItem(ASSESSMENT_DRAFT_STORAGE_KEY,JSON.stringify(state.foundationAssessmentDrafts||{}));}catch(error){console.warn('Không lưu được lựa chọn Foundation tạm:',error);toast('Không thể lưu lựa chọn tạm trên thiết bị này.','error');}}
function foundationDraftToolbar(kind,lessonId,questions,scopeId=''){
 const key=foundationDraftKey(kind,lessonId,scopeId),answers=state.foundationAssessmentDrafts[key]?.answers||{};const count=(questions||[]).filter(q=>Number.isInteger(answers[q.id])).length;if(!count)return '';
 const complete=count===(questions||[]).length;
 return `<div class="assessment-draft-toolbar"><span>Đã chọn tạm ${count}/${questions.length} câu · kết quả chưa được chấm</span>${complete?`<button type="button" class="secondary-button" data-foundation-batch-result="${kind}" data-lesson-id="${escapeHtml(lessonId)}" data-foundation-scope="${escapeHtml(scopeId)}">Xem bảng hoàn thành</button>`:''}</div>`;
}
function foundationDraftKey(kind,lessonId,scopeId=''){return `${kind}::${lessonId}${scopeId?`::${scopeId}`:''}`;}
function showFoundationAssessmentResult(kind,lessonId,questions,scopeId=''){
  const key=foundationDraftKey(kind,lessonId,scopeId),draft=state.foundationAssessmentDrafts[key]?.answers||{};
  const answered=(questions||[]).filter(q=>Number.isInteger(draft[q.id]));if(!answered.length||answered.length!==(questions||[]).length)return false;
  const correct=answered.filter(q=>draft[q.id]===Number(q.answerIndex)).length;
  state.pendingFoundationAssessment={kind,lessonId,questions,key,scopeId};
  showAssessmentResultModal({eyebrow:`FOUNDATION · ${kind.toUpperCase()}`,title:'Bạn đã hoàn thành phần luyện tập',correct,incorrect:answered.length-correct,total:answered.length,description:'Bạn đã trả lời hết câu hỏi trong phần này. Hãy xác nhận để lưu kết quả và mở phần giải thích.'});return true;
}
function stageFoundationAssessment(kind,lessonId,questionId,choiceIndex,questions,scopeId=''){
  if(!Array.isArray(questions)||!questions.length)return;
  const question=questions.find(q=>q.id===questionId);if(!question||!Number.isInteger(choiceIndex)||choiceIndex<0||choiceIndex>=question.choices.length)return;
  const key=foundationDraftKey(kind,lessonId,scopeId);const entry=state.foundationAssessmentDrafts[key]||{answers:{},startedAt:Date.now()};
  entry.answers=entry.answers||{};entry.answers[questionId]=choiceIndex;entry.answeredAt=entry.answeredAt||{};entry.answeredAt[questionId]=Date.now();state.foundationAssessmentDrafts[key]=entry;saveFoundationAssessmentDrafts();
  openFoundationLesson(lessonId);showFoundationAssessmentResult(kind,lessonId,questions,scopeId);
}
function confirmFoundationAssessmentResult(){
  const pending=state.pendingFoundationAssessment;if(!pending)return;
  const {kind,lessonId,questions,key,scopeId=''}=pending,draft=state.foundationAssessmentDrafts[key]?.answers||{};
  if(!questions.every(q=>Number.isInteger(draft[q.id]))){toast('Chưa hoàn thành tất cả câu hỏi.','error');return;}
  const isListening=kind==='foundation-listening',isReading=kind==='foundation-reading';
  const isFoundation=kind==='foundation-recognition'||kind==='foundation-application';
  if(!isListening&&!isReading&&!isFoundation)throw new Error(`Foundation assessment type không hợp lệ: ${kind}`);
  const progressKey=isListening?'foundationListeningProgress':isReading?'foundationReadingProgress':'foundationProgress';
  const storageKey=isListening?'toeic:foundation-listening-progress:v1':isReading?'toeic:foundation-reading-progress:v1':'toeic:foundation-progress:v1';
  const progressId=scopeId?`${lessonId}::${scopeId}`:lessonId;
  let nextProgress=state[progressKey];
  for(const q of questions){
    const correct=draft[q.id]===Number(q.answerIndex),at=Number(state.foundationAssessmentDrafts[key]?.answeredAt?.[q.id])||Date.now();
    if(kind==='foundation-recognition')nextProgress=recordFoundationAttempt(nextProgress,lessonId,q.id,correct,at);
    else if(kind==='foundation-application')nextProgress=recordFoundationApplicationAttempt(nextProgress,lessonId,q.id,correct,at);
    else if(isReading)nextProgress=recordFoundationReadingAttempt(nextProgress,progressId,q.id,correct,at);
    else nextProgress=recordFoundationListeningAttempt(nextProgress,progressId,q.id,correct,at);
  }
  try{localStorage.setItem(storageKey,JSON.stringify(nextProgress));}
  catch(error){
    console.warn('Không thể lưu kết quả Foundation:',error);
    throw new Error('Không thể lưu kết quả Foundation trên thiết bị. Lựa chọn tạm vẫn được giữ; hãy thử xác nhận lại.');
  }
  state[progressKey]=nextProgress;
  delete state.foundationAssessmentDrafts[key];saveFoundationAssessmentDrafts();state.pendingFoundationAssessment=null;closeAssessmentResultModal();openFoundationLesson(lessonId);renderFoundationPath();
  toast('Đã lưu kết quả Foundation và mở phần xem lại.');
}

function renderLearningObjectiveProgress() {
  const host = $('#learningObjectiveProgress');
  if (!host || !state.objectiveResourceMap) return;
  const policy = { defaultThreshold: 0.8, minimumUniqueItems: 10 };
  const rows = summarizeAllObjectives(state.objectiveProgress, state.objectiveResourceMap, policy);
  const active = rows.filter(row => row.kind !== 'learning_path');
  host.innerHTML = active.map(row => {
    const status = row.status === 'content_review_pending' ? 'Chờ kiểm duyệt nội dung' : row.status === 'practice_threshold_met' ? 'Đạt ngưỡng luyện tập' : row.status === 'in_progress' ? 'Đang củng cố' : 'Chưa đủ dữ liệu';
    const accuracy = row.accuracyPercent === null ? '—' : `${row.accuracyPercent}%`;
    const width = row.evidenceCoveragePercent;
    const averageTime = row.averageResponseTimeMs === null ? 'Chưa đo thời gian' : `TB ${Math.round(row.averageResponseTimeMs / 1000)} giây/lượt`;
    const recall = row.recallChecks ? `Ôn nhớ lại: ${row.recallAccuracyPercent}% (${row.recallChecks} lượt)` : 'Ôn nhớ lại: chưa có dữ liệu';
    const due = row.dueRecallItems ? ` · ${row.dueRecallItems} câu đến hạn ôn` : '';
    const explanation = row.explanationRubricItems ? `Tự đánh giá giải thích: ${row.explanationRubricAverage}/3 · ${row.explanationRubricItems} câu` : 'Tự đánh giá giải thích: chưa có dữ liệu';
    return `<article class="objective-progress-card"><div class="objective-progress-top"><strong>${escapeHtml(row.title)}</strong><span>${accuracy}</span></div><div class="objective-progress-track"><i style="width:${width}%"></i></div><div class="objective-progress-meta"><span>${row.uniqueItems}/${row.minimumUniqueItems} câu độc lập · ${row.evidenceCoveragePercent}% dữ liệu · ${status}</span><small>${row.totalAttempts} lượt trả lời</small></div><div class="objective-progress-extra"><span>${escapeHtml(averageTime)}</span><span>${escapeHtml(recall + due)}</span><span>${escapeHtml(explanation)}</span></div></article>`;
  }).join('');
  renderRecallQueue();
}

function renderRecallQueue() {
  const host = $('#learningRecallQueue');
  if (!host || !state.objectiveResourceMap) return;
  const due = listDueRecallItems(state.objectiveProgress, state.objectiveResourceMap, Date.now(), 60);
  const count = $('#learningRecallQueueCount');
  if (count) count.textContent = `${due.length} mục đến hạn`;
  if (!due.length) {
    host.innerHTML = '<div class="recall-queue-empty"><strong>Chưa có câu TOEIC đến hạn ôn.</strong><span>Lịch ôn sẽ xuất hiện sau khi bạn luyện câu hỏi và đến mốc nhớ lại. Hàng đợi sẽ tự cập nhật khi mở lại ứng dụng hoặc quay về cửa sổ này.</span></div>';
    return;
  }
  host.innerHTML = due.map(item => {
    const status = item.latestCorrect ? 'Lần gần nhất: đúng' : 'Lần gần nhất: cần củng cố';
    const date = new Date(item.dueAt).toLocaleString('vi-VN', { day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit' });
    const partLabel = item.part || item.kind || 'Luyện tập';
    return `<article class="learning-card recall-queue-item"><div class="learning-card-top"><span class="learning-category">${escapeHtml(partLabel)}</span><span class="learning-level">${item.latestCorrect?'Đã trả lời đúng':'Cần củng cố'}</span></div><h3>${escapeHtml(item.objectiveTitle)}</h3><p>Đến hạn ${escapeHtml(date)} · ${item.attempts} lượt làm</p><div class="learning-card-footer"><small>${escapeHtml(status)} · Câu hỏi đã đến lịch ôn</small><button type="button" class="secondary-button" data-recall-open="${escapeHtml(item.objectiveId)}" data-recall-item="${escapeHtml(item.itemId)}">Mở ôn tập →</button></div></article>`;
  }).join('');
}

function findRecallQuestionIndex(resourceId, questions, itemId) {
  const direct = (questions || []).findIndex(question => question.id === itemId);
  if (direct >= 0) return direct;
  const match = String(itemId).match(new RegExp(`^${resourceId.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}::index:(\\d+)::`));
  return match ? Number(match[1]) : -1;
}

function openRecallItem(objectiveId, itemId) {
  const objective = (state.objectiveResourceMap?.objectives || []).find(row => row.id === objectiveId);
  if (!objective) return;
  const resources = objective.resourceIds || [];
  if (objective.kind === 'grammar') {
    const lesson = state.grammarLessons.find(row => resources.includes(row.id) && findRecallQuestionIndex(row.id, row.exercises, itemId) >= 0);
    if (lesson) { const index = findRecallQuestionIndex(lesson.id, lesson.exercises, itemId); navigate('grammar'); openGrammarLesson(lesson.id); requestAnimationFrame(() => $(`#learningFocusContent [data-grammar-exercise="${index}"]`)?.scrollIntoView({behavior:'smooth',block:'center'})); return; }
    navigate('grammar'); return;
  }
  if (objective.kind === 'reading') {
    const reading = state.readings.find(row => resources.includes(row.id) && findRecallQuestionIndex(row.id, row.questions, itemId) >= 0);
    if (reading) { const index = findRecallQuestionIndex(reading.id, reading.questions, itemId); navigate('reading'); openReadingDetail(reading.id); requestAnimationFrame(() => $(`#learningFocusContent [data-reading-question="${index}"]`)?.scrollIntoView({behavior:'smooth',block:'center'})); return; }
    navigate('reading'); return;
  }
  if (objective.kind === 'listening') {
    const listening = state.listening.find(row => resources.includes(row.id) && findRecallQuestionIndex(row.id, row.questions, itemId) >= 0);
    if (listening) { const index = findRecallQuestionIndex(listening.id, listening.questions, itemId); navigate('listening'); openListeningDetail(listening.id); requestAnimationFrame(() => $(`#learningFocusContent [data-listening-question="${index}"]`)?.scrollIntoView({behavior:'smooth',block:'center'})); return; }
    navigate('listening'); return;
  }
  if (objective.kind === 'practice' && objective.part === 'Part 5') {
    if (state.practiceReviewPending || state.autoAdvanceWaiting) { toast('Hãy hoàn tất phần giải thích hoặc chuyển câu hiện tại trước khi mở ôn nhớ lại.', 'error'); return; }
    const mode = $('#practiceMode'); if (mode) mode.value = 'sentence-completion';
    $$('[data-practice-mode]').forEach(button => { const selected = button.dataset.practiceMode === 'sentence-completion'; button.classList.toggle('is-selected', selected); button.setAttribute('aria-pressed', String(selected)); });
    const exactQuestion=state.sentenceCompletionItems.find(question=>question.id===itemId);
    navigate('practice');
    startPracticeFocus(exactQuestion?itemId:null);
    toast(exactQuestion?'Đã mở đúng câu TOEIC Part 5 đến hạn ôn.':'Câu Part 5 trong lịch ôn đã thay đổi; ứng dụng sẽ mở một câu Part 5 còn hợp lệ để bạn tiếp tục.');
    return;
  }
  if (objective.kind === 'learning_path') { navigate('foundation'); return; }
  navigate('practice');
}

async function answerGrammarExercise(button){return stagePracticeBatchAnswer('grammar',button.dataset.lessonId,Number(button.dataset.exerciseIndex),Number(button.dataset.choiceIndex),button);}


function renderReadingLibrary(){
  const q=normalizeText($('#readingSearch').value),topic=$('#readingTopicFilter').value,level=$('#readingLevelFilter').value,part=$('#readingPartFilter')?.value||'';
  const list=state.readings.filter(item=>{if(part&&item.part!==part)return false;if(topic&&item.topic!==topic)return false;if(level&&item.level!==level)return false;return !q||normalizeText([item.title,item.topic,item.level,item.passage,...(item.vocabulary||[]).map(x=>x.word)].join(' ')).includes(q);});
  $('#readingCount').textContent=`${list.length} / ${state.readings.length} bài đọc`;
  $('#readingCardList').innerHTML=list.map(item=>{const progress=ensurePracticeProgress(state.readingProgress[item.id]||{});const done=countAttemptedPracticeQuestions(progress,(item.questions||[]).length);const sourceText=item.passage||(item.documents||[]).map(doc=>doc.content||'').join(' ')||'';const preview=(sourceText||item.questions?.[0]?.question||'Bộ câu hỏi luyện TOEIC theo Part.').replace(/\s+/g,' ').slice(0,190);const wordCount=Number(item.wordCount)>0?Number(item.wordCount):sourceText.split(/\s+/).filter(Boolean).length;const wordMeta=item.part==='Part 5'?`${(item.questions||[]).length} câu luyện`:`${wordCount} từ`;return `<article class="learning-card reading-card"><div class="learning-card-top"><span class="learning-category">${escapeHtml(item.part||'Reading')} · ${escapeHtml(item.documentType||item.topic)}</span><span class="learning-level">${escapeHtml(item.level)}</span></div><h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(preview)}${preview.length>=190?'…':''}</p><div class="reading-card-meta"><span>${wordMeta}</span><span>${done}/${(item.questions||[]).length} câu đã làm</span></div><div class="learning-card-footer"><small>${escapeHtml(item.part||'Reading')} · TOEIC Practice</small><button class="secondary-button" data-reading-open="${escapeHtml(item.id)}">Đọc bài <span>→</span></button></div></article>`;}).join('');
  $('#readingEmpty').hidden=list.length>0;
}
function openReadingDetail(id){
  const reading=state.readings.find(x=>x.id===id);if(!reading)return;state.activeReading=id;
  const vocab=(reading.vocabulary||[]).map(v=>`<button type="button" class="reading-vocab-chip" data-lookup-term="${escapeHtml(v.word)}"><strong>${escapeHtml(displayWord(v.word))}</strong><small>${escapeHtml(v.pos)}</small><span>${escapeHtml(v.meaning)}</span></button>`).join('');
  const prog=ensurePracticeProgress(state.readingProgress[id]||{});
  const documents=(reading.documents||[]).map((doc,i)=>`<section class="reading-document-card"><div class="reading-passage-label">${escapeHtml(doc.label||`DOCUMENT ${i+1}`)}</div><pre class="reading-passage">${escapeHtml(doc.content||'')}</pre></section>`).join('');
  const passageMarkup=reading.part==='Part 5'?`<div class="reading-part-intro"><span class="learning-category">PART 5 · INCOMPLETE SENTENCES</span><p>Chọn từ hoặc cụm từ phù hợp nhất để hoàn thành từng câu.</p></div>`:(documents||reading.passage)?`<div class="reading-passage-card"><div class="reading-passage-label">${escapeHtml(reading.part||'PASSAGE')} · ${reading.wordCount||String(reading.passage||'').split(/\s+/).filter(Boolean).length} WORDS</div>${documents?documents:`<pre class="reading-passage">${escapeHtml(reading.passage||'')}</pre>`}</div>`:'';
  const questions=(reading.questions||[]).map((q,i)=>{const saved=prog.answers?.[i],draftChoice=getPracticeDraftChoice(prog,i),history=getPracticeAttemptHistory(prog,i),attemptLabel=history.length&&!saved?` · LÀM LẠI LẦN ${history.length+1}`:'';const feedback=saved?.answered?`<p class="exercise-feedback visible">${savedChoiceHistoryMarkup(q,saved)}${escapeHtml(q.explanation)}</p>${practiceRetryActionMarkup('reading',id,i,prog,saved)}`:`<p class="exercise-feedback" hidden></p>${history.length?`<small class="practice-retry-hint">Đã lưu ${history.length} lần trước. Bạn đang làm lại câu này.</small>${practiceAttemptHistoryMarkup(prog,i)}`:''}`;return `<article class="lesson-exercise reading-question" data-started-at="${Date.now()}" data-reading-question="${i}"><div class="exercise-kicker">CÂU HỎI ${i+1}${attemptLabel}</div><h4>${escapeHtml(q.question)}</h4><div class="exercise-choice-grid">${q.choices.map((choice,j)=>`<button type="button" class="exercise-choice ${saved?.answered&&j===q.answerIndex?'is-correct':''} ${savedChoiceWrongClass(q,saved,j)?'is-wrong':''} ${!saved?.answered&&draftChoice===j?'is-selected':''}" data-reading-choice data-reading-id="${escapeHtml(id)}" data-question-index="${i}" data-choice-index="${j}" data-choice-id="${escapeHtml(choiceIdAt(q,j))}" ${saved?.answered?'disabled':''}><span>${String.fromCharCode(65+j)}</span>${escapeHtml(choice)}</button>`).join('')}</div>${feedback}</article>`;}).join('');
  const vocabMarkup=vocab?`<section class="detail-section"><h4>TỪ VỰNG TRONG BÀI · NHẤN ĐỂ TRA CỨU</h4><div class="reading-vocab-grid">${vocab}</div></section>`:'';
  const retryToolbar=practiceRetryAllToolbar('reading',id,prog,reading.questions||[])+practiceDraftToolbar('reading',id,prog,reading.questions||[]);
  const readerToolbar=(reading.passage||(reading.documents||[]).some(doc=>doc.content)||reading.part==='Part 5')?`<div class="reading-audio-toolbar"><div><strong>Nghe đọc nội dung</strong><small>Đọc giới thiệu Part, câu dẫn, văn bản, câu hỏi và từng lựa chọn A–D theo thứ tự.</small></div><div class="reading-audio-actions"><button type="button" class="secondary-button" data-reading-speak="${escapeHtml(id)}">▶ Nghe đọc bài</button><button type="button" class="text-button" data-stop-speech>⏹ Dừng</button></div><p class="reading-audio-status" data-reading-audio-status aria-live="polite">Sẵn sàng đọc bài bằng TTS.</p></div>`:'';
  const content=`${passageMarkup}${readerToolbar}<details class="translation-details"><summary>Xem bản dịch tiếng Việt</summary><p>${escapeHtml(reading.translation||'Chưa có bản dịch.')}</p></details>${vocabMarkup}<section class="detail-section"><h4>${escapeHtml(reading.part||'READING')} · CÂU HỎI</h4>${retryToolbar}<div class="lesson-exercises">${questions}</div></section><div class="modal-actions"><button class="primary-button" data-ai-reading="${escapeHtml(id)}">${icon('sparkles','ui-icon button-icon')} Phân tích bài đọc bằng Google AI</button></div>`;
  openLearningDetail({title:reading.title,subtitle:`${reading.part||'Reading'} · ${reading.documentType||reading.topic} · ${reading.level}`,eyebrow:'READING · TOEIC LEARNING',content});
  maybeShowPracticeBatchResult('reading',id);
}
async function playReadingText(id){
  if(!('speechSynthesis'in window)||typeof SpeechSynthesisUtterance==='undefined'){toast('Thiết bị chưa hỗ trợ Text-to-Speech.','error');return;}
  const reading=state.readings.find(item=>item.id===id);if(!reading)return;
  const status=$(`#learningFocusContent [data-reading-audio-status]`);
  const part=String(reading.part||'Reading');
  const partNames={'Part 5':'Incomplete Sentences','Part 6':'Text Completion','Part 7':'Reading Comprehension'};
  const title=`${part}: ${partNames[part]||reading.topic||reading.title||'Reading'}`;
  const leadIns={'Part 5':'Now, complete each sentence with the best answer.','Part 6':'Now, read the text and choose the best answer for each blank.','Part 7':'Now, read the passage and answer the questions.'};
  const leadIn=leadIns[part]||'Now, read the following text and answer the questions.';
  const documentText=(reading.documents||[]).map((doc,index)=>`${String(doc.label||`Document ${index+1}`).trim()}. ${String(doc.content||'').trim()}`).filter(value=>!/^Document \d+\.\s*$/i.test(value)).join('\n\n');
  const text=[String(reading.passage||'').trim(),documentText].filter(Boolean).join('\n\n');
  const questions=Array.isArray(reading.questions)?reading.questions:[];
  if(!text&&!questions.length){toast('Bài đọc này chưa có nội dung tiếng Anh để phát.','error');return;}
  stopSpeech();const token=listeningPlaybackToken,cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})},gender=cfg.defaultGender||'female';
  if(status)status.textContent='Đang khởi động giọng đọc…';
  if(!prepareSpeechEngine(token)||token!==listeningPlaybackToken)return;
  const say=async(value,label)=>{
    if(token!==listeningPlaybackToken)return false;
    if(status)status.textContent=label||'Đang đọc…';
    const ok=await speakUtterance(value,{accent:cfg.accent,gender,rate:cfg.rate,onStart:()=>{if(status)status.textContent=label||'Đang đọc…';}},token);
    if(token!==listeningPlaybackToken)return false;
    if(!ok){if(status)status.textContent=speechFailureMessage();return false;}
    return true;
  };
  if(!await say(title,`Đang giới thiệu ${title}…`))return;
  if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,token))return;
  if(!await say(leadIn,'Đang đọc hướng dẫn phần Reading…'))return;
  if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,token))return;
  if(text){
    if(!await say(text,'Đang đọc văn bản tiếng Anh…'))return;
    if(questions.length&&!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,token))return;
  }
  for(let index=0;index<questions.length;index++){
    const question=questions[index];
    if(question.question&&!await say(`Question ${index+1}. ${question.question}`,`Đang đọc câu hỏi ${index+1}/${questions.length}…`))return;
    if(!question.question&&index===0&&!text&&!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,token))return;
    const choices=Array.isArray(question.choices)?question.choices:[];
    if(choices.length){
      if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,token))return;
      for(let choiceIndex=0;choiceIndex<choices.length;choiceIndex++){
        const letter=String.fromCharCode(65+choiceIndex);
        if(!await say(`${letter}.`,`Đang đọc nhãn lựa chọn ${letter}…`))return;
        if(!await waitSpeechGap(PART_OPTION_LABEL_PAUSE_MS,token))return;
        if(!await say(String(choices[choiceIndex]),`Đang đọc lựa chọn ${letter}…`))return;
        if(choiceIndex<choices.length-1&&!await waitSpeechGap(PART_OPTION_GAP_MS,token))return;
      }
    }
    if(index<questions.length-1&&!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,token))return;
  }
  if(token===listeningPlaybackToken&&status)status.textContent='Đã đọc xong giới thiệu Part, văn bản, câu hỏi và các lựa chọn. Bạn có thể nghe lại hoặc chọn Dừng.';
}
async function answerReadingQuestion(button){return stagePracticeBatchAnswer('reading',button.dataset.readingId,Number(button.dataset.questionIndex),Number(button.dataset.choiceIndex),button);}


function renderListeningLibrary(){
  const q=normalizeText($('#listeningSearch')?.value||''),part=$('#listeningPartFilter')?.value||'',level=$('#listeningLevelFilter')?.value||'';
  const list=state.listening.filter(item=>{if(part&&item.part!==part)return false;if(level&&item.level!==level)return false;return !q||normalizeText([item.title,item.topic,item.part,item.level,(item.segments||[]).map(x=>x.text).join(' '),(item.vocabulary||[]).map(x=>x.word).join(' ')].join(' ')).includes(q);});
  $('#listeningCount').textContent=`${list.length} / ${state.listening.length} bài nghe`;
  $('#listeningCardList').innerHTML=list.map(item=>{const prog=ensurePracticeProgress(state.listeningProgress[item.id]||{});const done=countAttemptedPracticeQuestions(prog,(item.questions||[]).length);const count=(item.questions||[]).length;const kind=item.part==='Part 1'?'Image Description':item.part==='Part 2'?'Question–Response':item.part==='Part 3'?'Conversation':'Short Talk';return `<article class="learning-card listening-card"><div class="learning-card-top"><span class="learning-category">${escapeHtml(item.part)} · ${escapeHtml(kind)}</span><span class="learning-level">${escapeHtml(item.level)}</span></div><h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(item.topic)} · ${(item.segments||[]).length} lượt lời · ${count} câu hỏi</p><div class="reading-card-meta"><span>${done}/${count} câu đã làm</span><span>Audio tổng hợp</span></div><div class="learning-card-footer"><small>Listening Practice · ${escapeHtml(item.topic)}</small><button class="secondary-button" data-listening-open="${escapeHtml(item.id)}">Bắt đầu nghe <span>→</span></button></div></article>`;}).join('');
  $('#listeningEmpty').hidden=list.length>0;
}
function openListeningDetail(id){
  stopSpeech();const item=state.listening.find(x=>x.id===id);if(!item)return;state.activeListening=id;
  const prog=ensurePracticeProgress(state.listeningProgress[id]||{});
  const questions=(item.questions||[]).map((q,i)=>{const saved=prog.answers?.[i],draftChoice=getPracticeDraftChoice(prog,i),history=getPracticeAttemptHistory(prog,i),attemptLabel=history.length&&!saved?` · LÀM LẠI LẦN ${history.length+1}`:'';const feedback=saved?.answered?`<p class="exercise-feedback visible">${savedChoiceHistoryMarkup(q,saved)}${escapeHtml(q.explanation)}</p>${practiceRetryActionMarkup('listening',id,i,prog,saved)}`:`<p class="exercise-feedback" hidden></p>${history.length?`<small class="practice-retry-hint">Đã lưu ${history.length} lần trước. Bạn đang làm lại câu này.</small>${practiceAttemptHistoryMarkup(prog,i)}`:''}`;return `<article class="lesson-exercise listening-question" data-started-at="${Date.now()}" data-listening-question="${i}"><div class="exercise-kicker">CÂU HỎI ${i+1}${attemptLabel}</div><h4>${escapeHtml(q.question)}</h4><div class="exercise-choice-grid">${q.choices.map((choice,j)=>`<button type="button" class="exercise-choice ${saved?.answered&&j===q.answerIndex?'is-correct':''} ${savedChoiceWrongClass(q,saved,j)?'is-wrong':''} ${!saved?.answered&&draftChoice===j?'is-selected':''}" data-listening-choice data-listening-id="${escapeHtml(id)}" data-question-index="${i}" data-choice-index="${j}" data-choice-id="${escapeHtml(choiceIdAt(q,j))}" ${saved?.answered?'disabled':''}><span>${String.fromCharCode(65+j)}</span>${item.part==='Part 1'?'':escapeHtml(choice)}</button>`).join('')}</div>${feedback}</article>`;}).join('');
  const transcript=(item.segments||[]).map((seg,i)=>{const isPart1=item.part==='Part 1',letter=String.fromCharCode(65+i);return `<div class="transcript-line"><small>${isPart1?`OPTION ${letter}`:escapeHtml(seg.speaker||`Speaker ${i+1}`)}</small><p>${isPart1?`${letter}. `:''}${escapeHtml(seg.text)}</p></div>`;}).join('');
  const transcriptPartMeta={
    'Part 1':{name:item.topic||item.title||'Photographs',leadIn:PART1_LEAD_IN_TEXT},
    'Part 2':{name:'Question–Response',leadIn:'Now, listen to the question and choose the best response.'},
    'Part 3':{name:'Conversations',leadIn:'Now, listen to the conversation and answer the questions.'},
    'Part 4':{name:'Short Talks',leadIn:'Now, listen to the talk and answer the questions.'}
  }[item.part];
  const part1LeadInTranscript=transcriptPartMeta?`<div class="transcript-line transcript-part-title"><small>PART TITLE</small><p>${escapeHtml(item.part)}: ${escapeHtml(transcriptPartMeta.name)}</p></div><div class="transcript-line transcript-lead-in"><small>LEAD-IN</small><p>${escapeHtml(transcriptPartMeta.leadIn)}</p></div>`:'';
  const photoSrc=item.part==='Part 1'?item.photo:'';
  const illustrationMarkup=item.part==='Part 1'&&photoSrc?`<figure class="part1-illustration-frame part1-photo-frame"><img data-photo-id="${escapeHtml(item.id)}" src="${escapeHtml(photoSrc)}" alt="${escapeHtml(item.imageAlt||item.title)}" loading="eager" decoding="async"><figcaption>ẢNH CHỤP · Quan sát ảnh trước khi nghe</figcaption></figure>`:'';
  const vocab=(item.vocabulary||[]).map(v=>`<button type="button" class="reading-vocab-chip" data-lookup-term="${escapeHtml(v.word)}"><strong>${escapeHtml(displayWord(v.word))}</strong><span>${escapeHtml(v.meaning)}</span></button>`).join('');
  const vocabMarkup=vocab?`<section class="detail-section"><h4>TỪ VỰNG TRỌNG TÂM</h4><div class="reading-vocab-grid">${vocab}</div></section>`:'';
  const vocabPlayButton=vocab?`<button type="button" class="secondary-button" data-listening-vocab-play="${escapeHtml(id)}">Đọc từ vựng chậm</button>`:'';
  const playLabel=item.part==='Part 1'?'Nghe bốn mô tả A–D':'Nghe toàn bộ';
  const content=`${illustrationMarkup}<div class="listening-player-card"><div class="listening-player-head"><span class="listening-wave">♫</span><div><strong>${escapeHtml(item.part)} · ${escapeHtml(item.type==='photograph'?'Mô tả ảnh':item.type==='conversation'?'Hội thoại':item.type==='talk'?'Bài nói ngắn':'Câu hỏi – đáp')}</strong><small>${escapeHtml(item.topic)} · ${item.segments.length} lượt lời</small></div></div><div class="listening-player-actions"><button type="button" class="primary-button" data-listening-play="${escapeHtml(id)}">${icon('volume-2','ui-icon button-icon')} ${playLabel}</button>${vocabPlayButton}<button type="button" class="secondary-button" data-listening-stop>⏹ Dừng</button></div><div class="listening-player-status" id="listeningPlayerStatus" aria-live="polite">Sẵn sàng phát audio. Bạn nên nghe trước khi mở transcript.</div><div class="listening-speed-row"><label for="listeningSpeed">Tốc độ đọc trong bài này</label><select id="listeningSpeed"><option value="0.75">x0.75 · Chậm</option><option value="0.85">x0.85 · Rõ ràng</option><option value="0.92" selected>x0.92 · Tự nhiên</option><option value="1">x1.0 · Bình thường</option><option value="1.1">x1.1 · Nhanh</option></select></div><p class="tts-inline-note">Giọng nam/nữ, cao độ giọng và khoảng nghỉ được điều chỉnh trong mục Cấu hình → Giọng đọc.</p></div><section class="detail-section"><h4>QUESTIONS · CÂU HỎI NGHE HIỂU</h4><p class="listening-hint">${item.part==='Part 1'?'Nghe tên chủ đề Part 1, câu dẫn, từng nhãn A–D; mỗi nhãn nghỉ 1,5 giây trước khi đọc mô tả. Quan sát ảnh và chọn mô tả khớp nhất. Transcript chỉ mở sau khi bạn đã làm.':'Nghe nội dung, sau đó chọn đáp án. Transcript và bản dịch được để bên dưới để bạn tự kiểm tra sau.'}</p>${practiceRetryAllToolbar('listening',id,prog,item.questions||[])}${practiceDraftToolbar('listening',id,prog,item.questions||[])}<div class="lesson-exercises">${questions}</div></section><details class="transcript-details"><summary>Hiện transcript tiếng Anh</summary><div class="transcript-content">${part1LeadInTranscript}${transcript}</div><p class="transcript-translation"><strong>Dịch nghĩa:</strong> ${item.part==='Part 1'?'Bây giờ, hãy nghe bốn câu mô tả. ':''}${escapeHtml(item.transcriptTranslation||'Chưa có bản dịch.')}</p></details>${vocabMarkup}<div class="modal-actions"><button class="secondary-button" data-ai-listening="${escapeHtml(id)}">${icon('sparkles','ui-icon button-icon')} Phân tích bài nghe một chiều bằng Google AI</button></div>`;
  openLearningDetail({title:item.title,subtitle:`${item.part} · ${item.topic} · ${item.level}`,eyebrow:'LISTENING · TOEIC LEARNING',content});
  maybeShowPracticeBatchResult('listening',id);
}
let listeningPlaybackToken=0;
let listeningGapTimer=null;
let listeningGapResolve=null;
let activeSpeechCancel=null;
let speechVoicesCache=[];
function getSpeechVoices(){
  if(!('speechSynthesis' in window))return [];
  try{
    speechVoicesCache=(window.speechSynthesis.getVoices()||[]).filter(v=>String(v.lang||'').toLowerCase().startsWith('en'));
  }catch(error){
    // Some mobile engines throw while their voice catalogue is initializing.
    // Keep playback available through the system-default voice in that case.
    speechVoicesCache=[];
    console.warn('Không đọc được voice catalog; sẽ dùng voice mặc định:',error);
  }
  return speechVoicesCache;
}
function hasSpeechVoiceCatalog(){
  if(!('speechSynthesis' in window))return false;
  try{
    const all=window.speechSynthesis.getVoices()||[];
    if(all.length){speechVoicesCache=all.filter(v=>String(v.lang||'').toLowerCase().startsWith('en'));return true;}
  }catch(error){console.warn('Không đọc được voice catalog:',error);}
  return false;
}
function classifyVoiceGender(voice){
  const name=String(voice?.name||'').toLowerCase();
  const femaleNames=/\b(samantha|victoria|karen|moira|tessa|ava|aria|jenny|zira|hazel|susan|female|woman|siri female|google uk english female|microsoft zira|microsoft aria|microsoft jenny)\b/i;
  const maleNames=/\b(daniel|alex|fred|tom|arthur|oliver|guy|david|mark|george|ryan|lee|james|male|man|google uk english male|microsoft david|microsoft guy|microsoft ryan)\b/i;
  if(femaleNames.test(name))return 'female';if(maleNames.test(name))return 'male';return '';
}
function classifyVoiceHint(value=''){
  const hint=String(value||'').toLowerCase();
  if(/female|woman|nữ|woman speaker|she\b/.test(hint))return 'female';
  if(/male|man|nam|he\b/.test(hint))return 'male';
  return '';
}
function recommendedMaleVoice(voices=getSpeechVoices()){
  // The learner confirmed iOS Daniel (en-GB) sounds clearer than the default male voice.
  return voices.find(v=>/\bdaniel\b/i.test(v.name||'')&&String(v.lang||'').toLowerCase()==='en-gb')
    || voices.find(v=>/\bdaniel\b/i.test(v.name||'')) || null;
}
function refreshSpeechVoiceSelectors(){
  // Keep the settings controls synchronized with the device's asynchronously loaded voice catalogue.
  const voices=getSpeechVoices();
  const suggestedMale=recommendedMaleVoice(voices);
  const options=voices.map(v=>{
    const gender=classifyVoiceGender(v);
    const label=v===suggestedMale?' · gợi ý rõ ràng trên iPhone':gender==='male'?' · nhận diện nam':gender==='female'?' · nhận diện nữ':' · chưa xác định giới tính';
    return `<option value="${escapeHtml(v.voiceURI||v.name)}">${escapeHtml(v.name)} — ${escapeHtml(v.lang||'en')}${label}</option>`;
  }).join('');
  for(const gender of ['male','female']){
    const select=$(`#tts${gender==='male'?'Male':'Female'}Voice`);
    if(!select)continue;
    const saved=state.settings?.tts?.[`${gender}VoiceURI`]||'';
    select.innerHTML=`<option value="">Tự chọn voice phù hợp</option>${options}`;
    const selected=saved||(gender==='male'&&suggestedMale?(suggestedMale.voiceURI||suggestedMale.name):'');
    if(selected){
      if(Array.from(select.options||[]).some(option=>option.value===selected))select.value=selected;
      else if(typeof document!=='undefined'&&document.createElement){
        const missing=document.createElement('option');
        missing.value=selected;
        missing.textContent='Voice đã lưu nhưng thiết bị hiện tại không cung cấp';
        select.append(missing);
        select.value=selected;
      }
    }
    select.disabled=!voices.length;
  }
  const status=$('#ttsVoiceStatus');
  if(status){
    status.textContent=voices.length
      ?`Đã tìm thấy ${voices.length} voice tiếng Anh trên thiết bị này.${suggestedMale?' Giọng nam gợi ý: '+suggestedMale.name+' — '+suggestedMale.lang+'.':''}`
      :'Trình duyệt chưa cung cấp danh sách voice tiếng Anh. Khi phát, ứng dụng sẽ thử voice mặc định của hệ thống; hãy cài thêm English voice nếu không nghe được.';
  }
}
function chooseEnglishVoice(accent='en-US',speaker='',voiceHint='',excludeNames=[]){
  const voices=getSpeechVoices();if(!voices.length)return null;
  const cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})};
  const lang=accent==='en-GB'?'en-GB':'en-US';
  const exact=voices.filter(v=>String(v.lang||'').toLowerCase()===lang.toLowerCase());
  const pool=exact.length?exact:voices;
  const wanted=classifyVoiceHint(voiceHint||speaker)||cfg.defaultGender;
  const preferredURI=wanted==='male'?cfg.maleVoiceURI:wanted==='female'?cfg.femaleVoiceURI:'';
  if(preferredURI){const chosen=voices.find(v=>(v.voiceURI||v.name)===preferredURI);if(chosen)return chosen;}
  if(wanted==='male'){
    // Keep the previously verified Daniel preference while allowing another male voice per speaker.
    const daniel=recommendedMaleVoice(voices);
    if(daniel&&!excludeNames.includes(daniel.name))return daniel;
  }
  const gendered=pool.filter(v=>classifyVoiceGender(v)===wanted);
  const preferred=gendered.length?gendered:pool;
  const available=preferred.filter(v=>!excludeNames.includes(v.name));
  const candidates=available.length?available:preferred;
  return candidates.find(v=>/natural|neural|premium|enhanced/i.test(v.name))||candidates.find(v=>v.localService!==false)||candidates[0]||null;
}
function configureUtterance(utterance,{accent,gender,voice,rate,systemDefault=false}={}){
  const cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})};
  const chosen=systemDefault?null:(voice||chooseEnglishVoice(accent||cfg.accent,'',gender||cfg.defaultGender));
  utterance.lang=chosen?.lang||accent||cfg.accent||'en-US';
  utterance.rate=Math.min(1.15,Math.max(.75,Number(rate??cfg.rate)||.92));
  utterance.pitch=Math.min(1.2,Math.max(.8,Number(cfg.pitch)||1));
  utterance.volume=Math.min(1,Math.max(.1,Number(cfg.volume)||1));
  if(chosen)utterance.voice=chosen;
  return utterance;
}
function stopSpeech(){
  listeningPlaybackToken++;
  if(listeningGapTimer){clearTimeout(listeningGapTimer);listeningGapTimer=null;}
  if(listeningGapResolve){const resolve=listeningGapResolve;listeningGapResolve=null;resolve(false);}
  // Resolve any in-flight utterance before browser cancellation; some engines omit onerror for cancel().
  const cancelActive=activeSpeechCancel;activeSpeechCancel=null;if(cancelActive)cancelActive();
  if('speechSynthesis'in window){try{window.speechSynthesis.cancel();}catch(error){console.warn('Không thể dừng speech synthesis:',error);}}
  const status=$('#listeningPlayerStatus');if(status)status.textContent='Đã dừng audio.';document.querySelectorAll('[id^="foundationListeningStatus-"]').forEach(foundationStatus=>{foundationStatus.textContent='Đã dừng audio.';});
  if(typeof document!=='undefined')document.querySelectorAll('[data-reading-audio-status]').forEach(node=>{node.textContent='Đã dừng đọc.';});
  return listeningPlaybackToken;
}
function waitSpeechGap(ms,token){
  return new Promise(resolve=>{
    if(token!==listeningPlaybackToken)return resolve(false);
    listeningGapResolve=resolve;
    listeningGapTimer=setTimeout(()=>{
      listeningGapTimer=null;listeningGapResolve=null;
      resolve(token===listeningPlaybackToken);
    },Math.max(0,ms));
  });
}
function prepareSpeechEngine(token){
  if(token!==listeningPlaybackToken||!('speechSynthesis'in window))return false;
  const synth=window.speechSynthesis;
  // Do not await voiceschanged or a startup timer before the first utterance.
  // Mobile Safari can drop transient user activation while async preparation is pending.
  try{
    if(typeof synth.getVoices==='function')synth.getVoices();
    if(synth.paused&&typeof synth.resume==='function')synth.resume();
  }catch(error){console.warn('Không thể khởi động speech synthesis:',error);}
  return token===listeningPlaybackToken;
}
async function speakText(text,accent=null,speaker='',gender=null,lifecycle={}){
  if(!('speechSynthesis'in window)||typeof SpeechSynthesisUtterance==='undefined'){toast('Trình duyệt/thiết bị này chưa hỗ trợ đọc phát âm.','error');lifecycle.onError?.();return false;}
  const clean=String(text||'').trim();if(!clean)return false;
  stopSpeech();const token=listeningPlaybackToken;const cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})};
  if(lifecycle.onPrepare)lifecycle.onPrepare();
  if(!prepareSpeechEngine(token)||token!==listeningPlaybackToken)return false;
  const voice=chooseEnglishVoice(accent||cfg.accent,speaker,gender||cfg.defaultGender);
  // speakUtterance queues speech synchronously in the original click/tap call stack.
  const speech=speakUtterance(clean,{accent:accent||cfg.accent,gender:gender||cfg.defaultGender,voice,rate:cfg.rate,onStart:lifecycle.onStart},token);
  const ok=await speech;
  if(token!==listeningPlaybackToken)return false;
  if(!ok){lifecycle.onError?.();toast(speechFailureMessage(),'error');return false;}
  lifecycle.onEnd?.();return true;
}
let lastSpeechError='';
function speechFailureMessage(){
  const messages={
    'start-timeout':'Trình duyệt không khởi động được giọng đọc sau 10 giây. Hãy thử bấm nghe lại hoặc chọn voice khác trong Cấu hình.',
    'end-timeout':'Giọng đọc đã bắt đầu nhưng không gửi tín hiệu kết thúc. Hãy dừng audio rồi thử phát lại.',
    'not-allowed':'Trình duyệt đã chặn phát âm. Hãy bấm trực tiếp nút Nghe và kiểm tra quyền âm thanh của trang.',
    'voice-unavailable':'Voice đã chọn không khả dụng. Hệ thống đã thử dùng voice mặc định; vui lòng chọn voice khác nếu vẫn không nghe được.',
    'language-unavailable':'Thiết bị không có voice phù hợp với ngôn ngữ đang chọn. Hãy kiểm tra gói giọng đọc tiếng Anh.',
    'network':'Voice trực tuyến gặp lỗi mạng. Hãy thử voice cài sẵn trên thiết bị.',
    'synthesis-failed':'Bộ đọc của trình duyệt gặp lỗi. Hãy thử lại hoặc chọn voice khác trong Cấu hình.'
  };
  return messages[lastSpeechError]||'Không thể phát âm thanh. Hãy bấm nghe lại hoặc kiểm tra voice trong Cấu hình.';
}
function speakUtterance(text,{accent='en-US',voice=null,gender='female',rate=null,onStart=null}={},token){
  return new Promise(resolve=>{
    const clean=String(text||'').trim();
    if(token!==listeningPlaybackToken||!clean)return resolve(false);
    let settled=false,startTimer=null,endTimer=null,fallbackAttempted=false,activeAttempt=0;
    const clearWatchdogs=()=>{if(startTimer)clearTimeout(startTimer);if(endTimer)clearTimeout(endTimer);startTimer=null;endTimer=null;};
    const finish=(ok,error='')=>{
      if(settled)return;settled=true;activeAttempt++;clearWatchdogs();
      if(error)lastSpeechError=error;
      if(activeSpeechCancel===cancelActive)activeSpeechCancel=null;
      resolve(ok&&token===listeningPlaybackToken);
    };
    const cancelActive=()=>finish(false,'canceled');activeSpeechCancel=cancelActive;
    const enqueue=(selectedVoice,usingFallback=false)=>{
      if(settled||token!==listeningPlaybackToken)return finish(false,'canceled');
      const attempt=++activeAttempt;
      let utterance;
      try{
        utterance=configureUtterance(new SpeechSynthesisUtterance(clean),{accent,gender,voice:selectedVoice,rate,systemDefault:usingFallback});
      }catch(error){finish(false,'synthesis-failed');return;}
      const estimatedDuration=Math.min(180000,Math.max(SPEECH_END_TIMEOUT_MIN_MS,Math.ceil(clean.length*260/Math.max(.75,utterance.rate||1))+12000));
      startTimer=setTimeout(()=>{if(attempt===activeAttempt)finish(false,'start-timeout');},SPEECH_START_TIMEOUT_MS);
      endTimer=setTimeout(()=>{if(attempt===activeAttempt)finish(false,'end-timeout');},estimatedDuration);
      utterance.onstart=()=>{
        if(settled||attempt!==activeAttempt||token!==listeningPlaybackToken)return;
        if(startTimer){clearTimeout(startTimer);startTimer=null;}
        onStart?.();
      };
      utterance.onend=()=>{if(!settled&&attempt===activeAttempt)finish(true);};
      utterance.onerror=event=>{
        if(settled||attempt!==activeAttempt)return;
        const error=String(event?.error||'synthesis-failed');
        // Retry a failed named voice once with the system default. Do not cancel
        // the synthesis queue here: cancel() can emit a stale error for this
        // utterance on some engines and accidentally cancel the fallback too.
        if(!usingFallback&&!fallbackAttempted&&selectedVoice&&token===listeningPlaybackToken&&!['canceled','interrupted'].includes(error)){
          fallbackAttempted=true;clearWatchdogs();enqueue(null,true);return;
        }
        finish(false,error);
      };
      try{
        const synth=window.speechSynthesis;
        if(typeof synth.resume==='function')synth.resume();
        synth.speak(utterance);
      }catch(error){if(attempt===activeAttempt)finish(false,'synthesis-failed');}
    };
    lastSpeechError='';
    enqueue(voice,false);
  });
}

async function playListeningAudio(id, options={}){
  if(!('speechSynthesis'in window)||typeof SpeechSynthesisUtterance==='undefined'){toast('Thiết bị chưa hỗ trợ Text-to-Speech.','error');return;}
  const item=state.listening.find(x=>x.id===id);if(!item)return;
  const segments=item.segments||[];if(!segments.length)return;
  const isPart1=item.part==='Part 1';
  if(isPart1&&segments.length!==4){
    const message='Bài Listening Part 1 chưa đủ bốn mô tả A–D nên chưa thể phát theo định dạng chuẩn.';
    const status=options.statusElement||$('#listeningPlayerStatus');if(status)status.textContent=message;toast(message,'error');return;
  }
  stopSpeech();const playbackToken=++listeningPlaybackToken;
  const cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})};
  const speed=Number(options.speed??$('#listeningSpeed')?.value??cfg.rate);const status=options.statusElement||$('#listeningPlayerStatus');
  const speakerVoices=new Map();const usedVoiceNames={female:[],male:[]};
  const resolveSpeakerVoice=segment=>{
    const speaker=String(segment.speaker||'Speaker').trim(),key=speaker.toLowerCase();
    if(speakerVoices.has(key))return speakerVoices.get(key);
    const gender=classifyVoiceHint(segment.voice||speaker)||cfg.defaultGender;
    const segmentAccent=segment.accent||cfg.accent;
    const voice=chooseEnglishVoice(segmentAccent,speaker,gender,usedVoiceNames[gender]||[]);
    if(voice){speakerVoices.set(key,voice);(usedVoiceNames[gender]||[]).push(voice.name);}return voice;
  };
  const partMeta={
    'Part 1':{name:String(item.topic||item.title||'Photographs').trim(),leadIn:PART1_LEAD_IN_TEXT},
    'Part 2':{name:'Question–Response',leadIn:'Now, listen to the question and choose the best response.'},
    'Part 3':{name:'Conversations',leadIn:'Now, listen to the conversation and answer the questions.'},
    'Part 4':{name:'Short Talks',leadIn:'Now, listen to the talk and answer the questions.'}
  };
  const meta=partMeta[item.part]||{name:String(item.topic||item.title||'Listening').trim(),leadIn:'Now, listen to the audio and answer the questions.'};
  const leadSegment=segments[0],leadGender=classifyVoiceHint(leadSegment.voice||leadSegment.speaker)||cfg.defaultGender,leadVoice=resolveSpeakerVoice(leadSegment);
  if(status)status.textContent='Đang khởi động giọng đọc…';
  if(!prepareSpeechEngine(playbackToken)||playbackToken!==listeningPlaybackToken)return;
  const say=async(value,segment=leadSegment,label='Đang đọc…')=>{
    if(playbackToken!==listeningPlaybackToken)return false;
    const gender=classifyVoiceHint(segment?.voice||segment?.speaker)||cfg.defaultGender;
    const voice=resolveSpeakerVoice(segment||leadSegment);
    if(status)status.textContent=label;
    const ok=await speakUtterance(value,{accent:segment?.accent||cfg.accent,gender,voice,rate:speed,onStart:()=>{if(status)status.textContent=label;}},playbackToken);
    if(playbackToken!==listeningPlaybackToken)return false;
    if(!ok){if(status)status.textContent=speechFailureMessage();return false;}
    return true;
  };
  const title=`${item.part}: ${meta.name}`;
  // Guided Mock already speaks its transition/Part lead-in before calling this
  // shared player. Honor skipLeadIn so the same Part title and instruction are
  // not announced a second time; standalone practice keeps the full sequence.
  if(options.skipLeadIn!==true){
    if(status)status.textContent=`Đang giới thiệu ${title}…`;
    if(!await say(title,leadSegment,`Đang giới thiệu ${title}…`))return;
    if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,playbackToken))return;
    if(!await say(meta.leadIn,leadSegment,`Đang đọc câu dẫn ${item.part||'Listening'}…`))return;
    if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,playbackToken))return;
  }else if(status){
    status.textContent=`Đang phát nội dung ${title} sau câu dẫn…`;
  }
  for(let index=0;index<segments.length;index++){
    if(playbackToken!==listeningPlaybackToken)return;
    const segment=segments[index],speaker=segment.speaker||`Lượt lời ${index+1}`;
    const segmentLabel=isPart1?`Lựa chọn ${String.fromCharCode(65+index)}/4`:`${speaker} (${index+1}/${segments.length})`;
    const optionText=String(segment.text||'').replace(/^\s*[A-D][.)]\s+/i,'').trim();
    if(!await say(isPart1?`${String.fromCharCode(65+index)}.`:optionText,segment,isPart1?`Đang đọc nhãn ${String.fromCharCode(65+index)}…`:`Đang phát ${segmentLabel}…`))return;
    if(isPart1){
      if(!await waitSpeechGap(PART1_OPTION_LABEL_PAUSE_MS,playbackToken))return;
      if(!await say(optionText,segment,`Đang đọc nội dung lựa chọn ${String.fromCharCode(65+index)}…`))return;
    }
    if(index<segments.length-1){
      const gap=isPart1?PART1_OPTION_GAP_MS:Math.max(500,Number(cfg.sentencePauseMs)||850);
      if(status)status.textContent=`${segmentLabel} vừa kết thúc · chuẩn bị lượt tiếp theo trong ${(gap/1000).toFixed(2)} giây…`;
      if(!await waitSpeechGap(gap,playbackToken))return;
    }
  }
  const questions=Array.isArray(item.questions)?item.questions:[];
  if(!isPart1&&questions.length){
    if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,playbackToken))return;
    for(let questionIndex=0;questionIndex<questions.length;questionIndex++){
      const question=questions[questionIndex];
      // Part 2's audio segment is itself the question; its stored prompt is generic UI guidance.
      const isPart2=item.part==='Part 2';
      if(!isPart2&&question.question){
        if(!await say(`Question ${questionIndex+1}. ${question.question}`,leadSegment,`Đang đọc câu hỏi ${questionIndex+1}/${questions.length}…`))return;
      }
      const choices=Array.isArray(question.choices)?question.choices:[];
      if(choices.length){
        if(!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,playbackToken))return;
        for(let choiceIndex=0;choiceIndex<choices.length;choiceIndex++){
          const letter=String.fromCharCode(65+choiceIndex);
          if(!await say(`${letter}.`,leadSegment,`Đang đọc nhãn lựa chọn ${letter}…`))return;
          if(!await waitSpeechGap(PART_OPTION_LABEL_PAUSE_MS,playbackToken))return;
          if(!await say(String(choices[choiceIndex]),leadSegment,`Đang đọc lựa chọn ${letter}…`))return;
          if(choiceIndex<choices.length-1&&!await waitSpeechGap(PART_OPTION_GAP_MS,playbackToken))return;
        }
      }
      if(questionIndex<questions.length-1&&!await waitSpeechGap(PART_SEQUENCE_PAUSE_MS,playbackToken))return;
    }
  }
  if(playbackToken===listeningPlaybackToken&&status)status.textContent=`Đã phát xong ${title}, câu dẫn, nội dung và ${isPart1?'bốn lựa chọn A–D':'câu hỏi cùng các lựa chọn'}. Bạn có thể nghe lại hoặc mở transcript.`;
}
async function playListeningVocabulary(id){
  if(!('speechSynthesis'in window)||typeof SpeechSynthesisUtterance==='undefined'){toast('Thiết bị chưa hỗ trợ Text-to-Speech.','error');return;}
  const item=state.listening.find(x=>x.id===id);if(!item)return;
  const words=(item.vocabulary||[]).map(v=>String(v.word||'').trim()).filter(Boolean);
  if(!words.length){toast('Bài nghe này chưa có danh sách từ vựng để phát.','error');return;}
  stopSpeech();const token=++listeningPlaybackToken,cfg={...DEFAULT_TTS_SETTINGS,...(state.settings.tts||{})},status=$('#listeningPlayerStatus');
  if(status)status.textContent='Đang khởi động giọng đọc…';
  if(!prepareSpeechEngine(token)||token!==listeningPlaybackToken)return;
  if(status)status.textContent=`Đang yêu cầu đọc danh sách ${words.length} từ…`;
  for(let i=0;i<words.length;i++){
    if(token!==listeningPlaybackToken)return;
    if(status)status.textContent=`Từ ${i+1}/${words.length}: ${words[i]}`;
    const ok=await speakUtterance(words[i],{accent:cfg.accent,gender:cfg.defaultGender},token);
    if(token!==listeningPlaybackToken)return;
    if(!ok){if(status)status.textContent=speechFailureMessage();return;}
    if(i<words.length-1&&!await waitSpeechGap(cfg.wordPauseMs,token))return;
  }
  if(token===listeningPlaybackToken&&status)status.textContent=`Đã đọc xong ${words.length} từ. Khoảng nghỉ giữa các từ: ${(cfg.wordPauseMs/1000).toFixed(1)} giây.`;
}
function saveTtsSetting(key,value){
  if(!state.settings.tts)state.settings.tts={...DEFAULT_TTS_SETTINGS};
  const limits={wordPauseMs:[300,2500],sentencePauseMs:[300,2500]};
  if(limits[key])value=Math.min(limits[key][1],Math.max(limits[key][0],Number(value)||limits[key][0]));
  state.settings.tts[key]=value;
  dbSet('appSettings',state.settings).catch(err=>console.warn('Không lưu được cấu hình giọng đọc:',err));
}
function bindTtsSettings(){
  const bindings=[['ttsAccent','accent',v=>v],['ttsDefaultGender','defaultGender',v=>v],['ttsRate','rate',Number],['ttsPitch','pitch',Number],['ttsVolume','volume',Number],['ttsWordPause','wordPauseMs',Number],['ttsSentencePause','sentencePauseMs',Number],['ttsMaleVoice','maleVoiceURI',v=>v],['ttsFemaleVoice','femaleVoiceURI',v=>v]];
  for(const [id,key,cast] of bindings){const el=$(`#${id}`);if(!el)continue;el.addEventListener('change',()=>saveTtsSetting(key,cast(el.value)));}
  $('#refreshSpeechVoices')?.addEventListener('click',()=>{if('speechSynthesis'in window)window.speechSynthesis.getVoices();refreshSpeechVoiceSelectors();toast('Đã làm mới danh sách voice từ thiết bị.');});
  $('#previewMaleVoice')?.addEventListener('click',()=>speakText('Good morning. The meeting will begin in ten minutes.',null,'','male'));
  $('#previewFemaleVoice')?.addEventListener('click',()=>speakText('Good morning. The meeting will begin in ten minutes.',null,'','female'));
  $('#previewDefaultVoice')?.addEventListener('click',()=>speakText('This is a natural English pronunciation sample. Please listen to the clarity and speaking rhythm.'));
  if('speechSynthesis'in window){
    if(typeof window.speechSynthesis.addEventListener==='function')window.speechSynthesis.addEventListener('voiceschanged',refreshSpeechVoiceSelectors);
    else window.speechSynthesis.onvoiceschanged=refreshSpeechVoiceSelectors;
    refreshSpeechVoiceSelectors();
  }
}
async function answerListeningQuestion(button){return stagePracticeBatchAnswer('listening',button.dataset.listeningId,Number(button.dataset.questionIndex),Number(button.dataset.choiceIndex),button);}


function buildListeningAIPrompt(item){
  return `Bạn là giáo viên luyện TOEIC Listening cho người học Việt Nam. Hãy phân tích bài nghe theo đúng thông tin dưới đây. Đây là nội dung luyện tập do ứng dụng tạo, không phải đề thi chính thức.\n\nPHẦN: ${item.part}\nTIÊU ĐỀ: ${item.title}\nCHỦ ĐỀ: ${item.topic}\nCẤP ĐỘ: ${item.level}\n\nTRANSCRIPT:\n${(item.segments||[]).map(s=>`${s.speaker}: ${s.text}`).join('\n')}\n\nCÂU HỎI VÀ ĐÁP ÁN:\n${(item.questions||[]).map((q,i)=>`${i+1}. ${q.question}\n${q.choices.map((c,j)=>`${String.fromCharCode(65+j)}. ${c}`).join('\n')}\nĐáp án: ${q.choices[q.answerIndex]}\nGiải thích hiện có: ${q.explanation}`).join('\n\n')}\n\nTỪ VỰNG:\n${(item.vocabulary||[]).map(v=>`${v.word}: ${v.meaning}`).join('\n')}\n\nYÊU CẦU: Dịch từng lượt lời; giải thích nối âm, trọng âm và cụm từ quan trọng; chỉ ra từ khóa để bắt thông tin; phân tích lý do từng lựa chọn đúng/sai; hướng dẫn nghe bắt ý chính, thời gian, địa điểm, mục đích và suy luận; đề xuất một lần luyện nghe lại có mục tiêu. Hãy trả lời đầy đủ trong một phản hồi, không đặt câu hỏi ngược lại.`;
}

function openLookupTerm(term){
  const word=lookupWord(term);if(word){showDetail(word.id);return;}
  showAIPromptModal(`Hãy giải thích từ/cụm từ tiếng Anh “${term}” trong ngữ cảnh TOEIC. Yêu cầu: IPA nếu có, loại từ, nghĩa tiếng Việt theo từng ngữ cảnh, collocations, từ đồng/trái nghĩa phù hợp, 3 ví dụ TOEIC và các lỗi thường gặp. Không suy đoán khi thiếu dữ liệu.`,`Tra nghĩa, cách dùng và ví dụ TOEIC của từ ${term}`);
}
function buildGrammarAIPrompt(lesson){return `Bạn là giáo viên luyện thi TOEIC cho người Việt. Hãy dạy kỹ chủ điểm ngữ pháp sau, kiểm chứng cách dùng và không tự bịa quy tắc.\n\nCHỦ ĐIỂM: ${lesson.title}\nCẤP ĐỘ: ${lesson.level}\nCÔNG THỨC: ${lesson.formula}\nGIẢI THÍCH HIỆN CÓ: ${lesson.explanation}\nVÍ DỤ: ${(lesson.examples||[]).map(x=>`${x.en} — ${x.vi} — ${(x.breakdown||[]).map(y=>`${y.part}: ${y.text} (${y.meaning})`).join('; ')}`).join('\n')}\nMẸO: ${(lesson.tips||[]).join('\n')}\nBÀI TẬP: ${(lesson.exercises||[]).map(x=>`${x.question}\n${x.choices.map((c,i)=>`${String.fromCharCode(65+i)}. ${c}`).join('\n')}\nĐáp án: ${x.choices[x.answerIndex]} — ${x.explanation}`).join('\n\n')}\n\nHãy trình bày: (1) giải thích đơn giản, (2) cấu trúc và ngoại lệ, (3) phân tích từng ví dụ, (4) lỗi thường gặp, (5) bẫy TOEIC, (6) 5 câu hỏi mới có đáp án ở cuối.`;}
function buildReadingAIPrompt(reading){return `Bạn là giáo viên TOEIC Reading. Hãy phân tích bài đọc sau cho người học Việt Nam.\n\nTIÊU ĐỀ: ${reading.title}\nCHỦ ĐỀ: ${reading.topic}\nCẤP ĐỘ: ${reading.level}\nPASSAGE:\n${reading.passage}\n\nBẢN DỊCH THAM KHẢO:\n${reading.translation}\n\nTỪ VỰNG:\n${(reading.vocabulary||[]).map(x=>`${x.word} (${x.pos}) — ${x.meaning}`).join('\n')}\n\nCÂU HỎI VÀ ĐÁP ÁN:\n${(reading.questions||[]).map((x,i)=>`${i+1}. ${x.question}\n${x.choices.map((c,j)=>`${String.fromCharCode(65+j)}. ${c}`).join('\n')}\nĐáp án: ${x.choices[x.answerIndex]} — ${x.explanation}`).join('\n\n')}\n\nYêu cầu: dịch từng câu tự nhiên; phân tích cấu trúc ngữ pháp; giải thích từ khóa giúp tìm đáp án; phân tích vì sao từng lựa chọn đúng/sai; chỉ ra paraphrase và bẫy TOEIC; tạo 5 từ/cụm từ mở rộng và 3 câu hỏi tương tự. Hãy trả lời đầy đủ trong một lần, không hỏi ngược lại.`;}

function buildWordAIPrompt(word) {
  const senses=(word.senses||[]).map((s,i)=>`${i+1}. Loại từ: ${s.pos}\n   Nghĩa tiếng Việt: ${s.meaning_vi}\n   Definition: ${s.definition_en||'Chưa có'}\n   Synonyms: ${(s.synonyms||[]).join(', ')||'Chưa có'}\n   Antonyms: ${(s.antonyms||[]).join(', ')||'Chưa có'}`).join('\n');
  const forms=word.verb_forms?JSON.stringify(word.verb_forms,null,2):'Không áp dụng/chưa có';
  return `Bạn là giáo viên tiếng Anh chuyên luyện TOEIC cho người học Việt Nam. Hãy phân tích đầy đủ mục từ sau, kiểm tra độ chính xác và không tự bịa dữ liệu.\n\nTỪ: ${displayWord(word.word)}\nIPA: ${word.phonetic?.us||'Chưa có'}\nCHỦ ĐỀ: ${(word.topics||[]).join(', ')}\nCÁC NGHĨA:\n${senses}\nWORD FAMILY: ${JSON.stringify(word.word_family||[],null,2)}\nVERB FORMS: ${forms}\nCOLLOCATIONS: ${(word.collocations||[]).join(', ')||'Chưa có'}\nVÍ DỤ: ${(word.examples||[]).map(e=>`${e.en} — ${e.vi}`).join('\n')||'Chưa có'}\n\nYÊU CẦU PHÂN TÍCH:\n1. Giải thích từng nghĩa và ngữ cảnh sử dụng; chỉ rõ loại từ n/v/adj/adv/prep...\n2. Phân biệt từ đồng nghĩa và trái nghĩa theo đúng ngữ cảnh, chỉ ra sắc thái khác nhau.\n3. Kiểm tra word family, V1/V-s/es/V2/V3/V-ing nếu là động từ.\n4. Nêu collocations và lỗi thường gặp của người Việt.\n5. Tạo tối thiểu 3 ví dụ theo bối cảnh TOEIC (văn phòng, cuộc họp, nhân sự, tài chính, vận chuyển...).\n6. Đề xuất mẹo ghi nhớ dễ hiểu.\n7. Tạo 5 câu hỏi ôn tập kèm đáp án và giải thích ở phần riêng cuối bài.\nNếu dữ liệu nguồn chưa đủ hoặc một quan hệ đồng/trái nghĩa không tự nhiên, hãy nói rõ thay vì suy đoán.`;
}
function buildPracticeAIPrompt() {
  const q=state.currentQuestion; const f=state.lastFeedback; const w=state.words.find(x=>x.id===q?.wordId);
  if(!q||!f||!w)return 'Hãy giải thích câu hỏi TOEIC hiện tại và cách tìm đáp án đúng.';
  const options=(q.choices||[]).map((choice,i)=>{const correct=q.accepted.some(x=>normalizedAnswer(x)===normalizedAnswer(choice));return `${String.fromCharCode(65+i)}. ${choice}\n   Trạng thái: ${correct?'Đáp án đúng hợp lệ':'Phương án nhiễu'}\n   Giải nghĩa tham chiếu trong kho: ${getChoiceExplanation(q,choice,correct)}`;}).join('\n');
  return `Bạn là giáo viên TOEIC và chuyên gia giải thích từ vựng/ngữ pháp cho người Việt. Hãy phân tích toàn bộ câu hỏi, đáp án và các phương án lựa chọn dưới đây.\n\nDẠNG BÀI: ${q.mode}\nCÂU HỎI: ${q.prompt}\n${q.sentence?`CÂU CẦN HOÀN THÀNH: ${q.sentence}`:''}\n${q.translationVi?`BẢN DỊCH THAM CHIẾU: ${q.translationVi}`:''}\n${q.grammarPoint?`TRỌNG TÂM NGỮ PHÁP: ${q.grammarPoint}`:''}\n${q.explanation?`GIẢI THÍCH BIÊN SOẠN: ${q.explanation}`:''}\nGỢI Ý: ${q.hint||'Không có'}\nTỪ MỤC TIÊU: ${displayWord(w.word)}\nIPA: ${w.phonetic?.us||'Chưa có'}\nCÁC NGHĨA: ${(w.senses||[]).map(s=>`${s.pos}: ${s.meaning_vi} (${s.definition_en||''})`).join('; ')}\nTỪ ĐỒNG NGHĨA: ${(w.senses||[]).flatMap(s=>s.synonyms||[]).join(', ')||'Không có'}\nTỪ TRÁI NGHĨA: ${(w.senses||[]).flatMap(s=>s.antonyms||[]).join(', ')||'Không có'}\nWORD FAMILY: ${JSON.stringify(w.word_family||[])}\nVERB FORMS: ${JSON.stringify(w.verb_forms||{})}\n\nCÁC LỰA CHỌN:\n${options||'Câu trả lời dạng nhập văn bản.'}\n\nCÂU TRẢ LỜI NGƯỜI HỌC: ${f.input}\nKẾT QUẢ: ${f.correct?'ĐÚNG':'SAI'}\nĐÁP ÁN ĐÚNG: ${f.expected}\nVÍ DỤ CỦA TỪ: ${(w.examples||[]).map(e=>`${e.en} — ${e.vi}`).join('; ')||'Chưa có'}\n\nHÃY TRẢ LỜI THEO CẤU TRÚC:\n1. Kết luận ngắn về câu trả lời của tôi.\n2. Giải thích vì sao đáp án đúng là đúng, theo ngữ cảnh của câu hỏi.\n3. Phân tích TỪNG lựa chọn A/B/C/D: nghĩa tiếng Việt, loại từ, sắc thái, vì sao đúng hoặc sai. Không bỏ qua lựa chọn sai.\n4. So sánh các từ gần nghĩa/dễ nhầm và chỉ ra bẫy TOEIC.\n5. Mở rộng word family, collocations và ví dụ thực tế nếu có.\n6. Mẹo ghi nhớ và cách phân biệt.\n7. Tạo thêm 3 câu hỏi tương tự, để đáp án ở cuối.\nKhông tự khẳng định nghĩa nếu dữ liệu chưa đủ; hãy ghi rõ phần nào cần tra từ điển.`;
}
function showAIPromptModal(prompt, query='Phân tích nội dung đang học theo ngữ cảnh TOEIC') {
  state.lastAIPrompt=String(prompt||'').trim();state.lastGoogleQuery=String(query||'Phân tích nội dung TOEIC');
  clearAutoAdvance(); state.autoAdvanceCancelled=true; savePracticeSession(); updateAutoAdvanceUI();
  $('#googleSearchSummary').textContent=state.lastGoogleQuery;
  $('#googleSearchContext').value=state.lastAIPrompt;
  $('#googleSearchBackdrop').hidden=false;
  document.body.classList.add('google-search-open');
  $('#runGoogleAIButton').focus();
}
function closeGoogleSearchPanel(){
  $('#googleSearchBackdrop').hidden=true;document.body.classList.remove('google-search-open');
}
function buildOneWayGoogleAIUrl(prompt){
  // udm=50 is the currently observed Google Search AI Mode selector; Google does not document it as a stable public API.
  const url=new URL('https://www.google.com/search');url.searchParams.set('udm','50');url.searchParams.set('q',prompt);url.searchParams.set('hl','vi');return url.href;
}
function openGoogleSearch(){
  const prompt=String(state.lastAIPrompt||$('#googleSearchContext').value||'').trim();
  if(!prompt){toast('Không có nội dung để phân tích.','error');return;}
  const url=buildOneWayGoogleAIUrl(prompt);
  if(url.length>12000){toast('Nội dung quá dài để gửi trong một URL Google. Hãy rút gọn ngữ cảnh hoặc mở AI bằng từ/câu hỏi ngắn hơn.','error');return;}
  const opened=window.open(url,'_blank');
  if(opened){opened.opener=null;closeGoogleSearchPanel();toast('Đã gửi một truy vấn sang Google AI Mode. Đóng tab Google để quay lại bài học.');}
  else {toast('Trình duyệt đã chặn tab mới. Hãy cho phép mở cửa sổ bật lên cho website này.','error');}
}
function openGoogleAIFromPanel(){openGoogleSearch();}

function robotHeadMarkup(extraClass=''){
  return `<svg class="robot-head-svg ${extraClass}" viewBox="0 0 100 100" role="img" aria-label="Robot Buddy" focusable="false">
    <path class="robot-antenna-stem" d="M50 12V6"/><circle class="robot-antenna-light" cx="50" cy="5" r="4"/>
    <path class="robot-shell" d="M17 47C17 26 31 16 50 16s33 10 33 31v18c0 15-13 25-33 25S17 80 17 65V47Z"/>
    <path class="robot-ear" d="M17 48h-5v17h5M83 48h5v17h-5"/>
    <path class="robot-face-panel" d="M25 48c0-13 10-22 25-22s25 9 25 22v16c0 12-10 19-25 19S25 76 25 64V48Z"/>
    <ellipse class="robot-eye" cx="39" cy="52" rx="7" ry="9"/><ellipse class="robot-eye" cx="61" cy="52" rx="7" ry="9"/>
    <circle class="robot-pupil" cx="40" cy="53" r="3.2"/><circle class="robot-pupil" cx="62" cy="53" r="3.2"/>
    <path class="robot-brow robot-brow-left" d="M32 40q7-5 14 0"/><path class="robot-brow robot-brow-right" d="M54 40q7-5 14 0"/>
    <path class="robot-mouth robot-mouth-smile" d="M39 68q11 12 22 0"/>
    <path class="robot-mouth robot-mouth-flat" d="M41 70h18"/>
    <path class="robot-mouth robot-mouth-o" d="M44 68q6-7 12 0q0 9-6 9t-6-9Z"/>
    <path class="robot-mouth robot-mouth-worried" d="M40 74q10-10 20 0"/>
    <path class="robot-cheek robot-cheek-left" d="M27 64q5 4 10 0"/><path class="robot-cheek robot-cheek-right" d="M63 64q5 4 10 0"/>
    <path class="robot-shine" d="M31 30q5-7 12-8"/>
  </svg>`;
}
function setRobotEmotion(emotion='happy'){
  const allowed=['happy','thinking','celebrate','caring','sleepy','greeting','surprised','motivation','concerned','playful','listening','speaking','analyzing'];
  const selected=allowed.includes(emotion)?emotion:'happy';
  $$('#quickHelp .robot-head-svg').forEach(node=>{node.dataset.emotion=selected;});
  const launcher=$('#quickHelpLauncher');if(launcher)launcher.dataset.emotion=selected;
}
function robotReadSettings(){
  try{
    const value=JSON.parse(localStorage.getItem(ROBOT_BUDDY_SETTINGS_KEY)||'null');
    if(value&&typeof value==='object')return value;
  }catch{}
  // Migration reads only the old Robot onboarding preference, never learner progress.
  // This prevents v2.83 users from seeing the first-use Placement question again.
  try{
    const legacy=JSON.parse(localStorage.getItem('toeic:robot-companion-onboarding:v1')||'null');
    const choices={accepted:'start',skipped:'skip',returning:'returning'};
    if(legacy&&typeof legacy==='object'&&choices[legacy.status]){
      const migrated={onboardingChoice:choices[legacy.status],muted:false,migratedFrom:'v2.83.0'};
      localStorage.setItem(ROBOT_BUDDY_SETTINGS_KEY,JSON.stringify({...migrated,updatedAt:Date.now()}));
      return migrated;
    }
  }catch{}
  return {};
}
function robotSaveSettings(patch){
  const current=robotReadSettings();const next={...current,...patch,updatedAt:Date.now()};
  try{localStorage.setItem(ROBOT_BUDDY_SETTINGS_KEY,JSON.stringify(next));}catch(error){console.warn('Không thể lưu tùy chọn Robot Buddy:',error);}
  return next;
}
function updateRobotInsightsToggle(){
  const button=$('#robotInsightsToggle');if(!button)return;
  const enabled=robotReadSettings().learningInsightsEnabled===true;
  button.textContent=enabled?'Phân tích tiến độ: Bật':'Phân tích tiến độ: Tắt';
  button.setAttribute('aria-pressed',String(enabled));
}
function updateRobotMuteToggle(){
  const button=$('#robotMuteToggle');if(!button)return;
  const enabled=!robotBuddyMuted;
  button.textContent=enabled?'Lời nhắc: Bật':'Lời nhắc: Tắt';
  button.setAttribute('aria-pressed',String(enabled));
  button.title=enabled?'Tắt lời nhắc tự động':'Bật lời nhắc tự động';
}
function clearRobotProgressDashboards(){
  document.querySelectorAll('#robotChatLog .robot-progress-dashboard').forEach(node=>node.remove());
}
function toggleRobotInsights(){
  const enabled=robotReadSettings().learningInsightsEnabled===true;
  const nextEnabled=!enabled;
  robotSaveSettings({learningInsightsEnabled:nextEnabled});updateRobotInsightsToggle();
  if(!nextEnabled)clearRobotProgressDashboards();
  appendRobotMessage('bot',nextEnabled?'Mình đã bật phân tích tiến độ. Khi bạn hỏi “Tiến độ học của tôi”, mình sẽ đọc các bản ghi trên thiết bị để tổng hợp.':'Mình đã tắt phân tích tiến độ. Mình sẽ không đọc dữ liệu học tập để phân tích nữa. Bảng phân tích đã hiển thị được gỡ khỏi cuộc trò chuyện, nhưng các tin nhắn khác vẫn được giữ nguyên. Mình vẫn trò chuyện và hướng dẫn chức năng bình thường.');
}
function renderRobotMessageText(content,message){
  content.textContent='';
  const emphasis=/(Robot Buddy|TOEIC Dictionary|Vũ Nguyễn Hoàng Phúc)/giu;
  let cursor=0,match;
  while((match=emphasis.exec(message))){
    if(match.index>cursor)content.append(document.createTextNode(message.slice(cursor,match.index)));
    const strong=document.createElement('strong');strong.textContent=match[0];content.append(strong);cursor=match.index+match[0].length;
  }
  if(cursor<message.length)content.append(document.createTextNode(message.slice(cursor)));
}
function appendRobotActions(bubble,actions=[]){
  if(!Array.isArray(actions)||!actions.length)return;
  const actionRow=document.createElement('div');actionRow.className='robot-chat-actions';
  actions.forEach(action=>{
    const button=document.createElement('button');button.type='button';button.className='robot-chat-action';button.textContent=action.label||'Mở';
    if(action.command)button.dataset.robotCommand=action.command;
    if(action.page)button.dataset.robotPage=action.page;
    actionRow.append(button);
  });
  if(actionRow.childNodes.length)bubble.append(actionRow);
}
function appendRobotMessage(role,text,actions=[],options={}){
  const log=$('#robotChatLog');if(!log)return null;
  const item=document.createElement('article');item.className=`robot-chat-message ${role==='user'?'is-user':'is-bot'}`;
  if(role!=='user'){
    const avatar=document.createElement('span');avatar.className='robot-chat-avatar';avatar.innerHTML=robotHeadMarkup();
    item.append(avatar);
  }
  const bubble=document.createElement('div');bubble.className='robot-chat-bubble';
  const content=document.createElement('p');
  const message=String(text||'');
  if(role==='user')content.textContent=message;
  else if(options.stream){item.setAttribute('aria-busy','true');content.classList.add('is-streaming');content.textContent='';}
  else renderRobotMessageText(content,message);
  bubble.append(content);
  if(!options.deferActions)appendRobotActions(bubble,actions);
  item.append(bubble);log.append(item);log.scrollTop=log.scrollHeight;
  return options.stream?{item,content,bubble}:item;
}
function finishRobotStream(){
  const active=robotStreamState;if(!active)return;
  if(active.timer)clearTimeout(active.timer);
  robotStreamState=null;
  active.item.removeAttribute('aria-busy');
  active.content.classList.remove('is-streaming');
  renderRobotMessageText(active.content,active.message);
  appendRobotActions(active.bubble,active.actions);
  const log=$('#robotChatLog');if(log)log.scrollTop=log.scrollHeight;
  if(typeof active.onComplete==='function')active.onComplete();
}
function streamRobotMessage(text,actions=[],onComplete=null){
  finishRobotStream();
  const message=String(text||'');
  const rendered=appendRobotMessage('bot',message,[],{stream:true,deferActions:true});
  if(!rendered)return null;
  const segmenter=typeof Intl!=='undefined'&&typeof Intl.Segmenter==='function'?new Intl.Segmenter('vi',{granularity:'grapheme'}):null;
  const characters=segmenter?Array.from(segmenter.segment(message),part=>part.segment):Array.from(message);
  const active={...rendered,message,actions,onComplete,timer:null,index:0,characters};
  robotStreamState=active;
  const log=$('#robotChatLog');
  const finish=()=>{if(robotStreamState===active)finishRobotStream();};
  const reducedMotion=Boolean(window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches);
  if(reducedMotion||active.characters.length<2){finish();return rendered.item;}
  const tick=()=>{
    if(robotStreamState!==active)return;
    const character=active.characters[active.index]||'';
    active.index=Math.min(active.characters.length,active.index+(/[.!?…。！？\n]/u.test(character)?1:2));
    active.content.textContent=active.characters.slice(0,active.index).join('');
    if(log)log.scrollTop=log.scrollHeight;
    if(active.index>=active.characters.length){finish();return;}
    const pause=/[.!?…。！？]/u.test(character)?125:28;
    active.timer=setTimeout(tick,pause);
  };
  active.timer=setTimeout(tick,18);
  return rendered.item;
}

function appendRobotChoiceButtons(choices){
  const log=$('#robotChatLog');if(!log)return;
  const row=document.createElement('div');row.className='robot-onboarding-choices';
  choices.forEach(choice=>{
    const button=document.createElement('button');button.type='button';button.className=choice.primary?'robot-chat-action is-primary':'robot-chat-action';
    button.textContent=choice.label;button.dataset.robotChoice=choice.value;row.append(button);
  });
  log.append(row);log.scrollTop=log.scrollHeight;
}
function renderRobotQuickPrompts(){
  const root=$('#robotQuickPrompts');if(!root||!robotBuddyEngine)return;
  root.innerHTML='';
  robotBuddyEngine.quickPrompts.slice(0,12).forEach(prompt=>{
    const button=document.createElement('button');button.type='button';button.className='robot-prompt-chip';button.textContent=prompt.label;button.dataset.robotPrompt=prompt.text;root.append(button);
  });
}
function setRobotTyping(show){
  const node=$('#robotTyping');if(node)node.hidden=!show;
  if(show)setRobotEmotion('thinking');
}
function getRobotLearningSnapshot(){
  return {words:state.words,vocabularyProgress:state.progress,flashProgress:state.flashProgress,grammarItems:state.grammarLessons,grammarProgress:state.grammarProgress,readingItems:state.readings,readingProgress:state.readingProgress,listeningItems:state.listening,listeningProgress:state.listeningProgress,foundationItems:state.foundationLessons,foundationProgressMap:state.foundationProgress,foundationReadingItems:state.foundationReadingPassages,foundationReadingProgress:state.foundationReadingProgress,foundationListeningItems:state.foundationListeningClips,foundationListeningProgress:state.foundationListeningProgress,objectiveProgress:state.objectiveProgress,objectiveResourceMap:state.objectiveResourceMap,mockHistory:state.mockHistory};
}
function getRobotLearningInsightsNow(){
  if(robotReadSettings().learningInsightsEnabled!==true)return null;
  return buildRobotLearningInsights(getRobotLearningSnapshot());
}
function getRobotInsightActions(insights){
  if(!insights?.hasEvidence)return [];
  const routes=[
    {test:/tu vung/,page:'dictionary',label:'Mở Từ vựng'},
    {test:/flashcard/,page:'flashcards',label:'Mở Flashcard'},
    {test:/ngu phap/,page:'grammar',label:'Mở Ngữ pháp'},
    {test:/doc hieu|reading/,page:'reading',label:'Mở Đọc hiểu'},
    {test:/nghe hieu|listening/,page:'listening',label:'Mở Nghe hiểu'},
    {test:/foundation|nen tang|pre a1|a1 |a2 /,page:'foundation',label:'Mở Foundation'},
    {test:/thi thu|mock/,page:'mock',label:'Mở Thi thử'},
    {test:/on nho lai|recall/,page:'practice',label:'Mở Ôn tập'}
  ];
  const actions=[],seen=new Set();
  for(const group of ['review','practice','learn']){
    for(const item of insights.items?.[group]||[]){
      const area=String(item.area||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
      const route=routes.find(entry=>entry.test.test(area));
      if(route&&!seen.has(route.page)){
        seen.add(route.page);actions.push({label:route.label,page:route.page});
      }
      if(actions.length>=4)return actions;
    }
  }
  return actions;
}
function appendRobotProgressDashboard(insights,anchor=null,actions=[]){
  const log=$('#robotChatLog');if(!log||!insights)return null;
  const dashboard=document.createElement('section');dashboard.className='robot-progress-dashboard';dashboard.setAttribute('aria-label','Bảng tiến độ học tập cục bộ');
  const heading=document.createElement('div');heading.className='robot-progress-dashboard-heading';
  const title=document.createElement('strong');title.textContent='Bản đồ tiến độ học tập';
  const note=document.createElement('small');note.textContent='Số liệu trên thiết bị · không phải điểm TOEIC chính thức';
  heading.append(title,note);dashboard.append(heading);
  const totals=document.createElement('div');totals.className='robot-progress-totals';
  const totalCards=[['Cần học',insights.totals?.learn||0,'learn'],['Cần luyện',insights.totals?.practice||0,'practice'],['Cần ôn',insights.totals?.review||0,'review']];
  for(const [label,value,kind] of totalCards){const card=document.createElement('div');card.className=`robot-progress-total is-${kind}`;const caption=document.createElement('small');caption.textContent=label;const number=document.createElement('strong');number.textContent=Number(value).toLocaleString('vi-VN');card.append(caption,number);totals.append(card);}
  dashboard.append(totals);
  const list=document.createElement('div');list.className='robot-progress-section-list';
  for(const section of insights.sections||[]){
    const row=document.createElement('article');row.className='robot-progress-section';
    const top=document.createElement('div');top.className='robot-progress-section-top';
    const name=document.createElement('strong');name.textContent=section.name;
    const metric=document.createElement('span');
    if(Number.isFinite(section.totalUnits)&&section.totalUnits>0){metric.textContent=`${section.studiedUnits||0}/${section.totalUnits} mục có lượt học`;}else if(section.name==='Thi thử'){metric.textContent=`${section.studiedUnits||0} đề hoàn thành`;}else{metric.textContent='Chưa có mẫu số';}
    top.append(name,metric);row.append(top);
    if(Number.isFinite(section.coveragePercent)){
      const track=document.createElement('div');track.className='robot-progress-track';track.setAttribute('role','progressbar');track.setAttribute('aria-label',`${section.name}: mức độ có lượt học`);track.setAttribute('aria-valuemin','0');track.setAttribute('aria-valuemax','100');track.setAttribute('aria-valuenow',String(section.coveragePercent));
      const fill=document.createElement('span');fill.style.width=`${Math.max(0,Math.min(100,section.coveragePercent))}%`;track.append(fill);row.append(track);
      const foot=document.createElement('div');foot.className='robot-progress-section-foot';
      const coverage=document.createElement('small');coverage.textContent=`Mức độ đã có lượt học: ${section.coveragePercent}%`;
      const accuracy=document.createElement('small');accuracy.textContent=section.accuracy===null||section.attempted<5?`Chưa đủ dữ liệu đánh giá độ chính xác${section.attempted?` · ${section.attempted} câu đã trả lời`:''}`:`${section.accuracy}% đúng · ${section.attempted} câu`;
      foot.append(coverage,accuracy);row.append(foot);
    }else{
      const foot=document.createElement('small');foot.className='robot-progress-section-foot-note';foot.textContent=section.accuracy===null?`Chưa có đủ bài thi đã hoàn thành để đánh giá.`:`Độ chính xác trung bình nội bộ: ${section.accuracy}% · ${section.attempted} câu`;
      row.append(foot);
    }
    const chips=document.createElement('div');chips.className='robot-progress-section-chips';
    for(const [label,key] of [['Học', 'learn'],['Luyện','practice'],['Ôn','review']]){const value=Number(section[key])||0;if(!value)continue;const chip=document.createElement('span');chip.className=`is-${key}`;chip.textContent=`${label}: ${value}`;chips.append(chip);}
    if(chips.childNodes.length)row.append(chips);
    list.append(row);
  }
  dashboard.append(list);
  const foot=document.createElement('p');foot.className='robot-progress-dashboard-foot';foot.textContent='Tỷ lệ trên là số bài/tài nguyên đã có ít nhất một lượt học so với kho đang có, không phải tỷ lệ hoàn thành khóa học. Ngưỡng Cần luyện/Cần ôn là tín hiệu gợi ý nội bộ; khi dữ liệu ít, hệ thống không kết luận điểm yếu.';
  dashboard.append(foot);
  if(Array.isArray(actions)&&actions.length){
    const actionRow=document.createElement('div');actionRow.className='robot-progress-actions';
    actions.forEach(action=>{if(!action?.page)return;const button=document.createElement('button');button.type='button';button.className='robot-chat-action';button.textContent=action.label||'Mở nội dung';button.dataset.robotPage=action.page;actionRow.append(button);});
    if(actionRow.childNodes.length)dashboard.append(actionRow);
  }
  if(anchor?.parentNode)anchor.after(dashboard);else log.append(dashboard);
  log.scrollTop=log.scrollHeight;return dashboard;
}
function runRobotProgressAnalysis(){
  if(robotReadSettings().learningInsightsEnabled!==true){streamRobotMessage('Phân tích tiến độ đang tắt. Bạn có thể bật lại bằng nút “Phân tích tiến độ: Tắt” ở phía trên.');return;}
  const insights=getRobotLearningInsightsNow();
  appendRobotMessage('user','Phân tích tiến độ học tập của tôi.');
  setRobotEmotion('analyzing');
  streamRobotMessage('Mình sẽ tổng hợp những dấu vết học tập có sẵn trên thiết bị. Sau phần giới thiệu ngắn này, bạn sẽ thấy bảng riêng cho Cần học, Cần luyện và Cần ôn.',[],()=>{
    appendRobotProgressDashboard(insights,null,getRobotInsightActions(insights));setRobotEmotion('analyzing');
  });
}
function getRobotAppContext(){
  const page=state.activePage||'dashboard';
  const pageLabels={dashboard:'Trang chủ',dictionary:'Từ vựng',flashcards:'Flashcard',practice:'Ôn tập',mock:'Thi thử TOEIC',grammar:'Ngữ pháp',reading:'Đọc hiểu',listening:'Nghe hiểu',foundation:'Lộ trình Foundation',settings:'Cấu hình',data:'Quản lý dữ liệu'};
  let currentItem=null;
  if(page==='dictionary'){
    const word=state.words.find(item=>item.id===state.activeWordId);
    if(word){const sense=getPrimarySense(word);currentItem={kind:'word',title:displayWord(word.word),snippet:sense?.meaning_vi||sense?.definition_en||''};}
  }else if(page==='flashcards'){
    const word=state.flashSession?.words?.[state.flashSession.index];
    if(word)currentItem={kind:'flashcard',title:displayWord(word.word),snippet:getPrimarySense(word)?.meaning_vi||''};
  }else if(page==='practice'){
    const question=state.currentQuestion;
    if(question)currentItem={kind:'question',title:question.word?displayWord(question.word):'Câu hỏi luyện tập',snippet:question.prompt||question.question||''};
  }else if(page==='grammar'){
    const lesson=state.grammarLessons.find(item=>item.id===state.activeGrammarLesson);
    if(lesson)currentItem={kind:'lesson',title:lesson.title,snippet:lesson.summary||''};
  }else if(page==='reading'){
    const reading=state.readings.find(item=>item.id===state.activeReading);
    if(reading)currentItem={kind:'reading',title:reading.title,snippet:`${reading.part||'Reading'} · ${reading.documentType||reading.topic||''}`};
  }else if(page==='listening'){
    const listening=state.listening.find(item=>item.id===state.activeListening);
    if(listening)currentItem={kind:'listening',title:listening.title,snippet:`${listening.part||'Listening'} · ${listening.topic||''}`};
  }else if(page==='foundation'){
    const lesson=state.foundationLessons.find(item=>item.id===state.activeFoundationLesson);
    if(lesson)currentItem={kind:'foundation',title:lesson.title,snippet:lesson.objective||lesson.focus||''};
  }
  return {page,pageLabel:pageLabels[page]||'khu vực hiện tại',currentItem};
}
function getRobotContextualNudge(category){
  const context=getRobotAppContext(),item=context.currentItem;
  if(item?.title){
    const tips={dictionary:'Thử nghe phát âm và tự đặt một câu với từ này nhé.',flashcards:'Thử nhớ nghĩa trước khi lật thẻ nhé.',practice:'Hãy tìm từ khóa và tự loại trừ từng lựa chọn nhé.',grammar:'Xem ví dụ rồi tự làm một câu để kiểm tra nhé.',reading:'Tìm bằng chứng trong bài đọc thay vì chỉ đoán theo từ khóa nhé.',listening:'Lượt nghe tiếp theo, thử tập trung vào mục đích và hành động của người nói nhé.',foundation:'Hoàn thành phần tự kiểm tra nhỏ trước khi sang bài tiếp theo nhé.'};
    return `Bạn vẫn đang ở ${context.pageLabel} với nội dung “${item.title}”. ${tips[context.page]||'Mình có thể hỗ trợ nếu bạn cần.'}`;
  }
  return robotBuddyEngine.pick(category);
}
function sendRobotMessage(rawText){
  const text=String(rawText||'').trim();if(!text||!robotBuddyEngine)return;
  finishRobotStream();
  if(robotSpeakingTimer){clearTimeout(robotSpeakingTimer);robotSpeakingTimer=null;}
  if(robotTypingTimer){clearTimeout(robotTypingTimer);robotTypingTimer=null;}
  setRobotTyping(false);
  appendRobotMessage('user',text);
  // Keep the quick-prompt menu available during the whole chat session.
  const input=$('#robotChatInput');if(input)input.value='';
  setRobotTyping(true);
  const intent=robotBuddyEngine.classify(text);
  const settings=robotReadSettings();
  const reply=robotBuddyEngine.reply(text,getRobotAppContext());
  let progressInsights=null;
  if(intent.intent==='insights'&&settings.learningInsightsEnabled===true){
    progressInsights=getRobotLearningInsightsNow();
    reply.actions=getRobotInsightActions(progressInsights);
  }else if(intent.intent==='insights'&&settings.learningInsightsEnabled!==true){
    reply.text='Phân tích tiến độ đang tắt. Bạn có thể bật lại bằng nút “Phân tích tiến độ” phía trên; các hướng dẫn học tập thông thường vẫn hoạt động.';
  }
  robotTypingTimer=setTimeout(()=>{
    robotTypingTimer=null;setRobotTyping(false);setRobotEmotion('speaking');
    const onComplete=()=>{
      if(robotSpeakingTimer)clearTimeout(robotSpeakingTimer);
      robotSpeakingTimer=setTimeout(()=>setRobotEmotion(reply.emotion||'happy'),220);
    };
    if(progressInsights){
      streamRobotMessage('Mình đang tổng hợp những dấu vết học tập đã có trên thiết bị. Bảng dưới đây tách riêng phần cần học, cần luyện và cần ôn; đây là gợi ý nội bộ, không phải điểm TOEIC chính thức.',[],()=>{
        appendRobotProgressDashboard(progressInsights,null,reply.actions||[]);onComplete();
      });
    }else streamRobotMessage(reply.text,reply.actions||[],onComplete);
  },360);
}

function robotShowWelcome(){
  const log=$('#robotChatLog');if(!log||robotChatInitialized)return;
  robotChatInitialized=true;log.innerHTML='';
  const enabled=robotReadSettings().learningInsightsEnabled===true;
  appendRobotMessage('bot','Xin chào! Mình là Robot Buddy 🤖. Mình có thể trò chuyện, giới thiệu chức năng và hướng dẫn bạn sử dụng ứng dụng. Nếu bạn chủ động bật Phân tích tiến độ, mình có thể tổng hợp dữ liệu học đã lưu ngay trên thiết bị để gợi ý nội dung cần học, luyện và ôn. Mình không gửi dữ liệu học tập ra ngoài và không phải chatbot AI trực tuyến.',[{label:enabled?'Phân tích tiến độ của tôi':'Bật phân tích tiến độ',command:enabled?'analyze-progress':'enable-progress-analysis'}]);
  const settings=robotReadSettings();
  if(!settings.onboardingChoice){
    appendRobotMessage('bot','Trước khi bắt đầu, bạn có muốn làm bài đánh giá đầu vào có sẵn để tham khảo điểm bắt đầu không?');
    appendRobotChoiceButtons([
      {label:'Có, bắt đầu đánh giá',value:'start',primary:true},
      {label:'Không cần, bỏ qua',value:'skip'}
    ]);
  }else{
    appendRobotMessage('bot',robotBuddyEngine.pick('greeting'));
    renderRobotQuickPrompts();
  }
}
function setQuickHelpOpen(open){
  const panel=$('#quickHelpPanel'),launcher=$('#quickHelpLauncher');if(!panel||!launcher)return;
  panel.hidden=!open;launcher.setAttribute('aria-expanded',String(Boolean(open)));launcher.classList.toggle('is-open',Boolean(open));
  launcher.title=open?'Ẩn Robot Buddy':'Mở Robot Buddy';
  if(open){hideRobotIdleNudge();robotShowWelcome();launcher.classList.remove('has-update');setRobotEmotion('greeting');$('#robotChatInput')?.focus({preventScroll:true});}
  else{scheduleRobotIdle(90000);}
}
function toggleQuickHelp(){setQuickHelpOpen($('#quickHelpPanel')?.hidden!==false);}
function hideRobotIdleNudge(){const node=$('#robotIdleNudge');if(node)node.hidden=true;if(robotNudgeTimer){clearTimeout(robotNudgeTimer);robotNudgeTimer=null;}}
function robotCanNudge(){
  if(document.hidden||!document.hasFocus())return false;
  if(robotBuddyMuted||Date.now()<robotIdleSnoozeUntil)return false;
  if($('#quickHelp')?.hidden||$('#quickHelpPanel')&&!$('#quickHelpPanel').hidden)return false;
  if(learningFocusState.active)return false;
  if(state.activePage==='mock'&&state.mockExam?.status==='active')return false;
  for(const selector of ['#modalLayer','#learningFocusBackdrop','#installInviteBackdrop','#googleSearchBackdrop','#mobileGroupMenu']){
    const node=$(selector);if(node&&!node.hidden)return false;
  }
  const active=document.activeElement;
  if(active&&active.matches('input,textarea,select,[contenteditable="true"]'))return false;
  if(window.speechSynthesis?.speaking||window.speechSynthesis?.pending)return false;
  const now=Date.now();robotIdleNoticeTimes=robotIdleNoticeTimes.filter(time=>now-time<3600000);
  return robotIdleNoticeTimes.length<3;
}
function scheduleRobotIdle(delay=90000){
  if(robotIdleTimer)clearTimeout(robotIdleTimer);
  if(robotBuddyMuted)return;
  const now=Date.now();robotIdleNoticeTimes=robotIdleNoticeTimes.filter(time=>now-time<3600000);
  if(robotIdleNoticeTimes.length>=3){const wait=Math.max(1000,robotIdleNoticeTimes[0]+3600000-now+1000);robotIdleTimer=setTimeout(()=>scheduleRobotIdle(90000),wait);return;}
  robotIdleTimer=setTimeout(()=>{
    if(!robotCanNudge()){scheduleRobotIdle(30000);return;}
    showRobotIdleNudge();
  },Math.max(1000,delay));
}
function showRobotIdleNudge(){
  const root=$('#robotIdleNudge'),message=$('#robotIdleMessage');if(!root||!message||!robotBuddyEngine)return;
  const category=robotIdleStage===0?'caring':robotIdleStage===1?'encouragement':'caring';
  const context=getRobotAppContext();
  if(context.currentItem){
    message.textContent=getRobotContextualNudge(category);
  }else{
    const insights=getRobotLearningInsightsNow();
    if(insights?.hasEvidence&&insights.totals.review>0&&robotIdleStage===0){
      message.textContent=`Bạn đang có ${insights.totals.review} mục đến hạn ôn trên thiết bị. Khi thuận tiện, hãy mở mình và hỏi “Tiến độ học của tôi” nhé!`;
    }else if(insights?.hasEvidence&&insights.totals.practice>0&&robotIdleStage===1){
      message.textContent=`Mình thấy có ${insights.totals.practice} mục nên luyện thêm theo kết quả đã lưu. Bạn cứ học từng phần nhỏ nhé!`;
    }else{message.textContent=robotBuddyEngine.pick(category);}
  }
  root.hidden=false;setRobotEmotion(robotIdleStage===1?'motivation':'caring');
  robotIdleNoticeTimes.push(Date.now());robotIdleStage=Math.min(2,robotIdleStage+1);
  if(robotNudgeTimer)clearTimeout(robotNudgeTimer);
  robotNudgeTimer=setTimeout(()=>{hideRobotIdleNudge();scheduleRobotIdle(robotIdleStage===1?300000:600000);},14000);
}
function robotActivity(event){
  if(event?.target?.closest?.('#quickHelp'))return;
  hideRobotIdleNudge();
  scheduleRobotIdle(90000);
}
function initializeRobotIdleWatchers(){
  const onActivity=event=>robotActivity(event);
  ['pointerdown','keydown','touchstart','wheel','scroll'].forEach(type=>document.addEventListener(type,onActivity,{passive:true,capture:true}));
  document.addEventListener('visibilitychange',()=>{hideRobotIdleNudge();if(!document.hidden)scheduleRobotIdle(90000);else if(robotIdleTimer)clearTimeout(robotIdleTimer);});
  window.addEventListener('focus',()=>scheduleRobotIdle(90000));
  window.addEventListener('blur',()=>{if(robotIdleTimer)clearTimeout(robotIdleTimer);hideRobotIdleNudge();});
  scheduleRobotIdle(90000);
}
function handleRobotChoice(choice){
  if(choice!=='start'&&choice!=='skip')return;
  robotSaveSettings({onboardingChoice:choice,muted:robotBuddyMuted});
  if(choice==='start'){
    appendRobotMessage('user','Có, bắt đầu đánh giá đầu vào.');
    streamRobotMessage('Được rồi! Mình sẽ mở bài Placement hiện có. Đây là bài đánh giá tham khảo để gợi ý điểm bắt đầu, không phải chứng chỉ CEFR hay điểm ETS.');
    setQuickHelpOpen(false);setTimeout(()=>startPlacementDiagnostic(),250);return;
  }
  appendRobotMessage('user','Không cần, bỏ qua.');
  streamRobotMessage('Không sao cả! Bạn có thể vào học ngay. Khi cần tìm chức năng hoặc muốn trò chuyện, hãy nhấn vào đầu mình nhé.');
  renderRobotQuickPrompts();
}
function handleRobotCommand(command,page=''){
  if(command==='analyze-progress'){runRobotProgressAnalysis();return;}
  if(command==='enable-progress-analysis'){robotSaveSettings({learningInsightsEnabled:true});updateRobotInsightsToggle();runRobotProgressAnalysis();return;}
  if(command==='placement'){setQuickHelpOpen(false);startPlacementDiagnostic();return;}
  if(page){setQuickHelpOpen(false);navigate(page);return;}
}
function handleRobotInput(event){
  event.preventDefault();const input=$('#robotChatInput');if(!input)return;sendRobotMessage(input.value);
}
function initializeRobotCompanion(){
  if(robotBuddyEngine)return;
  const response=fetch(releaseDataUrl('./data/robot/robot-library.json'),{cache:'reload'})
    .then(result=>{if(!result.ok)throw new Error(`HTTP ${result.status}`);return result.json();})
    .catch(error=>{console.warn('Không tải được thư viện Robot Buddy; dùng bộ câu dự phòng.',error);return null;});
  return response.then(library=>{
    robotBuddyEngine=createRobotBuddy(library);
    const settings=robotReadSettings();robotBuddyMuted=settings.muted===true;
    updateRobotMuteToggle();updateRobotInsightsToggle();
    if(!settings.onboardingChoice)setQuickHelpOpen(true);
    else robotShowWelcome();
    initializeRobotIdleWatchers();
  });
}
function toggleRobotMute(){
  robotBuddyMuted=!robotBuddyMuted;robotSaveSettings({muted:robotBuddyMuted});
  updateRobotMuteToggle();
  hideRobotIdleNudge();
  if(robotBuddyMuted&&robotIdleTimer){clearTimeout(robotIdleTimer);robotIdleTimer=null;}
  if(!robotBuddyMuted)scheduleRobotIdle(90000);
}
function detectDeviceProfile(){
  const ua=String(navigator.userAgent||'');
  const uaData=navigator.userAgentData||{};
  const platform=String(uaData.platform||navigator.platform||'');
  const touchPoints=Number(navigator.maxTouchPoints||0);
  const isIPad=/iPad/i.test(ua)||(/MacIntel/i.test(platform)&&touchPoints>1);
  const isAndroid=/Android/i.test(ua)||/Android/i.test(platform);
  const isTablet=isIPad||/Tablet|PlayBook|Silk/i.test(ua)||(isAndroid&&!/Mobile/i.test(ua));
  const isMobile=!isTablet&&(uaData.mobile===true||/iPhone|iPod|Windows Phone|Android.*Mobile|Mobile/i.test(ua));
  let device='Laptop / PC',symbol='icon-device-laptop';
  if(isTablet){device='Máy tính bảng';symbol='icon-device-tablet';}
  else if(isMobile){device='Điện thoại';symbol='icon-device-mobile';}
  let os='Thiết bị cá nhân';
  if(isIPad)os='iPadOS';
  else if(isAndroid)os='Android';
  else if(/iPhone|iPod/i.test(ua))os='iOS';
  else if(/Windows/i.test(platform)||/Windows NT/i.test(ua))os='Windows';
  else if(/Mac/i.test(platform)||/Mac OS/i.test(ua))os='macOS';
  else if(/CrOS|Chrome OS/i.test(ua+' '+platform))os='ChromeOS';
  else if(/Linux/i.test(platform)||/Linux/i.test(ua))os='Linux';
  return {device,os,symbol};
}
function renderDeviceGreeting(){
  const greeting=$('#deviceGreeting');
  if(!greeting)return;
  const profile=detectDeviceProfile();
  const name=$('#deviceGreetingName');
  const platform=$('#deviceGreetingPlatform');
  const use=$('#deviceGreetingIcon use');
  if(name)name.textContent=profile.device;
  if(platform)platform.textContent=profile.os;
  if(use)use.setAttribute('href',`#${profile.symbol}`);
  greeting.setAttribute('aria-label',`Xin chào! Bạn đang sử dụng ${profile.device}, hệ điều hành ${profile.os}.`);
  greeting.title=`Xin chào! Thiết bị hiện tại: ${profile.device} · ${profile.os}`;
}

function updateDate(){const now=new Date();$('#todayLabel').textContent=new Intl.DateTimeFormat('vi-VN',{weekday:'long',day:'2-digit',month:'long',year:'numeric'}).format(now);}
function showServiceWorkerUpdateBanner(registration){
  const waiting=registration?.waiting,banner=$('#appUpdateBanner'),button=$('#appUpdateApply');
  if(!waiting||!navigator.serviceWorker.controller||!banner||!button)return;
  banner.hidden=false;
  button.disabled=false;
  button.textContent='Tải lại';
  button.onclick=()=>{
    const pending=registration.waiting;
    if(!pending){banner.hidden=true;return;}
    button.disabled=true;
    button.textContent='Đang cập nhật...';
    pending.postMessage({type:'SKIP_WAITING'});
  };
}
function watchServiceWorkerUpdates(registration){
  const checkWaiting=()=>showServiceWorkerUpdateBanner(registration);
  checkWaiting();
  registration.addEventListener('updatefound',()=>{
    const installing=registration.installing;
    if(!installing)return;
    installing.addEventListener('statechange',()=>{
      if(installing.state==='installed'&&navigator.serviceWorker.controller)checkWaiting();
    });
  });
}
async function registerSW(){
  if(!('serviceWorker'in navigator))return null;
  const hadController=Boolean(navigator.serviceWorker.controller);
  let reloadedForRelease=false;
  const reloadAfterWorkerSwap=()=>{
    if(!hadController||reloadedForRelease)return;
    reloadedForRelease=true;
    // Reload only after a user-approved waiting worker takes control.
    window.location.reload();
  };
  navigator.serviceWorker.addEventListener('controllerchange',reloadAfterWorkerSwap,{once:true});
  try{
    const registration=await navigator.serviceWorker.register('./sw.js',{scope:'./',updateViaCache:'none'});
    state.swRegistration=registration;
    watchServiceWorkerUpdates(registration);
    await navigator.serviceWorker.ready;
    try{await registration.update();}catch(updateError){console.warn('Không kiểm tra được bản Service Worker mới:',updateError);}
    showServiceWorkerUpdateBanner(registration);
    state.notificationProvider=new LocalNotificationProvider(()=>state.swRegistration);
    return registration;
  }catch(err){
    console.warn('Service Worker chưa đăng ký được:',err);
    navigator.serviceWorker.removeEventListener('controllerchange',reloadAfterWorkerSwap);
    state.notificationProvider=new LocalNotificationProvider(()=>null);
    return null;
  }
}
async function init(){try{const shellRelease=document.querySelector('meta[name="app-release"]')?.content;if(shellRelease!==APP_RELEASE_VERSION)throw new Error(`HTML/JavaScript release mismatch: HTML ${shellRelease||'missing'} · JS ${APP_RELEASE_VERSION}`);bindEvents();updateDate();renderDeviceGreeting();await loadData();await initializePractice();loadMockState();if(state.pendingMockResult&&!state.pendingSinglePractice)showPendingMockResult();await initializeRobotCompanion();}catch(err){console.error('TOEIC startup aborted:',err);const metric=$('#metricWords');if(metric)metric.textContent='!';const status=$('#metricWordsStatus');if(status){status.textContent=`KHỞI TẠO CHƯA HOÀN TẤT · ${err.message}`;status.dataset.integrity='mismatch';}const resultCount=$('#resultCount');if(resultCount)resultCount.textContent='Không thể khởi tạo ứng dụng';const updateBanner=$('#appUpdateBanner');if(updateBanner){updateBanner.hidden=false;const copy=updateBanner.querySelector('.app-update-copy small');if(copy)copy.textContent='Bản ứng dụng chưa đồng bộ. Hãy tải lại để nhận cùng một phiên bản.';}toast(`Không khởi tạo được ứng dụng: ${err.message}`,'error');}await registerSW();initializeInstallInvite();}
init();
