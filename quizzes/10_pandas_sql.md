# 10 · pandas & SQL

## 10_1 · df.query()

### What does `df.query("year == 2007 and continent == 'Asia'")` accept as its argument?
- [x] A single string describing the condition, using column names directly and `and`/`or`/`not` keywords
- [ ] A boolean mask object created outside the query
- [ ] A list of column names to filter on
- [ ] A dictionary mapping column names to filter values

### Inside a query string, how do you reference a Python variable like `median_life`?
- [x] Prefix it with `@`, e.g. `df.query("lifeExp > @median_life")`
- [ ] Just type the variable name; query resolves it automatically
- [ ] Wrap it in `{}` like an f-string literal
- [ ] You cannot reference Python variables inside a query string

### Why are string values written with single quotes inside a query, e.g. `"continent == 'Asia'"`?
- [x] The query expression itself is already inside double quotes, so the string literal needs the other quote style
- [ ] Single quotes make the match case-insensitive
- [ ] SQL requires single quotes and query mimics that convention
- [ ] Using double quotes would delete the column name

### How do you match against several values in a query, e.g. a set of countries?
- [x] Use `in` with a list: `df.query("country in ['Norway', 'Sweden', 'Denmark']")`
- [ ] Chain `==` conditions separated by commas
- [ ] Use `contains([...])` inside the query string
- [ ] Pass a second argument with the list to query

### When is `query()` most preferable to boolean indexing?
- [x] When there are three or more conditions — the string reads more clearly than nested `&` with parentheses
- [ ] In all cases; boolean indexing is deprecated in modern pandas
- [ ] Only when filtering on a single condition
- [ ] Only when the DataFrame has a datetime index

### What does `query()` return, and why does that matter?
- [x] A regular DataFrame, so you can chain another `query()` or any pandas method onto it
- [ ] A NumPy array that must be converted back to a DataFrame
- [ ] A boolean Series showing which rows matched
- [ ] The original DataFrame, modified in place

## 10_2 · SQLite Setup

### What makes SQLite convenient for learning SQL in a notebook?
- [x] It runs entirely inside the Python process — no server, no install beyond the standard library — and can live in memory via `:memory:`
- [ ] It requires a cloud account and an API key to use
- [ ] It only works with the Gapminder dataset
- [ ] It needs a separate database server process running

### How do you write a DataFrame into a table and read query results back as a DataFrame?
- [x] `df.to_sql("table", conn)` writes it; `pd.read_sql("SELECT ...", conn)` returns a DataFrame
- [ ] `df.to_database()` and `pd.from_sql()`
- [ ] `conn.write(df)` and `conn.read()`
- [ ] `df.save()` and `df.load()`

### What does `SELECT * FROM measurements` return, and what does `*` mean?
- [x] Every column of every row in the `measurements` table; `*` means "all columns"
- [ ] Only the first column; `*` means "first column only"
- [ ] A count of total rows; `*` means "count everything"
- [ ] The table's schema definition; `*` means "structure"

### What is the SQL equivalent of pandas `df.head(5)`?
- [x] Appending `LIMIT 5` to the query
- [ ] `SELECT TOP 5` is the only valid option in SQLite
- [ ] `HEAD 5` at the end of the query
- [ ] `FIRST 5 ROWS` at the end of the query

### How do you sort query results by `lifeExp` from highest to lowest?
- [x] `ORDER BY lifeExp DESC` (the pandas equivalent of `sort_values(..., ascending=False)`)
- [ ] `SORT lifeExp DOWN`
- [ ] `ORDER lifeExp DESCENDING`
- [ ] `GROUP BY lifeExp DESC`

### What does `SELECT DISTINCT year FROM measurements` do, and what is the `AS` keyword for?
- [x] `DISTINCT` returns each unique value once (like `unique()`); `AS` renames a column in the output
- [ ] `DISTINCT` counts rows; `AS` deletes a column from the result
- [ ] `DISTINCT` sorts the column; `AS` sums the column values
- [ ] Both are pandas-only keywords that don't exist in standard SQL

## 10_3 · WHERE

### What is the SQL `WHERE` equivalent of pandas `df.query("year == 2007")`, and what's the key syntax trap?
- [x] `WHERE year = 2007` — SQL uses a single `=` for equality, not `==`
- [ ] `WHERE year == 2007` — SQL requires `==` just like Python
- [ ] `FILTER year = 2007`
- [ ] `HAVING year = 2007`

### When mixing `AND` and `OR`, why are parentheses important, as in `WHERE year = 2007 AND (lifeExp > 80 OR lifeExp < 45)`?
- [x] SQL evaluates `AND` before `OR`, so without parentheses the grouping — and the result — would be different
- [ ] Parentheses are purely cosmetic and have no effect in SQL
- [ ] `OR` is evaluated before `AND`, so parentheses around `AND` are needed
- [ ] SQL ignores all parentheses in WHERE clauses

### What does `WHERE country IN ('Japan', 'China', 'India')` do?
- [x] Keeps rows where `country` matches any value in the list — cleaner than chaining several `OR` conditions
- [ ] Keeps rows where `country` equals the entire list as one value
- [ ] Excludes those three countries from the result
- [ ] Joins the three matching countries into a single combined row

### What does `WHERE year BETWEEN 1990 AND 2007` match?
- [x] Rows where `year` is in the inclusive range [1990, 2007] — shorthand for `year >= 1990 AND year <= 2007`
- [ ] Rows strictly between 1990 and 2007, with both endpoints excluded
- [ ] Only the exact years 1990 and 2007
- [ ] Rows that fall outside that year range

### In SQL's `LIKE`, what do the wildcards `%` and `_` match?
- [x] `%` matches any sequence of characters (including none); `_` matches exactly one character
- [ ] `%` matches exactly one character; `_` matches any sequence
- [ ] Both wildcards match exactly one digit character
- [ ] `%` is a literal percent sign and `_` is a literal underscore

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
- [ ] They always give the same number for any dataset
- [ ] `COUNT(*)` counts columns; `COUNT(DISTINCT)` counts rows
- [ ] `COUNT(DISTINCT)` counts only null values

### Why can't you put `AVG(gdpPercap) > 20000` in a `WHERE` clause?
- [x] `WHERE` is evaluated before grouping, so no aggregate exists yet — filtering on an aggregate must use `HAVING`
- [ ] `WHERE` cannot use the `>` comparison operator
- [ ] `AVG` is not a valid aggregate function in SQLite
- [ ] You must use `WHERE` for all conditions; `HAVING` does not exist in SQL

### What is the role of `HAVING` versus `WHERE`?
- [x] `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation
- [ ] `HAVING` filters individual rows; `WHERE` filters groups
- [ ] They are completely interchangeable in all contexts
- [ ] `HAVING` sorts the groups in the result

### How does SQL group by two keys, the equivalent of `groupby(["continent", "year"])`?
- [x] `GROUP BY continent, year` — one result row per unique combination
- [ ] `GROUP BY continent AND year`
- [ ] `GROUP BY continent THEN year`
- [ ] You can only group by one column at a time in SQL

## 10_5 · JOIN

### What does a SQL `JOIN ... ON` do?
- [x] Combines rows from two tables that share a matching value in the named key column
- [ ] Stacks two tables vertically, adding rows from the second below the first
- [ ] Renames columns across two tables to avoid name conflicts
- [ ] Sorts one table's rows using the other table's order

### What is the pandas equivalent of an `INNER JOIN`?
- [x] `measurements.merge(countries, on="country")` (i.e. `merge(how="inner")`)
- [ ] `pd.concat([measurements, countries])`
- [ ] `measurements.append(countries)`
- [ ] `measurements.join(countries, how="outer")`

### What does an `INNER JOIN` do with a row whose key has no match in the other table?
- [x] Drops it — only rows with a matching key in both tables survive (e.g. a fake "Narnia" row disappears)
- [ ] Keeps it and fills the other table's columns with `NULL`
- [ ] Raises an error when an unmatched row is encountered
- [ ] Duplicates it and flags it for review

### How does a `LEFT JOIN` differ from an `INNER JOIN`?
- [x] It keeps every row of the left table even with no match, filling the right table's columns with `NULL`
- [ ] It keeps only matching rows, exactly like an `INNER JOIN`
- [ ] It keeps every row of the right table instead of the left
- [ ] It removes the left table's unmatched rows from the result

### What is the purpose of table aliases like `FROM measurements AS m INNER JOIN countries AS c`?
- [x] They shorten the table names so column references (`m.country`, `c.continent`) are concise and unambiguous
- [ ] They rename the tables permanently inside the database
- [ ] They are required syntax or the JOIN will fail
- [ ] They sort the joined result by the aliased table name

### In `... INNER JOIN countries AS c ON m.country = c.country`, what does the `ON` clause specify?
- [x] The join condition — which column in each table holds the matching key
- [ ] The columns to return in the SELECT output
- [ ] The sort order of the joined result
- [ ] A row filter applied after the join is complete

## 10_6 · SQL vs pandas

### What is a subquery?
- [x] A `SELECT` nested inside another query; the inner query runs first and its result feeds the outer query
- [ ] A query that runs against a backup database
- [ ] A query that has no `FROM` clause
- [ ] Two queries connected with an `AND` keyword

### In `WHERE lifeExp > (SELECT AVG(lifeExp) FROM measurements WHERE year = 2007)`, what does the inner query contribute?
- [x] A single value (the global 2007 average) that the outer query compares each row against
- [ ] A list of countries to exclude from the outer query
- [ ] The columns to display in the outer query output
- [ ] The sort order for the outer query result

### A subquery can also feed an `IN` clause. What does that enable?
- [x] Filtering one query by a list of values computed from another query, without writing an explicit JOIN
- [ ] Joining three or more tables simultaneously
- [ ] Counting rows faster than a simple `COUNT(*)`
- [ ] Renaming columns in the output

### When is SQL the better tool than pandas?
- [x] When the data lives in a database and is too large to load entirely into memory — SQL filters/aggregates server-side
- [ ] When you need complex regex string parsing operations
- [ ] When you want to produce a seaborn visualization
- [ ] When the dataset has fewer than 100 rows

### When is pandas the better tool than SQL?
- [x] When the work needs complex string operations, regex, or multi-step text cleaning that SQL's `LIKE` can't express
- [ ] When the data is 50 million rows stored in a remote database
- [ ] When you only need a simple `GROUP BY` aggregation
- [ ] Whenever the data has a primary key defined

### What is the common two-step SQL-then-pandas workflow?
- [x] Use SQL to filter/aggregate a large dataset down to a small result, then use pandas for analysis and visualization
- [ ] Use pandas to load everything first, then re-import it into SQL
- [ ] Run the same query in both tools and compare the outputs
- [ ] Use SQL only for chart generation and plotting
