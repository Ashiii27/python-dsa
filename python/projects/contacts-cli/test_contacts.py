"""Spec for project 1.

    python test_contacts.py -v                          # grades contacts.py
    PY_TRACK_TARGET=solution_contacts python test_contacts.py
"""
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

_target = os.environ.get("PY_TRACK_TARGET", "contacts")
_spec = importlib.util.spec_from_file_location(_target, Path(__file__).parent / f"{_target}.py")
m = importlib.util.module_from_spec(_spec)
sys.modules[_target] = m
_spec.loader.exec_module(m)


class TestContact(unittest.TestCase):
    def test_valid(self):
        c = m.Contact("Ada", "ada@x.dev")
        self.assertEqual((c.name, c.email, c.phone), ("Ada", "ada@x.dev", ""))

    def test_invalid(self):
        with self.assertRaises(m.ValidationError):
            m.Contact("  ", "a@b.c")
        with self.assertRaises(m.ValidationError):
            m.Contact("Ada", "nope")


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = m.ContactBook()
        self.book.add(m.Contact("Ada", "ada@x.dev"))
        self.book.add(m.Contact("bob", "bob@y.dev", "123"))

    def test_add_duplicate(self):
        with self.assertRaises(m.DuplicateContact):
            self.book.add(m.Contact("ADA", "other@x.dev"))

    def test_len_and_order(self):
        self.assertEqual(len(self.book), 2)
        self.assertEqual([c.name for c in self.book], ["Ada", "bob"])

    def test_remove(self):
        self.book.remove("ADA")
        self.assertEqual(len(self.book), 1)
        with self.assertRaises(m.ContactNotFound):
            self.book.remove("nobody")

    def test_find(self):
        self.assertEqual([c.name for c in self.book.find("y.dev")], ["bob"])
        self.assertEqual([c.name for c in self.book.find("a")], ["Ada"])
        self.assertEqual(self.book.find("zzz"), [])

    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "db.json"
            self.book.save(path)
            self.assertEqual(len(json.loads(path.read_text())), 2)
            loaded = m.ContactBook.load(path)
            self.assertEqual([c.name for c in loaded], ["Ada", "bob"])
            self.assertEqual(len(m.ContactBook.load(Path(tmp) / "missing.json")), 0)


class TestCLI(unittest.TestCase):
    def test_flow(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = str(Path(tmp) / "db.json")
            self.assertEqual(m.main(["--db", db, "add", "Ada", "ada@x.dev"]), 0)
            self.assertEqual(m.main(["--db", db, "add", "Ada", "ada@x.dev"]), 1)
            self.assertEqual(m.main(["--db", db, "list"]), 0)
            self.assertEqual(m.main(["--db", db, "find", "ada"]), 0)
            self.assertEqual(m.main(["--db", db, "remove", "ghost"]), 1)
            self.assertEqual(m.main(["--db", db, "remove", "Ada"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
