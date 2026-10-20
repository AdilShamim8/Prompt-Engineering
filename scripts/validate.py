#!/usr/bin/env python3
"""Validation checks for the Prompt-Engineering repository.

Runs on the Python standard library alone (3.8+), per the no-dependencies
scope decision in ROADMAP.md.

Checks:
  1. LINKS    - every relative Markdown link in every .md file resolves
                to an existing file (URL-decoded, anchors stripped)
  2. H1       - every guide, lab, and template file starts with an H1
  3. INDEX    - every content file is listed in its directory's README
                (advanced guides, labs, templates)
  4. COVERAGE - every advanced guide is referenced by CURRICULUM.md

Usage:  python scripts/validate.py [--root PATH]
Exit code 0 = all checks pass; 1 = failures (printed with file:line).
"""

import argparse
import re
import sys
import urllib.parse
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
H1_RE = re.compile(r"^# \S")

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "irc://")


def iter_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        yield path


def check_links(root: Path, report: list):
    """Every relative link in every .md file must resolve to a file."""
    for path in iter_markdown(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        in_fence = False
        for lineno, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in LINK_RE.findall(line):
                if target.startswith(EXTERNAL_PREFIXES):
                    continue
                if target.startswith("#"):
                    continue
                decoded = urllib.parse.unquote(target.split("#")[0].strip())
                if not decoded:
                    continue
                resolved = (path.parent / decoded).resolve()
                if not resolved.exists():
                    report.append(
                        f"BROKEN LINK {path.relative_to(root)}:{lineno} -> {target}"
                    )


def check_h1(root: Path, report: list):
    """Guide, lab, and template files must open with an H1 title."""
    watched_dirs = ("Advanced Prompt Engineering Techniques", "labs", "templates")
    for path in iter_markdown(root):
        rel = path.relative_to(root)
        if len(rel.parts) < 2 or rel.parts[0] not in watched_dirs:
            continue
        if rel.name == "README.md":
            continue
        first_line = path.read_text(encoding="utf-8", errors="replace").lstrip().splitlines()
        if not first_line or not H1_RE.match(first_line[0]):
            report.append(f"MISSING H1 {rel}")


def check_index(root: Path, report: list):
    """Content files must be linked from their directory README (and CURRICULUM)."""
    pairs = [
        (root / "Advanced Prompt Engineering Techniques",
         root / "Advanced Prompt Engineering Techniques" / "README.md"),
        (root / "labs", root / "labs" / "README.md"),
        (root / "templates", root / "templates" / "README.md"),
    ]
    for directory, index in pairs:
        if not index.exists():
            report.append(f"MISSING INDEX {index.relative_to(root)}")
            continue
        index_text = index.read_text(encoding="utf-8", errors="replace")
        for md in sorted(directory.glob("*.md")):
            if md.name == "README.md":
                continue
            encoded = urllib.parse.quote(md.name)
            if md.name not in index_text and encoded not in index_text:
                report.append(
                    f"NOT INDEXED {md.relative_to(root)} "
                    f"(not linked from {index.relative_to(root)})"
                )


def check_curriculum_coverage(root: Path, report: list):
    """Every advanced guide must be referenced by CURRICULUM.md."""
    curriculum = root / "CURRICULUM.md"
    if not curriculum.exists():
        report.append("MISSING CURRICULUM.md at repository root")
        return
    text = curriculum.read_text(encoding="utf-8", errors="replace")
    advanced = root / "Advanced Prompt Engineering Techniques"
    for md in sorted(advanced.glob("*.md")):
        if md.name == "README.md":
            continue
        encoded = urllib.parse.quote(md.name)
        if md.name not in text and encoded not in text:
            report.append(
                f"NOT IN CURRICULUM {md.relative_to(root)} (no reference in CURRICULUM.md)"
            )


CHECKS = [
    ("LINKS", check_links),
    ("H1", check_h1),
    ("INDEX", check_index),
    ("COVERAGE", check_curriculum_coverage),
]


def main():
    parser = argparse.ArgumentParser(description="Validate repository consistency")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = parser.parse_args()
    root = Path(args.root).resolve()

    failures = 0
    for name, fn in CHECKS:
        report = []
        try:
            fn(root, report)
        except Exception as exc:  # a crashing check is a failed check
            report.append(f"CHECK ERROR {name}: {exc}")
        status = "PASS" if not report else "FAIL"
        print(f"[{status}] {name} ({len(report)} problem(s))")
        for line in report:
            print(f"    {line}")
        failures += len(report)

    if failures:
        print(f"\n{failures} problem(s) found. Fix before committing.")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
