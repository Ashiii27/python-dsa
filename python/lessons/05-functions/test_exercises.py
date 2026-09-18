import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_no_shared_default(self):
        self.assertEqual(m.append_to(1), [1])
        self.assertEqual(m.append_to(2), [2])
        bucket = [0]
        self.assertEqual(m.append_to(1, bucket), [0, 1])

    def test_apply_n(self):
        self.assertEqual(m.apply_n(lambda x: x * 2, 3, 1), 8)
        self.assertEqual(m.apply_n(lambda x: x * 2, 0, 5), 5)

    def test_counter(self):
        c = m.make_counter()
        self.assertEqual([c(), c(), c()], [1, 2, 3])
        self.assertEqual(m.make_counter(10)(), 11)

    def test_multipliers(self):
        fs = m.make_multipliers(3)
        self.assertEqual([f(10) for f in fs], [0, 10, 20])

    def test_counted(self):
        @m.counted
        def hello(x):
            """doc"""
            return x

        hello(1); hello(2)
        self.assertEqual(hello.calls, 2)
        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "doc")

    def test_fib(self):
        self.assertEqual(m.memoized_fib(10), 55)
        self.assertEqual(len(str(m.memoized_fib(200))), 42)

    def test_summarize(self):
        self.assertEqual(m.summarize(1, 2), "sum=3")
        self.assertEqual(m.summarize(1.005, 2, precision=1, label="total"), "total=3.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
