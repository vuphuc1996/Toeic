import os, subprocess, tempfile, unittest, zipfile
from pathlib import Path
from tools.package_source import package

class PackageSourceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.name", "Package test"], cwd=self.repo, check=True)
        (self.repo / "data").mkdir()
        (self.repo / "data" / "words.json").write_text("{}", encoding="utf8")
        (self.repo / "archive").mkdir(); (self.repo / "archive" / "old.md").write_text("archived")
        (self.repo / "release").mkdir(); (self.repo / "release" / "nested.zip").write_text("archive")
        (self.repo / "docs" / "archive").mkdir(parents=True); (self.repo / "docs" / "archive" / "history.md").write_text("history")
        (self.repo / "docs" / "changelog.md.tmp").write_text("temporary")
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.repo, check=True)
    def tearDown(self): self.tmp.cleanup()
    def test_single_root_and_tracked_only(self):
        (self.repo / "logs").mkdir(); (self.repo / "logs" / "test.log").write_text("ignored")
        out=Path(self.tmp.name)/"out.zip"; count=package(self.repo,"1.2.3",out)
        with zipfile.ZipFile(out) as z:
            names=z.namelist()
            self.assertEqual(count,2)
            self.assertTrue(all(n.startswith("Toeic_Dictionary_v1.2.3/") for n in names))
            self.assertFalse(any("/logs/" in n or n.startswith("Toeic_Dictionary_v1.2.3/archive/") or "/release/" in n or n.endswith(".log") or n.endswith(".zip") or n.endswith(".tmp") for n in names))
            self.assertIn("Toeic_Dictionary_v1.2.3/docs/archive/history.md", names)
            self.assertNotIn("Toeic_Dictionary_v1.2.3/docs/changelog.md.tmp", names)
            self.assertIn("Toeic_Dictionary_v1.2.3/data/words.json", names)
    def test_rejects_dirty_worktree(self):
        (self.repo/"data"/"words.json").write_text("dirty")
        with self.assertRaises(RuntimeError): package(self.repo,"1.2.3",Path(self.tmp.name)/"out.zip")
    def test_rejects_invalid_version(self):
        with self.assertRaises(ValueError): package(self.repo,"v1.2",Path(self.tmp.name)/"out.zip")

if __name__=="__main__": unittest.main()
