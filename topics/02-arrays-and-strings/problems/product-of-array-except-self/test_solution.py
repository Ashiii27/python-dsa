import unittest

from solution import product_except_self


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
        self.assertEqual(product_except_self([]), [])


if __name__ == "__main__":
    unittest.main()
