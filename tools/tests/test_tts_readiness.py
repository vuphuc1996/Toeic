from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
LISTENING = __import__("json").loads((ROOT / "data/listening/listening-library.json").read_text(encoding="utf-8"))["listening"]


class SpeechReadinessTests(unittest.TestCase):
    def test_safe_default_delays_are_defined(self):
        self.assertRegex(APP, r"startupDelayMs:\s*750")
        self.assertRegex(APP, r"part1LeadInPauseMs:\s*1000")
        self.assertRegex(APP, r"part1OptionPauseMs:\s*1300")

    def test_voice_selector_refresh_helper_is_defined_and_used(self):
        self.assertRegex(APP, r"function\s+refreshSpeechVoiceSelectors\s*\(")
        helper = APP[APP.index("function refreshSpeechVoiceSelectors("):APP.index("function chooseEnglishVoice(")]
        self.assertIn("getSpeechVoices()", helper)
        self.assertIn("gender==='male'?'Male':'Female'", helper)
        self.assertIn("ttsVoiceStatus", helper)
        self.assertIn("select.disabled=!voices.length", helper)
        self.assertIn("refreshSpeechVoiceSelectors", APP[APP.index("function bindTtsSettings("):APP.index("async function answerListeningQuestion(")])

    def test_voice_catalogue_is_checked_before_engine_buffer(self):
        prepare = APP[APP.index("async function prepareSpeechEngine("):APP.index("async function speakText(")]
        self.assertIn("await waitForSpeechVoiceCatalog(token,1200)", prepare)
        self.assertIn("return waitSpeechGap(readinessDelay,token)", prepare)
        self.assertIn("synth.cancel()", prepare)

    def test_all_single_utterance_routes_use_shared_preparation(self):
        speak = APP[APP.index("async function speakText("):APP.index("function speakUtterance(")]
        self.assertIn("await prepareSpeechEngine(token,cfg.startupDelayMs)", speak)
        self.assertIn("await speakUtterance(clean", speak)
        self.assertEqual(len(re.findall(r"speechSynthesis\.speak\(", APP)), 1)

    def test_listening_prepares_before_first_segment(self):
        play = APP[APP.index("async function playListeningAudio("):APP.index("async function playListeningVocabulary(")]
        self.assertLess(play.index("await prepareSpeechEngine(playbackToken,cfg.startupDelayMs)"), play.index("for(let index=0;index<segments.length;index++)"))
        self.assertIn("Math.max(1000,Number(cfg.part1OptionPauseMs)||1300)", play)
        self.assertIn("PART1_LEAD_IN_TEXT", play)
        self.assertIn("Lựa chọn ${letter}/4", play)
        self.assertIn("const speechText=isPart1?`${letter}. ${optionText}`:segment.text", play)
        self.assertIn("part1LeadInPauseMs", play)

    def test_every_part1_unit_has_four_clean_description_segments(self):
        part1 = [item for item in LISTENING if item.get("part") == "Part 1"]
        self.assertTrue(part1, "Listening library must include Part 1 units")
        for item in part1:
            self.assertEqual(len(item.get("segments", [])), 4, item.get("id"))
            for segment in item["segments"]:
                self.assertIsInstance(segment.get("text"), str)
                self.assertTrue(segment["text"].strip())

    def test_practice_and_mock_part1_use_the_same_audio_pipeline(self):
        self.assertIn("playListeningAudio(play.dataset.listeningPlay)", APP)
        self.assertIn("playListeningAudio(audio.dataset.mockAudio", APP)
        mock_markup = APP[APP.index("function mockGroupMarkup("):APP.index("function renderMockExam(")]
        self.assertIn("Câu dẫn → A → B → C → D", mock_markup)
        self.assertIn("có khoảng ngừng riêng", mock_markup)

    def test_part1_transcript_exposes_lead_in_and_letter_labels(self):
        detail = APP[APP.index("function openListeningDetail("):APP.index("let listeningPlaybackToken=0;")]
        self.assertIn("transcript-lead-in", detail)
        self.assertIn("OPTION ${letter}", detail)
        self.assertIn("${letter}. ", detail)
        self.assertIn("Now, listen to the four statements.", APP)

    def test_vocabulary_playback_prepares_before_reading(self):
        play = APP[APP.index("async function playListeningVocabulary("):APP.index("function saveTtsSetting(")]
        self.assertIn("await prepareSpeechEngine(token,cfg.startupDelayMs)", play)
        self.assertLess(play.index("await prepareSpeechEngine"), play.index("for(let i=0;i<words.length;i++)"))

    def test_reading_passages_use_the_same_tts_pipeline(self):
        self.assertIn('data-reading-speak="${escapeHtml(id)}"', APP)
        reader = APP[APP.index("function playReadingText(id){"):APP.index("async function answerReadingQuestion(")]
        self.assertIn("speakText(text", reader)
        self.assertIn("onStart:", reader)
        self.assertIn("onEnd:", reader)

    def test_tts_configuration_controls_are_persisted(self):
        for control in ("ttsStartupDelay", "ttsPart1LeadInPause", "ttsPart1OptionPause"):
            self.assertIn(f'id="{control}"', HTML)
            self.assertIn(f"['{control}'", APP)
        self.assertIn("startupDelayMs", APP)
        self.assertIn("part1LeadInPauseMs", APP)
        self.assertIn("part1OptionPauseMs", APP)
        self.assertIn("ttsPart1LeadInPause:String(tts.part1LeadInPauseMs)", APP)

    def test_reading_audio_toolbar_is_responsive_and_accessible(self):
        self.assertIn('aria-live="polite"', APP[APP.index("const readerToolbar="):APP.index("const content=", APP.index("const readerToolbar="))])
        self.assertIn(".reading-audio-toolbar", CSS)
        self.assertIn("@media(max-width:640px){.reading-audio-toolbar", CSS)

    def test_regression_is_executed_by_ci(self):
        self.assertIn("test_tts_readiness.py", WORKFLOW)
        self.assertIn("listening-tts-regression.mjs", WORKFLOW)


if __name__ == "__main__":
    unittest.main(verbosity=2)
