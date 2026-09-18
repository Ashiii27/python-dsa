import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_grid(self):
        g = m.make_grid(3, 3)
        g[0][0] = 1
        self.assertEqual(g, [[1, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_dedupe(self):
        self.assertEqual(m.dedupe_keep_order([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_word_count(self):
        self.assertEqual(m.word_count("a B a"), {"a": 2, "b": 1})

    def test_top_k(self):
        self.assertEqual(m.top_k_words("b a a c c", 2), [("a", 2), ("c", 2)])

    def test_group(self):
        self.assertEqual(m.group_by_length(["a", "bb", "cc", "d"]),
                         {1: ["a", "d"], 2: ["bb", "cc"]})

    def test_common(self):
        self.assertEqual(m.common_elements([3, 1, 2, 1], [1, 3, 9]), [1, 3])

    def test_invert(self):
        self.assertEqual(m.invert({"a": 1, "b": 2}), {1: "a", 2: "b"})

    def test_rotate(self):
        self.assertEqual(m.rotate([1, 2, 3, 4], 1), [4, 1, 2, 3])
        self.assertEqual(m.rotate([1, 2, 3], 5), [2, 3, 1])
        self.assertEqual(m.rotate([], 2), [])
        self.assertEqual(m.rotate([1, 2, 3], -1), [2, 3, 1])

    def test_flatten(self):
        self.assertEqual(m.flatten([1, [2, [3, [4]], 5], []]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
