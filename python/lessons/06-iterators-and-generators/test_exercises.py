import sys, types, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_countdown(self):
        self.assertEqual(list(m.countdown(3)), [3, 2, 1])
        self.assertEqual(list(m.countdown(0)), [])

    def test_take(self):
        self.assertEqual(m.take(m.evens(), 4), [0, 2, 4, 6])
        self.assertEqual(m.take([1, 2], 5), [1, 2])

    def test_evens_is_lazy(self):
        self.assertIsInstance(m.evens(), types.GeneratorType)

    def test_pairs(self):
        self.assertEqual(list(m.sliding_pairs([1, 2, 3])), [(1, 2), (2, 3)])
        self.assertEqual(list(m.sliding_pairs([1])), [])

    def test_rle(self):
        self.assertEqual(m.run_length_encode("aaabbc"), [("a", 3), ("b", 2), ("c", 1)])
        self.assertEqual(m.run_length_encode(""), [])

    def test_flatten_once(self):
        self.assertEqual(m.flatten_once([[1, 2], [3], []]), [1, 2, 3])

    def test_unique_justseen(self):
        self.assertEqual(list(m.unique_justseen([1, 1, 2, 2, 1])), [1, 2, 1])

    def test_fib_stream(self):
        self.assertEqual(m.take(m.fib_stream(), 7), [0, 1, 1, 2, 3, 5, 8])

    def test_sum_squares(self):
        self.assertEqual(m.lazy_sum_of_squares(4), 14)


if __name__ == "__main__":
    unittest.main(verbosity=2)
