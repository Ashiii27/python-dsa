import unittest

from solution import length_of_longest_substring


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(length_of_longest_substring('abcabcbb'), 3)
        self.assertEqual(length_of_longest_substring('bbbbb'), 1)
        self.assertEqual(length_of_longest_substring(''), 0)


if __name__ == "__main__":
    unittest.main()
