import contextlib, io, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_frequencies(self):
        self.assertEqual(m.word_frequencies("Hi, hi there!"), {"hi": 2, "there": 1})

    def test_report(self):
        self.assertEqual(m.format_report({"a": 2, "b": 2, "c": 5}, 2), "c: 5\na: 2")
        self.assertEqual(m.format_report({}, 3), "")

    def test_parser(self):
        args = m.build_parser().parse_args(["hello world", "-n", "1"])
        self.assertEqual(args.top, 1)
        self.assertEqual(args.text, "hello world")
        self.assertEqual(m.build_parser().parse_args(["x"]).top, 3)

    def test_version_flag(self):
        buf = io.StringIO()
        with self.assertRaises(SystemExit), contextlib.redirect_stdout(buf):
            m.build_parser().parse_args(["--version"])
        self.assertIn(m.VERSION, buf.getvalue())

    def test_main(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = m.main(["a a b", "-n", "1"])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "a: 2")


if __name__ == "__main__":
    unittest.main(verbosity=2)
