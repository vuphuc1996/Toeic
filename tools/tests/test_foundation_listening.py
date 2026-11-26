"""Quality and integration checks for the Pre-A1–A2 synthesized listening practice."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FoundationListeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/learning-path/foundation-listening.json").read_text(encoding="utf-8"))
        cls.lessons = json.loads((ROOT / "data/learning-path/pre-a1-a1.json").read_text(encoding="utf-8"))["lessons"]
        cls.app = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.sw = (ROOT / "sw.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "assets/css/design-system.css").read_text(encoding="utf-8")

    def test_all_clips_map_one_to_each_stable_lesson(self):
        self.assertEqual(len(self.data["clips"]), 36)
        self.assertEqual({x["lessonId"] for x in self.data["clips"]}, {x["id"] for x in self.lessons})
        self.assertEqual(len({x["id"] for x in self.data["clips"]}), 36)

    def test_a2_clips_map_one_to_each_a2_lesson(self):
        a2_ids={x['id'] for x in self.lessons if x['level']=='A2'}
        a2_clips={x['lessonId'] for x in self.data['clips'] if x.get('level')=='A2'}
        self.assertEqual(len(a2_clips),13)
        self.assertEqual(a2_clips,a2_ids)
        self.assertEqual(sum(x.get('level')=='A2' for x in self.data['clips']),26)
        self.assertEqual(sum(bool(x.get('supplementary')) for x in self.data['clips']),13)

    def test_scripts_and_question_banks_are_complete_and_unique(self):
        question_ids = []
        for clip in self.data["clips"]:
            with self.subTest(clip=clip["id"]):
                expected_questions = 3 if clip.get('level') == 'A2' else 2
                self.assertGreaterEqual(len(clip["script"].split()), 50 if clip.get('level') == 'A2' else 25)
                self.assertLessEqual(len(clip["script"].split()), 105)
                self.assertEqual(len(clip["questions"]), expected_questions)
                if clip.get('level') == 'A2' and not clip.get('supplementary'):
                    self.assertEqual(len(clip.get('segments', [])), 4)
                    self.assertEqual(clip.get('minimumUniqueQuestions'), 3)
                    self.assertEqual(clip.get('practiceAccuracyThreshold'), 0.67)
                    self.assertEqual('\n'.join(f"{x['speaker']}: {x['text']}" for x in clip['segments']), clip['script'])
                for question in clip["questions"]:
                    self.assertEqual(len(question["choices"]), 4)
                    self.assertEqual(len(set(question["choices"])), 4)
                    self.assertIn(question["answerIndex"], range(4))
                    self.assertTrue(question["prompt"] and question["rationale"])
                    question_ids.append(question["id"])
        self.assertEqual(len(question_ids), 98)
        self.assertEqual(len(question_ids), len(set(question_ids)))

    def test_new_a2_listening_answers_match_spoken_details(self):
        expected={
            "a2-present-perfect-experience::listening1": [
                "Updated the delivery list","The supplier confirmation"],
            "a2-basic-passive-voice::listening1": [
                "Every evening","Yesterday"],
            "a2-defining-relative-clauses::listening1": [
                "The office assistant","On the shared drive"],
        }
        for clip_id,answers in expected.items():
            clip=next(x for x in self.data["clips"] if x["id"]==clip_id)
            for question,answer in zip(clip["questions"],answers):
                self.assertEqual(question["choices"][question["answerIndex"]],answer,clip_id)
                self.assertTrue(question["rationale"])
        invitation = next(x for x in self.data["clips"] if x["lessonId"] == "a2-invitations-offers")
        self.assertIn("name cards", invitation['script'].lower())
        self.assertIn("this afternoon", invitation['script'].lower())
        self.assertIn("another lunch next week", invitation['script'].lower())

    def test_a2_original_question_pairs_match_v275_baseline(self):
        import hashlib
        baseline = json.loads((ROOT / 'tools/foundation-a2-question-baseline-v2.75.0.json').read_text(encoding='utf-8'))
        for clip in self.data['clips']:
            if clip.get('level') != 'A2' or clip.get('supplementary'):
                continue
            payload = json.dumps(clip['questions'][:2], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            self.assertEqual(hashlib.sha256(payload).hexdigest(), baseline['resources']['listening'][clip['lessonId']])

    def test_a2_dialogues_have_two_configurable_voice_genders_and_three_questions(self):
        a2 = [x for x in self.data['clips'] if x.get('level') == 'A2' and not x.get('supplementary')]
        self.assertEqual(len(a2), 13)
        extended = [x for x in self.data['clips'] if x.get('level') == 'A2' and x.get('supplementary')]
        self.assertEqual(len(extended), 13)
        self.assertTrue(all(x.get('reviewState') == 'pending-independent-review' for x in extended))
        for clip in a2:
            with self.subTest(clip=clip['id']):
                self.assertEqual(sorted(x['voice'] for x in clip['segments']), ['female','female','male','male'])
                self.assertEqual([q['id'].rsplit('::', 1)[-1] for q in clip['questions']], ['q1','q2','q3'])
                self.assertTrue(all(len(segment['text'].split()) >= 5 for segment in clip['segments']))
                self.assertTrue(clip['questions'][2]['rationale'].strip())

    def test_selected_answer_matches_the_listening_detail(self):
        clip = next(x for x in self.data["clips"] if x["lessonId"] == "a1-plurals")
        question = next(x for x in clip["questions"] if x["id"].endswith("::q2"))
        self.assertEqual(question["choices"][question["answerIndex"]], "To the storage room")

    def test_answer_key_positions_are_balanced(self):
        counts = [sum(q["answerIndex"] == i for clip in self.data["clips"] for q in clip["questions"]) for i in range(4)]
        self.assertEqual(counts, [25, 25, 24, 24])


    def test_supplementary_a2_listening_has_varied_formats_and_isolated_evidence(self):
        rows=[x for x in self.data["clips"] if x.get("supplementary")]
        self.assertEqual(len(rows),13)
        self.assertEqual(len({x["lessonId"] for x in rows}),13)
        self.assertGreaterEqual(len({x["format"] for x in rows}),10)
        self.assertTrue(all(x["id"]==f'{x["lessonId"]}::listening2' for x in rows))
        self.assertTrue(all(x.get("evidenceScope")=="listening2" for x in rows))
        self.assertTrue(all(len(x["segments"])==6 and len(x["questions"])==3 for x in rows))
        self.assertTrue(all(75 <= len(x['script'].split()) <= 100 for x in rows))
        self.assertTrue(all(sorted(s['voice'] for s in x['segments']) == ['female','female','female','male','male','male'] for x in rows))
        self.assertTrue(all([q['skill'] for q in x['questions']] == ['listen-for-detail','understand-purpose-context','infer-next-action'] for x in rows))
        self.assertIn("`${lessonId}::${scopeId}`",self.app)
        self.assertIn("data-foundation-listening-scope",self.app)

    def test_a2_practice_policy_is_stricter_without_changing_older_levels(self):
        policy = self.data["evidencePolicy"]
        self.assertEqual(policy["minimumUniqueQuestions"], 2)
        self.assertEqual(policy["practiceAccuracyThreshold"], 0.8)
        self.assertEqual(policy["a2MinimumUniqueQuestions"], 3)
        self.assertEqual(policy["a2PracticeAccuracyThreshold"], 0.67)
        self.assertIn("CEFR certification", policy["scope"])

    def test_scope_discloses_synthesized_audio_not_ets_recording(self):
        self.assertIn("browser-speech-synthesis", self.data["playback"]["engine"])
        self.assertIn("not authentic recorded audio", self.data["evidencePolicy"]["scope"])
        self.assertTrue(self.data["playback"]["scriptHiddenByDefault"])
        self.assertTrue(self.data["playback"]["usesCurrentAppVoiceSettings"])

    def test_path_cards_use_per_resource_question_count_and_practice_threshold(self):
        self.assertIn("const listeningResource=(state.foundationListeningClips||[]).find(item=>item.lessonId===lesson.id&&!item.supplementary);", self.app)
        self.assertIn("renderFoundationListeningPanel(extendedListeningClip,id,'listening2')", self.app)
        self.assertIn("scopeId?`${lessonId}::${scopeId}`:lessonId", self.app)
        self.assertIn("listeningResource?.questions?.length||2", self.app)
        self.assertIn("listeningResource?.minimumUniqueQuestions||2", self.app)
        self.assertIn("listeningResource?.practiceAccuracyThreshold||0.8", self.app)
        self.assertIn("${listening.uniqueQuestions}/${listeningTarget} câu", self.app)

    def test_runtime_keeps_listening_evidence_separate_and_integrated(self):
        self.assertIn("./data/learning-path/foundation-listening.json", self.app)
        self.assertIn("toeic:foundation-listening-progress:v1", self.app)
        self.assertIn("recordFoundationListeningAttempt", self.app)
        self.assertIn("data-foundation-listening-answer", self.app)
        self.assertIn("data-foundation-listening-play", self.app)
        self.assertIn("data-foundation-listening-transcript-toggle", self.app)
        self.assertIn("./foundation-listening-evidence.js", self.app)

    def test_service_worker_precaches_required_and_app_shell_resources(self):
        required = self.sw.split("const REQUIRED = ", 1)[1].split(";", 1)[0]
        shell = self.sw.split("const APP_SHELL = ", 1)[1].split(";", 1)[0]
        version = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))["version"]
        arrays = [json.loads(required), json.loads(shell)]
        path = "./assets/js/foundation-listening-evidence.js"
        data_path = "./data/learning-path/foundation-listening.json"
        for resources in arrays:
            self.assertIn(path, resources)
            self.assertIn(f"{path}?__release={version}", resources)
            self.assertIn(data_path, resources)


if __name__ == "__main__":
    unittest.main()
