import unittest

from solution import subarray_sum


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum([1, -1, 0], 0), 3)
        self.assertEqual(subarray_sum([], 0), 0)


if __name__ == "__main__":
    unittest.main()
