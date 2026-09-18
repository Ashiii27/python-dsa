import dataclasses, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _loader import load  # noqa: E402

m = load(__file__)


class Test(unittest.TestCase):
    def test_point(self):
        self.assertTrue(dataclasses.is_dataclass(m.Point))
        p, q = m.Point(0, 0), m.Point(3, 4)
        self.assertEqual(p.distance_to(q), 5.0)
        self.assertEqual(m.Point(1, 2), m.Point(1, 2))
        self.assertEqual(len({m.Point(1, 2), m.Point(1, 2)}), 1)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            p.x = 5

    def test_student(self):
        s = m.Student("ann")
        self.assertEqual(s.grades, [])
        self.assertEqual(m.Student("bob").grades, [])
        self.assertEqual(s.average, 0.0)
        s.add(90); s.add(80)
        self.assertEqual(s.average, 85)
        with self.assertRaises(ValueError):
            s.add(101)

    def test_first_or_none(self):
        self.assertEqual(m.first_or_none(x for x in [7, 8]), 7)
        self.assertIsNone(m.first_or_none([]))

    def test_group(self):
        a = m.Student("a", [95.0])
        b = m.Student("b", [85.0])
        c = m.Student("c", [40.0])
        self.assertEqual(m.group_students([a, b, c]),
                         {"A": ["a"], "B": ["b"], "F": ["c"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
