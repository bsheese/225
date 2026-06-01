# 09 — Data Aggregation: Module Outline

## Audience
Undergrad CS and data science majors with Python and pandas experience (modules 06–08); familiar with single-key `groupby().mean()` from module 06 but no prior exposure to multi-key groupby, `agg()`, `transform()`, `filter()`, or `pivot_table()`.

## Dataset

| Dataset | Source | Used in | Why |
|---|---|---|---|
| Gapminder | jennybc/gapminder GitHub (TSV) | 09.1–09.7 | Panel data with two natural grouping dimensions (continent, year) and three meaningful numerics; no cleaning needed |

Every notebook is self-contained: each loads Gapminder from the source URL in its first code cell so it can be opened on its own through its Colab badge. Notebook 09.1 explains the load; 09.2–09.7 repeat the identical load cell without re-explaining it.

## Notebooks

| Notebook | Topic | Main Tools |
|---|---|---|
| 09.1 | Meet Gapminder | `pd.read_csv(url, sep="\t")`, `.info()`, `.describe()`, single-key groupby review |
| 09.2 | Multiple Groupby Keys | `groupby([col1, col2])`, MultiIndex, `reset_index()`, `unstack()` |
| 09.3 | `agg()` in Depth | `agg(["mean", "std", ...])`, named aggregation syntax, `size()` vs `count()`, `nunique()` |
| 09.4 | `transform()` | `groupby().transform("mean")`, deviation and z-score columns |
| 09.5 | `filter()` | `groupby().filter(lambda g: ...)`, contrast with row-level boolean indexing |
| 09.6 | `pivot_table()` | `pd.pivot_table(values=, index=, columns=, aggfunc=)`, `margins=True`, heatmap |
| 09.7 | Exercises | All module 09 tools on Gapminder |

## What Is Intentionally Excluded
- `apply()` with custom functions — increasingly deprecated in favor of `agg()`
- `resample()` — time-series specific; covered in module 11
- `pd.Grouper` — too advanced
- Cumulative operations: `cumsum()`, `cummax()`, `cummin()`
- `pd.concat()` and `merge()` — data combination covered in module 10
- Weighted aggregations (e.g., population-weighted means)
- New visualization types or statistical concepts — seaborn and descriptives appear as tools, not lessons

## Learning Sequence
Dataset orientation (09.1) → multi-key groupby and MultiIndex (09.2) → multiple aggregations with `agg()` (09.3) → group-level columns with `transform()` (09.4) → group-level filtering with `filter()` (09.5) → wide-format tables with `pivot_table()` (09.6) → exercises (09.7)
