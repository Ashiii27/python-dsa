# Project 1 — Contacts CLI

Build a small address book that stores contacts in a JSON file and is driven from the terminal.

## Requirements

1. `Contact` — a dataclass with `name: str`, `email: str`, `phone: str = ""`.
   - Validate on creation: name non-empty, email contains exactly one `@`.
   - Invalid input raises `ValidationError`.
2. `ContactBook`
   - `add(contact)` — rejects duplicate names with `DuplicateContact`.
   - `remove(name)` — raises `ContactNotFound` if absent.
   - `find(query)` — case-insensitive substring match on name or email, sorted by name.
   - `save(path)` / `ContactBook.load(path)` — JSON round-trip; loading a missing file
     returns an empty book.
3. CLI via `argparse` with subcommands `add`, `remove`, `list`, `find`, storing the file
   at `--db contacts.json`. Exit code 0 on success, 1 on a handled error (print the message
   to stderr — never a traceback).

## How to work

```bash
cd projects/contacts-cli
python test_contacts.py -v   # RED (contacts.py is a stub)
# implement contacts.py until GREEN
python contacts.py add "Ada" ada@lovelace.dev --db /tmp/c.json
python contacts.py list --db /tmp/c.json
```

The tests in `test_contacts.py` are the spec. A reference implementation lives in
`solution_contacts.py` — read it only after you pass, or when you're truly stuck.
