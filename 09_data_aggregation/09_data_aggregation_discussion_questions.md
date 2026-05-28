# 09 — Data Aggregation: Discussion Questions

## Meet Gapminder (09.1)
1. The global mean life expectancy across all 1,704 rows is about 59.5 years, but the mean for individual countries in 2007 alone is about 67 years. Why are these two numbers different? What does the gap reveal about the data's structure — and why would averaging all rows without grouping by year produce a number that does not accurately describe any real point in time?
2. The Gapminder dataset has 142 countries and 12 time points, giving exactly 1,704 rows. A student wants to find all countries that appear more or fewer than 12 times, suspecting data entry errors. Write out the pandas steps you would take (in plain English or pseudocode). What would it mean if a country appeared only 6 times?

## Multiple Groupby Keys (09.2)
3. `groupby(["continent", "year"])["lifeExp"].mean()` produces a MultiIndex Series. After calling `reset_index()`, you have a flat DataFrame with three columns: `continent`, `year`, and `lifeExp`. If you then called `groupby("continent")["lifeExp"].mean()` on that flat DataFrame, what would you get, and how does it differ from calling `groupby("continent")["lifeExp"].mean()` on the original full dataset?
4. `unstack("year")` puts years on the columns; `unstack("continent")` puts continents on the columns. For the specific question "which year saw the largest jump in Africa's life expectancy between consecutive observations?", which orientation is easier to work with? Why?

## `agg()` (09.3)
5. The named aggregation `agg(n_countries=("country", "nunique"))` counts distinct country names within each group. For the 2007 snapshot (one row per country), this equals `size()`. For the full dataset (12 rows per country), `nunique()` and `size()` give very different numbers. What does each one tell you, and which would you want when trying to find how many countries are in each continent?
6. `size()` counts every row including rows where data is missing; `count()` counts only non-null values in a specified column. Gapminder has no missing values, so they agree here. Construct a concrete scenario (a different dataset) where they would give different answers and where the difference would matter for an analysis.

## `transform()` (09.4)
7. `agg("mean")` returns one value per group (5 rows for 5 continents). `transform("mean")` returns one value per original row (142 rows for the 2007 snapshot). If you tried to compute `df["lifeExp"] - df.groupby("continent")["lifeExp"].agg("mean")`, pandas would not produce the result you want. Explain why, in terms of index alignment.
8. The within-continent z-score uses two `transform()` calls: one for the mean and one for the standard deviation. Suppose you wrote a single `transform()` with a custom lambda: `groupby("continent")["lifeExp"].transform(lambda g: (g - g.mean()) / g.std())`. Would this produce the same result? What is one advantage of the lambda approach and one advantage of the two-call approach?

## `filter()` (09.5)
9. `groupby("continent").filter(lambda g: g["gdpPercap"].median() > 10000)` keeps Europe and Oceania. A student instead writes `df[df.groupby("continent")["gdpPercap"].transform("median") > 10000]`. Would these produce identical results? If not, how would they differ?
10. `filter()` drops all rows from a group if the group fails the condition. Describe a real-world analysis scenario where this all-or-nothing behavior is exactly what you want, and a second scenario where dropping entire groups would be the wrong approach and row-level filtering would be better.

## `pivot_table()` (09.6)
11. `pd.pivot_table(df, values="lifeExp", index="continent", columns="year", aggfunc="mean")` and `df.groupby(["continent", "year"])["lifeExp"].mean().unstack("year")` produce tables with the same values. Identify one task where `pivot_table()` is more convenient and one task where the `groupby().unstack()` chain is more convenient.
12. The continent × year pivot table has an `All` margin row and column when `margins=True`. The bottom-right cell is the grand mean across all rows and all years. A student argues this cell is misleading because it weights every row equally rather than weighting by how many countries are in each continent and how large the population is. Is the student correct? What would you have to do differently to compute a country-count-weighted global mean?
