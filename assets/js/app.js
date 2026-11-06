const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const icon = (name, cls='ui-icon') => `<svg class="${cls}" aria-hidden="true"><use href="#icon-${name}"></use></svg>`;
const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const DB_NAME = 'toeic-vocabulary-phase1';
const DB_STORE = 'workspace';
const state = { words: [], baseWords: [], categories: [], activePage: 'dashboard', activeLetter: '', deferredInstall: null, localWorkspace: false };

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
  const [categoryResponse,...letterResponses]=await Promise.all([fetch(manifest.categories),...manifest.letters.map(x=>fetch(x.file))]);
  if(!categoryResponse.ok) throw new Error('Không đọc được categories.json.');
  const categoryData=await categoryResponse.json();
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
}
function populateFilters(){
  const options=state.categories.map(c=>`<option value="${escapeHtml(c.id)}">${escapeHtml(c.label)}</option>`).join('');
  $('#topicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+options;
  $('#dataTopicFilter').innerHTML='<option value="">Tất cả chủ đề</option>'+options;
  $('#dataLetterFilter').innerHTML='<option value="">Tất cả A–Z</option>'+ALPHABET.map(l=>`<option value="${l}">${l}</option>`).join('');
}
function navigate(page){
  state.activePage=page;
  $$('.page').forEach(p=>p.classList.toggle('active',p.id===`page-${page}`));
  $$('[data-page]').forEach(b=>b.classList.toggle('active',b.dataset.page===page));
  const titles={dashboard:'Tổng quan',dictionary:'Từ vựng',data:'Quản lý dữ liệu'};
  $('#pageTitle').textContent=titles[page]||'Tổng quan';
  if(page==='dictionary') renderDictionary(); if(page==='data') renderDataTable();
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
  $('#wordTableBody').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<tr><td><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(w.word)}<span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span></button></td><td>${posMarkup(w)}</td><td>${escapeHtml(s.meaning_vi||'—')}</td><td>${topicsMarkup(w.topics)}</td><td><button class="row-action" data-detail="${escapeHtml(w.id)}">Chi tiết →</button></td></tr>`}).join('');
  $('#wordCardList').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<article class="word-card"><div class="word-card-head"><div><button class="word-name" data-detail="${escapeHtml(w.id)}">${escapeHtml(w.word)}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span></div>${posMarkup(w)}</div><div class="word-meaning">${escapeHtml(s.meaning_vi||'—')}</div>${topicsMarkup(w.topics)}</article>`}).join('');
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
  $('#dataTableBody').innerHTML=list.map(w=>{const s=getPrimarySense(w);return `<tr><td><button class="word-name" data-edit="${escapeHtml(w.id)}">${escapeHtml(w.word)}</button><span class="word-ipa">${escapeHtml(w.phonetic?.us||'')}</span></td><td>${posMarkup(w)}</td><td>${escapeHtml(s.meaning_vi||'—')}</td><td>${topicsMarkup(w.topics)}</td><td><div class="row-actions"><button class="row-action icon-action" data-edit="${escapeHtml(w.id)}" title="Sửa từ vựng" aria-label="Sửa ${escapeHtml(w.word)}">${icon('edit')}</button><button class="row-action icon-action danger-text" data-delete="${escapeHtml(w.id)}" title="Xóa từ vựng" aria-label="Xóa ${escapeHtml(w.word)}">${icon('trash')}</button></div></td></tr>`}).join('');
  $('#dataEmpty').hidden=list.length>0;
}
function showDetail(id){
  const w=state.words.find(x=>x.id===id); if(!w)return;
  $('#modalEyebrow').textContent='VOCABULARY DETAIL'; $('#modalTitle').textContent='Chi tiết từ vựng';
  const senses=w.senses.map(s=>`<div class="meaning-line"><span class="meaning-pos">${escapeHtml(s.pos||'')}</span><strong>${escapeHtml(s.meaning_vi||'')}</strong><small>${escapeHtml(s.definition_en||'')}</small>${s.synonyms?.length?`<div class="detail-pills" style="margin-top:7px">${s.synonyms.map(x=>`<span class="detail-pill">≈ ${escapeHtml(x)}</span>`).join('')}</div>`:''}${s.antonyms?.length?`<div class="detail-pills" style="margin-top:5px">${s.antonyms.map(x=>`<span class="detail-pill">≠ ${escapeHtml(x)}</span>`).join('')}</div>`:''}</div>`).join('');
  const family=w.word_family?.length?`<div class="detail-section"><h4>WORD FAMILY</h4><div class="detail-pills">${w.word_family.map(x=>`<span class="detail-pill"><strong>${escapeHtml(x.word)}</strong> · ${escapeHtml(x.pos||'')} — ${escapeHtml(x.meaning_vi||'')}</span>`).join('')}</div></div>`:'';
  const verbs=w.verb_forms?`<div class="detail-section"><h4>VERB FORMS</h4><div class="detail-pills">${Object.entries({V1:w.verb_forms.v1,'V-s/es':w.verb_forms.vs_es,V2:w.verb_forms.v2,V3:w.verb_forms.v3,'V-ing':w.verb_forms.ving}).filter(x=>x[1]).map(([k,v])=>`<span class="detail-pill"><strong>${k}:</strong> ${escapeHtml(v)}</span>`).join('')}</div></div>`:'';
  const examples=(w.examples||[]).map(e=>`<div class="example-card"><strong>${escapeHtml(e.en)}</strong><span>${escapeHtml(e.vi)}</span></div>`).join('');
  $('#modalContent').innerHTML=`<h3 class="detail-word">${escapeHtml(w.word)}</h3><div class="detail-ipa">${escapeHtml(w.phonetic?.us||'Chưa có phiên âm')}</div><div class="detail-pos">${posMarkup(w)}</div><div class="detail-section"><h4>MEANING & DEFINITIONS</h4>${senses||'<p>Chưa có nghĩa.</p>'}</div>${family}${verbs}<div class="detail-section"><h4>TOPICS</h4>${topicsMarkup(w.topics)}</div>${w.collocations?.length?`<div class="detail-section"><h4>COLLOCATIONS</h4><div class="detail-pills">${w.collocations.map(x=>`<span class="detail-pill">${escapeHtml(x)}</span>`).join('')}</div></div>`:''}<div class="detail-section"><h4>EXAMPLES</h4>${examples||'<p>Chưa có ví dụ.</p>'}</div><div class="modal-actions"><button class="secondary-button" data-edit="${escapeHtml(w.id)}">${icon('edit','ui-icon button-icon')} Sửa bản ghi</button></div>`;
  $('#modalBackdrop').hidden=false;
}
function openEditor(id=null){
  const old=state.words.find(w=>w.id===id); const s=old?.senses?.[0]||{};
  $('#modalEyebrow').textContent=old?'DATA MANAGEMENT · EDIT':'DATA MANAGEMENT · NEW'; $('#modalTitle').textContent=old?'Chỉnh sửa từ vựng':'Thêm từ vựng mới';
  const topicOptions=state.categories.map(c=>`<option value="${escapeHtml(c.id)}">${escapeHtml(c.id)} · ${escapeHtml(c.label)}</option>`).join('');
  $('#modalContent').innerHTML=`<form id="wordEditorForm"><div class="editor-grid">
  <label class="field"><span class="field-label">TỪ TIẾNG ANH *</span><input name="word" required value="${escapeHtml(old?.word||'')}" placeholder="Ví dụ: schedule"></label>
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
async function deleteWord(id){const item=state.words.find(w=>w.id===id);if(!item)return;if(!confirm(`Xóa từ "${item.word}" khỏi bản dữ liệu trên thiết bị?`))return;state.words=state.words.filter(w=>w.id!==id);await persistWorkspace();updateOverview();renderDictionary();renderDataTable();toast(`Đã xóa ${item.word} khỏi bản dữ liệu cục bộ.`);}
function closeModal(){ $('#modalBackdrop').hidden=true; $('#modalContent').innerHTML=''; }
function downloadFile(name,content,type){const blob=new Blob([content],{type});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function exportJSON(){const payload={schemaVersion:1,exportedAt:new Date().toISOString(),note:'TOEIC Vocabulary Phase 1 workspace export. Import back through Data Management.',words:sortWords(state.words)};downloadFile('toeic-vocabulary-export.json',JSON.stringify(payload,null,2),'application/json;charset=utf-8');toast('Đã xuất tệp JSON.');}
function csvEscape(v){const s=String(v??'');return /[",\r\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s;}
function exportCSV(){const headers=['id','word','ipa','pos','meaning_vi','definition_en','synonyms','antonyms','topics','example_en','example_vi','collocations'];const rows=state.words.map(w=>{const s=getPrimarySense(w);return [w.id,w.word,w.phonetic?.us||'',s.pos,s.meaning_vi,s.definition_en,(s.synonyms||[]).join('|'),(s.antonyms||[]).join('|'),w.topics.join('|'),w.examples?.[0]?.en||'',w.examples?.[0]?.vi||'',w.collocations.join('|')];});const csv='\uFEFF'+[headers,...rows].map(r=>r.map(csvEscape).join(',')).join('\r\n');downloadFile('toeic-vocabulary-export.csv',csv,'text/csv;charset=utf-8');toast('Đã xuất tệp CSV.');}
function parseCSV(text){const rows=[];let row=[],cell='',quoted=false;for(let i=0;i<text.length;i++){const ch=text[i];if(quoted){if(ch==='"'&&text[i+1]==='"'){cell+='"';i++;}else if(ch==='"')quoted=false;else cell+=ch;}else if(ch==='"')quoted=true;else if(ch===','){row.push(cell);cell='';}else if(ch==='\n'){row.push(cell.replace(/\r$/,''));rows.push(row);row=[];cell='';}else cell+=ch;}if(cell.length||row.length){row.push(cell.replace(/\r$/,''));rows.push(row);}const [headers,...items]=rows;return items.filter(r=>r.some(x=>x.trim())).map(r=>Object.fromEntries(headers.map((h,i)=>[h.trim(),r[i]??'']))).map(r=>({id:r.id,word:r.word,phonetic:{us:r.ipa},senses:[{pos:r.pos,meaning_vi:r.meaning_vi,definition_en:r.definition_en,synonyms:String(r.synonyms||'').split('|').filter(Boolean),antonyms:String(r.antonyms||'').split('|').filter(Boolean)}],topics:String(r.topics||'').split('|').filter(Boolean),examples:[{en:r.example_en,vi:r.example_vi}],collocations:String(r.collocations||'').split('|').filter(Boolean)}));}
async function importFile(file){const text=await file.text();let imported;if(file.name.toLowerCase().endsWith('.csv'))imported=parseCSV(text.replace(/^\uFEFF/,''));else{const parsed=JSON.parse(text);imported=Array.isArray(parsed)?parsed:(parsed.words||[]);}if(!Array.isArray(imported)||!imported.length)throw new Error('Không tìm thấy danh sách từ vựng trong tệp.');const map=new Map(state.words.map(w=>[w.id,w]));let added=0,updated=0;for(const raw of imported){const rec=normalizeRecord(raw);const duplicate=[...map.values()].find(w=>normalizeText(w.word)===normalizeText(rec.word));if(duplicate&&duplicate.id!==rec.id){rec.id=duplicate.id;updated++;}else if(map.has(rec.id))updated++;else added++;map.set(rec.id,rec);}state.words=[...map.values()];await persistWorkspace();updateOverview();renderDictionary();renderDataTable();toast(`Import hoàn tất: ${added} mới, ${updated} cập nhật.`);}
async function resetWorkspace(){if(!confirm('Khôi phục toàn bộ dữ liệu từ các tệp JSON gốc? Mọi thay đổi cục bộ trên thiết bị sẽ bị xóa.'))return;await dbDelete('workspace');state.words=[...state.baseWords];state.localWorkspace=false;updateStorageLabel();updateOverview();renderDictionary();renderDataTable();toast('Đã khôi phục dữ liệu gốc.');}
function goToLetter(letter){state.activeLetter=letter||'';$('#dictionarySearch').value='';$('#topicFilter').value='';$('#posFilter').value='';navigate('dictionary');}
function bindEvents(){
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
  $('#modalContent').addEventListener('click',e=>{const edit=e.target.closest('[data-edit]');if(edit)openEditor(edit.dataset.edit);});
  $('#globalSearch').addEventListener('keydown',e=>{if(e.key==='Enter'){navigate('dictionary');$('#dictionarySearch').value=e.target.value;renderDictionary();}});
  $('#globalSearch').addEventListener('input',e=>{if(e.target.value.length>=2){navigate('dictionary');$('#dictionarySearch').value=e.target.value;renderDictionary();}});
  document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();$('#globalSearch').focus();}if(e.key==='Escape')closeModal();});
  window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();state.deferredInstall=e;$('#installButton').hidden=false;});
  $('#installButton').addEventListener('click',async()=>{if(!state.deferredInstall)return;state.deferredInstall.prompt();await state.deferredInstall.userChoice;state.deferredInstall=null;$('#installButton').hidden=true;});
}
function updateDate(){const now=new Date();$('#todayLabel').textContent=new Intl.DateTimeFormat('vi-VN',{weekday:'long',day:'2-digit',month:'long',year:'numeric'}).format(now);}
async function registerSW(){if(!('serviceWorker'in navigator))return;try{await navigator.serviceWorker.register('./sw.js',{scope:'./'});}catch(err){console.warn('Service Worker chưa đăng ký được:',err);}}
async function init(){bindEvents();updateDate();try{await loadData();}catch(err){console.error(err);$('#metricWords').textContent='!';toast(`Không tải được dữ liệu: ${err.message}`,'error');$('#resultCount').textContent='Không tải được dữ liệu';}registerSW();}
init();
