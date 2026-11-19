/**
 * Robot Buddy — scripted, offline companion for the GitHub Pages PWA.
 * It composes varied offline replies from the bundled dialogue/FAQ library,
 * lightweight rules and current in-memory app context. The UI streams the reply
 * progressively. It never opens storage, calls APIs, sends learner data outside
 * the device or uses a generative model.
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
    const tokens = new Set(text.split(' ').filter(token => token.length > 1));
    let best = null;
    let bestScore = 0;
    for (const item of this.library.faq || []) {
      let score = 0;
      for (const keyword of item.keywords || []) {
        const normalized = normalizeRobotText(keyword);
        if (normalized && (normalized.length <= 3 ? tokens.has(normalized) : text.includes(normalized))) score += Math.max(2, normalized.split(' ').length * 2);
        else {
          for (const token of normalized.split(' ')) if (token.length > 2 && tokens.has(token)) score += 1;
        }
      }
      if (score > bestScore) { best = item; bestScore = score; }
    }
    return best && bestScore >= 2 ? String(best.answer || '') : '';
  }

  pickResponse(group, variants) {
    return this.pick(`response:${group}`, variants);
  }

  composeResponse(group, parts) {
    return parts.map(part => String(part || '').trim()).filter(Boolean).join(' ');
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
      const opener = this.pickResponse('context-open', [
        'Được, mình sẽ dựa vào nội dung bạn đang mở để hướng dẫn nhé.',
        'Mình đã nhận ra khu vực bạn đang học. Cùng xem từng bước nhé.',
        'Để mình bám sát màn hình hiện tại thay vì hướng dẫn chung chung nhé.'
      ]);
      const contextLine = title
        ? `Bạn đang ở ${pageLabel}, nội dung hiện tại là “${title}”.${snippet ? ` Thông tin đang hiển thị: ${snippet}.` : ''}`
        : `Bạn đang ở ${pageLabel}.`;
      const transition = this.pickResponse('context-transition', [
        'Một cách làm phù hợp ở bước này là:',
        'Bạn có thể thử theo trình tự sau:',
        'Mình gợi ý bạn bắt đầu như sau:'
      ]);
      const close = this.pickResponse('context-close', [
        'Bạn cứ làm từng bước; khi gặp đúng chỗ vướng, hãy gửi câu hỏi cụ thể hơn cho mình.',
        'Thử cách này trước nhé. Mình vẫn có thể hướng dẫn tiếp theo nội dung bạn đang mở.',
        'Đừng vội chuyển bài; tự kiểm tra lại một lần sẽ giúp bạn nhớ lâu hơn.'
      ]);
      const text = this.composeResponse('context', [opener, contextLine, transition, tips, close]);
      return { intent: match.intent, emotion: 'thinking', text, actions: [], source: 'current-app-interaction-context' };
    }
    if (match.intent === 'insights') return { intent: match.intent, emotion: 'analyzing', text: '', actions: [], source: 'local-learning-insights' };
    if (match.intent === 'insights-off') return { intent: match.intent, emotion: 'caring', text: 'Bạn có thể tắt phân tích tiến độ bằng nút trong phần đầu khung trò chuyện. Mình vẫn có thể trò chuyện và hướng dẫn sử dụng bình thường.', actions: [], source: 'local-dialogue-library' };
    if (match.intent === 'feature') {
      const command = PAGE_COMMANDS[match.action];
      const label = command?.label?.replace(/^Mở\s+/, '') || 'mục bạn cần';
      const opener = this.pickResponse('feature-open', [
        `Được nhé, mình hiểu bạn đang muốn đến phần ${label}.`,
        `Mình sẽ đưa bạn đến đúng khu vực ${label}.`,
        `Bạn đang cần ${label}; mình chỉ nhanh đường vào nhé.`
      ]);
      const guidance = this.pickFeature(match.action);
      const nextStep = command
        ? this.pickResponse('feature-close', [
          `Bạn có thể nhấn nút “${command.label}” bên dưới để chuyển thẳng đến đó.`,
          `Dùng nút “${command.label}” bên dưới là nhanh nhất.`,
          `Mình đã chuẩn bị lối tắt “${command.label}” ngay dưới câu trả lời.`
        ])
        : '';
      return {
        intent: match.intent, emotion: match.emotion,
        text: this.composeResponse('feature', [opener, guidance, nextStep]),
        actions: command ? [{ ...command, action: match.action }] : [],
        source: 'local-context-composition'
      };
    }
    if (match.intent === 'faq') {
      const answer = this.pickFaq(message);
      const opener = this.pickResponse('faq-open', [
        'Mình tìm được hướng dẫn phù hợp trong tài liệu hỗ trợ hiện có.',
        'Mình sẽ giải thích dựa trên thông tin được tích hợp trong ứng dụng nhé.',
        'Phần này mình có thể hướng dẫn dựa trên nội dung hỗ trợ sẵn có:'
      ]);
      const close = this.pickResponse('faq-close', [
        'Bạn thử theo các bước đó nhé.',
        'Bạn có thể làm theo hướng dẫn này ngay trong ứng dụng.',
        'Nếu bạn đang ở màn hình liên quan, mình có thể chỉ tiếp đường đi.'
      ]);
      return { intent: match.intent, emotion: match.emotion, text: this.composeResponse('faq', [opener, answer, close]), actions: [], source: 'local-faq-composition' };
    }
    const group = ({
      identity: 'greeting', greeting: 'greeting', thanks: 'reaction', goodbye: 'rest',
      celebrate: 'reaction', playful: 'reaction', encouragement: 'encouragement', rest: 'rest', help: 'help', unknown: 'help'
    })[match.intent] || 'help';
    let text = this.pick(group);
    if (match.intent === 'celebrate') {
      text = this.composeResponse('celebrate', [text, this.pickResponse('celebrate-close', [
        'Cùng giữ nhịp học tích cực này nhé!', 'Một bước tiến nhỏ cũng đáng được ghi nhận. Tiếp tục nào!',
        'Hãy tận dụng đà này để hoàn thành thêm một mục tiêu nhỏ nhé.'
      ])]);
    }
    if (match.intent === 'playful') {
      text = this.composeResponse('playful', [text, this.pickResponse('playful-close', [
        'Học nghiêm túc nhưng vẫn nên có những phút vui vẻ mà!', 'Nạp chút năng lượng rồi mình quay lại TOEIC nhé!',
        'Một chút vui vẻ cũng giúp buổi học dễ chịu hơn.'
      ])]);
    }
    if (match.intent === 'identity') {
      const opener = this.pickResponse('identity-open', ['Chào bạn! 😊 Mình là Robot Buddy.', 'Mình là Robot Buddy đây! Rất vui được đồng hành cùng bạn.']);
      const role = 'Mình là người bạn đồng hành trong TOEIC Dictionary, được xây dựng bởi Vũ Nguyễn Hoàng Phúc để hỗ trợ tìm chức năng, hướng dẫn cách học và đọc tiến độ học được lưu trên thiết bị khi bạn bật phân tích.';
      const boundary = 'Mình không phải chatbot AI trực tuyến và không gọi API để tạo câu trả lời; nội dung được kết hợp từ thư viện hỗ trợ, quy tắc và ngữ cảnh ứng dụng ngay trên thiết bị. Dữ liệu học tập không được gửi ra ngoài.';
      text = this.composeResponse('identity', [opener, role, boundary, '💙']);
    }
    if (match.intent === 'thanks') text = this.composeResponse('thanks', [text, this.pickResponse('thanks-close', ['Mình vui vì giúp được bạn!', 'Cứ gọi mình khi cần hỗ trợ nhé!', 'Rất sẵn lòng đồng hành cùng bạn.'])]);
    if (match.intent === 'unknown') {
      const current = context.currentItem?.title ? ` Mình thấy bạn đang học “${String(context.currentItem.title).slice(0, 90)}” trong mục ${context.pageLabel || 'hiện tại'}.` : '';
      const opener = this.pickResponse('unknown-open', [
        'Mình chưa xác định chắc ý bạn muốn hỏi, nên không muốn đoán sai.',
        'Câu hỏi này nằm ngoài phần mình nhận diện được ngay lúc này.',
        'Mình cần thêm một chút ngữ cảnh để trả lời đúng trọng tâm.'
      ]);
      const clarify = this.pickResponse('unknown-clarify', [
        'Bạn đang muốn hỏi về từ vựng, ngữ pháp, Listening, Reading hay cách sử dụng ứng dụng?',
        'Bạn có thể nói rõ hơn mục tiêu: giải thích kiến thức, hướng dẫn thao tác hay tìm bài luyện phù hợp?',
        'Bạn gửi thêm tên từ, câu hỏi hoặc phần bài học đang xem nhé; mình sẽ bám vào thông tin đó để hỗ trợ.'
      ]);
      text = this.composeResponse('unknown', [opener, current, clarify]);
    }
    return { intent: match.intent, emotion: match.emotion, text, actions: [], source: match.intent === 'unknown' ? 'local-clarification-composition' : 'local-dialogue-composition' };
  }

  get quickPrompts() {
    return Array.isArray(this.library.quickPrompts) ? this.library.quickPrompts : [];
  }
}

export function createRobotBuddy(library, random = Math.random) {
  return new RobotBuddyEngine(library, random);
}
