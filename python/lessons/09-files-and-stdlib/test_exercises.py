import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_write_read(self):
        p = self.root / "nested" / "a.txt"
        self.assertEqual(m.write_lines(p, ["a", "", " ", "b"]), 4)
        self.assertEqual(m.read_nonempty_lines(p), ["a", "b"])

    def test_word_count(self):
        p = self.root / "w.txt"
        p.write_text("Hello, hello world\nworld!\n", encoding="utf-8")
        self.assertEqual(m.count_words_in_file(p), {"hello": 2, "world": 2})

    def test_json(self):
        p = self.root / "d.json"
        m.save_json(p, {"b": 1, "a": [1, 2]})
        self.assertEqual(m.load_json(p), {"b": 1, "a": [1, 2]})
        self.assertTrue(p.read_text(encoding="utf-8").startswith('{\n  "a"'))
        self.assertEqual(m.load_json(self.root / "missing.json", "fallback"), "fallback")
        (self.root / "bad.json").write_text("{nope", encoding="utf-8")
        self.assertIsNone(m.load_json(self.root / "bad.json"))

    def test_largest_files(self):
        (self.root / "small.txt").write_text("a", encoding="utf-8")
        (self.root / "big.txt").write_text("a" * 100, encoding="utf-8")
        (self.root / "mid.txt").write_text("a" * 50, encoding="utf-8")
        self.assertEqual(m.largest_files(self.root, 2), ["big.txt", "mid.txt"])

    def test_csv(self):
        p = self.root / "c.csv"
        p.write_text("name,amount\na,1.5\nb,\nc,2\n", encoding="utf-8")
        self.assertEqual(m.csv_column_sum(p, "amount"), 3.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
