#!/usr/bin/env python3
"""Execute every course notebook and report failures.

Each notebook is copied into its own temp subdirectory and executed there.
nbconvert sets the kernel's working directory to wherever the notebook file
lives, so this keeps committed outputs untouched and stops side-effect writes
(the figures/ PNGs in module 07, SQLite files in module 10) from leaking into
the source tree. Every notebook is self-contained and loads its data from a
URL, so the copy is safe.

Before executing anything, a static check verifies that every notebook's
saved state is fully cleared: every code cell has execution_count = null and
no saved outputs. Committed notebooks ship with no output on purpose (see
CLAUDE.md) so students run each cell themselves in Colab rather than reading
canned results, and so a saved output can never drift out of sync with the
cell that produced it. Use `--clear` to put a notebook back into this state
after authoring/debugging it interactively.

Clearing outputs means this script's execution pass is the only thing that
verifies a notebook still runs top to bottom without erroring; nothing here
checks that computed values match what the surrounding prose claims about
them, so a re-verification of prose-vs-output is still a manual step after
substantive edits. Execution also runs against this repo's exact pinned
pandas version (see requirements.txt), not whatever pandas Colab happens to
ship at the time a student opens the notebook, which can lag a major version
or more behind. A clean run here does not guarantee a clean run on Colab;
treat that gap as real, especially for anything that depends on
version-specific behavior (Copy-on-Write, dtype defaults, deprecation
warnings).

The full suite runs in about three minutes, so there is no reason to skip it
before a push that touches notebooks.

Usage:
    python smoke_test.py                  # static check, then execute everything
    python smoke_test.py 07 11_2          # only paths containing a pattern
    python smoke_test.py --counts         # static check only, no execution
    python smoke_test.py --clear          # clear outputs in place, no execution
    python smoke_test.py --list           # show what would run, don't run
    python smoke_test.py --timeout 600    # per-notebook timeout in seconds

Exit status is non-zero if the static check or any notebook fails.
"""

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parent
VENV_DIR = ROOT / "venv"

EXCLUDE_DIR_PARTS = {"venv", ".ipynb_checkpoints", "_site"}


def venv_warning():
    """None if running from ./venv (or if no ./venv exists, as in CI);
    otherwise a banner to print.

    Jupyter picks a kernel via sys.prefix, which is set by which python ran
    this script, not by whether `source venv/bin/activate` was typed.
    (Checking sys.executable directly doesn't work: venv/bin/python3 is a
    symlink to the system interpreter, so resolving it collapses both paths
    to the same file. sys.prefix is what venvs actually redirect via
    pyvenv.cfg, so it's the correct signal.) If this process isn't running
    with ./venv's prefix, notebooks execute against whatever kernel is
    registered elsewhere on the machine, which can be missing or have
    outdated packages. Failures from that mismatch look exactly like real
    notebook bugs, so flag it loudly rather than let it masquerade as one.
    """
    if not VENV_DIR.exists():
        return None  # CI installs into its own interpreter; nothing to compare
    try:
        running = pathlib.Path(sys.prefix).resolve()
        expected = VENV_DIR.resolve()
    except OSError:
        return None
    if running == expected:
        return None
    return (
        "\n"
        "############################################################\n"
        "#  WARNING: not running from this project's venv.\n"
        f"#  Expected prefix: {expected}\n"
        f"#  Actual prefix:   {running}\n"
        "#  Run `source venv/bin/activate` first. Otherwise notebooks\n"
        "#  execute against whatever Jupyter kernel is registered\n"
        "#  elsewhere, and failures below may be environment artifacts,\n"
        "#  not real bugs.\n"
        "############################################################\n"
    )


def collect(patterns):
    nbs = []
    for p in sorted(ROOT.rglob("*.ipynb")):
        rel = p.relative_to(ROOT)
        if EXCLUDE_DIR_PARTS & set(rel.parts):
            continue
        if patterns and not any(pat in str(rel) for pat in patterns):
            continue
        nbs.append(rel)
    return nbs


def check_saved_state(nbs):
    """Verify each notebook's committed state is fully cleared.

    Returns a list of problem strings (empty means all clean): every code
    cell must have execution_count = null and an empty outputs list.
    Applies to every notebook, exercises included: a solution cell teaches
    by its code, not by a saved result the student never had to produce.
    """
    problems = []
    for rel in nbs:
        nb = json.loads((ROOT / rel).read_text())
        for i, c in enumerate(nb["cells"]):
            if c["cell_type"] != "code":
                continue
            if c.get("execution_count") is not None:
                problems.append(
                    f"{rel}: code cell {i} has a saved execution_count ({c['execution_count']})"
                )
            if c.get("outputs"):
                problems.append(f"{rel}: code cell {i} has saved output(s)")
    return problems


# Cell metadata that only makes sense alongside a saved output (execution
# timestamps, Colab's output-rendering hints) and goes stale the moment the
# output it describes is cleared.
OUTPUT_ONLY_METADATA_KEYS = {"execution", "outputId", "colab"}


def _detect_format(raw, nb):
    """Reverse-engineer the (indent, sort_keys, trailing_newline) a notebook
    was last saved with, by brute-forcing json.dumps against the raw text.

    Notebooks in this repo were saved by a mix of tools/versions (classic
    Jupyter, Colab exports, ...) and are not all serialized the same way
    (some 1-space indent, some 2; some with sorted keys, some insertion
    order; some with a trailing newline, some without). Guessing wrong
    would rewrite a whole file's formatting on a one-line content edit and
    bury the real diff in noise, so every write reuses whatever format the
    file already had rather than imposing one convention.
    """
    for indent in (1, 2):
        for sort_keys in (True, False):
            for trailing_newline in (True, False):
                dumped = json.dumps(nb, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
                if trailing_newline:
                    dumped += "\n"
                if dumped == raw:
                    return indent, sort_keys, trailing_newline
    return None


def _write_notebook(path, nb, fmt):
    indent, sort_keys, trailing_newline = fmt
    dumped = json.dumps(nb, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
    if trailing_newline:
        dumped += "\n"
    path.write_text(dumped)


def clear_outputs(nbs):
    """Reset every code cell to execution_count = null, outputs = [] in place.

    Also strips per-cell metadata that only described the now-removed output
    (execution timestamps, Colab's outputId/base_uri/height hints). Reuses
    each file's own existing JSON formatting (see _detect_format) so a
    clear-only pass produces a minimal diff.
    """
    changed_count = 0
    unrecognized = []
    for rel in nbs:
        path = ROOT / rel
        raw = path.read_text()
        nb = json.loads(raw)
        fmt = _detect_format(raw, nb)
        if fmt is None:
            unrecognized.append(rel)
            fmt = (1, True, True)  # nbformat's own default; best effort
        changed = False
        for c in nb["cells"]:
            if c["cell_type"] != "code":
                continue
            if c.get("execution_count") is not None:
                c["execution_count"] = None
                changed = True
            if c.get("outputs"):
                c["outputs"] = []
                changed = True
            meta = c.get("metadata", {})
            for key in OUTPUT_ONLY_METADATA_KEYS & meta.keys():
                del meta[key]
                changed = True
        if changed:
            _write_notebook(path, nb, fmt)
            changed_count += 1
    print(f"Cleared {changed_count}/{len(nbs)} notebook(s)"
          f" ({len(nbs) - changed_count} already clean).")
    if unrecognized:
        print("Could not recognize the existing JSON formatting for "
              f"{len(unrecognized)} notebook(s); wrote nbformat's default "
              "format instead, so their diff may be larger than necessary:")
        for rel in unrecognized:
            print(f"  {rel}")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("patterns", nargs="*",
                    help="only check notebooks whose path contains one of these substrings")
    ap.add_argument("--list", action="store_true",
                    help="list notebooks that would run, then exit")
    ap.add_argument("--counts", action="store_true",
                    help="run only the static saved-state check, no execution")
    ap.add_argument("--clear", action="store_true",
                    help="clear outputs/execution_count in place, no execution")
    ap.add_argument("--timeout", type=int, default=600,
                    help="per-notebook timeout in seconds (default 600)")
    args = ap.parse_args()

    nbs = collect(args.patterns)
    if not nbs:
        print("No notebooks matched.")
        return 1
    if args.list:
        for nb in nbs:
            print(nb)
        print(f"\n{len(nbs)} notebooks")
        return 0

    if args.clear:
        return clear_outputs(nbs)

    problems = check_saved_state(nbs)
    if problems:
        print(f"Static check: {len(problems)} problem(s) in saved notebook state:")
        for p in problems:
            print(f"  {p}")
        print("\nClear outputs before committing, e.g.:")
        print("  python smoke_test.py --clear <notebook>")
    else:
        print(f"Static check: all {len(nbs)} notebooks have clean saved state.")
    if args.counts:
        return 1 if problems else 0

    warning = venv_warning()
    if warning:
        print(warning)

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        # Two isolation measures so notebooks really execute on THIS
        # interpreter and not whatever else lives on the machine:
        #
        # 1. Invoke nbconvert as `sys.executable -m nbconvert`, never
        #    `-m jupyter nbconvert`. The latter goes through jupyter_core's
        #    dispatcher, which finds a `jupyter-nbconvert` executable on
        #    PATH; if ~/.local/bin holds one (shebang /usr/bin/python3), the
        #    whole run silently switches interpreter and package set, and a
        #    local pass proves nothing about the pinned environment. This
        #    machine had exactly that.
        # 2. Point JUPYTER_DATA_DIR at an empty temp dir so user-level
        #    kernelspecs (~/.local/share/jupyter/kernels) cannot shadow the
        #    environment's own kernel during kernel-name resolution.
        env = dict(os.environ, JUPYTER_DATA_DIR=str(pathlib.Path(tmp) / "jupyter_data"))
        for i, nb in enumerate(nbs, 1):
            print(f"[{i}/{len(nbs)}] {nb} ... ", end="", flush=True)
            start = time.time()
            try:
                work_dir = pathlib.Path(tmp) / str(nb).replace("/", "__")
                work_dir.mkdir()
                nb_copy = work_dir / nb.name
                shutil.copy(ROOT / nb, nb_copy)
                proc = subprocess.run(
                    [sys.executable, "-m", "nbconvert", "--to", "notebook",
                     "--execute", str(nb_copy), "--output-dir", str(work_dir),
                     "--ExecutePreprocessor.timeout", str(args.timeout)],
                    capture_output=True, text=True, timeout=args.timeout + 60, env=env,
                )
                ok = proc.returncode == 0
                err = proc.stderr
            except subprocess.TimeoutExpired:
                ok, err = False, f"hard timeout after {args.timeout}s"
            elapsed = time.time() - start
            if ok:
                print(f"ok ({elapsed:.0f}s)")
            else:
                print(f"FAIL ({elapsed:.0f}s)")
                tail = "\n".join(line for line in err.splitlines() if line.strip())[-2000:]
                failures.append((nb, tail))

    print(f"\n{len(nbs) - len(failures)}/{len(nbs)} notebooks passed.")
    for nb, tail in failures:
        print(f"\n=== FAILED: {nb} ===\n{tail}")
    if failures and warning:
        print(warning)
    return 1 if (failures or problems) else 0


if __name__ == "__main__":
    sys.exit(main())
