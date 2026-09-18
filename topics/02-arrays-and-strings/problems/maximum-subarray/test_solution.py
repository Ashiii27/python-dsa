import unittest

from solution import max_subarray


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(max_subarray([-3]), -3)


if __name__ == "__main__":
    unittest.main()
