import unittest

from solution import spiral_order


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(spiral_order([[1,2,3],[4,5,6],[7,8,9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(spiral_order([[1,2,3]]), [1, 2, 3])
        self.assertEqual(spiral_order([]), [])


if __name__ == "__main__":
    unittest.main()
