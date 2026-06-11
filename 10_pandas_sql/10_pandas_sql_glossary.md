# 10 — pandas and SQL: Glossary

**aggregate function** — A SQL function that collapses multiple rows into a single value per group. The standard functions are `COUNT`, `AVG(col)`, `SUM(col)`, `MIN(col)`, and `MAX(col)`; `COUNT` comes in three forms (`COUNT(*)` for all rows, `COUNT(col)` for non-null values, `COUNT(DISTINCT col)` for unique values). Aggregate functions appear in `SELECT` and `HAVING`; they cannot appear in `WHERE`.

**alias (`AS`)** — A temporary name given to a column or table. Column aliases (`SELECT lifeExp AS life_expectancy`) rename the output column. Table aliases (`FROM measurements AS m`) shorten long names for use in `ON` clauses. Table aliases are required when the same column name exists in both joined tables.

**`BETWEEN`** — A SQL range condition: `WHERE year BETWEEN 1990 AND 2007` keeps rows where the value falls in the closed interval [1990, 2007]. Equivalent to `WHERE year >= 1990 AND year <= 2007`.

**`COUNT(DISTINCT col)`** — Counts how many unique values appear in a column within each group. Distinct from `COUNT(*)`, which counts every row including duplicates. The SQL equivalent of pandas `.nunique()`.

**database** — A structured system for storing and querying data. SQL is the standard language that almost every relational database understands. SQLite is a lightweight database that runs inside a Python process with no server required.

**`df.query()`** — A pandas method that filters rows using a readable string expression. Column names are used directly; `and`/`or`/`not` replace `&`/`|`/`~`; Python variables are referenced with `@varname`.

**`GROUP BY`** — A SQL clause that divides rows into groups by the values of one or more columns, then applies aggregate functions within each group. The SQL equivalent of `groupby().agg()`. Every non-aggregated column in `SELECT` must appear in `GROUP BY`.

**`HAVING`** — A SQL clause that filters groups after aggregation. It appears after `GROUP BY` and can reference aggregate functions. `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation is complete. The SQL equivalent of `groupby().filter()`.

**`IN`** — A SQL operator that tests whether a value matches any member of a list: `WHERE country IN ('Japan', 'China')`. Negated with `NOT IN`. The SQL equivalent of `.isin([...])`.

**`INNER JOIN`** — A join that keeps only rows where the key value exists in both tables. Rows with no match in the other table are dropped. The SQL equivalent of `df1.merge(df2, on="key")` (the pandas default).

**`LEFT JOIN`** — A join that keeps every row from the left table even when there is no matching row in the right table. Unmatched columns from the right table become `NULL`. Used to detect missing matches by filtering `WHERE right_table.col IS NULL`.

**`LIKE`** — A SQL string pattern-matching operator. `%` matches any sequence of characters; `_` matches exactly one character. Less powerful than regex; use pandas `.str.contains()` for complex patterns.

**`NULL`** — SQL's missing-value sentinel, equivalent to pandas `NaN`. Aggregate functions ignore `NULL`. A `NULL` value cannot be tested with `=`; use `IS NULL` or `IS NOT NULL`.

**`ON`** — The clause that specifies the join condition between two tables: `JOIN countries AS c ON m.country = c.country`. It names the column in each table that holds the shared key.

**`pd.read_sql(query, conn)`** — The pandas function that sends a SQL string to a database connection and returns the result as a DataFrame.

**relational table** — A rectangular data structure in a database with named, typed columns, analogous to a pandas DataFrame. Related tables share a key column that allows them to be joined.

**subquery** — A `SELECT` statement nested inside another SQL statement. Used in `WHERE` to compare against a computed value (`WHERE lifeExp > (SELECT AVG(lifeExp) FROM ...)`), or in `IN` to filter based on a list produced by another query.

**`to_sql(name, conn)`** — A pandas method that writes a DataFrame into a database table. `index=False` prevents writing the integer row index as a database column. `if_exists="replace"` overwrites an existing table of the same name.

**`WHERE`** — A SQL clause that filters rows before grouping or aggregation. Appears after `FROM` and before `GROUP BY`. The SQL equivalent of boolean indexing or `df.query()`.
