"""Reference implementation of the Contacts CLI project."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence


class ValidationError(Exception):
    """Invalid contact data."""


class DuplicateContact(Exception):
    """A contact with this name already exists."""


class ContactNotFound(Exception):
    """No contact with this name."""


@dataclass
class Contact:
    name: str
    email: str
    phone: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValidationError("name must not be empty")
        if self.email.count("@") != 1:
            raise ValidationError(f"invalid email: {self.email}")


class ContactBook:
    def __init__(self, contacts: Sequence[Contact] = ()) -> None:
        self._contacts: dict[str, Contact] = {c.name.lower(): c for c in contacts}

    def __len__(self) -> int:
        return len(self._contacts)

    def __iter__(self):
        return iter(sorted(self._contacts.values(), key=lambda c: c.name.lower()))

    def add(self, contact: Contact) -> None:
        key = contact.name.lower()
        if key in self._contacts:
            raise DuplicateContact(f"{contact.name} already exists")
        self._contacts[key] = contact

    def remove(self, name: str) -> Contact:
        try:
            return self._contacts.pop(name.lower())
        except KeyError as exc:
            raise ContactNotFound(f"{name} not found") from exc

    def find(self, query: str) -> list[Contact]:
        q = query.lower()
        hits = [c for c in self._contacts.values() if q in c.name.lower() or q in c.email.lower()]
        return sorted(hits, key=lambda c: c.name.lower())

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(c) for c in self]
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "ContactBook":
        try:
            raw = json.loads(Path(path).read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return cls()
        return cls([Contact(**row) for row in raw])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="contacts", description="Tiny address book.")
    parser.add_argument("--db", default="contacts.json")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add")
    add.add_argument("name")
    add.add_argument("email")
    add.add_argument("--phone", default="")

    remove = sub.add_parser("remove")
    remove.add_argument("name")

    sub.add_parser("list")

    find = sub.add_parser("find")
    find.add_argument("query")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    book = ContactBook.load(args.db)
    try:
        if args.command == "add":
            book.add(Contact(args.name, args.email, args.phone))
            book.save(args.db)
            print(f"added {args.name}")
        elif args.command == "remove":
            book.remove(args.name)
            book.save(args.db)
            print(f"removed {args.name}")
        elif args.command == "list":
            for contact in book:
                print(f"{contact.name} <{contact.email}> {contact.phone}".rstrip())
        elif args.command == "find":
            for contact in book.find(args.query):
                print(f"{contact.name} <{contact.email}>")
    except (ValidationError, DuplicateContact, ContactNotFound) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
