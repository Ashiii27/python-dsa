import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Test(unittest.TestCase):
    def test_top_k(self):
        self.assertEqual(m.top_k_largest([5, 1, 9, 3], 2), [9, 5])
        self.assertEqual(m.k_smallest_with_heap([5, 1, 9, 3], 2), [1, 3])

    def test_lower_bound(self):
        self.assertEqual(m.lower_bound([1, 3, 3, 5], 3), 1)
        self.assertEqual(m.lower_bound([1, 3], 9), 2)

    def test_prefix(self):
        self.assertEqual(m.prefix_sums([1, 2, 3]), [0, 1, 3, 6])
        self.assertEqual(m.prefix_sums([]), [0])

    def test_graph_bfs(self):
        g = m.build_graph([(1, 2), (1, 3), (2, 4)])
        self.assertEqual(sorted(g[1]), [2, 3])
        self.assertEqual(m.bfs_order(g, 1), [1, 2, 3, 4])

    def test_anagrams(self):
        self.assertEqual(m.group_anagrams(["eat", "tea", "tan", "ate"]),
                         [["eat", "tea", "ate"], ["tan"]])

    def test_climb(self):
        self.assertEqual(m.climb_stairs(1), 1)
        self.assertEqual(m.climb_stairs(2), 2)
        self.assertEqual(m.climb_stairs(5), 8)
        self.assertEqual(len(str(m.climb_stairs(500))), 105)

    def test_inorder(self):
        root = Node(2, Node(1), Node(3))
        self.assertEqual(m.iterative_inorder(root), [1, 2, 3])
        self.assertEqual(m.iterative_inorder(None), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
