import unittest

from solution import rotate


def _rotated(matrix):
    rotate(matrix)
    return matrix


class SolutionTests(unittest.TestCase):
    def test_examples_and_edges(self):
        self.assertEqual(_rotated([[1,2],[3,4]]), [[3, 1], [4, 2]])
        self.assertEqual(_rotated([]), [])


if __name__ == "__main__":
    unittest.main()
