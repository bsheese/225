# 10 — pandas and SQL: Discussion Questions

## `df.query()` (10.1)
1. `df.query("lifeExp > 70 and continent == 'Asia'")` and `df[(df["lifeExp"] > 70) & (df["continent"] == "Asia")]` produce the same result. Give a specific example of a filter condition that `query()` cannot express but boolean indexing can. Then give an example of a condition where `query()` is clearly more readable. What property of a condition tips the balance toward each approach?
2. The `@variable` injection syntax lets you write `df.query("lifeExp > @median_life")` where `median_life` was computed earlier. Why is this feature important? What would go wrong if you tried to embed a computed value directly into the query string by formatting it as a Python f-string, like `df.query(f"lifeExp > {median_life}")`? (Hint: think about what happens if the value is a float with many decimal places, or if the string contains a column name by coincidence.)

## SQLite Setup and SELECT (10.2)
3. The `to_sql()` call uses `if_exists="replace"`. If you changed this to `if_exists="append"` and ran the setup cell twice, what would happen to the database? What would `SELECT COUNT(*) FROM measurements` return after the second run, and why?
4. `SELECT DISTINCT year FROM measurements ORDER BY year` returns 12 rows. `SELECT year FROM measurements ORDER BY year` would return 1,704 rows. Why do both queries work without raising an error, even though `year` is not in `GROUP BY`? What is `DISTINCT` actually doing that makes the column reference valid here?

## `WHERE` (10.3)
5. The notebook shows that `AND` takes precedence over `OR` in SQL, just as multiplication takes precedence over addition in arithmetic. Predict the result of this query without running it: `WHERE year = 2007 AND lifeExp > 80 OR lifeExp < 45`. Because `AND` binds tighter than `OR`, which rows actually come back, and why is that almost certainly not what the author intended? Write the version with explicit parentheses that returns only 2007 rows whose life expectancy is either above 80 or below 45.
6. `LIKE '%land'` matches countries ending in "land." What would `LIKE '_land'` match, and how is `_` different from `%`? Name a character-matching scenario where `_` would be more useful than `%`. Why is `LIKE` not sufficient for matching all country names that contain a two-to-four letter suffix?

## `GROUP BY` and `HAVING` (10.4)
7. The rule "every column in SELECT that is not aggregated must appear in GROUP BY" feels strict. Why does SQL enforce this? Construct a specific example where violating this rule would produce ambiguous or meaningless results (that is, a query where the output would be non-deterministic if the rule were relaxed).
8. `WHERE` filters rows before aggregation; `HAVING` filters groups after aggregation. Could you always rewrite a `HAVING` clause as a `WHERE` clause by adding a subquery? Write out what the `HAVING AVG(lifeExp) > 75` condition from notebook 10.4 would look like if rewritten using a `WHERE` clause and a subquery. What is the practical cost of that approach compared to using `HAVING`?

## `JOIN` (10.5)
9. The Narnia example adds a row to `measurements` with no matching `countries` entry, and demonstrates that `INNER JOIN` drops it while `LEFT JOIN` preserves it with a `NULL` continent. Exercise 11 adds a row to `countries` with no matching `measurements` entry, and does a `LEFT JOIN` from `countries` to catch the NULL. Why does the direction of the join (which table is on the left) matter? What would you get if you wrote `FROM measurements LEFT JOIN countries` instead of `FROM countries LEFT JOIN measurements` in exercise 11?
10. The `ON` clause specifies `m.country = c.country`. What would happen if you accidentally wrote `ON m.country = m.country` (joining a table to itself)? What would happen if you omitted the `ON` clause entirely? Which of those two mistakes would produce an error, and which would silently produce a surprising (and very large) result?

## SQL vs pandas (10.6)
11. The notebook states that SQL is better when "the data lives in a database and is too large to load entirely into memory." Give a concrete example of an analysis task on a 500-million-row database table where this advantage matters. Then give a concrete example of an analysis task on that same table where you would prefer to pull a sample into pandas and work there, even though SQL could technically do the computation.
12. The two-step workflow in 10.6 has SQL do the aggregation (1,704 rows to 60) and pandas do the visualization and derived columns. Could the gain-since-1952 calculation in the pandas step be done in SQL? Sketch what that SQL query would look like (you can use pseudocode). What makes the pandas version easier to write and debug, even if the SQL version is theoretically possible?
