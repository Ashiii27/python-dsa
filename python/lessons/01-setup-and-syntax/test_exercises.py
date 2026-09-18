import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(m.greet("Ada"), "Hello, Ada! Your name has 3 letters.")

    def test_classify(self):
        self.assertEqual([m.classify(-2), m.classify(0), m.classify(7)],
                         ["negative", "zero", "positive"])

    def test_truthy(self):
        for falsy in (0, 0.0, "", [], {}, set(), None, False):
            self.assertFalse(m.is_truthy(falsy), falsy)
        for truthy in (1, -1, "0", [0], {"a": 1}, {0}, True):
            self.assertTrue(m.is_truthy(truthy), truthy)

    def test_same_object(self):
        a = [1]
        self.assertTrue(m.same_object(a, a))
        self.assertFalse(m.same_object(a, [1]))
        self.assertTrue(m.same_object(None, None))

    def test_fizzbuzz(self):
        self.assertEqual(m.fizzbuzz(15)[-1], "FizzBuzz")
        self.assertEqual(m.fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(m.fizzbuzz(0), [])

    def test_safe_div(self):
        self.assertEqual(m.safe_div(7, 2), 3.5)
        self.assertIsNone(m.safe_div(1, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
