import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
LISTENING = json.loads((ROOT / "data/listening/listening-library.json").read_text(encoding="utf-8"))["listening"]


class SpeechReadinessTests(unittest.TestCase):
    def test_audio_start_is_immediate_and_watchdogs_are_defined(self):
        self.assertRegex(APP, r"SPEECH_START_TIMEOUT_MS\s*=\s*10000")
        self.assertRegex(APP, r"SPEECH_END_TIMEOUT_MIN_MS\s*=\s*20000")
        self.assertRegex(APP, r"PART1_TITLE_PAUSE_MS\s*=\s*1000")
        self.assertRegex(APP, r"PART1_LEAD_IN_PAUSE_MS\s*=\s*1000")
        self.assertRegex(APP, r"PART1_OPTION_LABEL_PAUSE_MS\s*=\s*1500")
        self.assertRegex(APP, r"PART1_OPTION_GAP_MS\s*=\s*1300")

    def test_voice_selector_refresh_helper_is_defined_and_used(self):
        self.assertRegex(APP, r"function\s+refreshSpeechVoiceSelectors\s*\(")
        helper = APP[APP.index("function refreshSpeechVoiceSelectors("):APP.index("function chooseEnglishVoice(")]
        self.assertIn("getSpeechVoices()", helper)
        self.assertIn("gender==='male'?'Male':'Female'", helper)
        self.assertIn("ttsVoiceStatus", helper)
        self.assertIn("select.disabled=!voices.length", helper)
        self.assertIn("refreshSpeechVoiceSelectors", APP[APP.index("function bindTtsSettings("):APP.index("async function answerListeningQuestion(")])

    def test_voice_catalogue_is_checked_synchronously_without_startup_buffer(self):
        prepare = APP[APP.index("function prepareSpeechEngine("):APP.index("async function speakText(")]
        self.assertIn("synth.getVoices()", prepare)
        self.assertIn("synth.resume()", prepare)
        self.assertNotRegex(prepare, r"\n\s*await\s+")
        self.assertNotIn("waitSpeechGap", prepare)
        self.assertNotIn("TTS_PREPARATION_DELAY_MS", APP)

    def test_all_single_utterance_routes_queue_speech_without_awaiting_preparation(self):
        speak = APP[APP.index("async function speakText("):APP.index("let lastSpeechError")]
        self.assertIn("prepareSpeechEngine(token)", speak)
        self.assertNotIn("await prepareSpeechEngine", speak)
        self.assertIn("const speech=speakUtterance(", speak)
        self.assertLess(speak.index("const speech=speakUtterance("), speak.index("const ok=await speech"))
        self.assertEqual(len(re.findall(r"\bsynth\.speak\(utterance\)", APP)), 1)
        self.assertEqual(len(re.findall(r"function\s+speakText\s*\(", APP)), 1)
        self.assertEqual(len(re.findall(r"function\s+speakUtterance\s*\(", APP)), 1)

    def test_shared_speech_utterance_has_watchdogs_and_default_voice_fallback(self):
        utterance = APP[APP.index("function speakUtterance("):APP.index("async function playListeningAudio(")]
        self.assertIn("SPEECH_START_TIMEOUT_MS", utterance)
        self.assertIn("SPEECH_END_TIMEOUT_MIN_MS", utterance)
        self.assertIn("fallbackAttempted", utterance)
        self.assertIn("enqueue(null,true)", utterance)
        self.assertIn("activeAttempt", utterance, "stale events from a failed voice must not settle its fallback attempt")
        self.assertIn("getSpeechVoices()", APP)
        self.assertIn("voice catalogue is initializing", APP)
        self.assertIn("speechFailureMessage()", APP)

    def test_part1_uses_title_lead_in_separate_labels_and_descriptions(self):
        play = APP[APP.index("async function playListeningAudio("):APP.index("async function playListeningVocabulary(")]
        self.assertLess(play.index("prepareSpeechEngine(playbackToken)"), play.index("const say=async"))
        self.assertNotIn("await prepareSpeechEngine", play)
        self.assertIn("'Part 1':{name:String(item.topic||item.title||'Photographs').trim(),leadIn:PART1_LEAD_IN_TEXT}", play)
        self.assertIn("const title=`${item.part}: ${meta.name}`", play)
        self.assertIn("say(title,leadSegment", play)
        self.assertIn("waitSpeechGap(PART_SEQUENCE_PAUSE_MS,playbackToken)", play)
        self.assertIn("say(meta.leadIn,leadSegment", play)
        self.assertIn("say(isPart1?`${String.fromCharCode(65+index)}.`:optionText", play)
        self.assertIn("waitSpeechGap(PART1_OPTION_LABEL_PAUSE_MS,playbackToken)", play)
        self.assertIn("say(optionText,segment,`Đang đọc nội dung lựa chọn", play)
        self.assertIn("const gap=isPart1?PART1_OPTION_GAP_MS", play)
        self.assertIn("waitSpeechGap(gap,playbackToken)", play)
        self.assertNotIn("cfg.part1LeadInPauseMs", play)
        self.assertNotIn("cfg.part1OptionPauseMs", play)

    def test_parts_2_to_4_have_heading_lead_in_questions_and_lettered_choices(self):
        play = APP[APP.index("async function playListeningAudio("):APP.index("async function playListeningVocabulary(")]
        for part, title, lead in (
            ("Part 2", "Question–Response", "Now, listen to the question and choose the best response."),
            ("Part 3", "Conversations", "Now, listen to the conversation and answer the questions."),
            ("Part 4", "Short Talks", "Now, listen to the talk and answer the questions."),
        ):
            self.assertIn(f"'{part}':{{name:'{title}',leadIn:'{lead}'}}", play)
        self.assertIn("const choices=Array.isArray(question.choices)?question.choices:[]", play)
        self.assertIn("say(`${letter}.`,leadSegment", play)
        self.assertIn("waitSpeechGap(PART_OPTION_LABEL_PAUSE_MS,playbackToken)", play)
        self.assertIn("say(String(choices[choiceIndex]),leadSegment", play)

    def test_every_part1_unit_has_four_clean_description_segments(self):
        part1 = [item for item in LISTENING if item.get("part") == "Part 1"]
        self.assertTrue(part1, "Listening library must include Part 1 units")
        for item in part1:
            self.assertEqual(len(item.get("segments", [])), 4, item.get("id"))
            self.assertTrue(item.get("topic"), item.get("id"))
            for segment in item["segments"]:
                self.assertIsInstance(segment.get("text"), str)
                self.assertTrue(segment["text"].strip())

    def test_practice_and_mock_part1_use_the_same_full_audio_pipeline(self):
        self.assertIn("playListeningAudio(play.dataset.listeningPlay)", APP)
        self.assertIn("playListeningAudio(audio.dataset.mockAudio", APP)
        mock = APP[APP.index("function updateMockGuidedFlow("):APP.index("function renderMockExam(")]
        self.assertIn("if(group.part==='Part 1'){", mock)
        self.assertIn("playListeningAudio(group.unitId,{statusElement});", mock)
        self.assertIn("Part 1 owns its full title → lead-in → A/B/C/D script", mock)
        self.assertIn("Part 1: ${group.topic||group.title||'Photographs'}. ${PART1_LEAD_IN_TEXT}", mock)
        markup = APP[APP.index("function mockGroupMarkup("):APP.index("function ensureMockGuidedFlow(")]
        self.assertIn("nhãn A/B/C/D (nghỉ 1,5 giây)", markup)

    def test_practice_transcript_exposes_part_title_lead_in_and_letter_labels(self):
        detail = APP[APP.index("function openListeningDetail("):APP.index("let listeningPlaybackToken=0;")]
        self.assertIn("transcript-part-title", detail)
        self.assertIn("${escapeHtml(item.part)}: ${escapeHtml(transcriptPartMeta.name)}", detail)
        self.assertIn("transcript-lead-in", detail)
        self.assertIn("OPTION ${letter}", detail)
        self.assertIn("${letter}. ", detail)
        self.assertIn("Now, listen to the four statements.", APP)

    def test_vocabulary_playback_uses_synchronous_preparation(self):
        play = APP[APP.index("async function playListeningVocabulary("):APP.index("function saveTtsSetting(")]
        self.assertIn("prepareSpeechEngine(token)", play)
        self.assertNotIn("await prepareSpeechEngine", play)
        self.assertLess(play.index("prepareSpeechEngine(token)"), play.index("for(let i=0;i<words.length;i++)"))

    def test_reading_passages_use_the_same_tts_pipeline(self):
        self.assertIn('data-reading-speak="${escapeHtml(id)}"', APP)
        reader = APP[APP.index("function playReadingText(id){"):APP.index("async function answerReadingQuestion(")]
        self.assertIn("const title=`${part}: ${partNames[part]||reading.topic", reader)
        self.assertIn("Now, read the passage and answer the questions.", reader)
        self.assertIn("say(text,'Đang đọc văn bản tiếng Anh…')", reader)
        self.assertIn("say(`Question ${index+1}. ${question.question}`", reader)
        self.assertIn("say(`${letter}.`", reader)
        self.assertIn("waitSpeechGap(PART_OPTION_LABEL_PAUSE_MS,token)", reader)

    def test_fixed_timing_is_not_user_configurable(self):
        for control in ("ttsStartupDelay", "ttsPart1LeadInPause", "ttsPart1OptionPause"):
            self.assertNotIn(f'id="{control}"', HTML)
            self.assertNotIn(f"['{control}'", APP)
        self.assertIn("Nhấn Nghe để đưa nội dung vào bộ phát ngay", HTML)
        self.assertNotIn("Mọi lượt đọc chờ voice và chuẩn bị engine 2 giây", HTML)
        self.assertIn("nghỉ 1,5 giây rồi mới đọc mô tả", HTML)

    def test_reading_audio_toolbar_is_responsive_and_accessible(self):
        self.assertIn('aria-live="polite"', APP[APP.index("const readerToolbar="):APP.index("const content=", APP.index("const readerToolbar="))])
        self.assertIn(".reading-audio-toolbar", CSS)
        self.assertIn("@media(max-width:640px){.reading-audio-toolbar", CSS)

    def test_regression_is_executed_by_ci(self):
        self.assertIn("test_tts_readiness.py", WORKFLOW)
        self.assertIn("listening-tts-regression.mjs", WORKFLOW)


if __name__ == "__main__":
    unittest.main(verbosity=2)
