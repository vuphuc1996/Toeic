import { LocalNotificationProvider } from './notification-provider.js';
const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const icon = (name, cls='ui-icon') => `<svg class="${cls}" aria-hidden="true"><use href="#icon-${name}"></use></svg>`;
const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const DB_NAME = 'toeic-vocabulary-phase1';
const DB_STORE = 'workspace';
const state = { words: [], baseWords: [], categories: [], relatedTerms: new Map(), activePage: 'dashboard', activeLetter: '', deferredInstall: null, localWorkspace: false, progress: {}, reminder: null, settings: { autoNextEnabled: true, autoNextDelaySeconds: 3 }, notificationProvider: null, swRegistration: null, currentQuestion: null, questionAnswered: false, sessionSeenIds: [], lastFeedback: null, autoAdvanceTimer: null, autoAdvanceAt: null, autoAdvanceRemaining: null, autoAdvanceCancelled: false };

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
  const el=document.createElement('div'); el.className=`toast ${type==='error'?'error':''}`; el.textContent=message; $('#toastRegion').append(el); setTimeout(()=>el.remove(),3400);
}
function normalizeText(value='') { return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/đ/g,'d').trim(); }
function escapeHtml(value='') { return String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch])); }
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
  return {id,word,phonetic:raw.phonetic&&typeof raw.phonetic==='object'?raw.phonetic:{us:String(raw.ipa||'')},senses,topics:[...new Set(topics)],word_family:Array.isArray(raw.word_family)?raw.word_family:[],verb_forms:raw.verb_forms&&typeof raw.verb_forms==='object'?raw.verb_forms:null,examples:examples.map(e=>({en:String(e.en||''),vi:String(e.vi||'')})),collocations:Array.isArray(raw.collocations)?raw.collocations:String(raw.collocations||'').split(',').map(x=>x.trim()).filter(Boolean)};
}
async function loadData() {
  const manifestResponse=await fetch('./data/manifest.json',{cache:'no-store'});
  if(!manifestResponse.ok) throw new Error(`Không đọc được manifest.json (${manifestResponse.status}).`);
  const manifest=await manifestResponse.json();
  const [categoryResponse,relatedResponse,...letterResponses]=await Promise.all([fetch(manifest.categories),fetch('./data/related-terms.json').catch(()=>null),...manifest.letters.map(x=>fetch(x.file))]);
  if(!categoryResponse.ok) throw new Error('Không đọc được categories.json.');
  const categoryData=await categoryResponse.json();
  if(relatedResponse?.ok){const relatedData=await relatedResponse.json();state.relatedTerms=new Map((relatedData.terms||[]).map(item=>[normalizedAnswer(item.term),item]));}else{state.relatedTerms=new Map();}
  const loaded=[];
  for(let i=0;i<letterResponses.length;i++){
    const response=letterResponses[i];
    if(!response.ok) throw new Error(`Không đọc được dữ liệu chữ ${manifest.letters[i].letter}.`);
    const payload=await response.json();
    if(!Array.isArray(payload.words)) throw new Error(`Tệp ${manifest.letters[i].letter}.json không có mảng words.`);
    loaded.push(...payload.words.map(normalizeRecord));
  }
  state.baseWords=sortWords(loaded); state.categories=categoryData.categories||[];
  const saved=await dbGet('workspace');
  if(Array.isArray(saved)){state.words=sortWords(saved.map(normalizeRecord));state.localWorkspace=true;}
  else {state.words=[...state.baseWords];state.localWorkspace=false;}
  updateOverview(); populateFilters(); renderDictionary(); renderDataTable(); updateStorageLabel();
}
function updateOverview(){
  $('#metricWords').textContent=state.words.length.toLocaleString('vi-VN');
  $('#metricTopics').textContent=state.categories.length.toLocaleString('vi-VN');
  const letters=new Set(state.words.map(w=>w.word[0].toUpperCase()));
  $('#metricLetters').textContent=`${letters.size}/26`;
  $('#totalDataFooter').textContent=state.words.length.toLocaleString('vi-VN');
  const dash=$('#dashboardAlphabet');
  dash.innerHTML=ALPHABET.map(l=>{const n=state.words.filter(w=>w.word[0].toUpperCase()===l).length;return `<button class="letter-tile ${n?'has-words':''}" data-letter="${l}"><strong>${l}</strong><small>${n}</small></button>`}).join('');
  if(state.progress) updatePracticeStats();
}
function populateFilters(){
  const options=state.categories.map(c=>`<option value="${escapeHtml(c.id)}">${escapeHtml(c.label)}</option>`).join('');
  $('#topicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+options;
  $('#dataTopicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+options;
  $('#dataLetterFilter').innerHTML='<option value="">Tất cả A–Z</option>'+ALPHABET.map(l=>`<option value="${l}">${l}</option>`).join('');
}
function navigate(page){
  if(state.activePage==='practice'&&page!=='practice') pauseAutoAdvance();
  state.activePage=page;
  $$('.page').forEach(p=>p.classList.toggle('active',p.id===`page-${page}`));
  $$('[data-page]').forEach(b=>b.classList.toggle('active',b.dataset.page===page));
  const titles={dashboard:'Tổng quan',dictionary:'Từ vựng',practice:'Ôn tập',data:'Quản lý dữ liệu',settings:'Cấu hình'};
  $('#pageTitle').textContent=titles[page]||'Tổng quan';
  if(page==='dictionary') renderDictionary();
  if(page==='data') renderDataTable();
  if(page==='practice'){if(!state.currentQuestion)nextQuestion();renderQuestion();updatePracticeStats();resumeAutoAdvance();}
  if(page==='settings') renderReminderStatus();
  window.scrollTo({top:0,behavior:'smooth'});
}
function filteredWords(){
  const query=normalizeText($('#dictionarySearch').value); const topic=$('#topicFilter').value; const pos=$('#posFilter').value;
  return sortWords(state.words.filter(w=>{
    if(state.activeLetter && w.word[0].toUpperCase()!==state.activeLetter) return false;
    if(topic && !w.topics.includes(topic)) return false;
    if(pos && !w.senses.some(s=>s.pos.split('/').includes(pos))) return false;
    if(query){const search=[w.word,w.phonetic?.us,...w.senses.flatMap(s=>[s.meaning_vi,s.definition_en,...s.synonyms,...s.antonyms]),...w.topics].join(' ');if(!normalizeText(search).includes(query))return false;}
    return true;
  }));
}
function renderDictionary(){
  $('#alphabetFilter').innerHTML=`<button class="alphabet-chip ${!state.activeLetter?'active':''}" data-letter="">ALL</button>`+ALPHABET.map(l=>`<button class="alphabet-chip ${state.activeLetter===l?'active':''}" data-letter="${l}">${l}</button>`).join('');
  const list=filteredWords(); $('#resultCount').textContent=`${list.length} từ vựng`;
  const topic=$('#topicFilter').value, pos=$('#posFilter').value;
  $('#activeFilters').textContent=[state.activeLetter||'',topic||'',pos||''].filter(Boolean).join(' · ');
  $('#wordTableBody').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<tr><td><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(displayWord(w.word))}<span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span></button></td><td>${posMarkup(w)}</td><td>${escapeHtml(s.meaning_vi||'—')}</td><td>${topicsMarkup(w.topics)}</td><td><button class="row-action" data-detail="${escapeHtml(w.id)}">Chi tiết →</button></td></tr>`}).join('');
  $('#wordCardList').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<article class="word-card"><div class="word-card-head"><div><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(displayWord(w.word))}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span></div>${posMarkup(w)}</div><div class="word-meaning">${escapeHtml(s.meaning_vi||'—')}</div>${topicsMarkup(w.topics)}</article>`}).join('');
  $('#dictionaryEmpty').hidden=list.length>0;
}
function renderDataTable(){
  const q=normalizeText($('#dataSearch').value); const letter=$('#dataLetterFilter').value; const topic=$('#dataTopicFilter').value; const pos=$('#dataPosFilter').value;
  const list=sortWords(state.words.filter(w=>{
    if(letter && w.word[0].toUpperCase()!==letter) return false;
    if(topic && !w.topics.includes(topic)) return false;
    if(pos && !w.senses.some(s=>s.pos.split('/').includes(pos))) return false;
    return !q || normalizeText([w.word,...w.senses.flatMap(s=>[s.meaning_vi,s.definition_en,...s.synonyms,...s.antonyms]),...w.topics].join(' ')).includes(q);
  }));
  $('#dataCount').textContent=`${list.length} / ${state.words.length} bản ghi`;
  $('#dataTableBody').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<tr><td><button class="word-name" data-edit="${escapeHtml(w.id)}">${escapeHtml(displayWord(w.word))}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span></td><td>${posMarkup(w)}</td><td>${escapeHtml(s.meaning_vi||'—')}</td><td>${topicsMarkup(w.topics)}</td><td><div class="row-actions"><button class="row-action icon-action" data-edit="${escapeHtml(w.id)}" title="Sửa từ vựng" aria-label="Sửa ${escapeHtml(displayWord(w.word))}">${icon('edit')}</button><button class="row-action icon-action danger-text" data-delete="${escapeHtml(w.id)}" title="Xóa từ vựng" aria-label="Xóa ${escapeHtml(displayWord(w.word))}">${icon('trash')}</button></div></td></tr>`}).join('');
  $('#dataEmpty').hidden=list.length>0;
}
function showDetail(id){
  const w=state.words.find(x=>x.id===id); if(!w)return;
  $('#modalEyebrow').textContent='VOCABULARY DETAIL'; $('#modalTitle').textContent='Chi tiết từ vựng';
  const senses=w.senses.map(s=>`<div class="meaning-line"><span class="meaning-pos">${escapeHtml(s.pos||'')}</span><strong>${escapeHtml(s.meaning_vi||'')}</strong><small>${escapeHtml(s.definition_en||'')}</small>${s.synonyms?.length?`<div class="detail-pills" style="margin-top:7px">${s.synonyms.map(x=>`<span class="detail-pill">≈ ${escapeHtml(x)}</span>`).join('')}</div>`:''}${s.antonyms?.length?`<div class="detail-pills" style="margin-top:5px">${s.antonyms.map(x=>`<span class="detail-pill">≠ ${escapeHtml(x)}</span>`).join('')}</div>`:''}</div>`).join('');
  const family=w.word_family?.length?`<div class="detail-section"><h4>WORD FAMILY</h4><div class="detail-pills">${w.word_family.map(x=>`<span class="detail-pill"><strong>${escapeHtml(displayWord(x.word))}</strong> · ${escapeHtml(x.pos||'')} — ${escapeHtml(x.meaning_vi||'')}</span>`).join('')}</div></div>`:'';
  const verbs=w.verb_forms?`<div class="detail-section"><h4>VERB FORMS</h4><div class="detail-pills">${Object.entries({V1:w.verb_forms.v1,'V-s/es':w.verb_forms.vs_es,V2:w.verb_forms.v2,V3:w.verb_forms.v3,'V-ing':w.verb_forms.ving}).filter(x=>x[1]).map(([k,v])=>`<span class="detail-pill"><strong>${k}:</strong> ${escapeHtml(v)}</span>`).join('')}</div></div>`:'';
  const examples=(w.examples||[]).map(e=>`<div class="example-card"><strong>${escapeHtml(e.en)}</strong><span>${escapeHtml(e.vi)}</span></div>`).join('');
  $('#modalContent').innerHTML=`<h3 class="detail-word">${escapeHtml(displayWord(w.word))}</h3><div class="detail-ipa">${escapeHtml(w.phonetic?.us||'Chưa có phiên âm')}</div><div class="detail-pos">${posMarkup(w)}</div><div class="detail-section"><h4>MEANING & DEFINITIONS</h4>${senses||'<p>Chưa có nghĩa.</p>'}</div>${family}${verbs}<div class="detail-section"><h4>TOPICS</h4>${topicsMarkup(w.topics)}</div>${w.collocations?.length?`<div class="detail-section"><h4>COLLOCATIONS</h4><div class="detail-pills">${w.collocations.map(x=>`<span class="detail-pill">${escapeHtml(x)}</span>`).join('')}</div></div>`:''}<div class="detail-section"><h4>EXAMPLES</h4>${examples||'<p>Chưa có ví dụ.</p>'}</div><div class="modal-actions"><button class="secondary-button" data-ai-word="${escapeHtml(w.id)}">${icon('sparkles','ui-icon button-icon')} Phân tích bằng Google AI</button><button class="secondary-button" data-edit="${escapeHtml(w.id)}">${icon('edit','ui-icon button-icon')} Sửa bản ghi</button></div>`;
  $('#modalBackdrop').hidden=false;
}
function openEditor(id=null){
  const old=state.words.find(w=>w.id===id); const s=old?.senses?.[0]||{};
  $('#modalEyebrow').textContent=old?'DATA MANAGEMENT · EDIT':'DATA MANAGEMENT · NEW'; $('#modalTitle').textContent=old?'Chỉnh sửa từ vựng':'Thêm từ vựng mới';
  const topicOptions=state.categories.map(c=>`<option value="${escapeHtml(c.id)}">${escapeHtml(c.id)} · ${escapeHtml(c.label)}</option>`).join('');
  $('#modalContent').innerHTML=`<form id="wordEditorForm"><div class="editor-grid">
  <label class="field"><span class="field-label">TỪ TIẾNG ANH *</span><input name="word" required value="${escapeHtml(old?displayWord(old.word):'')}" placeholder="Ví dụ: Schedule"></label>
  <label class="field"><span class="field-label">PHIÊN ÂM IPA</span><input name="ipa" value="${escapeHtml(old?.phonetic?.us||'')}" placeholder="/ˈskedʒ.uːl/"></label>
  <label class="field"><span class="field-label">LOẠI TỪ CHÍNH *</span><select name="pos"><option value="n">n – Danh từ</option><option value="v">v – Động từ</option><option value="adj">adj – Tính từ</option><option value="adv">adv – Trạng từ</option><option value="prep">prep – Giới từ</option><option value="conj">conj – Liên từ</option><option value="pron">pron – Đại từ</option><option value="n/v">n/v – Danh từ / Động từ</option></select></label>
  <label class="field"><span class="field-label">CHỦ ĐỀ (CÓ THỂ CHỌN NHIỀU)</span><select name="topics" multiple size="3">${topicOptions}</select></label>
  <label class="field full"><span class="field-label">NGHĨA TIẾNG VIỆT *</span><input name="meaning" required value="${escapeHtml(s.meaning_vi||'')}" placeholder="Nghĩa tiếng Việt"></label>
  <label class="field full"><span class="field-label">GIẢI THÍCH TIẾNG ANH</span><input name="definition" value="${escapeHtml(s.definition_en||'')}" placeholder="English definition"></label>
  <label class="field"><span class="field-label">TỪ ĐỒNG NGHĨA (PHÂN TÁCH BẰNG DẤU PHẨY)</span><input name="synonyms" value="${escapeHtml((s.synonyms||[]).join(', '))}" placeholder="arrange, plan"></label>
  <label class="field"><span class="field-label">TỪ TRÁI NGHĨA</span><input name="antonyms" value="${escapeHtml((s.antonyms||[]).join(', '))}" placeholder="cancel"></label>
  <label class="field full"><span class="field-label">VÍ DỤ TIẾNG ANH</span><input name="exampleEn" value="${escapeHtml(old?.examples?.[0]?.en||'')}" placeholder="The manager scheduled a meeting."></label>
  <label class="field full"><span class="field-label">DỊCH VÍ DỤ</span><input name="exampleVi" value="${escapeHtml(old?.examples?.[0]?.vi||'')}" placeholder="Quản lý đã lên lịch cuộc họp."></label>
  <label class="field full"><span class="field-label">COLLOCATIONS (PHÂN TÁCH BẰNG DẤU PHẨY)</span><input name="collocations" value="${escapeHtml((old?.collocations||[]).join(', '))}" placeholder="work schedule, daily schedule"></label>
  </div><p class="editor-help">Các trường có dấu * là bắt buộc. Để thêm nhiều nghĩa hoặc đầy đủ word family/verb forms, có thể chỉnh sửa JSON sau khi export.</p><div class="modal-actions"><button type="submit" class="primary-button">Lưu bản ghi</button></div></form>`;
  const form=$('#wordEditorForm'); form.elements.pos.value=s.pos||'n';
  const topics=old?.topics||[]; [...form.elements.topics.options].forEach(o=>o.selected=topics.includes(o.value));
  $('#modalBackdrop').hidden=false;
  form.addEventListener('submit',async e=>{e.preventDefault();const fd=new FormData(form);const w=String(fd.get('word')).trim();const pos=String(fd.get('pos'));const record=normalizeRecord({id:old?.id||undefined,word:w,phonetic:{us:String(fd.get('ipa')||'')},senses:[{pos,meaning_vi:String(fd.get('meaning')||''),definition_en:String(fd.get('definition')||''),synonyms:String(fd.get('synonyms')||'').split(',').map(x=>x.trim()).filter(Boolean),antonyms:String(fd.get('antonyms')||'').split(',').map(x=>x.trim()).filter(Boolean)},...(old?.senses?.slice(1)||[])],topics:[...form.elements.topics.selectedOptions].map(o=>o.value),examples:[{en:String(fd.get('exampleEn')||''),vi:String(fd.get('exampleVi')||'')}].filter(x=>x.en||x.vi),collocations:String(fd.get('collocations')||'').split(',').map(x=>x.trim()).filter(Boolean),word_family:old?.word_family||[],verb_forms:old?.verb_forms||null});
    const duplicate=state.words.find(x=>x.id!==old?.id&&normalizeText(x.word)===normalizeText(record.word));
    if(duplicate){toast(`Từ này đã tồn tại: ${duplicate.word}. Hãy mở bản ghi hiện có để chỉnh sửa.`, 'error');return;}
    if(old)state.words=state.words.map(x=>x.id===id?record:x);else state.words.push(record);
    await persistWorkspace(); closeModal(); updateOverview(); renderDictionary(); renderDataTable(); toast(old?'Đã cập nhật từ vựng.':'Đã thêm từ vựng mới.');
  });
}
async function persistWorkspace(){state.words=sortWords(state.words);await dbSet('workspace',state.words);state.localWorkspace=true;updateStorageLabel();}
function updateStorageLabel(){ $('#storageLabel').textContent=state.localWorkspace?'Bản chỉnh sửa đang lưu trên thiết bị · IndexedDB':'Đang đọc bộ dữ liệu gốc từ GitHub'; }
async function deleteWord(id){const item=state.words.find(w=>w.id===id);if(!item)return;if(!confirm(`Xóa từ "${displayWord(item.word)}" khỏi bản dữ liệu trên thiết bị?`))return;state.words=state.words.filter(w=>w.id!==id);await persistWorkspace();updateOverview();renderDictionary();renderDataTable();toast(`Đã xóa ${displayWord(item.word)} khỏi bản dữ liệu cục bộ.`);}
function closeModal(){ $('#modalBackdrop').hidden=true; $('#modalContent').innerHTML=''; }
function downloadFile(name,content,type){const blob=new Blob([content],{type});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function exportJSON(){const payload={schemaVersion:1,exportedAt:new Date().toISOString(),note:'TOEIC Vocabulary Phase 1 workspace export. Import back through Data Management.',words:sortWords(state.words)};downloadFile('toeic-vocabulary-export.json',JSON.stringify(payload,null,2),'application/json;charset=utf-8');toast('Đã xuất tệp JSON.');}
function csvEscape(v){const s=String(v??'');return /[",\r\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s;}
function exportCSV(){const headers=['id','word','ipa','pos','meaning_vi','definition_en','synonyms','antonyms','topics','example_en','example_vi','collocations'];const rows=state.words.map(w=>{const s=getPrimarySense(w);return [w.id,w.word,w.phonetic?.us||'',s.pos,s.meaning_vi,s.definition_en,(s.synonyms||[]).join('|'),(s.antonyms||[]).join('|'),w.topics.join('|'),w.examples?.[0]?.en||'',w.examples?.[0]?.vi||'',w.collocations.join('|')];});const csv='\uFEFF'+[headers,...rows].map(r=>r.map(csvEscape).join(',')).join('\r\n');downloadFile('toeic-vocabulary-export.csv',csv,'text/csv;charset=utf-8');toast('Đã xuất tệp CSV.');}
function parseCSV(text){const rows=[];let row=[],cell='',quoted=false;for(let i=0;i<text.length;i++){const ch=text[i];if(quoted){if(ch==='"'&&text[i+1]==='"'){cell+='"';i++;}else if(ch==='"')quoted=false;else cell+=ch;}else if(ch==='"')quoted=true;else if(ch===','){row.push(cell);cell='';}else if(ch==='\n'){row.push(cell.replace(/\r$/,''));rows.push(row);row=[];cell='';}else cell+=ch;}if(cell.length||row.length){row.push(cell.replace(/\r$/,''));rows.push(row);}const [headers,...items]=rows;return items.filter(r=>r.some(x=>x.trim())).map(r=>Object.fromEntries(headers.map((h,i)=>[h.trim(),r[i]??'']))).map(r=>({id:r.id,word:r.word,phonetic:{us:r.ipa},senses:[{pos:r.pos,meaning_vi:r.meaning_vi,definition_en:r.definition_en,synonyms:String(r.synonyms||'').split('|').filter(Boolean),antonyms:String(r.antonyms||'').split('|').filter(Boolean)}],topics:String(r.topics||'').split('|').filter(Boolean),examples:[{en:r.example_en,vi:r.example_vi}],collocations:String(r.collocations||'').split('|').filter(Boolean)}));}
async function importFile(file){const text=await file.text();let imported;if(file.name.toLowerCase().endsWith('.csv'))imported=parseCSV(text.replace(/^\uFEFF/,''));else{const parsed=JSON.parse(text);imported=Array.isArray(parsed)?parsed:(parsed.words||[]);}if(!Array.isArray(imported)||!imported.length)throw new Error('Không tìm thấy danh sách từ vựng trong tệp.');const map=new Map(state.words.map(w=>[w.id,w]));let added=0,updated=0;for(const raw of imported){const rec=normalizeRecord(raw);const duplicate=[...map.values()].find(w=>normalizeText(w.word)===normalizeText(rec.word));if(duplicate&&duplicate.id!==rec.id){rec.id=duplicate.id;updated++;}else if(map.has(rec.id))updated++;else added++;map.set(rec.id,rec);}state.words=[...map.values()];await persistWorkspace();updateOverview();renderDictionary();renderDataTable();toast(`Import hoàn tất: ${added} mới, ${updated} cập nhật.`);}
async function resetWorkspace(){if(!confirm('Khôi phục toàn bộ dữ liệu từ các tệp JSON gốc? Mọi thay đổi cục bộ trên thiết bị sẽ bị xóa.'))return;await dbDelete('workspace');state.words=[...state.baseWords];state.localWorkspace=false;updateStorageLabel();updateOverview();renderDictionary();renderDataTable();toast('Đã khôi phục dữ liệu gốc.');}
function goToLetter(letter){state.activeLetter=letter||'';$('#dictionarySearch').value='';$('#topicFilter').value='';$('#posFilter').value='';navigate('dictionary');}
// Phase 2 – adaptive practice, per-character feedback and study reminders.
const REVIEW_INTERVALS = [10 * 60 * 1000, 1 * 86400000, 3 * 86400000, 7 * 86400000, 14 * 86400000, 30 * 86400000];
const PRACTICE_DEFAULT_REMINDER = { enabled: false, intervalMinutes: 60, nextAt: null, pendingAnswered: true, lastTriggeredAt: null, pendingWordId: null };
const REMINDER_INTERVAL_OPTIONS = [60, 90, 120, 180, 1];
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
function choosePracticeWord(mode='random') {
  const now = Date.now();
  let candidates = state.words.filter(w => eligibleModes(w).includes(mode) || mode === 'random');
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
  const chosen = forcedWordId ? state.words.find(w => w.id === forcedWordId) : choosePracticeWord(mode);
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
    const distractors = state.words.filter(w=>w.id!==chosen.id).map(w=>getPrimarySense(w).meaning_vi).filter(Boolean);
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
    const distractors = state.words.filter(w=>w.id!==chosen.id).flatMap(w=>(getPrimarySense(w)[key]||[]));
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
  await dbSet('practiceSession', { currentQuestion: state.currentQuestion, questionAnswered: state.questionAnswered, sessionSeenIds: state.sessionSeenIds, lastFeedback: state.lastFeedback, autoAdvanceCancelled: state.autoAdvanceCancelled });
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
    $('#questionHint').textContent='Câu hỏi được chọn từ kho từ vựng và ưu tiên từ bạn chưa thuộc.';
    $('#choiceList').hidden=true; $('#answerForm').hidden=false; $('#answerInput').value='';
    $('#nextQuestionButton').disabled=true; $('#answerFeedback').hidden=true; $('#choiceReview').hidden=true; return;
  }
  const names = {missing:'MISSING LETTERS', 'meaning-to-word':'VIETNAMESE → ENGLISH', 'word-to-meaning':'ENGLISH → VIETNAMESE', pos:'PART OF SPEECH', synonym:'SYNONYM', antonym:'ANTONYM', verb:'VERB FORMS'};
  $('#questionType').textContent = names[q.mode] || 'PRACTICE';
  $('#questionPrompt').textContent=q.prompt; $('#questionHint').textContent=q.hint || '';
  $('#questionCounter').textContent=`${state.sessionSeenIds.length} từ đã gặp trong lượt này`;
  $('#questionPriority').textContent=progressPriorityLabel(q.wordId);
  const isChoice=q.choices?.length>0;
  $('#choiceList').hidden=!isChoice;
  $('#choiceList').innerHTML=isChoice?q.choices.map((choice,i)=>{
    const picked=state.questionAnswered&&state.lastFeedback&&normalizedAnswer(state.lastFeedback.input)===normalizedAnswer(choice);
    const isRight=q.accepted.some(a=>normalizedAnswer(a)===normalizedAnswer(choice));
    const cls=state.questionAnswered&&isRight?' correct-choice':state.questionAnswered&&picked?' wrong-choice':'';
    return `<button type="button" class="choice-option${picked?' selected':''}${cls}" data-choice="${escapeHtml(choice)}" ${state.questionAnswered?'disabled':''}><span>${String.fromCharCode(65+i)}</span>${escapeHtml(choice)}</button>`;
  }).join(''):'';
  $('#answerForm').hidden=isChoice;
  $('#answerInput').value=''; $('#answerInput').disabled=state.questionAnswered;
  $('#answerLabel').textContent=q.expectedWord?'NHẬP TỪ TIẾNG ANH':'CÂU TRẢ LỜI';
  $('#answerInput').placeholder=q.mode==='verb'?'Nhập dạng động từ...':q.mode==='missing'?'Điền từ hoàn chỉnh...':'Nhập câu trả lời...';
  $('#checkAnswerButton').disabled=state.questionAnswered;
  $('#answerFeedback').hidden=!state.questionAnswered;
  $('#nextQuestionButton').disabled=!state.questionAnswered;
  $('#skipQuestionButton').disabled=state.questionAnswered;
  if (state.questionAnswered && state.lastFeedback) renderFeedback(state.lastFeedback);
  else { $('#choiceReview').hidden=true; $('#autoAdvanceRow').hidden=true; }
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
    const relation=q.mode==='synonym'?'đồng nghĩa với':'trái nghĩa với';
    const source=state.words.find(w=>w.id===q.wordId);
    const refs=findRelatedSources(choice);
    if(alias) {
      const context=refs.length?` Có liên hệ trong dữ liệu với: ${refs.map(w=>`${displayWord(w.word)} (${getPrimarySense(w).meaning_vi})`).join('; ')}.`:'';
      return `Nghĩa tiếng Việt: ${alias.meaning_vi}. Đây là phương án ${relation} ${displayWord(q.word)} trong câu hỏi hiện tại.${context}`;
    }
    if(isCorrect) {
      const meaning=source?getPrimarySense(source).meaning_vi:'';
      return `Phương án này được lưu là ${relation} ${displayWord(q.word)}. Nghĩa riêng của lựa chọn chưa có trong bảng tham chiếu; nghĩa từ gốc: ${meaning||'xem từ điển gốc'}.`;
    }
    if(refs.length) return `Được dùng trong nhóm từ liên hệ của ${refs.map(w=>`${displayWord(w.word)} – ${getPrimarySense(w).meaning_vi}`).join('; ')}. Chưa có nghĩa độc lập đã kiểm chứng trong bảng tham chiếu.`;
    return 'Chưa có nghĩa riêng trong bảng tham chiếu hiện tại. Có thể dùng nút Google AI để phân tích và kiểm chứng thêm.';
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
  const senses=(w.senses||[]).map(s=>`<div class="reference-sense"><span class="meaning-pos">${escapeHtml(s.pos||'')}</span><strong>${escapeHtml(s.meaning_vi||'')}</strong>${s.definition_en?`<small>${escapeHtml(s.definition_en)}</small>`:''}${s.synonyms?.length?`<p><b>Đồng nghĩa:</b> ${s.synonyms.map(escapeHtml).join(', ')}</p>`:''}${s.antonyms?.length?`<p><b>Trái nghĩa:</b> ${s.antonyms.map(escapeHtml).join(', ')}</p>`:''}</div>`).join('');
  const examples=(w.examples||[]).map(e=>`<small class="reference-example">${escapeHtml(e.en)}${e.vi?` — ${escapeHtml(e.vi)}`:''}</small>`).join('');
  const family=(w.word_family||[]).length?`<p><b>Word family:</b> ${w.word_family.map(f=>`${escapeHtml(displayWord(f.word))} (${escapeHtml(f.pos||'')}) – ${escapeHtml(f.meaning_vi||'')}`).join('; ')}</p>`:'';
  const forms=w.verb_forms?`<p><b>Verb forms:</b> ${Object.entries({V1:w.verb_forms.v1,'V-s/es':w.verb_forms.vs_es,V2:w.verb_forms.v2,V3:w.verb_forms.v3,'V-ing':w.verb_forms.ving}).filter(([,v])=>v).map(([k,v])=>`${k}: ${escapeHtml(v)}`).join(' · ')}</p>`:'';
  const selected=feedback.correct?'Bạn đã trả lời đúng.':`Bạn nhập/chọn: ${escapeHtml(feedback.input)} · Đáp án: ${escapeHtml(feedback.expected)}`;
  return `<div class="reference-title-row"><strong>${escapeHtml(displayWord(w.word))}</strong><span>${escapeHtml(w.phonetic?.us||'')}</span></div><p class="reference-overview">${escapeHtml(selected)}</p>${senses}${family}${forms}${w.collocations?.length?`<p><b>Collocations:</b> ${w.collocations.map(escapeHtml).join(', ')}</p>`:''}${examples}${w.topics?.length?`<p><b>Chủ đề:</b> ${w.topics.map(escapeHtml).join(', ')}</p>`:''}`;
}
function renderFeedback(feedback) {
  $('#answerFeedback').hidden=false;
  $('#feedbackHeading').textContent=feedback.correct?'Chính xác! Bạn làm tốt lắm.':'Chưa chính xác – hãy ghi nhớ vị trí cần sửa.';
  $('#feedbackHeading').className=`feedback-heading ${feedback.correct?'is-correct':'is-wrong'}`;
  $('#feedbackExplanation').textContent=feedback.correct?'Đáp án đã được ghi nhận. Hãy xem nghĩa của tất cả lựa chọn bên dưới.':`Đáp án đúng: ${feedback.expected}. Bạn có thể xem lại từng lựa chọn để ghi nhớ.`;
  const q=state.currentQuestion;
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
  const weak=state.words.filter(w=>{const p=getWordProgress(w.id);return p.reviewCount && (p.wrongCount>0 || (p.dueAt&&p.dueAt<=Date.now()));})
    .sort((a,b)=>{const pa=getWordProgress(a.id),pb=getWordProgress(b.id);const sa=(pb.wrongCount*3)-(pa.wrongCount*3)+(pa.dueAt||0)-(pb.dueAt||0);return sa;}).slice(0,6);
  $('#weakWordList').innerHTML=weak.length?weak.map(w=>{const p=getWordProgress(w.id);return `<button class="weak-word-item" data-weak-word="${escapeHtml(w.id)}"><span><strong>${escapeHtml(displayWord(w.word))}</strong><small>${escapeHtml(getPrimarySense(w).meaning_vi||'')}</small></span><em>${p.wrongCount} lỗi</em></button>`;}).join(''):'<p class="muted">Bạn chưa có từ sai. Hãy bắt đầu luyện tập để tạo dữ liệu ưu tiên.</p>';
}
async function submitAnswer(value) {
  const q=state.currentQuestion; if(!q||state.questionAnswered)return;
  const input=String(value??'').trim(); if(!input){toast('Hãy nhập hoặc chọn câu trả lời trước.','error');return;}
  const correct=q.accepted.some(answer=>normalizedAnswer(answer)===normalizedAnswer(input));
  state.questionAnswered=true; state.sessionSeenIds.push(q.wordId);
  state.lastFeedback={correct,input,expected:q.expectedDisplay||q.accepted[0]||''};
  await updatePracticeProgress(q.wordId,correct,input);
  if(state.reminder.enabled){state.reminder.pendingAnswered=true;state.reminder.pendingWordId=null;state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;await dbSet('reminderSettings',state.reminder);}
  await savePracticeSession(); renderQuestion(); renderReminderStatus();
  $('#nextQuestionButton').disabled=false; $('#skipQuestionButton').disabled=true;
  scheduleAutoAdvance();
  toast(correct?'Đã ghi nhận câu trả lời đúng.':'Đã lưu kết quả. Từ này sẽ được ưu tiên ôn lại.');
}
async function nextQuestion(modeOverride=null) {
  clearAutoAdvance();
  state.autoAdvanceCancelled=false;
  const mode=modeOverride||$('#practiceMode').value||'random';
  const q=makeQuestion(mode);
  if(!q){toast('Chưa có từ phù hợp với dạng bài này. Hãy thêm dữ liệu hoặc chọn dạng khác.','error');return;}
  state.currentQuestion=q; state.questionAnswered=false; state.lastFeedback=null;
  await savePracticeSession(); renderQuestion();
}
async function skipQuestion() {
  if(!state.currentQuestion||state.questionAnswered)return;
  state.sessionSeenIds.push(state.currentQuestion.wordId);
  await nextQuestion($('#practiceMode').value);
}
function clearAutoAdvance() {
  if(state.autoAdvanceTimer){clearInterval(state.autoAdvanceTimer);state.autoAdvanceTimer=null;}
  state.autoAdvanceAt=null;
  state.autoAdvanceRemaining=null;
}
function updateAutoAdvanceUI() {
  const row=$('#autoAdvanceRow');
  if(!row)return;
  const active=!!state.questionAnswered && !!state.settings.autoNextEnabled && !state.autoAdvanceCancelled;
  row.hidden=!active;
  if(active&&state.autoAdvanceAt){const seconds=Math.max(0,Math.ceil((state.autoAdvanceAt-Date.now())/1000));$('#autoAdvanceStatus').textContent=`Tự động chuyển câu tiếp theo sau ${seconds} giây.`;}
  else if(active){const seconds=Math.max(0,Math.ceil((state.autoAdvanceRemaining??((Number(state.settings.autoNextDelaySeconds)||3)*1000))/1000));$('#autoAdvanceStatus').textContent=`Tự động chuyển câu tiếp theo sau ${seconds} giây.`;}
}
function pauseAutoAdvance() {
  if(state.autoAdvanceAt) state.autoAdvanceRemaining=Math.max(0,state.autoAdvanceAt-Date.now());
  if(state.autoAdvanceTimer){clearInterval(state.autoAdvanceTimer);state.autoAdvanceTimer=null;}
  state.autoAdvanceAt=null;
  if(state.questionAnswered) updateAutoAdvanceUI();
}
function resumeAutoAdvance() {
  if(!state.questionAnswered||!state.settings.autoNextEnabled||state.autoAdvanceCancelled||state.activePage!=='practice'||document.hidden)return;
  if(state.autoAdvanceTimer)return;
  const delay=state.autoAdvanceRemaining ?? ((Number(state.settings.autoNextDelaySeconds)||3)*1000);
  state.autoAdvanceRemaining=null;
  state.autoAdvanceAt=Date.now()+Math.max(0,delay);
  state.autoAdvanceTimer=setInterval(async()=>{
    if(state.activePage!=='practice'||document.hidden)return;
    const remaining=state.autoAdvanceAt-Date.now();
    updateAutoAdvanceUI();
    if(remaining<=0){clearAutoAdvance();await nextQuestion();}
  },200);
  updateAutoAdvanceUI();
}
function scheduleAutoAdvance() {
  clearAutoAdvance();
  state.autoAdvanceCancelled=false;
  if(!state.settings.autoNextEnabled||!state.questionAnswered){updateAutoAdvanceUI();return;}
  state.autoAdvanceRemaining=(Number(state.settings.autoNextDelaySeconds)||3)*1000;
  resumeAutoAdvance();
  savePracticeSession();
}
async function holdCurrentQuestion() {
  clearAutoAdvance();
  state.autoAdvanceCancelled=true;
  await savePracticeSession();
  updateAutoAdvanceUI();
  toast('Đã giữ câu hỏi. Bạn có thể xem kỹ đáp án và giải nghĩa.');
}
function setAutoNextSettings(enabled, seconds) {
  state.settings.autoNextEnabled=!!enabled;
  state.settings.autoNextDelaySeconds=[3,5,10].includes(Number(seconds))?Number(seconds):3;
  dbSet('appSettings',state.settings).catch(err=>console.warn('Không lưu được cấu hình tự chuyển:',err));
  if(!state.settings.autoNextEnabled) clearAutoAdvance();
  else if(state.questionAnswered&&!state.autoAdvanceCancelled) scheduleAutoAdvance();
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
  const testButton=$('#testNotificationButton'); if(testButton)testButton.disabled=permission!=='granted';
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
async function testNativeNotification() {
  if(!('Notification'in window)||!('serviceWorker'in navigator)){toast('Thiết bị này không hỗ trợ thông báo qua Service Worker.','error');showReminderPopup('TOEIC Dictionary – Kiểm tra nhắc nhở','Popup trong website vẫn hoạt động khi trang đang mở.');return;}
  if(Notification.permission!=='granted'){await requestNotificationPermission();if(Notification.permission!=='granted')return;}
  try {
    const result=await state.notificationProvider.sendNotification({title:'TOEIC Dictionary – Thông báo thử',body:'Nếu bạn nhìn thấy thông báo này trong khu vực thông báo của thiết bị, quyền hệ thống đã hoạt động.',url:new URL('./?open=practice',location.href).href,tag:'toeic-test-notification'});
    if(result.delivered)toast('Đã gửi thông báo thử cho hệ điều hành. Hãy kiểm tra banner/Trung tâm thông báo.');
    else {showReminderPopup('TOEIC Dictionary – Kiểm tra nhắc nhở','Thông báo hệ thống chưa khả dụng. Popup trong website vẫn hoạt động khi trang mở.');toast('Không gửi được thông báo hệ thống.','error');}
  } catch(err){console.error(err);toast('Không gửi được thông báo thử. Kiểm tra HTTPS, quyền trình duyệt và Service Worker.','error');}
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
  const settings=await dbGet('appSettings');
  if(settings&&typeof settings==='object')state.settings={...state.settings,...settings};
  const session=await dbGet('practiceSession');
  if(session){
    state.currentQuestion=session.currentQuestion||null; state.questionAnswered=!!session.questionAnswered;
    state.sessionSeenIds=Array.isArray(session.sessionSeenIds)?session.sessionSeenIds:[];
    state.lastFeedback=session.lastFeedback||null;
    state.autoAdvanceCancelled=!!session.autoAdvanceCancelled;
    if(state.currentQuestion?.word){const oldWord=String(state.currentQuestion.word);const newWord=displayWord(oldWord);state.currentQuestion.prompt=String(state.currentQuestion.prompt||'').split(oldWord).join(newWord);state.currentQuestion.word=newWord;if(state.currentQuestion.expectedWord&&state.currentQuestion.expectedDisplay)state.currentQuestion.expectedDisplay=displayWord(state.currentQuestion.expectedDisplay);}
  }
  if(state.currentQuestion&&!state.words.some(w=>w.id===state.currentQuestion.wordId)){state.currentQuestion=null;state.questionAnswered=false;}
  updatePracticeStats(); renderQuestion(); renderReminderStatus(); syncSettingsUI();
  if(state.reminder.enabled&&!state.reminder.nextAt){state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;await dbSet('reminderSettings',state.reminder);}
  setInterval(()=>{checkReminder();renderReminderStatus();},15000);
  document.addEventListener('visibilitychange',()=>{if(document.hidden)pauseAutoAdvance();else {checkReminder();resumeAutoAdvance();}});
  window.addEventListener('focus',()=>{checkReminder();resumeAutoAdvance();});
  if(new URLSearchParams(location.search).get('open')==='practice')navigate('practice');
  if(state.questionAnswered&&!state.autoAdvanceCancelled&&state.settings.autoNextEnabled){state.autoAdvanceRemaining=(Number(state.settings.autoNextDelaySeconds)||3)*1000;}
}
function syncSettingsUI(){
  const enabled=$('#autoNextEnabled');if(enabled)enabled.checked=!!state.settings.autoNextEnabled;
  const delay=$('#autoNextDelay');if(delay)delay.value=String([3,5,10].includes(Number(state.settings.autoNextDelaySeconds))?state.settings.autoNextDelaySeconds:3);
  renderReminderStatus();
}
function bindPracticeEvents() {
  $('#newQuestionButton').addEventListener('click',()=>nextQuestion());
  $('#nextQuestionButton').addEventListener('click',()=>nextQuestion());
  $('#skipQuestionButton').addEventListener('click',skipQuestion);
  $('#practiceMode').addEventListener('change',()=>nextQuestion($('#practiceMode').value));
  $('#answerForm').addEventListener('submit',e=>{e.preventDefault();submitAnswer($('#answerInput').value);});
  $('#choiceList').addEventListener('click',e=>{const b=e.target.closest('[data-choice]');if(b&&!state.questionAnswered){$$('.choice-option',$('#choiceList')).forEach(x=>x.classList.remove('selected'));b.classList.add('selected');submitAnswer(b.dataset.choice);}});
  $('#weakWordList').addEventListener('click',e=>{const b=e.target.closest('[data-weak-word]');if(b)showDetail(b.dataset.weakWord);});
  $('#reminderEnabled').addEventListener('change',e=>setReminderEnabled(e.target.checked));
  $('#reminderInterval').addEventListener('change',async()=>{const selected=Number($('#reminderInterval').value);state.reminder.intervalMinutes=REMINDER_INTERVAL_OPTIONS.includes(selected)?selected:60;if(state.reminder.enabled)state.reminder.nextAt=Date.now()+state.reminder.intervalMinutes*60000;await dbSet('reminderSettings',state.reminder);renderReminderStatus();toast(`Đã cập nhật chu kỳ ${state.reminder.intervalMinutes===1?'kiểm thử 1 phút':state.reminder.intervalMinutes+' phút'}.`);});
  $('#notificationPermissionButton').addEventListener('click',requestNotificationPermission);
  $('#testNotificationButton').addEventListener('click',testNativeNotification);
  $('#autoNextEnabled').addEventListener('change',e=>setAutoNextSettings(e.target.checked,$('#autoNextDelay').value));
  $('#autoNextDelay').addEventListener('change',()=>setAutoNextSettings($('#autoNextEnabled').checked,$('#autoNextDelay').value));
  $('#holdQuestionButton').addEventListener('click',holdCurrentQuestion);
  $('#analyzeAnswerAIButton').addEventListener('click',()=>showAIPromptModal(buildPracticeAIPrompt()));
}

function bindEvents(){
  bindPracticeEvents();
  $$('[data-page]').forEach(b=>b.addEventListener('click',()=>navigate(b.dataset.page)));
  $$('[data-go]').forEach(b=>b.addEventListener('click',()=>navigate(b.dataset.go)));
  $('#dashboardAlphabet').addEventListener('click',e=>{const b=e.target.closest('[data-letter]');if(b)goToLetter(b.dataset.letter);});
  $('#alphabetFilter').addEventListener('click',e=>{const b=e.target.closest('[data-letter]');if(b){state.activeLetter=b.dataset.letter;renderDictionary();}});
  ['dictionarySearch','topicFilter','posFilter'].forEach(id=>$('#'+id).addEventListener('input',renderDictionary));
  $('#resetFilters').addEventListener('click',()=>{state.activeLetter='';$('#dictionarySearch').value='';$('#topicFilter').value='';$('#posFilter').value='';renderDictionary();});
  $('#wordTableBody').addEventListener('click',e=>{const b=e.target.closest('[data-detail]');if(b)showDetail(b.dataset.detail);});
  $('#wordCardList').addEventListener('click',e=>{const b=e.target.closest('[data-detail]');if(b)showDetail(b.dataset.detail);});
  $('#dataTableBody').addEventListener('click',e=>{const edit=e.target.closest('[data-edit]'),del=e.target.closest('[data-delete]');if(edit)openEditor(edit.dataset.edit);if(del)deleteWord(del.dataset.delete);});
  $('#dataSearch').addEventListener('input',renderDataTable);
  $('#dataLetterFilter').addEventListener('change',renderDataTable); $('#dataTopicFilter').addEventListener('change',renderDataTable); $('#dataPosFilter').addEventListener('change',renderDataTable);
  $('#resetDataFilters').addEventListener('click',()=>{$('#dataSearch').value='';$('#dataLetterFilter').value='';$('#dataTopicFilter').value='';$('#dataPosFilter').value='';renderDataTable();});
  $('#addWordButton').addEventListener('click',()=>openEditor());
  $('#importButton').addEventListener('click',()=>$('#importFile').click());
  $('#importFile').addEventListener('change',async e=>{const file=e.target.files?.[0];if(!file)return;try{await importFile(file);}catch(err){toast(`Import thất bại: ${err.message}`,'error');}finally{e.target.value='';}});
  $('#exportJsonButton').addEventListener('click',exportJSON);$('#exportCsvButton').addEventListener('click',exportCSV);$('#resetLocalButton').addEventListener('click',resetWorkspace);
  $('#closeModal').addEventListener('click',closeModal);$('#modalBackdrop').addEventListener('click',e=>{if(e.target.id==='modalBackdrop')closeModal();});
  $('#modalContent').addEventListener('click',async e=>{const edit=e.target.closest('[data-edit]');const ai=e.target.closest('[data-ai-word]');const copy=e.target.closest('[data-copy-ai-prompt]');const open=e.target.closest('[data-open-gemini]');if(edit)openEditor(edit.dataset.edit);if(ai){const w=state.words.find(x=>x.id===ai.dataset.aiWord);if(w)showAIPromptModal(buildWordAIPrompt(w));}if(copy)await copyAIPrompt();if(open)openGeminiWithPrompt();});
  $('#globalSearch').addEventListener('keydown',e=>{if(e.key==='Enter'){navigate('dictionary');$('#dictionarySearch').value=e.target.value;renderDictionary();}});
  $('#globalSearch').addEventListener('input',e=>{if(e.target.value.length>=2){navigate('dictionary');$('#dictionarySearch').value=e.target.value;renderDictionary();}});
  document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();$('#globalSearch').focus();}if(e.key==='Escape'){if($('#installInviteBackdrop').hidden)closeModal();}});
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
function buildWordAIPrompt(word) {
  const senses=(word.senses||[]).map((s,i)=>`${i+1}. Loại từ: ${s.pos}\n   Nghĩa tiếng Việt: ${s.meaning_vi}\n   Definition: ${s.definition_en||'Chưa có'}\n   Synonyms: ${(s.synonyms||[]).join(', ')||'Chưa có'}\n   Antonyms: ${(s.antonyms||[]).join(', ')||'Chưa có'}`).join('\n');
  const forms=word.verb_forms?JSON.stringify(word.verb_forms,null,2):'Không áp dụng/chưa có';
  return `Bạn là giáo viên tiếng Anh chuyên luyện TOEIC cho người học Việt Nam. Hãy phân tích đầy đủ mục từ sau, kiểm tra độ chính xác và không tự bịa dữ liệu.\n\nTỪ: ${displayWord(word.word)}\nIPA: ${word.phonetic?.us||'Chưa có'}\nCHỦ ĐỀ: ${(word.topics||[]).join(', ')}\nCÁC NGHĨA:\n${senses}\nWORD FAMILY: ${JSON.stringify(word.word_family||[],null,2)}\nVERB FORMS: ${forms}\nCOLLOCATIONS: ${(word.collocations||[]).join(', ')||'Chưa có'}\nVÍ DỤ: ${(word.examples||[]).map(e=>`${e.en} — ${e.vi}`).join('\n')||'Chưa có'}\n\nYÊU CẦU PHÂN TÍCH:\n1. Giải thích từng nghĩa và ngữ cảnh sử dụng; chỉ rõ loại từ n/v/adj/adv/prep...\n2. Phân biệt từ đồng nghĩa và trái nghĩa theo đúng ngữ cảnh, chỉ ra sắc thái khác nhau.\n3. Kiểm tra word family, V1/V-s/es/V2/V3/V-ing nếu là động từ.\n4. Nêu collocations và lỗi thường gặp của người Việt.\n5. Tạo tối thiểu 3 ví dụ theo bối cảnh TOEIC (văn phòng, cuộc họp, nhân sự, tài chính, vận chuyển...).\n6. Đề xuất mẹo ghi nhớ dễ hiểu.\n7. Tạo 5 câu hỏi ôn tập kèm đáp án và giải thích ở phần riêng cuối bài.\nNếu dữ liệu nguồn chưa đủ hoặc một quan hệ đồng/trái nghĩa không tự nhiên, hãy nói rõ thay vì suy đoán.`;
}
function buildPracticeAIPrompt() {
  const q=state.currentQuestion; const f=state.lastFeedback; const w=state.words.find(x=>x.id===q?.wordId);
  if(!q||!f||!w)return 'Hãy giải thích câu hỏi TOEIC hiện tại và cách tìm đáp án đúng.';
  const options=(q.choices||[]).map((choice,i)=>{const correct=q.accepted.some(x=>normalizedAnswer(x)===normalizedAnswer(choice));return `${String.fromCharCode(65+i)}. ${choice}\n   Trạng thái: ${correct?'Đáp án đúng hợp lệ':'Phương án nhiễu'}\n   Giải nghĩa tham chiếu trong kho: ${getChoiceExplanation(q,choice,correct)}`;}).join('\n');
  return `Bạn là giáo viên TOEIC và chuyên gia giải thích từ vựng/ngữ pháp cho người Việt. Hãy phân tích toàn bộ câu hỏi, đáp án và các phương án lựa chọn dưới đây.\n\nDẠNG BÀI: ${q.mode}\nCÂU HỎI: ${q.prompt}\nGỢI Ý: ${q.hint||'Không có'}\nTỪ MỤC TIÊU: ${displayWord(w.word)}\nIPA: ${w.phonetic?.us||'Chưa có'}\nCÁC NGHĨA: ${(w.senses||[]).map(s=>`${s.pos}: ${s.meaning_vi} (${s.definition_en||''})`).join('; ')}\nTỪ ĐỒNG NGHĨA: ${(w.senses||[]).flatMap(s=>s.synonyms||[]).join(', ')||'Không có'}\nTỪ TRÁI NGHĨA: ${(w.senses||[]).flatMap(s=>s.antonyms||[]).join(', ')||'Không có'}\nWORD FAMILY: ${JSON.stringify(w.word_family||[])}\nVERB FORMS: ${JSON.stringify(w.verb_forms||{})}\n\nCÁC LỰA CHỌN:\n${options||'Câu trả lời dạng nhập văn bản.'}\n\nCÂU TRẢ LỜI NGƯỜI HỌC: ${f.input}\nKẾT QUẢ: ${f.correct?'ĐÚNG':'SAI'}\nĐÁP ÁN ĐÚNG: ${f.expected}\nVÍ DỤ CỦA TỪ: ${(w.examples||[]).map(e=>`${e.en} — ${e.vi}`).join('; ')||'Chưa có'}\n\nHÃY TRẢ LỜI THEO CẤU TRÚC:\n1. Kết luận ngắn về câu trả lời của tôi.\n2. Giải thích vì sao đáp án đúng là đúng, theo ngữ cảnh của câu hỏi.\n3. Phân tích TỪNG lựa chọn A/B/C/D: nghĩa tiếng Việt, loại từ, sắc thái, vì sao đúng hoặc sai. Không bỏ qua lựa chọn sai.\n4. So sánh các từ gần nghĩa/dễ nhầm và chỉ ra bẫy TOEIC.\n5. Mở rộng word family, collocations và ví dụ thực tế nếu có.\n6. Mẹo ghi nhớ và cách phân biệt.\n7. Tạo thêm 3 câu hỏi tương tự, để đáp án ở cuối.\nKhông tự khẳng định nghĩa nếu dữ liệu chưa đủ; hãy ghi rõ phần nào cần tra từ điển.`;
}
function showAIPromptModal(prompt) {
  state.lastAIPrompt=prompt;
  clearAutoAdvance(); state.autoAdvanceCancelled=true; savePracticeSession(); updateAutoAdvanceUI();
  $('#modalEyebrow').textContent='GOOGLE AI · LEARNING ASSISTANT';
  $('#modalTitle').textContent='Phân tích nội dung bằng Google AI';
  $('#modalContent').innerHTML=`<div class="ai-prompt-intro"><span class="ai-prompt-icon">${icon('sparkles')}</span><div><strong>Prompt đã được tạo từ dữ liệu hiện tại</strong><p>Gồm câu hỏi, câu trả lời, đáp án đúng/sai, toàn bộ lựa chọn và thông tin từ điển liên quan.</p></div></div><label class="field ai-prompt-field"><span class="field-label">NỘI DUNG GỬI GOOGLE GEMINI</span><textarea id="aiPromptTextarea" rows="17" readonly>${escapeHtml(prompt)}</textarea></label><div class="modal-actions ai-prompt-actions"><button type="button" class="secondary-button" data-copy-ai-prompt>${icon('copy','ui-icon button-icon')} Sao chép prompt</button><button type="button" class="primary-button" data-open-gemini>${icon('sparkles','ui-icon button-icon')} Mở Google Gemini</button></div><p class="ai-prompt-note">Website không gửi dữ liệu tự động. Bạn chủ động sao chép/dán prompt vào Gemini và có thể chỉnh sửa trước khi gửi.</p>`;
  $('#modalBackdrop').hidden=false;
}
async function copyAIPrompt() {
  const area=$('#aiPromptTextarea'); if(!area)return;
  try { await navigator.clipboard.writeText(area.value); toast('Đã sao chép toàn bộ prompt AI.'); }
  catch { area.focus();area.select();try{document.execCommand('copy');toast('Đã sao chép prompt.');}catch{toast('Hãy chọn và sao chép nội dung prompt thủ công.','error');} }
}
async function openGeminiWithPrompt() {
  window.open('https://gemini.google.com/app','_blank','noopener,noreferrer');
  await copyAIPrompt();
  toast('Đã mở Google Gemini. Dán prompt vừa sao chép vào khung trò chuyện.');
}
function updateDate(){const now=new Date();$('#todayLabel').textContent=new Intl.DateTimeFormat('vi-VN',{weekday:'long',day:'2-digit',month:'long',year:'numeric'}).format(now);}
async function registerSW(){if(!('serviceWorker'in navigator))return null;try{const registration=await navigator.serviceWorker.register('./sw.js',{scope:'./'});await navigator.serviceWorker.ready;state.swRegistration=registration;state.notificationProvider=new LocalNotificationProvider(()=>state.swRegistration);return registration;}catch(err){console.warn('Service Worker chưa đăng ký được:',err);state.notificationProvider=new LocalNotificationProvider(()=>null);return null;}}
async function init(){bindEvents();updateDate();try{await loadData();await initializePractice();}catch(err){console.error(err);$('#metricWords').textContent='!';toast(`Không tải được dữ liệu: ${err.message}`,'error');$('#resultCount').textContent='Không tải được dữ liệu';}await registerSW();initializeInstallInvite();}
init();
