import unittest

from solution import max_profit


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit([]), 0)


if __name__ == "__main__":
    unittest.main()
