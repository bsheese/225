"""One-time migration: extract the `quiz_data = [...]` lists from the
practice-quiz notebooks and emit human-readable Markdown into ../quizzes/.

225's quizzes are one flat list per notebook, launched via
`QuizApp(quiz_data, 'Some Title')`. Each notebook becomes one Markdown unit
with a single section (the QuizApp title). Notebooks that don't define
`quiz_data` (e.g. the markdown/code-exercise quizzes in 09-11) are skipped.

After this runs, the Markdown files in ../quizzes/ are the canonical source.

Usage:
    python quiz_site/extract_from_notebooks.py
"""
import ast
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "quizzes"

# Friendly unit titles keyed by the unit folder name. Fallback prettifies the
# folder name if a key is missing.
TITLES = {
    "06_pandas_intro": "06 · Pandas Intro",
    "07_data_vis": "07 · Data Visualization",
    "08_data_cleaning": "08 · Data Cleaning",
    "09_data_aggregation": "09 · Data Aggregation",
    "10_pandas_sql": "10 · Pandas & SQL",
    "11_time": "11 · Time Series",
}

QUIZAPP_RE = re.compile(r"""QuizApp\(\s*quiz_data\s*,\s*(['"])(?P<title>.*?)\1""")


def _match_bracket(src: str, open_idx: int, open_ch="[", close_ch="]") -> int:
    """Index just past the bracket matching src[open_idx], skipping brackets
    that appear inside string literals."""
    depth = 0
    i = open_idx
    quote = None
    while i < len(src):
        c = src[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced brackets while slicing quiz_data literal")


def find_quiz(nb_path: Path):
    """Return (title, questions) or None if the notebook has no quiz_data."""
    nb = json.loads(nb_path.read_text())
    questions = None
    title = nb_path.parent.name
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        m = re.search(r"^quiz_data\s*=\s*", src, re.MULTILINE)
        if m and questions is None:
            open_idx = src.index("[", m.end())
            literal = src[open_idx:_match_bracket(src, open_idx)]
            questions = ast.literal_eval(literal)
        tm = QUIZAPP_RE.search(src)
        if tm:
            title = tm.group("title")
    if questions is None:
        return None
    return title, questions


def to_markdown(unit_title: str, section_title: str, questions: list) -> str:
    lines = [f"# {unit_title}", "", f"## {section_title}", ""]
    for q in questions:
        lines.append(f"### {q['question']}")
        answer = q["answer"]
        if answer not in q["options"]:
            raise ValueError(
                f"answer not among options: {answer!r} in {section_title!r}"
            )
        for opt in q["options"]:
            mark = "x" if opt == answer else " "
            lines.append(f"- [{mark}] {opt}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    OUT.mkdir(exist_ok=True)
    notebooks = sorted(REPO.glob("**/*practice_quiz*.ipynb"))
    if not notebooks:
        raise SystemExit("no practice_quiz notebooks found")
    made = 0
    for nb in notebooks:
        unit_dir = nb.parent.name
        result = find_quiz(nb)
        if result is None:
            print(f"skip {unit_dir} (no quiz_data)")
            continue
        section_title, questions = result
        unit_title = TITLES.get(unit_dir, unit_dir.replace("_", " "))
        md = to_markdown(unit_title, section_title, questions)
        (OUT / f"{unit_dir.lower()}.md").write_text(md)
        print(f"{unit_dir.lower()}.md  ({len(questions)} questions)")
        made += 1
    print(f"\nwrote {made} quiz file(s)")


if __name__ == "__main__":
    main()
