import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_squares(self):
        self.assertEqual(m.squares_of_evens([1, 2, 3, 4]), [4, 16])

    def test_index(self):
        self.assertEqual(m.index_of_first([1, 2, 2], 2), 1)
        self.assertEqual(m.index_of_first([], 2), -1)

    def test_transpose(self):
        self.assertEqual(m.transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(m.transpose([]), [])

    def test_flatten(self):
        self.assertEqual(m.flatten_matrix([[1, 2], [3]]), [1, 2, 3])

    def test_running_total(self):
        self.assertEqual(m.running_total([1, 2, 3]), [1, 3, 6])
        self.assertEqual(m.running_total([]), [])

    def test_chunk(self):
        self.assertEqual(m.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        with self.assertRaises(ValueError):
            m.chunk([1], 0)

    def test_first_non_repeating(self):
        self.assertEqual(m.first_non_repeating("swiss"), "w")
        self.assertIsNone(m.first_non_repeating("aabb"))

    def test_collatz(self):
        self.assertEqual(m.collatz_steps(1), 0)
        self.assertEqual(m.collatz_steps(6), 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
