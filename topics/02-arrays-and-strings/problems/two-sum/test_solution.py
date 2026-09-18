import unittest

from solution import two_sum


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([1, 2], 10), [])


if __name__ == "__main__":
    unittest.main()
