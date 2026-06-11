# 10 — pandas and SQL: Module Outline

## Audience
Undergrad CS and data science majors with Python, pandas, and groupby experience (modules 06–09); no prior SQL or relational database exposure.

## Dataset

| Dataset | Source | Used in | Why |
|---|---|---|---|
| Gapminder | jennybc/gapminder GitHub (TSV) | 10.1–10.7 | Same dataset from module 09; split into two tables to motivate JOIN |

Every notebook is self-contained: each loads Gapminder from the source URL in its first code cell so it can be opened on its own through its Colab badge. Notebooks 10.2–10.7 additionally rebuild the in-memory SQLite database from that load at the start of the notebook, since an in-memory database never persists between sessions.

The split into `countries` (142 × 2) and `measurements` (1704 × 5) is artificial but models real relational database design, where redundant data is stored once and joined when needed. A `sqlite3` in-memory database is recreated in each notebook's setup cell. The setup also writes the original flat file as a third table, `gapminder`; notebooks 10.3 and 10.4 query it for continent-level questions so that JOIN syntax first appears in 10.5, where it is taught.

## Notebooks

| Notebook | Topic | Main Tools |
|---|---|---|
| 10.1 | `df.query()` | Multi-condition query strings, `@variable` injection, `in` / `not in` lists |
| 10.2 | SQLite Setup | `sqlite3.connect(":memory:")`, `to_sql()`, `pd.read_sql()`, `SELECT`, `LIMIT`, `ORDER BY`, `DISTINCT`, `AS` |
| 10.3 | `WHERE` | `=`, `AND`/`OR`/`NOT`, `IN`, `BETWEEN`, `LIKE` |
| 10.4 | `GROUP BY` and `HAVING` | `COUNT(*)`, `AVG`, `SUM`, `MIN`, `MAX`, `COUNT(DISTINCT)`, `GROUP BY`, `HAVING` |
| 10.5 | `JOIN` | `INNER JOIN`, `LEFT JOIN`, `ON`, table aliases, NULL detection |
| 10.6 | SQL vs pandas | Subqueries, `WHERE col > (SELECT ...)`, when to use each tool, two-step workflow |
| 10.7 | Exercises | All module 10 tools |

## Growing Translation Table
The SQL-pandas translation table accumulates across notebooks: 7 rows in 10.2, 13 rows in 10.3, 21 rows in 10.4, 23 rows in 10.5, 24 rows in 10.6. Each table is a strict superset of the previous one, so students see the same reference artifact grow with each new concept added to the vocabulary.

## What Is Intentionally Excluded
- Window functions (`OVER`, `PARTITION BY`) — the SQL equivalent of `transform()`; too advanced for this module
- CTEs (`WITH` clause) — out of scope
- Database design and normalization theory
- `RIGHT JOIN` and `FULL OUTER JOIN` — rare in analytical practice; rewrite as `LEFT JOIN` with tables swapped (SQLite has supported both since 3.39, but they are not worth teaching here)
- Non-SQLite database connections (PostgreSQL, MySQL) — noted as portable but not demonstrated
- `INSERT`, `UPDATE`, `DELETE` — DML is out of scope; this module is read-only analytics
- Query optimization and indexing

## Learning Sequence
Python-side query syntax (10.1) → SQLite setup and SELECT (10.2) → WHERE filtering (10.3) → GROUP BY aggregation and HAVING (10.4) → JOIN across tables (10.5) → subqueries and SQL vs pandas comparison (10.6) → exercises (10.7)
