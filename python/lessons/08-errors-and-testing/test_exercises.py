import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(m.parse_int("42"), 42)
        self.assertEqual(m.parse_int("x", 0), 0)
        with self.assertRaises(ValueError) as ctx:
            m.parse_int("x")
        self.assertEqual(str(ctx.exception), "invalid int: x")
        self.assertIsNotNone(ctx.exception.__cause__)

    def test_validate_age(self):
        self.assertEqual(m.validate_age(30), 30)
        with self.assertRaises(m.OutOfRange) as ctx:
            m.validate_age(-1)
        self.assertEqual(ctx.exception.value, -1)
        self.assertIsInstance(ctx.exception, m.ValidationError)

    def test_safe_get(self):
        data = {"a": {"b": {"c": 1}}}
        self.assertEqual(m.safe_get(data, "a", "b", "c"), 1)
        self.assertIsNone(m.safe_get(data, "a", "z"))
        self.assertIsNone(m.safe_get(data, "a", "b", "c", "d"))

    def test_divide_all(self):
        self.assertEqual(m.divide_all([1, 2], 2), [0.5, 1.0])
        self.assertEqual(m.divide_all([1], 0), [None])

    def test_collecting(self):
        with m.collecting() as bucket:
            bucket.extend([1, 2])
        self.assertEqual(bucket, [2, 4])

        with self.assertRaises(RuntimeError):
            with m.collecting() as bucket2:
                bucket2.append(3)
                raise RuntimeError
        self.assertEqual(bucket2, [6])

    def test_retry(self):
        state = {"n": 0}

        def flaky():
            state["n"] += 1
            if state["n"] < 3:
                raise RuntimeError("nope")
            return "ok"

        self.assertEqual(m.retry(5, flaky), "ok")
        self.assertEqual(state["n"], 3)
        with self.assertRaises(RuntimeError):
            m.retry(2, lambda: (_ for _ in ()).throw(RuntimeError("always")))
        with self.assertRaises(ValueError):
            m.retry(0, lambda: 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
