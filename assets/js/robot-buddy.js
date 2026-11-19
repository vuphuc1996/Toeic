/**
 * Robot Buddy — scripted, offline companion for the GitHub Pages PWA.
 * It uses the bundled dialogue library and receives optional, read-only local
 * learning insights from the application. It never opens storage, calls APIs,
 * sends learner data outside the device or uses a generative model.
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
  dashboard: { label: 'Mở Trang chủ', page: 'dashboard' },
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
  { action: 'dashboard', terms: ['trang chu', 'tong quan', 'dashboard', 'thong ke tong quan'] },
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
    if (/(tien do|hoc den dau|ket qua hoc|phan tich hoc tap|can hoc|can luyen|can on|thong ke hoc|learning progress)/.test(text)) return { intent: 'insights', emotion: 'analyzing' };
    if (/(tat phan tich|ngung doc tien do|khong phan tich tien do)/.test(text)) return { intent: 'insights-off', emotion: 'caring' };
    if (/(noi dung dang xem|noi dung nay|bai nay|cau nay|tu nay|giai thich (?:bai|cau|tu) nay|giup toi (?:bai|cau|tu) nay|explain this|help me with this)/.test(text)) return { intent: 'context-help', emotion: 'thinking' };
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

  reply(message = '', context = {}) {
    const match = this.classify(message);
    if (match.intent === 'context-help') {
      const pageLabel = String(context.pageLabel || 'khu vực hiện tại');
      const item = context.currentItem && typeof context.currentItem === 'object' ? context.currentItem : null;
      const title = String(item?.title || '').trim();
      const snippet = String(item?.snippet || '').trim().slice(0, 180);
      const tips = ({
        dictionary: 'Hãy xem nghĩa theo từ loại, nghe phát âm và đọc ví dụ trước khi tự đặt một câu mới.',
        flashcards: 'Thử tự nhớ nghĩa trước khi lật thẻ; nếu chưa nhớ, đọc ví dụ rồi thử lại.',
        practice: 'Đọc kỹ câu hỏi, gạch từ khóa và tự loại trừ từng lựa chọn trước khi xem giải thích.',
        grammar: 'Xem công thức và ví dụ song ngữ, sau đó tự làm một câu để kiểm tra cách dùng.',
        reading: 'Đọc câu hỏi để xác định từ khóa, sau đó tìm bằng chứng trực tiếp trong đoạn hoặc tài liệu.',
        listening: 'Lượt đầu nắm ý chính và người nói; lượt sau tập trung vào chi tiết, mục đích và hành động tiếp theo.',
        foundation: 'Đọc mục tiêu bài học, xem ví dụ rồi làm phần tự kiểm tra trước khi chuyển sang bài tiếp theo.'
      })[context.page] || 'Bạn có thể cho mình biết phần nào đang khó; mình sẽ hướng dẫn theo chức năng hiện có.';
      const text = title
        ? `Bạn đang ở ${pageLabel}, nội dung hiện tại là “${title}”.${snippet ? ` Thông tin đang hiển thị: ${snippet}.` : ''} ${tips}`
        : `Bạn đang ở ${pageLabel}. ${tips}`;
      return { intent: match.intent, emotion: 'thinking', text, actions: [], source: 'current-app-interaction-context' };
    }
    if (match.intent === 'insights') return { intent: match.intent, emotion: 'analyzing', text: '', actions: [], source: 'local-learning-insights' };
    if (match.intent === 'insights-off') return { intent: match.intent, emotion: 'caring', text: 'Bạn có thể tắt phân tích tiến độ bằng nút trong phần đầu khung trò chuyện. Mình vẫn có thể trò chuyện và hướng dẫn sử dụng bình thường.', actions: [], source: 'local-dialogue-library' };
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
    if (match.intent === 'identity') text = 'Chào bạn! 😊 Mình là Robot Buddy, người bạn đồng hành được tạo ra dành riêng cho TOEIC Dictionary. Mình được tạo ra bởi nhà phát triển Vũ Nguyễn Hoàng Phúc với mong muốn giúp việc học tiếng Anh của bạn thú vị và dễ dàng hơn. Mình có thể trò chuyện, hướng dẫn các chức năng, đọc tiến độ học được lưu ngay trên thiết bị để gợi ý nội dung cần học, luyện và ôn. Mình không phải chatbot AI trực tuyến: không gọi API, không kết nối máy chủ để phân tích và không gửi dữ liệu học tập của bạn ra ngoài thiết bị. 💙';
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
