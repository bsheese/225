# 09 — Data Aggregation: Glossary

**`agg()`** — A groupby method that applies one or more aggregation functions to each group and returns all results in one DataFrame. Accepts a list of function names (`["mean", "std"]`) or the named-aggregation syntax.

**broadcast** — The behavior of `transform()`: a group-level statistic is computed once per group, then copied to every row in that group so the result has the same shape as the original DataFrame.

**`filter()`** — A groupby method that applies a boolean function to each group and keeps all rows from groups where the function returns `True`. Used to remove entire groups by a condition computed across the whole group, not row by row.

**long format** — A table layout where each row is one observation and grouping variables are regular columns. The output of `reset_index()` on a MultiIndex result. Most seaborn charts expect long format.

**margins** — Row and column totals added to a pivot table with `margins=True`. Each margin cell uses the same aggregation function as the rest of the table.

**MultiIndex** — A hierarchical pandas index where each row is identified by a combination of values from two or more levels. Produced by `groupby([col1, col2])`. Flattened to a regular index with `reset_index()`.

**named aggregation** — The syntax for controlling output column names inside `agg()`: `agg(output_name=("source_column", "function"))`. Allows aggregating multiple source columns with different functions in one call.

**panel data** — A dataset where the same units are observed at multiple time points. Each row is identified by a `(unit, time)` pair. Gapminder is panel data: 142 countries × 12 years = 1,704 rows.

**pivot table** — A two-dimensional aggregation where one variable goes on the rows, another on the columns, and a summary statistic fills each cell. Produced by `pd.pivot_table()` or by `groupby().mean().unstack()`.

**`transform()`** — A groupby method that computes a group statistic and returns a Series aligned to the original DataFrame's index, with one value per original row. Used to add group-level information back to every row without a separate merge.

**`unstack()`** — A pandas method that pivots one level of a MultiIndex into columns, converting a long-format result into a wide-format table.

**wide format** — A table layout where groups appear as rows and a second variable (often time) appears as columns. Produced by `unstack()` or `pivot_table()`. More compact for reading across time; less convenient for seaborn.

**within-group z-score** — A deviation standardized by the group's own mean and standard deviation: `(value - group_mean) / group_std`. Allows comparing how extreme a value is within its group regardless of the group's absolute scale.
