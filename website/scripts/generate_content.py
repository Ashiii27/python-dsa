#!/usr/bin/env python3
"""Generate the website content from the repository's markdown and Python sources.

The repository files are the single source of truth. This script turns them into
Docusaurus pages under website/docs-*/ (gitignored, rebuilt on every build):

  python/lessons/NN-name/  ->  docs-python/NN-name.mdx   (notes + exercises + tests runner)
  topics/NN-name/          ->  docs-dsa/NN-name/...      (overview, study guide, problems)
  docs/*.md                ->  docs-guides/*.md
  practice/*.md            ->  docs-practice/*.md

Usage:  python3 scripts/generate_content.py
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEB = REPO / "website"
BASE_URL = os.environ.get("SITE_BASE_URL", "/")
if not BASE_URL.startswith("/"):
    BASE_URL = "/" + BASE_URL
if not BASE_URL.endswith("/"):
    BASE_URL += "/"

GITHUB_BLOB = "https://github.com/Ashiii27/python-dsa/blob/main"

OUT_DIRS = {
    "python": WEB / "docs-python",
    "dsa": WEB / "docs-dsa",
    "guides": WEB / "docs-guides",
    "practice": WEB / "docs-practice",
}

# source repo path (posix) -> site route (without base URL)
ROUTES: dict[str, str] = {}
# source repo path -> out file
OUT_FILES: dict[str, Path] = {}

# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
MD_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_TAG_RE = re.compile(r"<(/?[A-Za-z][A-Za-z0-9-]*)")

KNOWN_HTML = {
    "details", "summary", "code", "kbd", "br", "hr", "strong", "em", "sup",
    "sub", "img", "a", "div", "span", "p", "b", "i", "ul", "ol", "li",
    "table", "thead", "tbody", "tr", "td", "th", "pre", "blockquote",
    "abbr", "del", "ins", "h1", "h2", "h3", "h4", "h5", "h6", "caption",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return path.resolve().relative_to(REPO).as_posix()


def split_front_h1(text: str) -> tuple[str, str]:
    """Return (title, body) stripping a single leading '# Title' line."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip():
            if line.startswith("# "):
                title = line[2:].strip()
                body = "\n".join(lines[i + 1:]).lstrip("\n")
                return title, body
            break
    return "", text


def yaml_str(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def gh(path: str) -> str:
    return f"{GITHUB_BLOB}/{path}"


def strip_slash_ext(route: str) -> str:
    return route


# ---------------------------------------------------------------------------
# markdown link rewriting
# ---------------------------------------------------------------------------

def rewrite_links(md_text: str, src_rel: str, self_route: str,
                  anchor_map: dict[str, str] | None = None) -> str:
    """Rewrite markdown links from repo-relative paths to site routes / GitHub."""
    anchor_map = anchor_map or {}
    src_dir = (REPO / src_rel).parent

    def sub(m: re.Match) -> str:
        bang, text, target = m.group(1), m.group(2), m.group(3)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        path_part, _, anchor = target.partition("#")
        anchor_suffix = f"#{anchor}" if anchor else ""
        resolved = (src_dir / path_part).resolve()
        try:
            key = resolved.relative_to(REPO).as_posix()
        except ValueError:
            return m.group(0)
        # direct file map
        if key in anchor_map:
            mapped = anchor_map[key]
            if mapped.startswith("#"):
                return f"[{text}]({mapped})"
            return f"[{text}]({mapped}{anchor_suffix})"
        if key in ROUTES:
            route = BASE_URL + ROUTES[key].lstrip("/")
            return f"[{text}]({route}{anchor_suffix})"
        # directory -> its README/index page
        if resolved.is_dir():
            for candidate in (f"{key}/README.md", f"{key}/index.md"):
                if candidate in ROUTES:
                    route = BASE_URL + ROUTES[candidate].lstrip("/")
                    return f"[{text}]({route}{anchor_suffix})"
        if bang:
            return f"![{text}]({gh(key)})"
        return f"[{text}]({gh(key)}{anchor_suffix})"

    return MD_LINK_RE.sub(sub, md_text)


# ---------------------------------------------------------------------------
# MDX escaping (only used for .mdx output)
# ---------------------------------------------------------------------------

def escape_mdx(text: str) -> str:
    """Escape MDX-sensitive characters outside code spans and fenced blocks."""
    out_lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        parts = INLINE_CODE_RE.split(line)
        rebuilt: list[str] = []
        for i, part in enumerate(parts):
            if i % 2 == 1:  # inline code span
                rebuilt.append(part)
                continue
            seg = part.replace("{", "&#123;").replace("}", "&#125;")

            def lt(m: re.Match) -> str:
                # keep known HTML tags, escape everything else (`<=`, `<int>`, …)
                after = seg[m.start() + 1:]
                tag_m = re.match(r"(/?)([A-Za-z][A-Za-z0-9-]*)", after)
                if tag_m and tag_m.group(2).lower() in KNOWN_HTML:
                    return m.group(0)
                return "&lt;"

            rebuilt.append(re.sub(r"<", lt, seg))
        out_lines.append("".join(rebuilt))
    return "\n".join(out_lines)


# ---------------------------------------------------------------------------
# page writing
# ---------------------------------------------------------------------------

def write_page(out: Path, title: str, body: str, *, position: int | None = None,
               sidebar_label: str | None = None, description: str | None = None,
               slug: str | None = None, mdx: bool = True,
               extra_fm: dict[str, str] | None = None) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    fm = [f"title: {yaml_str(title)}"]
    if position is not None:
        fm.append(f"sidebar_position: {position}")
    if sidebar_label:
        fm.append(f"sidebar_label: {yaml_str(sidebar_label)}")
    if description:
        fm.append(f"description: {yaml_str(description)}")
    if slug:
        fm.append(f"slug: {slug}")
    for k, v in (extra_fm or {}).items():
        fm.append(f"{k}: {v}")
    content = "---\n" + "\n".join(fm) + "\n---\n\n" + body.strip() + "\n"
    out.write_text(content, encoding="utf-8")


def code_fence(code: str, lang: str = "python") -> str:
    return f"```{lang}\n{code.rstrip()}\n```"


def js_str(s: str) -> str:
    """Encode a Python string as a JS string literal (via JSON)."""
    return json.dumps(s)


def pyrunner_jsx(title: str, module: str, code: str, tests: str,
                 extra_files: dict[str, str] | None = None) -> str:
    """Emit a <PyRunner ... /> JSX component with brace-wrapped JS props."""
    props = [
        "  title=" + "{" + js_str(title) + "}",
        "  module=" + "{" + js_str(module) + "}",
        "  code=" + "{" + js_str(code) + "}",
        "  tests=" + "{" + js_str(tests) + "}",
    ]
    if extra_files:
        props.append("  extraFiles=" + "{" + json.dumps(extra_files, ensure_ascii=False) + "}")
    return "<PyRunner\n" + "\n".join(props) + "\n/>\n"


# ---------------------------------------------------------------------------
# registrations (routes) — everything must be known before rewriting links
# ---------------------------------------------------------------------------

def register_all() -> None:
    ROUTES["README.md"] = "/"
    ROUTES["CONTRIBUTING.md"] = "/guides/contributing"

    for p in sorted((REPO / "python" / "lessons").iterdir()):
        if p.is_dir():
            key = rel(p / "notes.md")
            ROUTES[key] = f"/python/{p.name}"
            for stub in ("exercises.py", "solutions.py", "test_exercises.py"):
                ROUTES[rel(p / stub)] = f"/python/{p.name}#practice-exercises"
    ROUTES["python/README.md"] = "/python"
    ROUTES["python/projects/README.md"] = "/python/projects"
    for p in sorted((REPO / "python" / "projects").iterdir()):
        if p.is_dir() and (p / "README.md").exists():
            key = rel(p / "README.md")
            ROUTES[key] = f"/python/projects/{p.name}"

    for p in sorted((REPO / "topics").iterdir()):
        if not p.is_dir():
            continue
        ROUTES[rel(p / "README.md")] = f"/dsa/{p.name}"
        if (p / "study-guide.md").exists():
            ROUTES[rel(p / "study-guide.md")] = f"/dsa/{p.name}/study-guide"
        problems = p / "problems"
        if problems.is_dir():
            if (problems / "README.md").exists():
                ROUTES[rel(problems / "README.md")] = f"/dsa/{p.name}/problems"
            for prob in sorted(problems.iterdir()):
                if prob.is_dir() and (prob / "README.md").exists():
                    ROUTES[rel(prob / "README.md")] = f"/dsa/{p.name}/{prob.name}"
    ROUTES["docs/learning-path.md"] = "/guides/learning-path"

    for p in sorted((REPO / "docs").iterdir()):
        if p.suffix == ".md":
            ROUTES[rel(p)] = f"/guides/{p.stem}"
    for p in sorted((REPO / "practice").iterdir()):
        if p.suffix == ".md":
            ROUTES[rel(p)] = f"/practice/{p.stem}"
    ROUTES["templates/problem-template.md"] = "/guides/templates#problem-write-up-template"
    ROUTES["templates/python_dsa_templates.py"] = "/guides/templates#python-dsa-templates"


# ---------------------------------------------------------------------------
# generators per section
# ---------------------------------------------------------------------------

def gen_python_track() -> list[dict]:
    """Build docs-python/. Returns lesson metadata for the landing page."""
    lessons = []
    lessons_dir = REPO / "python" / "lessons"
    for lp in sorted(lessons_dir.iterdir()):
        if not lp.is_dir():
            continue
        num = int(lp.name[:2])
        notes = read(lp / "notes.md")
        title, body = split_front_h1(notes)
        body = rewrite_links(body, rel(lp / "notes.md"), f"/python/{lp.name}")
        exercises = read(lp / "exercises.py")
        solutions = read(lp / "solutions.py")
        tests = read(lp / "test_exercises.py")
        loader = read(REPO / "python" / "_loader.py")

        body = escape_mdx(body)
        body += "\n\n---\n\n## Practice exercises\n\n"
        body += (
            "Fill in the stubs below (or edit `exercises.py` locally), then run the "
            "test suite — right here in your browser, no install needed.\n\n"
        )
        body += pyrunner_jsx(
            f"{title} — exercises", "exercises", exercises, tests,
            extra_files={"_loader.py": loader},
        ) + "\n"
        body += ":::details Reference solution\n"
        body += code_fence(solutions) + "\n"
        body += ":::\n\n"
        body += ":::tip Run it locally\n"
        body += f"```bash\ncd python/lessons/{lp.name}\npython test_exercises.py\n```\n"
        body += ":::\n"

        short = re.sub(r"^Lesson \d+\s*[—–-]\s*", "", title)
        out = OUT_DIRS["python"] / f"{lp.name}.mdx"
        write_page(out, title, body, position=num,
                   sidebar_label=f"{lp.name[:2]} · {short}",
                   description=short, slug=f"/{lp.name}")
        OUT_FILES[rel(lp / "notes.md")] = out
        lessons.append({"id": lp.name, "title": title,
                        "href": f"/python/{lp.name}", "num": num})

    # ---- track landing (composed from python/README.md)
    readme = read(REPO / "python" / "README.md")
    title, body = split_front_h1(readme)
    body = rewrite_links(body, "python/README.md", "/python")
    body = escape_mdx(body)
    body += "\n\n---\n\n## Your progress\n\n" + track_progress_jsx("python", lessons)
    out = OUT_DIRS["python"] / "index.mdx"
    write_page(out, title or "Learn Python", body, position=0,
               sidebar_label="Track overview", slug="/")
    OUT_FILES["python/README.md"] = out

    # ---- projects
    proj_readme = REPO / "python" / "projects" / "README.md"
    if proj_readme.exists():
        title, body = split_front_h1(read(proj_readme))
        body = rewrite_links(body, rel(proj_readme), "/python/projects")
        body = escape_mdx(body)
        out = OUT_DIRS["python"] / "projects" / "index.mdx"
        write_page(out, title or "Capstone Projects", body, position=20,
                   sidebar_label="Capstone projects", slug="/projects")
        OUT_FILES[rel(proj_readme)] = out

    for proj in sorted((REPO / "python" / "projects").iterdir()):
        if not proj.is_dir() or not (proj / "README.md").exists():
            continue
        preadme = proj / "README.md"
        title, body = split_front_h1(read(preadme))
        body = rewrite_links(body, rel(preadme), f"/python/projects/{proj.name}")
        body = escape_mdx(body)
        stub = proj / "contacts.py"
        tests = proj / "test_contacts.py"
        extra = ""
        for other in sorted(proj.glob("*.py")):
            if other.name not in ("contacts.py", "test_contacts.py"):
                extra += f"\n\n:::details Reference: `{other.name}`\n" + code_fence(read(other)) + ":::\n"
        if stub.exists() and tests.exists():
            body += "\n\n---\n\n## Build it in your browser\n\n"
            body += pyrunner_jsx(title, stub.stem, read(stub), read(tests)) + "\n"
        body += extra
        out = OUT_DIRS["python"] / "projects" / f"{proj.name}.mdx"
        write_page(out, title, body, position=21, slug=f"/projects/{proj.name}")
        OUT_FILES[rel(preadme)] = out

    return lessons


def track_progress_jsx(track: str, items: list[dict]) -> str:
    payload = json.dumps(
        [{"id": i["id"], "title": i["title"], "href": BASE_URL + i["href"].lstrip("/")}
         for i in items],
        ensure_ascii=False, indent=2)
    payload = "\n".join("  " + line for line in payload.splitlines())
    return f'<TrackProgress track="{track}" items={{[\n{payload}\n]}} />\n'


def gen_dsa_track() -> list[dict]:
    topics_meta: list[dict] = []
    for tp in sorted((REPO / "topics").iterdir()):
        if not tp.is_dir():
            continue
        num = int(tp.name[:2])
        t_readme = tp / "README.md"
        title, body = split_front_h1(read(t_readme))
        body = rewrite_links(body, rel(t_readme), f"/dsa/{tp.name}")
        body = escape_mdx(body)
        out = OUT_DIRS["dsa"] / tp.name / "index.mdx"
        write_page(out, title, body, position=num,
                   sidebar_label=f"{tp.name[:2]} · {title}",
                   slug=f"/{tp.name}")
        OUT_FILES[rel(t_readme)] = out

        cat = {"label": f"{tp.name[:2]} · {title}", "position": num}
        (OUT_DIRS["dsa"] / tp.name / "_category_.json").write_text(
            json.dumps(cat, indent=2), encoding="utf-8")

        topics_meta.append({"id": tp.name, "title": title,
                            "href": f"/dsa/{tp.name}", "num": num})

        # ---- study guide (pure markdown copy, CommonMark)
        sg = tp / "study-guide.md"
        if sg.exists():
            title2, body2 = split_front_h1(read(sg))
            body2 = rewrite_links(body2, rel(sg), f"/dsa/{tp.name}/study-guide")
            out2 = OUT_DIRS["dsa"] / tp.name / "study-guide.md"
            write_page(out2, title2 or f"{title} — Study Guide", body2,
                       position=2, sidebar_label="Study guide",
                       slug=f"/{tp.name}/study-guide", mdx=False)
            OUT_FILES[rel(sg)] = out2

        problems = tp / "problems"
        if not problems.is_dir():
            continue

        # problem order from the problems README table when possible
        order: list[str] = []
        p_readme = problems / "README.md"
        if p_readme.exists():
            for m in re.finditer(r"\(\./([a-z0-9-]+)/README\.md\)", read(p_readme)):
                if m.group(1) not in order:
                    order.append(m.group(1))
        prob_dirs = [d for d in sorted(problems.iterdir())
                     if d.is_dir() and (d / "README.md").exists()]
        ordered = [d for d in prob_dirs if d.name in order]
        ordered += [d for d in prob_dirs if d.name not in order]

        if p_readme.exists():
            title3, body3 = split_front_h1(read(p_readme))
            body3 = rewrite_links(body3, rel(p_readme), f"/dsa/{tp.name}/problems")
            body3 = escape_mdx(body3)
            out3 = OUT_DIRS["dsa"] / tp.name / "problems.mdx"
            write_page(out3, title3 or f"{title} — Problems", body3,
                       position=3, sidebar_label="Problem ladder",
                       slug=f"/{tp.name}/problems")
            OUT_FILES[rel(p_readme)] = out3

        for i, prob in enumerate(ordered):
            preadme = prob / "README.md"
            title4, body4 = split_front_h1(read(preadme))
            sol = prob / "solution.py"
            tests = prob / "test_solution.py"
            body4 = rewrite_links(
                body4, rel(preadme), f"/dsa/{tp.name}/{prob.name}",
                anchor_map={
                    rel(sol): "#python-solution" if sol.exists() else "",
                    rel(tests): "#test-suite" if tests.exists() else "",
                })
            body4 = escape_mdx(body4)
            if tests.exists():
                body4 += "\n\n---\n\n## Test suite\n\n"
                body4 += "Run the tests below in your browser, or edit the solution and re-run.\n\n"
                if sol.exists():
                    body4 += pyrunner_jsx(title4, "solution", read(sol), read(tests)) + "\n"
                body4 += ":::details View the raw test file\n"
                body4 += code_fence(read(tests)) + "\n:::\n"
            out4 = OUT_DIRS["dsa"] / tp.name / f"{prob.name}.mdx"
            write_page(out4, title4, body4, position=10 + i,
                       sidebar_label=title4,
                       slug=f"/{tp.name}/{prob.name}")
            OUT_FILES[rel(preadme)] = out4

    # ---- DSA landing page
    phases = [
        ("0. Setup & foundations", topics_meta[0:2], "Write clean Python for problem solving, then predict time and space from constraints."),
        ("1. Linear structures", topics_meta[2:6], "The highest-frequency interview patterns: two pointers, windows, stacks, hashing."),
        ("2. Recursion & search", topics_meta[6:9], "Recursive thinking, backtracking, sorting, and binary search on indices and answers."),
        ("3. Trees & heaps", topics_meta[9:12], "Hierarchical data, BST invariants, and streaming top-k with heaps."),
        ("4. Graphs & DP", topics_meta[12:15], "The core hard-interview territory: traversal, shortest paths, and DP states."),
        ("5. Advanced DSA", topics_meta[15:24], "Reach top-tier company hard-question readiness."),
    ]
    body = (
        "This track takes you from Python foundations to top-tier interview level. "
        "Every topic has a **study guide** (concepts, pattern signals, worked example, drills), "
        "a **problem ladder**, and worked write-ups with proofs, complexity, and tests.\n\n"
        "> New to Python? Do the "
        f"[Python Track]({BASE_URL}python/) first — it hands you straight into this curriculum.\n\n"
        "## Curriculum\n\n"
    )
    for label, items, outcome in phases:
        body += f"### {label}\n\n*{outcome}*\n\n"
        for it in items:
            body += f"- [{it['title']}]({BASE_URL}{it['href'].lstrip('/')})\n"
        body += "\n"
    body += "---\n\n## How to study each topic\n\n"
    body += (
        "1. **Understand** — read the topic overview and study guide, trace examples by hand.\n"
        "2. **Implement** — code the core templates without looking.\n"
        "3. **Drill** — solve the problem ladder; write brute force → optimized → complexity → edge cases.\n"
        "4. **Review** — use the [revision flashcards]({bf}/guides/revision-flashcards) and "
        "[patterns cheatsheet]({bf}/guides/patterns-cheatsheet).\n\n"
        "---\n\n## Your progress\n\n"
    ).format(bf=BASE_URL.rstrip("/"))
    body += track_progress_jsx("dsa", topics_meta)
    out = OUT_DIRS["dsa"] / "index.mdx"
    write_page(out, "DSA with Python", body, position=0,
               sidebar_label="Track overview", slug="/")
    OUT_FILES["docs/learning-path.md"] = OUT_FILES.get("docs/learning-path.md", out)
    return topics_meta


GUIDE_ORDER = [
    "learning-path", "problem-solving-framework", "patterns-cheatsheet",
    "complexity-and-python", "interview-playbook", "visual-guides",
    "revision-checklists", "revision-flashcards", "resources",
]


def gen_guides() -> None:
    pos = 1
    for stem in GUIDE_ORDER:
        src = REPO / "docs" / f"{stem}.md"
        if not src.exists():
            continue
        title, body = split_front_h1(read(src))
        body = rewrite_links(body, rel(src), f"/guides/{stem}")
        out = OUT_DIRS["guides"] / f"{stem}.md"
        write_page(out, title, body, position=pos, slug=f"/{stem}", mdx=False)
        OUT_FILES[rel(src)] = out
        pos += 1

    # templates page (composed)
    t1 = REPO / "templates" / "problem-template.md"
    t2 = REPO / "templates" / "python_dsa_templates.py"
    title, body = split_front_h1(read(t1))
    body = rewrite_links(body, rel(t1), "/guides/templates")
    body = (
        f"# Templates\n\nCopy-paste skeletons for your own practice.\n\n"
        f"## Problem write-up template\n\n{body.strip()}\n\n"
        f"---\n\n## Python DSA templates\n\n"
        f"Reusable reference implementations for every core structure and algorithm:\n\n"
        + code_fence(read(t2))
        + f"\n\n[View on GitHub]({gh('templates/python_dsa_templates.py')})\n"
    )
    out = OUT_DIRS["guides"] / "templates.md"
    write_page(out, "Templates", body, position=pos, slug="/templates", mdx=False)
    OUT_FILES["templates/problem-template.md"] = out
    pos += 1

    src = REPO / "CONTRIBUTING.md"
    if src.exists():
        title, body = split_front_h1(read(src))
        body = rewrite_links(body, rel(src), "/guides/contributing")
        out = OUT_DIRS["guides"] / "contributing.md"
        write_page(out, title or "Contributing", body, position=pos,
                   slug="/contributing", mdx=False)
        OUT_FILES[rel(src)] = out


def gen_practice() -> None:
    order = ["top-interview-questions", "extended-practice",
             "company-style-sheets", "study-tracker"]
    pos = 1
    for stem in order:
        src = REPO / "practice" / f"{stem}.md"
        if not src.exists():
            continue
        title, body = split_front_h1(read(src))
        body = rewrite_links(body, rel(src), f"/practice/{stem}")
        out = OUT_DIRS["practice"] / f"{stem}.md"
        write_page(out, title, body, position=pos, slug=f"/{stem}", mdx=False)
        OUT_FILES[rel(src)] = out
        pos += 1


def main() -> int:
    for d in OUT_DIRS.values():
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)

    register_all()
    lessons = gen_python_track()
    gen_dsa_track()
    gen_guides()
    gen_practice()

    pages = sum(1 for d in OUT_DIRS.values() for _ in d.rglob("*.md*"))
    print(f"generate_content: wrote {pages} pages (base URL: {BASE_URL})")
    print(f"  python lessons: {len(lessons)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
