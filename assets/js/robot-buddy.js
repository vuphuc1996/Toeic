/**
 * Robot Buddy — scripted, offline companion for the GitHub Pages PWA.
 * It uses only the bundled dialogue library and user interface intent.
 * It MUST NOT read learner progress, IndexedDB, localStorage learning keys,
 * Google AI, external APIs, network services or generative models.
 */

export function normalizeRobotText(value = '') {
  return String(value)
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/đ/g, 'd').replace(/Đ/g, 'd')
    .toLowerCase().replace(/[^a-z0-9\s]/g, ' ')
    .replace(/\s+/g, ' ').trim();
}

const PAGE_COMMANDS = Object.freeze({
  dictionary: { label: 'Mở Từ vựng', page: 'dictionary' },
  flashcards: { label: 'Mở Flashcard', page: 'flashcards' },
  practice: { label: 'Mở Ôn tập', page: 'practice' },
  grammar: { label: 'Mở Ngữ pháp', page: 'grammar' },
  reading: { label: 'Mở Đọc hiểu', page: 'reading' },
  listening: { label: 'Mở Nghe hiểu', page: 'listening' },
  mock: { label: 'Mở Thi thử', page: 'mock' },
  foundation: { label: 'Mở Foundation', page: 'foundation' },
  settings: { label: 'Mở Cấu hình', page: 'settings' },
  data: { label: 'Mở Quản lý dữ liệu', page: 'data' },
  placement: { label: 'Bắt đầu đánh giá', command: 'placement' }
});

const FEATURE_INTENTS = Object.freeze([
  { action: 'dictionary', terms: ['tu vung', 'dictionary', 'tra tu', 'tim tu', 'tu moi'] },
  { action: 'flashcards', terms: ['flashcard', 'flash cards', 'the tu', 'the ghi nho'] },
  { action: 'practice', terms: ['on tap', 'review', 'luyen tap', 'luyen tu', 'cau hoi'] },
  { action: 'grammar', terms: ['ngu phap', 'grammar', 'gramma'] },
  { action: 'reading', terms: ['reading', 'doc hieu', 'bai doc', 'luyen doc'] },
  { action: 'listening', terms: ['listening', 'nghe hieu', 'luyen nghe', 'phat am', 'giong doc'] },
  { action: 'mock', terms: ['mock', 'thi thu', 'de thi', 'thi toeic'] },
  { action: 'foundation', terms: ['foundation', 'lo trinh', 'nen tang', 'bai hoc nen tang'] },
  { action: 'placement', terms: ['placement', 'danh gia dau vao', 'kiem tra dau vao', 'diem bat dau'] },
  { action: 'settings', terms: ['cau hinh', 'cai dat', 'nhac nho', 'reminder'] },
  { action: 'data', terms: ['quan ly du lieu', 'du lieu ca nhan', 'sao luu', 'import', 'export', 'nhap du lieu', 'xuat du lieu'] }
]);

const FALLBACK_LIBRARY = Object.freeze({
  categories: {
    greeting: { emotion: 'greeting', messages: [{ text: 'Xin chào! Mình là Robot Buddy. Mình có thể chỉ bạn các khu vực trong ứng dụng.' }] },
    caring: { emotion: 'caring', messages: [{ text: 'Bạn có cần mình hỗ trợ điều gì không?' }] },
    encouragement: { emotion: 'motivation', messages: [{ text: 'Cứ tiến từng bước nhỏ nhé. Bạn không cần phải vội vàng đâu!' }] },
    help: { emotion: 'listening', messages: [{ text: 'Bạn hãy nói tên mục đang muốn mở nhé. Mình sẽ thử chỉ đường.' }] },
    rest: { emotion: 'sleepy', messages: [{ text: 'Một khoảng nghỉ ngắn cũng rất đáng giá. Quay lại khi bạn thấy thoải mái nhé.' }] },
    reaction: { emotion: 'happy', messages: [{ text: 'Mình đã sẵn sàng cho bước tiếp theo!' }] },
    learning: { emotion: 'thinking', messages: [{ text: 'Bạn có thể chọn một mục tiêu nhỏ và bắt đầu từ đó.' }] }
  },
  features: {}, faq: [], quickPrompts: []
});

export class RobotBuddyEngine {
  constructor(library = FALLBACK_LIBRARY, random = Math.random) {
    this.library = library && typeof library === 'object' ? library : FALLBACK_LIBRARY;
    this.random = typeof random === 'function' ? random : Math.random;
    this.cursors = new Map();
    this.lastByGroup = new Map();
  }

  pick(group, listOverride = null) {
    const source = Array.isArray(listOverride)
      ? listOverride
      : this.library.categories?.[group]?.messages;
    if (!Array.isArray(source) || source.length === 0) {
      const fallback = FALLBACK_LIBRARY.categories[group]?.messages || FALLBACK_LIBRARY.categories.help.messages;
      return fallback[0].text;
    }
    const last = this.lastByGroup.get(group);
    let index = Math.floor(this.random() * source.length);
    if (source.length > 1 && index === last) index = (index + 1) % source.length;
    this.lastByGroup.set(group, index);
    return String(source[index]?.text || source[index] || 'Mình đang ở đây để hỗ trợ bạn.');
  }

  pickFeature(action) {
    const feature = this.library.features?.[action];
    const list = feature?.messages;
    if (!Array.isArray(list) || !list.length) return this.pick('help');
    return this.pick(`feature:${action}`, list);
  }

  pickFaq(message) {
    const text = normalizeRobotText(message);
    const match = (this.library.faq || []).find(item =>
      (item.keywords || []).some(keyword => text.includes(normalizeRobotText(keyword)))
    );
    return match ? String(match.answer || '') : '';
  }

  classify(message = '') {
    const text = normalizeRobotText(message);
    if (!text) return { intent: 'help', emotion: 'listening' };
    if (/(ban la ai|robot buddy|ten gi|gioi thieu ban)/.test(text)) return { intent: 'identity', emotion: 'happy' };
    if (/(^|\s)(xin chao|chao ban|hello|hi|hey)(?=\s|$)/.test(text)) return { intent: 'greeting', emotion: 'greeting' };
    if (/(chuc mung|tuyet voi|wow|yay|that tuyet)/.test(text)) return { intent: 'celebrate', emotion: 'celebrate' };
    if (/(ke chuyen cuoi|noi dua|dua chut|joke|vui mot chut)/.test(text)) return { intent: 'playful', emotion: 'playful' };
    if (/(cam on|thank you|thanks|tuyet voi)/.test(text)) return { intent: 'thanks', emotion: 'happy' };
    if (/(tam biet|hen gap lai|bye bye|goodbye)/.test(text)) return { intent: 'goodbye', emotion: 'sleepy' };
    if (/(dong vien|co gang|nan long|chan qua|\bchan\b|met qua|\bmet\b|ap luc|stress|buon qua)/.test(text)) return { intent: 'encouragement', emotion: 'motivation' };
    if (/(nghi ngoi|nghi mot chut|tam nghi|nghi day)/.test(text)) return { intent: 'rest', emotion: 'sleepy' };

    const faq = this.pickFaq(message);
    if (faq) return { intent: 'faq', emotion: 'thinking' };
    for (const feature of FEATURE_INTENTS) {
      if (feature.terms.some(term => text.includes(normalizeRobotText(term)))) {
        return { intent: 'feature', action: feature.action, emotion: 'thinking' };
      }
    }
    if (/(tro giup|giup minh|ho tro|khong biet|khong ro|huong dan)/.test(text)) return { intent: 'help', emotion: 'listening' };
    return { intent: 'unknown', emotion: 'thinking' };
  }

  reply(message = '') {
    const match = this.classify(message);
    if (match.intent === 'feature') {
      const command = PAGE_COMMANDS[match.action];
      return {
        intent: match.intent, emotion: match.emotion,
        text: this.pickFeature(match.action),
        actions: command ? [{ ...command, action: match.action }] : [],
        source: 'static-feature-library'
      };
    }
    if (match.intent === 'faq') {
      return { intent: match.intent, emotion: match.emotion, text: this.pickFaq(message), actions: [], source: 'static-faq' };
    }
    const group = ({
      identity: 'greeting', greeting: 'greeting', thanks: 'reaction', goodbye: 'rest',
      celebrate: 'reaction', playful: 'reaction', encouragement: 'encouragement', rest: 'rest', help: 'help', unknown: 'help'
    })[match.intent] || 'help';
    let text = this.pick(group);
    if (match.intent === 'celebrate') text = `${text} Cùng giữ tinh thần tích cực nhé!`;
    if (match.intent === 'playful') text = `${text} Mình cũng thích những phút vui vẻ như thế này!`;
    if (match.intent === 'identity') text = 'Mình là Robot Buddy, nhân vật đồng hành của TOEIC Dictionary. Mình dùng thư viện hội thoại được đóng gói sẵn, không đọc tiến độ học và không phải chatbot AI trực tuyến.';
    if (match.intent === 'thanks') text = `${text} Cảm ơn bạn đã trò chuyện cùng mình!`;
    if (match.intent === 'unknown') text = `${text} Hiện tại mình phản hồi theo các chủ đề và từ khóa đã được chuẩn bị sẵn, nên có thể chưa hiểu mọi câu hỏi tự do.`;
    return { intent: match.intent, emotion: match.emotion, text, actions: [], source: 'static-dialogue-library' };
  }

  get quickPrompts() {
    return Array.isArray(this.library.quickPrompts) ? this.library.quickPrompts : [];
  }
}

export function createRobotBuddy(library, random = Math.random) {
  return new RobotBuddyEngine(library, random);
}
