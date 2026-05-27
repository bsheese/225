# Module 10: pandas, query(), and SQL

## Module goal

Teach students to query data using SQL-like syntax, starting with `df.query()` as a stepping stone from boolean indexing, then moving to real SQL via SQLite. Every SQL concept is anchored to its pandas equivalent so students build on what they already know rather than starting from scratch. By the end, students can write basic SQL queries against a relational database and understand when SQL is the right tool instead of pandas.

## Dataset: Gapminder (split into two tables)

Students already know this data. The module splits it into two relational tables to motivate the JOIN lesson:

```python
import pandas as pd
import sqlite3

url = "https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv"
df = pd.read_csv(url, sep="\t")

# Two tables that naturally need a JOIN
countries = df[["country", "continent"]].drop_duplicates().reset_index(drop=True)
measurements = df[["country", "year", "lifeExp", "pop", "gdpPercap"]]
```

Loading into SQLite:
```python
conn = sqlite3.connect(":memory:")
countries.to_sql("countries", conn, index=False, if_exists="replace")
measurements.to_sql("measurements", conn, index=False, if_exists="replace")
```

Querying back:
```python
pd.read_sql("SELECT * FROM countries LIMIT 5", conn)
```

- **countries**: 142 rows × 2 columns (`country`, `continent`)
- **measurements**: 1,704 rows × 5 columns (`country`, `year`, `lifeExp`, `pop`, `gdpPercap`)
- No missing values. The split is the entire setup; no cleaning needed.
- The split is artificial (the full dataset has continent in every row), but it creates a realistic relational scenario where JOIN is genuinely necessary.

## What students already know (do not re-teach)

- Boolean indexing: `df[df["lifeExp"] > 70]`
- `groupby().agg()` — module 09
- `groupby().filter()` — module 09
- `merge()` — briefly introduced; covered more in this module's JOIN notebook
- Basic seaborn charts — used as tools, not taught again

## Scope

**Cover:**
- `df.query()` — string expression syntax, variable injection with `@`, chaining with `&` and `|`
- SQLite in-memory databases via `sqlite3` standard library
- `df.to_sql()` and `pd.read_sql()` as the pandas/SQL bridge
- `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`
- `GROUP BY` with aggregate functions: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
- `HAVING` — group-level filtering
- `INNER JOIN` and `LEFT JOIN`
- Simple subqueries in `WHERE` clauses
- Side-by-side SQL vs pandas translation

**Do not cover:**
- `CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE` — students are analysts, not DBAs
- SQLAlchemy — unnecessary for this audience
- PostgreSQL, MySQL — no server setup in a notebook course
- Window functions (`OVER`, `PARTITION BY`) — too advanced
- Indexes and query optimization — out of scope
- `df.eval()` — rarely used; skip

---

## Notebook plan

### 10.1 — `df.query()`: SQL-Like Filtering in pandas

**Goal:** introduce `df.query()` as a cleaner alternative to boolean indexing for complex filter conditions, and establish the string-expression syntax that directly prefigures SQL WHERE clauses.

**Primary calls:** `df.query("expression")`, `@variable` injection, chaining conditions with `&` and `|`, `str.contains()` inside query via backticks

**Content:**
- Motivation: students know `df[(df["lifeExp"] > 70) & (df["year"] == 2007)]`. Works fine for two conditions; gets unwieldy at four or five. Show a realistic 3-condition filter and let students feel the bracket clutter.
- `df.query("lifeExp > 70 and year == 2007")` — same result, cleaner syntax. Show the output is identical.
- Variable injection: sometimes the threshold comes from a calculation, not a literal. Show `threshold = df["lifeExp"].mean()` then `df.query("lifeExp > @threshold")`. The `@` prefix pulls in a Python variable.
- String conditions: `df.query("continent == 'Asia'")` — note the inner single quotes inside the double-quoted string.
- Column names with spaces: if a column has spaces, wrap it in backticks: `` df.query("`life exp` > 70") ``. Mention briefly; the Gapminder columns don't need this.
- `query()` chains naturally: `df.query("year == 2007").query("lifeExp > 70")` — or combine into one. Show both.
- When to use `query()` vs boolean indexing: for 1-2 conditions, boolean indexing is fine; for 3+ conditions or when the expression is going to be logged or read by someone else, `query()` is cleaner. Neither is always right.
- Close with a bridge: `query()` uses string expressions that look a lot like what you'd write in a database query. In the next notebook, we'll see where that syntax comes from.

---

### 10.2 — Setting Up SQLite: Your First SQL Queries

**Goal:** load data into a SQLite database, run the first SQL queries, and establish the `pd.read_sql()` pattern that all remaining notebooks use.

**Primary calls:** `sqlite3.connect(":memory:")`, `df.to_sql()`, `pd.read_sql("SELECT ...", conn)`, `SELECT`, `FROM`, `LIMIT`, `ORDER BY`, `SELECT DISTINCT`

**Content:**
- Motivation: `df.query()` filters a DataFrame that is already in memory. But most real data lives in databases, not CSV files. SQL is the language every database speaks. If you can write SQL, you can work with data anywhere — not just in Python.
- The setup: load the Gapminder URL into pandas as usual, split into `countries` and `measurements`, call `to_sql()` to write both into a SQLite in-memory database. Explain `:memory:` briefly — the database lives in RAM and disappears when the session ends, which is fine for learning.
- First query: `pd.read_sql("SELECT * FROM countries LIMIT 5", conn)`. Show that the result is a regular DataFrame. Students can then use all of their pandas skills on the result.
- `SELECT` specific columns: `SELECT country, continent FROM countries` — contrast with pandas `df[["country", "continent"]]`. They do the same thing.
- `ORDER BY`: `SELECT country, continent FROM countries ORDER BY country` — contrast with `df.sort_values("country")`.
- `ORDER BY ... DESC`: descending sort.
- `SELECT DISTINCT continent FROM countries` — deduplicate, contrast with `df["continent"].unique()`.
- `LIMIT`: cap output rows — contrast with `df.head(n)`.
- Side-by-side table: for each SQL clause introduced so far, show the pandas equivalent. Start building this table; it will grow across the module.
- Close with a bridge: we can select, sort, and deduplicate. The next step is filtering — which maps to what students already know from boolean indexing and `query()`.

---

### 10.3 — Filtering with WHERE

**Goal:** teach the SQL WHERE clause and show it is the SQL equivalent of `df.query()` and boolean indexing.

**Primary calls:** `WHERE`, comparison operators, `AND` / `OR` / `NOT`, `IN`, `BETWEEN`, `LIKE`

**Content:**
- Motivation: show the pandas filter `df.query("year == 2007 and lifeExp > 70")` from notebook 10.1, then show the SQL equivalent side by side:
  ```sql
  SELECT * FROM measurements WHERE year = 2007 AND lifeExp > 70
  ```
  Note the small syntax differences: `=` not `==`, `AND` capitalized, no quotes around column names.
- Standard comparisons: `=`, `!=`, `<`, `>`, `<=`, `>=`.
- `AND` and `OR`: build up a multi-condition filter incrementally.
- `NOT`: `WHERE NOT continent = 'Africa'`.
- `IN`: `WHERE continent IN ('Asia', 'Europe')` — contrast with `df.query("continent in ['Asia', 'Europe']")` and the pandas `isin()` approach.
- `BETWEEN`: `WHERE year BETWEEN 1990 AND 2007` — contrast with `df.query("1990 <= year <= 2007")`.
- `LIKE`: `WHERE country LIKE 'A%'` — SQL's string matching operator. Contrast with `str.startswith()` or `str.contains()`. `%` = any sequence of characters, `_` = any single character.
- Note: SQL `LIKE` is less powerful than pandas regex. For complex string patterns, pulling data into pandas first and using `str.contains()` is often cleaner. This is one real case where pandas wins.
- `WHERE` evaluation order: AND before OR; use parentheses when combining both.
- Side-by-side table: add WHERE, IN, BETWEEN, LIKE to the growing translation table.
- Close: we can now filter rows. Next: summarizing groups — the SQL equivalent of `groupby().agg()`.

---

### 10.4 — GROUP BY and HAVING

**Goal:** teach SQL GROUP BY with aggregate functions, and HAVING as the group-level filter that mirrors `groupby().filter()`.

**Primary calls:** `GROUP BY`, `COUNT(*)`, `COUNT(DISTINCT ...)`, `AVG()`, `SUM()`, `MIN()`, `MAX()`, `HAVING`, `GROUP BY` with multiple columns

**Content:**
- Motivation: students know `df.groupby("continent")["lifeExp"].mean()`. Show the SQL side by side:
  ```sql
  SELECT continent, AVG(lifeExp) FROM measurements GROUP BY continent
  ```
  Note that SQL requires you to list every non-aggregated column in GROUP BY (unlike pandas, which handles this automatically).
- Aggregate functions: `COUNT(*)`, `AVG()`, `SUM()`, `MIN()`, `MAX()`. Show each on a real question about the Gapminder data.
- `COUNT(*)` vs `COUNT(col)`: `COUNT(*)` counts rows; `COUNT(col)` counts non-null values in that column. Parallel to pandas `size()` vs `count()` from module 09.
- `COUNT(DISTINCT col)`: counts distinct values — equivalent to `nunique()` in pandas.
- Column aliases with `AS`: `SELECT AVG(lifeExp) AS avg_life FROM measurements GROUP BY continent`. Required when you want a readable output column name.
- Multiple grouping keys: `GROUP BY continent, year` — the SQL equivalent of `groupby(["continent", "year"])`.
- `HAVING`: filter groups after aggregation. `HAVING AVG(gdpPercap) > 10000` keeps only groups where the aggregate condition is true — contrast with `filter(lambda g: g["gdpPercap"].mean() > 10000)` from module 09. Distinguish from WHERE: WHERE filters rows before grouping, HAVING filters groups after.
- A concrete example that uses both: "Which continents had a mean GDP per capita above $10,000 in years after 1980?" — requires WHERE (filter years first), GROUP BY (aggregate per continent), and HAVING (filter the groups).
- Side-by-side table: add GROUP BY, COUNT, AVG/SUM/MIN/MAX, HAVING.
- Close: we can now filter, group, and aggregate. The one thing we cannot do yet is combine rows from two tables — which requires a JOIN.

---

### 10.5 — JOIN: Combining Tables

**Goal:** teach INNER JOIN and LEFT JOIN as the SQL equivalent of pandas `merge()`.

**Primary calls:** `INNER JOIN ... ON`, `LEFT JOIN ... ON`, multi-table queries, table aliases

**Content:**
- Motivation: the `measurements` table has no continent column. To group by continent, we need to bring it in from the `countries` table. In pandas, this is `merge()`. In SQL, it is `JOIN`.
- Show the pandas version first: `measurements.merge(countries, on="country")` — students know this from module 09 context. Now show the SQL equivalent:
  ```sql
  SELECT m.country, c.continent, m.year, m.lifeExp
  FROM measurements AS m
  INNER JOIN countries AS c ON m.country = c.country
  ```
- Table aliases: `measurements AS m` and `countries AS c` — shorthand for qualifying column names. Explain the `m.country` notation: necessary when both tables have a column with the same name.
- `INNER JOIN`: only rows where the key exists in both tables. Equivalent to pandas `merge(how="inner")`.
- What gets dropped: rows with no match on either side disappear. Show this with a concrete example — add one fake country to measurements that doesn't appear in countries, and show it vanishes from the INNER JOIN result.
- `LEFT JOIN`: keeps all rows from the left table even if there is no match in the right table; fills missing columns with NULL. Equivalent to pandas `merge(how="left")`. Use the same fake-country example to show the difference: now the row stays but the continent column is NULL.
- Combine JOIN with WHERE, GROUP BY, and HAVING: "For each continent, what is the mean life expectancy in 2007, keeping only continents with more than 20 countries?" — a query that uses all four clauses together.
- Side-by-side table: add INNER JOIN and LEFT JOIN.
- Note: RIGHT JOIN and FULL OUTER JOIN exist but are rarely used when you control the query; a LEFT JOIN with the tables swapped is always equivalent. Don't teach them.
- Close: with SELECT, WHERE, GROUP BY, HAVING, and JOIN, students can express almost any analytical question a business analyst would ask. The last notebook puts it all together and discusses when to use SQL vs pandas.

---

### 10.6 — SQL vs pandas: When to Use Each

**Goal:** consolidate the full SQL vocabulary, present a decision framework for SQL vs pandas, and demonstrate a realistic end-to-end workflow that uses both.

**Primary calls:** subqueries (`WHERE col IN (SELECT ...)`), the full side-by-side translation table, realistic multi-clause queries

**Content:**
- Subqueries: sometimes the value in a WHERE or HAVING clause comes from another query. Show a simple example: "Find all countries whose 2007 life expectancy was above the global average."
  ```sql
  SELECT country, lifeExp
  FROM measurements
  WHERE year = 2007 AND lifeExp > (SELECT AVG(lifeExp) FROM measurements WHERE year = 2007)
  ```
  Contrast with the pandas approach: compute the mean first, store it in a variable, use `query("lifeExp > @mean")`. Both work; the subquery is self-contained; the pandas version is easier to debug step by step.
- The complete side-by-side translation table: every SQL clause introduced across the module next to its pandas equivalent. This is the key reference artifact of the module.
- When SQL wins:
  - The data is in a database and loading it all into pandas would be slow or impossible (filter before loading)
  - You need to join many tables and the join logic is complex
  - You are writing a query that other people (who know SQL, not pandas) need to read
  - The database engine can run the aggregation faster than Python on large data
- When pandas wins:
  - You need complex string operations (regex, multi-step extraction)
  - You need `transform()` — SQL has window functions but they are more complex
  - You are iterating quickly and need to inspect intermediate results
  - The data is already in a DataFrame
- Realistic workflow: fetch a filtered aggregate from SQLite using SQL, then refine and visualize in pandas. Show a complete example: one SQL query that does the heavy lifting (join, group, filter), then pandas for cleanup and charting.
- Close: point students to the exercises notebook. Also note that everything they learned here transfers directly to PostgreSQL, MySQL, and any other SQL database — the syntax is nearly identical.

---

### 10.7 — Exercises

**Goal:** practice the full module — `df.query()`, SELECT/WHERE/ORDER BY, GROUP BY/HAVING, JOIN, and subqueries.

**Structure:** same as previous exercise notebooks — markdown question cell, blank `# your code here` cell, hidden solution cell with `#@title Solution` and `"cellView": "form"` metadata.

**Setup:** students load Gapminder, split into `countries` and `measurements`, and load both into a SQLite in-memory database at the top. All exercises run against that connection.

**Exercises:**

1. Using `df.query()`, find all countries in Asia with a life expectancy above 72 in 2007. Return country name and life expectancy, sorted descending.
2. Using `df.query()` and a variable injected with `@`, find all rows where GDP per capita is above the dataset-wide mean. How many rows is that?
3. Write a SQL `SELECT` query that returns all distinct years in the measurements table, sorted ascending.
4. Write a SQL query that returns the 10 countries with the highest life expectancy in 2007, showing country name and life expectancy.
5. Write a SQL query using `WHERE` and `IN` to return all rows from measurements where the year is 1952 or 2007.
6. Write a SQL query using `WHERE` and `LIKE` to find all countries whose name starts with the letter "C".
7. Write a SQL `GROUP BY` query that returns the average life expectancy per continent across all years. Sort by average life expectancy descending.
8. Write a SQL query that returns the number of distinct countries in each continent. (`COUNT(DISTINCT country)`)
9. Write a SQL query using `HAVING` to find continents where the average GDP per capita in 2007 exceeded $15,000.
10. Write a SQL `INNER JOIN` query that combines the `countries` and `measurements` tables. Return continent, year, and mean life expectancy, grouped by continent and year, for years after 1990. Sort by continent and year.
11. Write a SQL `LEFT JOIN` query. Add a fake row to `countries` (country="Narnia", continent="Fantasy") using `pd.concat()`, reload it into SQLite, then LEFT JOIN against measurements and show how the row with no matching measurements appears.
12. Write a SQL subquery that returns all countries whose 1952 life expectancy was below the global average for 1952.
13. (Challenge) In a single SQL query (using JOIN, GROUP BY, and HAVING), find all continents where the average life expectancy in 2007 was above 70, and for each such continent, return the continent name, the number of countries, and the average and minimum life expectancy. Then pass the result to a seaborn bar chart.

---

## Writing and pedagogy reminders

- Read `writing_sample.md` before writing any prose.
- No em-dashes anywhere.
- Every notebook opens with the Colab badge cell (before title, before everything).
- Every code cell is preceded by a markdown cell that earns it.
- Every output is interpreted in prose immediately after.
- Show the limited tool's failure first, then introduce the new one as the fix.
- Introduce each clause or function at its minimum; add one element per subsequent example.
- Close each notebook with a bridge to the next.
- The side-by-side SQL vs pandas table should grow across notebooks 10.2–10.6, not appear all at once.
- `df.query()` in notebook 10.1 should feel like a payoff, not groundwork — students can use it immediately. SQL in 10.2 should feel like "oh, that syntax looks familiar."
