import unittest

from solution import max_area


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(max_area([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(max_area([1, 1]), 1)
        self.assertEqual(max_area([]), 0)


if __name__ == "__main__":
    unittest.main()
