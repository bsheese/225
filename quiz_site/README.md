# Practice quiz site

Self-serve practice quizzes published to GitHub Pages — one URL, students pick a
quiz from a menu. No hosting to manage, nothing for students to install.

**Live URL (after the one-time setup below):**
https://bsheese.github.io/225/

## Authoring

Quizzes are plain Markdown in [`../quizzes/`](../quizzes). One file per unit.
This Markdown is the **single source of truth** — edit it directly.

```markdown
# 06 · Pandas Intro          <- unit title (one # per file)

## Pandas Intro Quiz         <- the quiz section (one menu entry)

### What does `s.loc['b']` return?
- [ ] 1
- [x] 2                      <- [x] = correct answer
- [ ] KeyError
```

- Exactly one option per question must be marked `- [x]`.
- Question and option text may use inline Markdown (e.g. `` `code` ``).

## How it ships

1. You edit `quizzes/*.md` and push to `main`.
2. `.github/workflows/quizzes.yml` runs `python quiz_site/build.py`, which parses
   the Markdown into `_site/quizzes.json` and copies the static template.
3. The workflow deploys `_site/` to GitHub Pages.

`_site/` is generated and gitignored — never edit it by hand.

## Preview locally

```bash
python quiz_site/build.py
python -m http.server -d _site 8000   # then open http://localhost:8000
```

## One-time GitHub setup

In the repo on GitHub: **Settings → Pages → Build and deployment → Source →
"GitHub Actions"**. After that, every push that touches `quizzes/` or
`quiz_site/` republishes automatically.

## Notes

- Correct answers are present in `quizzes.json` and therefore visible to anyone
  who inspects the page. These are ungraded self-assessment quizzes, so that's
  fine — don't use this for anything exam-grade.
- `extract_from_notebooks.py` was the one-time migration that generated the
  initial Markdown from the `quiz_data = [...]` practice-quiz notebooks (units
  06–08). It isn't part of the build; the Markdown is canonical now. The 09–11
  practice-quiz notebooks use a different markdown/code-exercise format and were
  not migrated — author Markdown for them here if you want them on the site.
- This site engine is shared with the cs377 course; the only repo-specific
  pieces are the title in `quiz_site/template/index.html` and this extractor.
