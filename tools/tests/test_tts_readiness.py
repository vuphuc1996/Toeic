from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")


class SpeechReadinessTests(unittest.TestCase):
    def test_safe_default_delays_are_defined(self):
        self.assertRegex(APP, r"startupDelayMs:\s*750")
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
        self.assertIn("Mô tả ${String.fromCharCode(65+index)}/4", play)

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
        for control in ("ttsStartupDelay", "ttsPart1OptionPause"):
            self.assertIn(f'id="{control}"', HTML)
            self.assertIn(f"['{control}'", APP)
        self.assertIn("startupDelayMs", APP)
        self.assertIn("part1OptionPauseMs", APP)

    def test_reading_audio_toolbar_is_responsive_and_accessible(self):
        self.assertIn('aria-live="polite"', APP[APP.index("const readerToolbar="):APP.index("const content=", APP.index("const readerToolbar="))])
        self.assertIn(".reading-audio-toolbar", CSS)
        self.assertIn("@media(max-width:640px){.reading-audio-toolbar", CSS)

    def test_regression_is_executed_by_ci(self):
        self.assertIn("test_tts_readiness.py", WORKFLOW)
        self.assertIn("listening-tts-regression.mjs", WORKFLOW)


if __name__ == "__main__":
    unittest.main(verbosity=2)
