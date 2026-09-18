import heapq, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class TestVector(unittest.TestCase):
    def test_ops(self):
        a, b = m.Vector(1, 2), m.Vector(3, 4)
        self.assertEqual(a + b, m.Vector(4, 6))
        self.assertEqual(b - a, m.Vector(2, 2))
        self.assertEqual(a * 2, m.Vector(2, 4))
        self.assertEqual(abs(m.Vector(3, 4)), 5.0)
        self.assertEqual(repr(a), "Vector(1, 2)")
        self.assertEqual(len({m.Vector(1, 2), m.Vector(1, 2)}), 1)


class TestStack(unittest.TestCase):
    def test_stack(self):
        s = m.Stack()
        self.assertFalse(s)
        s.push(1); s.push(2)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertIn(1, s)
        s.pop()
        with self.assertRaises(IndexError):
            s.pop()


class TestTemperature(unittest.TestCase):
    def test_property(self):
        t = m.Temperature(100)
        self.assertEqual(t.fahrenheit, 212)
        t.fahrenheit = 32
        self.assertEqual(t.celsius, 0)
        self.assertEqual(m.Temperature.from_fahrenheit(212).celsius, 100)
        with self.assertRaises(ValueError):
            m.Temperature(-300)


class TestTask(unittest.TestCase):
    def test_ordering(self):
        heap = []
        for t in (m.Task("c", 3), m.Task("a", 1), m.Task("b", 2)):
            heapq.heappush(heap, t)
        self.assertEqual([heapq.heappop(heap).name for _ in range(3)], ["a", "b", "c"])
        self.assertEqual(repr(m.Task("a", 1)), "Task('a', 1)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
