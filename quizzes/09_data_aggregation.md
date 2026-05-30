# 09 · Data Aggregation

## 09_1 · Meet Gapminder

### Gapminder has 142 countries and 12 years (1952–2007). Why does it have 1,704 rows?
- [x] It is **panel data** — each country appears once per year, so 142 × 12 = 1,704, uniquely identified by the `(country, year)` pair
- [ ] There are 1,704 countries
- [ ] Each country has a random number of rows
- [ ] 1,704 is the number of columns

### `gdpPercap` has a mean of about `$7,215` but a median of only about `$3,532`. What does that tell you?
- [x] The distribution is right-skewed — a handful of wealthy countries pull the mean well above the median
- [ ] The data has errors, since mean and median should match
- [ ] Most countries are wealthy
- [ ] GDP per capita is normally distributed

### Why is `df.groupby("continent")["lifeExp"].mean()` over all years called out as insufficient for the module's questions?
- [x] Collapsing to one number per continent throws away the time dimension and the within-continent variation the module wants to study
- [ ] It produces an error on panel data
- [ ] It is slower than computing it by hand
- [ ] It only works on a single country

### Why does the notebook flag Oceania's continent-level statistics as needing caution?
- [x] Oceania has only 2 countries (Australia and New Zealand), so its summaries don't represent a region the way the others do
- [ ] Oceania has the most countries, skewing the average
- [ ] Oceania has missing data for every year
- [ ] Oceania is not actually in the dataset

### What does each row of the Gapminder dataset represent?
- [x] One country in one year, with its life expectancy, population, and GDP per capita
- [ ] One continent's total for all years
- [ ] One year's global average
- [ ] One country across all years combined

### Why is aggregating across all countries without grouping described as producing statistics that "do not describe any country well"?
- [x] The columns span huge ranges and multiple distributions (e.g. bimodal life expectancy), so a single global number isn't representative of any group
- [ ] Aggregation always loses precision
- [ ] pandas cannot aggregate without a group
- [ ] The dataset is too small to summarize

## 09_2 · Multiple Keys & the MultiIndex

### What does passing a list of columns to `df.groupby(["continent", "year"])` create?
- [x] One group for every unique combination of the keys, with the result indexed by both keys (a MultiIndex)
- [ ] Two separate groupby results
- [ ] An error — groupby accepts only one column
- [ ] A group for continent only, ignoring year

### What is a MultiIndex?
- [x] A hierarchical index where each row is identified by a tuple of values across multiple levels (e.g. `(continent, year)`)
- [ ] A DataFrame with two copies of the index
- [ ] An index that has been sorted twice
- [ ] A list of column names

### How do you retrieve the value for `("Africa", 2007)` from a MultiIndex Series?
- [x] `result.loc[("Africa", 2007)]` — pass a tuple of the outer and inner level
- [ ] `result["Africa"]["2007"]` only
- [ ] `result.get("Africa 2007")`
- [ ] You must `reset_index()` first; tuple access is impossible

### What does `reset_index()` do to a grouped result with a MultiIndex?
- [x] Flattens the index levels into ordinary columns, giving one row per combination — convenient for merging, filtering, and plotting
- [ ] Deletes the grouping keys
- [ ] Re-runs the groupby
- [ ] Sorts the rows numerically

### What does `result.unstack("year")` produce from a `(continent, year)` MultiIndex Series?
- [x] A wide table with continents on the rows and years pivoted into columns
- [ ] A flat long table with a column per index level
- [ ] A single total across all years
- [ ] The same Series with a reset index

### How do you aggregate two columns at once, e.g. `groupby(["continent","year"])[["lifeExp","gdpPercap"]].mean()`?
- [x] Select a list of columns — the result is a DataFrame with one column per aggregated variable
- [ ] You cannot aggregate more than one column per groupby
- [ ] It returns a Series of tuples
- [ ] You must run two separate groupby calls and concatenate

## 09_3 · agg() in Depth

### Why is a single statistic like the mean often not enough to describe a group?
- [x] Two groups with the same mean can differ wildly in spread — you need std, min, max, etc. to see the full picture
- [ ] The mean is always wrong for grouped data
- [ ] pandas cannot compute a mean per group
- [ ] One statistic takes longer to compute than several

### What does `groupby("continent")["lifeExp"].agg(["mean", "median", "std", "min", "max"])` return?
- [x] A DataFrame with one row per continent and one column per requested function
- [ ] Five separate Series
- [ ] Only the first function's result
- [ ] A single combined number per group

### What is the named-aggregation syntax?
- [x] `agg(output_name=("source_column", "function"))` — names each output column and specifies its source column and function
- [ ] `agg("column", "function", "name")`
- [ ] `agg({name: column})` only
- [ ] `agg(function=column)` with no output name

### What is the difference between `size()` and `count()` on a groupby?
- [x] `size()` counts every row in the group (including nulls); `count()` counts only non-null values in a column
- [ ] They are identical in every dataset
- [ ] `size()` counts columns; `count()` counts rows
- [ ] `count()` includes nulls; `size()` excludes them

### Why use `groupby("continent")["country"].nunique()` instead of `count()` to find how many countries are in each continent?
- [x] `nunique()` counts distinct countries; `count()` would count rows (52 countries × 12 years = 624 for Africa), a different question
- [ ] `count()` does not work on string columns
- [ ] They give the same answer here
- [ ] `nunique()` is required before any groupby

### After a named aggregation, what kind of object do you get back?
- [x] A plain DataFrame you can sort, filter, or pass straight to a chart (after `reset_index()`)
- [ ] A MultiIndex Series that cannot be charted
- [ ] A dictionary of results
- [ ] A NumPy array

## 09_4 · transform()

### What does `transform()` do differently from `agg()` on a groupby?
- [x] It computes a group statistic and **broadcasts it back to every row** in the group, preserving the original DataFrame's shape
- [ ] It collapses each group to a single row, like agg
- [ ] It deletes the grouping column
- [ ] It sorts the rows by group

### `df2007.groupby("continent")["lifeExp"].mean()` returns 5 rows. What does the same groupby with `.transform("mean")` return?
- [x] 142 rows (one per country), where every country carries its continent's mean
- [ ] 5 rows, identical to agg
- [ ] 1 row with the global mean
- [ ] An error

### Why can you assign a `transform()` result directly as a new column with no merge?
- [x] It returns a Series aligned to the original index, so the values line up row-for-row automatically
- [ ] Because it sorts the DataFrame first
- [ ] Because transform drops the index
- [ ] You cannot — a merge is always required

### How would you build a column measuring each country's life expectancy relative to its continent's average?
- [x] Subtract the transformed group mean: `df["lifeExp"] - df.groupby("continent")["lifeExp"].transform("mean")`
- [ ] Use `agg("mean")` and subtract — the shapes align automatically
- [ ] Use `filter()` with a lambda
- [ ] It cannot be done in pandas

### Computing a within-group z-score needs the group mean and group standard deviation. How is that expressed?
- [x] `(value - groupby.transform("mean")) / groupby.transform("std")` — two transforms, both broadcast to every row
- [ ] `groupby.agg(["mean", "std"])` subtracted directly from the column
- [ ] A single `transform("zscore")` call
- [ ] `df.std()` divided by `df.mean()`

### Why is a within-group z-score more comparable across continents than a raw deviation in years?
- [x] It rescales each deviation by that group's own standard deviation, so a z-score of 2 means the same "distance from the mean" in every group
- [ ] It converts years into a percentage
- [ ] It removes outliers automatically
- [ ] Raw deviations are always negative

## 09_5 · filter()

### What does `groupby().filter()` do?
- [x] Applies a condition to each group as a whole and keeps **all rows** of the groups that pass (dropping every row of those that fail)
- [ ] Keeps individual rows that pass a row-level condition
- [ ] Removes columns that fail a condition
- [ ] Fills missing values per group

### Why is row-level boolean indexing the wrong tool for "keep continents whose median GDP exceeds 10,000"?
- [x] The condition is a property of the whole group, not of each row — boolean indexing would keep scattered individual rich countries instead of whole qualifying continents
- [ ] Boolean indexing cannot use a median
- [ ] It would keep entire continents but in the wrong order
- [ ] There is no difference; both give the same result

### What does the function passed to `filter(lambda g: ...)` receive and return?
- [x] It receives the sub-DataFrame for each group and must return a single boolean (keep or drop the whole group)
- [ ] It receives one row and returns a modified row
- [ ] It receives a column name and returns a list
- [ ] It receives the whole DataFrame and returns a number

### How do you keep only groups with at least 10 rows?
- [x] `groupby(...).filter(lambda g: len(g) >= 10)`
- [ ] `groupby(...).filter("size >= 10")`
- [ ] `groupby(...).count() >= 10`
- [ ] `df[df.size >= 10]`

### What is a common reason to filter out small groups before computing statistics?
- [x] Statistics like standard deviation are unreliable on very few observations (e.g. Oceania's 2 countries)
- [ ] Small groups always contain errors
- [ ] pandas refuses to aggregate groups under 10 rows
- [ ] Small groups slow the computation down

### What can you do with the result of `filter()`?
- [x] It is a plain DataFrame, so you can chain a `groupby().agg()` (filter-then-aggregate is the most common pattern)
- [ ] Nothing — filter results are read-only
- [ ] Only plot it, not aggregate it
- [ ] It must be converted back with `reset_index()` before any use

## 09_6 · pivot_table()

### What are the four core arguments of `pd.pivot_table()`?
- [x] `values=` (what to aggregate), `index=` (rows), `columns=` (columns), and `aggfunc=` (how to aggregate)
- [ ] `data=`, `x=`, `y=`, and `hue=`
- [ ] `rows=`, `cols=`, `sum=`, and `mean=`
- [ ] `on=`, `how=`, `left=`, and `right=`

### How does `pivot_table` relate to the `groupby(...).mean().unstack()` pattern from 09.2?
- [x] It produces the same wide table in a single call with explicit `index`/`columns`/`values` arguments, no MultiIndex/unstack step needed
- [ ] It produces a completely different result
- [ ] It only works on a single grouping dimension
- [ ] It is slower and always discouraged

### What does adding `columns="year"` to a pivot table do?
- [x] Creates a two-dimensional grid directly — e.g. continents on rows, years across columns
- [ ] Selects only the `year` column
- [ ] Sorts the table by year
- [ ] Raises an error unless `index` is also year

### What does `margins=True` add to a pivot table?
- [x] A grand-total row and column (labeled `All` by default) computed with the same aggregation function
- [ ] Extra whitespace around the table
- [ ] A confidence interval per cell
- [ ] The standard deviation of each row

### What is one capability `groupby().agg().unstack()` has that `pivot_table()` lacks?
- [x] Named aggregations — `pivot_table()` does not support the `name=("col","func")` syntax
- [ ] Grouping by more than one column
- [ ] Computing a mean
- [ ] Producing a wide table

### Why does a pivot table make a natural input to `sns.heatmap()`?
- [x] A pivot table is already a 2-D grid of numbers indexed by two categorical dimensions — exactly what a heatmap visualizes
- [ ] Because heatmaps require a MultiIndex Series
- [ ] Because pivot tables contain only one column
- [ ] They are unrelated; heatmaps need raw data
