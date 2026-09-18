import unittest

from solution import min_window


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(min_window('ADOBECODEBANC', 'ABC'), 'BANC')
        self.assertEqual(min_window('a', 'aa'), '')
        self.assertEqual(min_window('abc', ''), '')


if __name__ == "__main__":
    unittest.main()
