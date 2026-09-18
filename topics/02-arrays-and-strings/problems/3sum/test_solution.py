import unittest

from solution import three_sum


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(three_sum([]), [])


if __name__ == "__main__":
    unittest.main()
