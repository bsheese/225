# 10 · pandas & SQL

## 10_1 · df.query()

### What does `df.query("year == 2007 and continent == 'Asia'")` accept as its argument?
- [x] A single string describing the condition, using column names directly and `and`/`or`/`not` keywords
- [ ] A boolean mask object
- [ ] A list of column names
- [ ] A dictionary of column-value pairs

### Inside a query string, how do you reference a Python variable like `median_life`?
- [x] Prefix it with `@`, e.g. `df.query("lifeExp > @median_life")`
- [ ] Just type the variable name; query resolves it automatically
- [ ] Wrap it in `{}` like an f-string
- [ ] You cannot use variables inside query

### Why are string values written with single quotes inside a query, e.g. `"continent == 'Asia'"`?
- [x] The query expression itself is already inside double quotes, so the string literal needs the other quote style
- [ ] Single quotes make the match case-insensitive
- [ ] SQL requires single quotes and query mimics SQL
- [ ] Double quotes would delete the column

### How do you match against several values in a query, e.g. a set of countries?
- [x] Use `in` with a list: `df.query("country in ['Norway', 'Sweden', 'Denmark']")`
- [ ] Chain `==` with commas
- [ ] Use `contains([...])`
- [ ] Pass a second argument to query

### When is `query()` most preferable to boolean indexing?
- [x] When there are three or more conditions — the string reads more clearly than nested `&` with parentheses
- [ ] Always; boolean indexing is deprecated
- [ ] Only for a single condition
- [ ] Only when the DataFrame has a datetime index

### What does `query()` return, and why does that matter?
- [x] A regular DataFrame, so you can chain another `query()` or any pandas method onto it
- [ ] A NumPy array that must be converted back
- [ ] A boolean Series
- [ ] The original DataFrame, modified in place

## 10_2 · SQLite Setup

### What makes SQLite convenient for learning SQL in a notebook?
- [x] It runs entirely inside the Python process — no server, no install beyond the standard library — and can live in memory via `:memory:`
- [ ] It requires a cloud account and an API key
- [ ] It only works with the Gapminder dataset
- [ ] It needs a separate database server running

### How do you write a DataFrame into a table and read query results back as a DataFrame?
- [x] `df.to_sql("table", conn)` writes it; `pd.read_sql("SELECT ...", conn)` returns a DataFrame
- [ ] `df.to_database()` and `pd.from_sql()`
- [ ] `conn.write(df)` and `conn.read()`
- [ ] `df.save()` and `df.load()`

### What does `SELECT * FROM measurements` return, and what does `*` mean?
- [x] Every column of every row in the `measurements` table; `*` means "all columns"
- [ ] Only the first column; `*` means "first"
- [ ] A count of rows; `*` means "count"
- [ ] The table's schema; `*` means "structure"

### What is the SQL equivalent of pandas `df.head(5)`?
- [x] Appending `LIMIT 5` to the query
- [ ] `SELECT TOP 5` is the only option in SQLite
- [ ] `HEAD 5`
- [ ] `FIRST 5 ROWS`

### How do you sort query results by `lifeExp` from highest to lowest?
- [x] `ORDER BY lifeExp DESC` (the pandas equivalent of `sort_values(..., ascending=False)`)
- [ ] `SORT lifeExp DOWN`
- [ ] `ORDER lifeExp DESCENDING`
- [ ] `GROUP BY lifeExp DESC`

### What does `SELECT DISTINCT year FROM measurements` do, and what is the `AS` keyword for?
- [x] `DISTINCT` returns each unique value once (like `unique()`); `AS` renames a column in the output
- [ ] `DISTINCT` counts rows; `AS` deletes a column
- [ ] `DISTINCT` sorts the column; `AS` sums it
- [ ] Both are pandas-only and don't exist in SQL

## 10_3 · WHERE

### What is the SQL `WHERE` equivalent of pandas `df.query("year == 2007")`, and what's the key syntax trap?
- [x] `WHERE year = 2007` — SQL uses a single `=` for equality, not `==`
- [ ] `WHERE year == 2007` — SQL requires `==` like Python
- [ ] `FILTER year = 2007`
- [ ] `HAVING year = 2007`

### When mixing `AND` and `OR`, why are parentheses important, as in `WHERE year = 2007 AND (lifeExp > 80 OR lifeExp < 45)`?
- [x] SQL evaluates `AND` before `OR`, so without parentheses the grouping — and the result — would be different
- [ ] Parentheses are purely cosmetic in SQL
- [ ] `OR` is evaluated before `AND`, so parentheses around AND are needed
- [ ] SQL ignores parentheses entirely

### What does `WHERE country IN ('Japan', 'China', 'India')` do?
- [x] Keeps rows where `country` matches any value in the list — cleaner than chaining several `OR` conditions
- [ ] Keeps rows where country equals the whole list
- [ ] Excludes those three countries
- [ ] Joins the three countries into one row

### What does `WHERE year BETWEEN 1990 AND 2007` match?
- [x] Rows where `year` is in the inclusive range [1990, 2007] — shorthand for `year >= 1990 AND year <= 2007`
- [ ] Rows strictly between 1990 and 2007 (both excluded)
- [ ] Only the years 1990 and 2007
- [ ] Rows outside that range

### In SQL's `LIKE`, what do the wildcards `%` and `_` match?
- [x] `%` matches any sequence of characters (including none); `_` matches exactly one character
- [ ] `%` matches one character; `_` matches any sequence
- [ ] Both match exactly one digit
- [ ] `%` is a literal percent sign and `_` a literal underscore

### What is the SQL equivalent of pandas `df["country"].str.startswith("New")`?
- [x] `WHERE country LIKE 'New%'`
- [ ] `WHERE country LIKE '%New'`
- [ ] `WHERE country = 'New_'`
- [ ] `WHERE country CONTAINS 'New'`

## 10_4 · GROUP BY & HAVING

### How does SQL express the pandas `df.groupby("continent")["lifeExp"].mean()`?
- [x] The grouping key goes in `GROUP BY continent` and the aggregate goes in `SELECT AVG(lifeExp)`
- [ ] `GROUP BY AVG(lifeExp)` and `SELECT continent`
- [ ] `WHERE continent GROUP lifeExp`
- [ ] `AGGREGATE continent BY lifeExp`

### Which SQL aggregate functions correspond to pandas `.size()`, `.count()`, and `.mean()`?
- [x] `COUNT(*)`, `COUNT(col)` (non-null only), and `AVG(col)`
- [ ] `SIZE()`, `COUNT()`, and `MEAN()`
- [ ] `TOTAL()`, `NONNULL()`, and `AVERAGE()`
- [ ] `COUNT(*)`, `SUM(col)`, and `MEDIAN(col)`

### What is the difference between `COUNT(*)` and `COUNT(DISTINCT country)` within a group?
- [x] `COUNT(*)` counts all rows; `COUNT(DISTINCT country)` counts unique countries — the SQL equivalent of `nunique()`
- [ ] They always give the same number
- [ ] `COUNT(*)` counts columns; `COUNT(DISTINCT)` counts rows
- [ ] `COUNT(DISTINCT)` counts nulls only

### Why can't you put `AVG(gdpPercap) > 10000` in a `WHERE` clause?
- [x] `WHERE` is evaluated before grouping, so no aggregate exists yet — filtering on an aggregate must use `HAVING`
- [ ] `WHERE` cannot use the `>` operator
- [ ] `AVG` is not a valid SQL function
- [ ] You must use `WHERE` for all conditions; HAVING doesn't exist

### What is the role of `HAVING` versus `WHERE`?
- [x] `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation
- [ ] `HAVING` filters rows; `WHERE` filters groups
- [ ] They are interchangeable
- [ ] `HAVING` sorts the groups

### How does SQL group by two keys, the equivalent of `groupby(["continent", "year"])`?
- [x] `GROUP BY continent, year` — one result row per unique combination
- [ ] `GROUP BY continent AND year`
- [ ] `GROUP BY continent THEN year`
- [ ] You can only group by one column in SQL

## 10_5 · JOIN

### What does a SQL `JOIN ... ON` do?
- [x] Combines rows from two tables that share a matching value in the named key column
- [ ] Stacks two tables vertically
- [ ] Renames columns across tables
- [ ] Sorts one table by another

### What is the pandas equivalent of an `INNER JOIN`?
- [x] `measurements.merge(countries, on="country")` (i.e. `merge(how="inner")`)
- [ ] `pd.concat([measurements, countries])`
- [ ] `measurements.append(countries)`
- [ ] `measurements.join(countries, how="outer")` always

### What does an `INNER JOIN` do with a row whose key has no match in the other table?
- [x] Drops it — only rows with a matching key in both tables survive (e.g. a fake "Narnia" row disappears)
- [ ] Keeps it with NULLs filled in
- [ ] Raises an error
- [ ] Duplicates it

### How does a `LEFT JOIN` differ from an `INNER JOIN`?
- [x] It keeps every row of the left table even with no match, filling the right table's columns with `NULL`
- [ ] It keeps only matching rows, like INNER
- [ ] It keeps every row of the right table
- [ ] It removes the left table's unmatched rows

### What is the purpose of table aliases like `FROM measurements AS m INNER JOIN countries AS c`?
- [x] They shorten the table names so column references (`m.country`, `c.continent`) are concise and unambiguous
- [ ] They rename the tables permanently in the database
- [ ] They are required or the JOIN fails
- [ ] They sort the joined result

### In `... INNER JOIN countries AS c ON m.country = c.country`, what does the `ON` clause specify?
- [x] The join condition — which column in each table holds the matching key
- [ ] The columns to return
- [ ] The sort order of the result
- [ ] A filter applied after the join

## 10_6 · SQL vs pandas

### What is a subquery?
- [x] A `SELECT` nested inside another query; the inner query runs first and its result feeds the outer query
- [ ] A query that runs on a backup database
- [ ] A query with no `FROM` clause
- [ ] Two queries joined with `AND`

### In `WHERE lifeExp > (SELECT AVG(lifeExp) FROM measurements WHERE year = 2007)`, what does the inner query contribute?
- [x] A single value (the global 2007 average) that the outer query compares each row against
- [ ] A list of countries to exclude
- [ ] The columns to display
- [ ] The sort order

### A subquery can also feed an `IN` clause. What does that enable?
- [x] Filtering one query by a list of values computed from another query, without writing an explicit JOIN
- [ ] Joining three tables at once
- [ ] Counting rows faster
- [ ] Renaming columns

### When is SQL the better tool than pandas?
- [x] When the data lives in a database and is too large to load entirely into memory — SQL filters/aggregates server-side
- [ ] When you need complex regex string parsing
- [ ] When you want to make a seaborn chart
- [ ] When the dataset has fewer than 100 rows

### When is pandas the better tool than SQL?
- [x] When the work needs complex string operations, regex, or multi-step text cleaning that SQL's `LIKE` can't express
- [ ] When the data is 50 million rows in a remote database
- [ ] When you only need a simple `GROUP BY`
- [ ] Whenever the data has a primary key

### What is the common two-step SQL-then-pandas workflow?
- [x] Use SQL to filter/aggregate a large dataset down to a small result, then use pandas for analysis and visualization
- [ ] Use pandas to load everything, then re-import it into SQL
- [ ] Run the same query in both and compare
- [ ] Use SQL only for plotting
