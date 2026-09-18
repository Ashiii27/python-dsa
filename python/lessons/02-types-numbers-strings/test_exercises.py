import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_digits_sum(self):
        self.assertEqual(m.digits_sum(-123), 6)
        self.assertEqual(m.digits_sum(0), 0)

    def test_floor_div_mod(self):
        self.assertEqual(m.floor_div_mod(-7, 2), (-4, 1))
        self.assertEqual(m.floor_div_mod(7, 3), (2, 1))

    def test_almost_equal(self):
        self.assertTrue(m.almost_equal(0.1 + 0.2, 0.3))
        self.assertFalse(m.almost_equal(1.0, 1.001))

    def test_build_sentence(self):
        self.assertEqual(m.build_sentence(["hi", "there"]), "hi there.")
        self.assertEqual(m.build_sentence([]), "")

    def test_normalize(self):
        self.assertEqual(m.normalize("  Hello\t\n  WORLD "), "hello world")

    def test_palindrome(self):
        self.assertTrue(m.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(m.is_palindrome(""))
        self.assertFalse(m.is_palindrome("race a car"))

    def test_initials(self):
        self.assertEqual(m.title_initials("ada  lovelace king"), "A.L.K.")

    def test_to_base(self):
        self.assertEqual(m.to_base(255, 16), "ff")
        self.assertEqual(m.to_base(10, 2), "1010")
        self.assertEqual(m.to_base(0, 7), "0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
