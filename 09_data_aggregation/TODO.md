# Module 09: Groupby and Aggregation in Depth

## Module goal

Build a thorough, systematic understanding of pandas groupby mechanics: splitting data into groups, aggregating with multiple functions simultaneously, transforming while preserving shape, filtering entire groups by condition, and reshaping results with `pivot_table()`. Visualizations and descriptive statistics appear throughout as tools to interpret the results — but the lesson is always about the groupby operation, not the chart or the statistic.

## Dataset: Gapminder

```python
import pandas as pd
url = "https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv"
df = pd.read_csv(url, sep="\t")
```

- **Shape:** 1,704 rows × 6 columns
- **Columns:** `country` (142 unique), `continent` (5 unique), `year` (12 values: 1952–2007 in 5-year steps), `lifeExp` (float), `pop` (int), `gdpPercap` (float)
- **No missing values.** No cleaning needed; load and go.
- **Structure:** panel data — every country appears once per year, so `(country, year)` is the unique key

The panel structure is load-bearing for the module. Many groupby examples become natural because the data has two grouping dimensions (continent and year) and three meaningful numerics to aggregate.

## What module 06 already covered (do not repeat)

- `groupby(col)[col].mean()` — single key, single function
- `value_counts()` — covered as a groupby alternative for counting
- `describe()` — summary statistics on a whole column
- `groupby()` as a setup step before a seaborn chart

Every notebook in this module should open with an explicit "you already know X from module 06; here we go further" framing.

## Scope exclusions

- `apply()` with custom functions — increasingly deprecated in favor of `agg()`; leave it out
- `resample()` — time-series specific; not in scope
- `pd.Grouper` — too advanced
- `groupby().cumsum()`, `cummax()` — cumulative operations; out of scope
- Teaching new visualization types or new statistical concepts — use seaborn and descriptives as tools only, do not introduce new chart families or statistical ideas

---

## Notebook plan

### 09.1 — Meet Gapminder

**Goal:** introduce the dataset, establish the analytical questions the module will answer, and give students a brief review of the single-key groupby they already know.

**Primary calls:** `pd.read_csv(url, sep="\t")`, `df.info()`, `df.describe()`, `groupby(col)[col].agg("mean")`, `value_counts()`

**Content:**
- Load the dataset and orient students: what does each row represent? What is a panel dataset? Why does every country appear 12 times?
- Quick scan: `df.info()`, `df.describe()`, `df["continent"].value_counts()`, `df["year"].unique()`
- A motivating question: "What is the average life expectancy in each continent in 2007?" Show this with a simple `groupby("continent")["lifeExp"].mean()` — one line they already know.
- Pose the questions this module will answer: What if we want multiple statistics at once? What if we want to group by continent AND year simultaneously? What if we want to add a group-level column back to the original DataFrame? Establish that the single-key groupby from module 06 cannot answer any of these.

---

### 09.2 — Multiple Groupby Keys and the MultiIndex

**Goal:** teach groupby with multiple keys, explain the MultiIndex that results, and show how to work with it (reset_index, unstack).

**Primary calls:** `groupby(["continent", "year"])`, `reset_index()`, `unstack("continent")`, `unstack("year")`

**Content:**
- Motivation: the single-key groupby from 09.1 answered "which continent has the highest life expectancy?" but not "how has each continent's life expectancy changed over time?" The second question requires two grouping keys.
- `groupby(["continent", "year"])["lifeExp"].mean()` — show the MultiIndex result and explain what it is: a hierarchical index where each row is identified by a (continent, year) pair.
- Reading a MultiIndex result: how to access a specific level with `.loc[]`.
- `reset_index()` — flatten the MultiIndex back to regular columns. Show before and after. This is the most common next step after a multi-key groupby.
- `unstack("continent")` — pivot one level of the index into columns, producing a year × continent table. Show that the same data can be viewed as long (MultiIndex) or wide (unstacked), and that neither is wrong — each is more convenient for different tasks.
- Visualization: a line chart (using the unstacked result) of life expectancy per continent over time. This is not a new chart type; it is the payoff for learning unstack.

---

### 09.3 — `agg()` in Depth

**Goal:** teach aggregating with multiple functions simultaneously and the named-aggregation syntax.

**Primary calls:** `agg(["mean", "median", "std", "min", "max"])`, `agg(name=("col", "func"))`, `agg` with different functions per column

**Content:**
- Motivation: `groupby("continent")["lifeExp"].mean()` gives one number per continent. But the mean alone hides whether a continent is homogeneous or spread out. You want mean, median, std, and count in one table.
- `groupby("continent")["lifeExp"].agg(["mean", "median", "std", "min", "max"])` — show the multi-column result.
- The **named-aggregation syntax** (pandas 3.0 style): `agg(avg_life=("lifeExp", "mean"), total_pop=("pop", "sum"), n_countries=("country", "nunique"))`. Emphasize that this is the preferred form when you want to aggregate multiple source columns and control the output column names.
- Aggregating different columns with different functions in the same call.
- `nunique()` as an aggregation function — useful for counting distinct values within a group (e.g., how many countries are in each continent?).
- `size()` vs `count()` — the difference between counting rows and counting non-null values within a group.
- Visualization: a bar chart of mean GDP per capita by continent using the aggregated result — show that the aggregated DataFrame is a regular DataFrame and can be charted the same way as any other.

---

### 09.4 — `transform()`: Group-Level Columns

**Goal:** teach transform(), contrasting it sharply with agg() to make the distinction clear.

**Primary calls:** `groupby(col)[col].transform("mean")`, `groupby(col)[col].transform("median")`, arithmetic on transformed columns

**Content:**
- Motivation: `agg()` reduces a group of rows to one row. But sometimes you want to add information about the group back to every row. If you want to ask "how does this country compare to its continent's average?", you need the continent mean aligned to the same rows as the original DataFrame — not a separate summary table.
- The core distinction: `agg()` returns one row per group; `transform()` returns one value per original row, with the group result broadcast to every row in that group. Show both side by side on the same groupby so the difference is concrete.
- `df["continent_avg_life"] = df.groupby("continent")["lifeExp"].transform("mean")` — show the result: every row in Asia has the same Asia mean, every row in Europe has the same Europe mean, etc.
- A derived column: `df["life_vs_continent"] = df["lifeExp"] - df["continent_avg_life"]` — "how far above or below its continent average is each country?" This is a question that requires transform and cannot be answered with agg alone.
- Within-group standardization (z-score): `(df["lifeExp"] - transform("mean")) / transform("std")` — normalize each country relative to its continent peers. This is the standard pattern for making variables comparable across groups with different baselines.
- Visualization: a histogram of `life_vs_continent` — most countries cluster near zero; the outliers are the story.
- Practical example: find the country that is furthest above its continent average in 2007. This demonstrates why the derived column is useful beyond just understanding the transform concept.

---

### 09.5 — `filter()`: Keeping Groups by Condition

**Goal:** teach groupby filter(), contrasting it with boolean row-level indexing to show when filter is the right tool.

**Primary calls:** `groupby(col).filter(lambda g: condition)`, chaining filter with agg

**Content:**
- Motivation: boolean indexing (`df[df["gdpPercap"] > 5000]`) filters individual rows. But sometimes the question is about an entire group: "keep only continents where the median 2007 GDP per capita exceeds a threshold." A row-level filter cannot express this because the condition is computed across the whole group, not row by row.
- `groupby("continent").filter(lambda g: g["gdpPercap"].median() > 5000)` — the lambda receives a sub-DataFrame for each group and must return a boolean scalar. If True, the entire group is kept; if False, it is dropped entirely.
- Show the result: all rows for dropped continents are gone, not just the rows that individually failed the condition.
- Contrast with row-level indexing: apply the analogous row-level filter and show that it produces a different (and for this question, wrong) answer. Make the distinction concrete.
- A practical chain: `filter()` to narrow down to continents of interest, then `groupby().agg()` to summarize — filter is a setup step, not an endpoint.
- The `lambda g:` pattern: note that `g` is a full sub-DataFrame. Students can call `g["col"].mean()`, `len(g)`, `g["col"].max()`, etc. inside the lambda.
- Example: find all continents that had at least one country with life expectancy above 75 in every year since 1982.

---

### 09.6 — `pivot_table()`: A Different Interface

**Goal:** teach pivot_table() as an alternative to groupby().unstack(), and show when each form is more convenient.

**Primary calls:** `pd.pivot_table(df, values=, index=, columns=, aggfunc=)`, `margins=True`, `fill_value=`

**Content:**
- Motivation: the multi-key groupby followed by unstack() from 09.2 produces a wide table, but the syntax requires two steps and the column naming is automatic. `pivot_table()` produces the same wide table in one call with more control over layout and with optional row/column totals.
- Simplest call: `pd.pivot_table(df2007, values="lifeExp", index="continent", aggfunc="mean")` — one aggregation, one grouping dimension. Show that this is identical to `groupby("continent")["lifeExp"].mean()` but produces a DataFrame with a named index.
- Add a second dimension: `pd.pivot_table(df, values="lifeExp", index="continent", columns="year", aggfunc="mean")` — the continent × year grid of mean life expectancy. Compare this to the `groupby(["continent","year"]).mean().unstack("year")` from 09.2 and show they are equivalent.
- `aggfunc=` accepts a list: `aggfunc=["mean", "std"]` produces a multi-level column header.
- `margins=True` — adds a grand total row and column. Useful for frequency tables where you want row and column sums.
- `fill_value=` — replaces NaN in the result when a combination has no data. Use `fill_value=0` for count/frequency tables.
- When to use pivot_table vs. groupby().unstack(): pivot_table is more concise when you are working directly toward a wide table and want margins. groupby().agg() then unstack is better when you need a named-aggregation step first.
- Visualization: a heatmap of the continent × year pivot table using the technique from module 07.6 — the result is a natural fit for a heatmap.

---

### 09.7 — Exercises

**Goal:** practice all module tools.

**Structure:** same as 07.9 and 08.9 — markdown question, blank `# your code here` cell, hidden solution cell with `#@title Solution` and `"cellView": "form"` metadata.

**Exercises to cover:**

1. Load the Gapminder dataset. Using `value_counts()`, confirm that each country appears exactly 12 times. Then show how many countries are in each continent.
2. Compute the mean, median, and standard deviation of `lifeExp` for each continent in 2007. Return as a single DataFrame.
3. Using named aggregations, produce a table that shows for each continent: average life expectancy, total population, and number of distinct countries. Filter to the year 2007 first.
4. Using a multi-key groupby on `["continent", "year"]`, compute the mean GDP per capita. Then `unstack("year")` and show the result as a wide table.
5. Find the 5 countries with the highest life expectancy in 2007.
6. Find the 5 countries with the lowest GDP per capita in 2007.
7. Using `transform()`, add a column `continent_avg_gdp` that holds the continent-level mean GDP per capita for each row (computed across all years). Do not filter to a single year — use all rows.
8. Using the column from exercise 7, find the country in each continent that was furthest above its continent average GDP in 2007.
9. Using `transform()`, compute a within-continent z-score for `lifeExp` (for each row: subtract the continent mean and divide by the continent std). Store in a new column `life_zscore`. Which country had the highest z-score in 2007?
10. Using `filter()`, keep only continents where every country had a life expectancy above 50 in every year from 1977 onward. How many rows remain?
11. Using `filter()`, find all continents where the mean GDP per capita in 2007 exceeded 10,000. Then compute the average population for those continents across all years.
12. Using `pivot_table()`, build a continent × year table of mean life expectancy. Add `margins=True` to show overall means. Display the result.
13. Create a heatmap (using `sns.heatmap()`) of the pivot table from exercise 12. Use an appropriate sequential colormap.
14. (Challenge) For each continent, identify which country experienced the largest increase in life expectancy between 1952 and 2007. Return a DataFrame with one row per continent showing the country name and the gain in years.

---

## Writing and pedagogy reminders

- Read `writing_sample.md` before writing any prose.
- No em-dashes anywhere.
- Every notebook opens with the Colab badge cell (before title, before everything).
- Every code cell is preceded by a markdown cell that earns it.
- Every output is interpreted in prose immediately after.
- Show what the limited tool cannot do first, then introduce the new one as the fix.
- Introduce each function at its minimum; add one parameter per subsequent example.
- Close each notebook with a bridge to the next.
- Visualizations and descriptive statistics are tools, not lessons. Do not explain why a heatmap works or what standard deviation means — students already know. Use them and move on.
