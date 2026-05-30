# 09 · Data Aggregation

## 09_1 · Meet Gapminder

### Gapminder has 142 countries and 12 years (1952–2007). Why does it have 1,704 rows?
- [x] It is **panel data** — each country appears once per year, so 142 × 12 = 1,704, uniquely identified by `(country, year)`
- [ ] There are 1,704 distinct countries in the dataset
- [ ] Each country has a different random number of year rows
- [ ] 1,704 is the number of columns in the raw data

### `gdpPercap` has a mean of about `$7,215` but a median of only about `$3,532`. What does that tell you?
- [x] The distribution is right-skewed — a handful of wealthy countries pull the mean well above the median
- [ ] The data contains errors, since the mean and median should match
- [ ] Most countries in the dataset are wealthy
- [ ] GDP per capita follows a normal distribution

### Why is `df.groupby("continent")["lifeExp"].mean()` over all years called out as insufficient for the module's questions?
- [x] Collapsing to one number per continent discards the time dimension and within-continent variation the module wants to study
- [ ] It produces an error when run on panel data
- [ ] It is slower than computing the statistic manually
- [ ] It only operates on a single country at a time

### Why does the notebook flag Oceania's continent-level statistics as needing caution?
- [x] Oceania has only 2 countries (Australia and New Zealand), so its summaries don't represent a region the way others do
- [ ] Oceania has the most countries, which skews the continental average
- [ ] Oceania has missing data for every year in the dataset
- [ ] Oceania is not actually included in the dataset

### What does each row of the Gapminder dataset represent?
- [x] One country in one year, with its life expectancy, population, and GDP per capita
- [ ] One continent's total aggregated across all years
- [ ] One year's global average across all countries
- [ ] One country's values combined across all years

### Why is aggregating across all countries without grouping described as producing statistics that "do not describe any country well"?
- [x] The columns span huge ranges and multiple distributions (e.g. bimodal life expectancy), so a single global number isn't representative of any group
- [ ] Aggregation always loses numeric precision
- [ ] pandas cannot aggregate data without a grouping key
- [ ] The dataset is too small to compute meaningful summaries

## 09_2 · Multiple Keys & the MultiIndex

### What does passing a list of columns to `df.groupby(["continent", "year"])` create?
- [x] One group for every unique combination of the keys, with the result indexed by both keys (a MultiIndex)
- [ ] Two separate groupby results, one per key
- [ ] An error — groupby only accepts a single column name
- [ ] A group for continent only, ignoring the year key

### What is a MultiIndex?
- [x] A hierarchical index where each row is identified by a tuple of values across multiple levels (e.g. `(continent, year)`)
- [ ] A DataFrame that stores two separate copies of the index
- [ ] An index that has been sorted twice in different directions
- [ ] A plain list of all column names in the DataFrame

### How do you retrieve the value for `("Africa", 2007)` from a MultiIndex Series?
- [x] `result.loc[("Africa", 2007)]` — pass a tuple of the outer and inner level
- [ ] `result["Africa"]["2007"]` only, with string conversion
- [ ] `result.get("Africa 2007")` as a combined key
- [ ] You must call `reset_index()` first; tuple access is not supported

### What does `reset_index()` do to a grouped result with a MultiIndex?
- [x] Flattens the index levels into ordinary columns, giving one row per combination — convenient for merging, filtering, and plotting
- [ ] Deletes all grouping key values from the result
- [ ] Re-runs the groupby operation from scratch
- [ ] Sorts the rows numerically by the first index level

### What does `result.unstack("year")` produce from a `(continent, year)` MultiIndex Series?
- [x] A wide table with continents on the rows and years pivoted into columns
- [ ] A flat long table with a separate column per index level
- [ ] A single total value aggregated across all years
- [ ] The same Series with only a reset integer index

### How do you aggregate two columns at once, e.g. `groupby(["continent","year"])[["lifeExp","gdpPercap"]].mean()`?
- [x] Select a list of columns — the result is a DataFrame with one column per aggregated variable
- [ ] You cannot aggregate more than one column per groupby call
- [ ] It returns a Series of tuples, one per group
- [ ] You must run two separate groupby calls and concatenate the results

## 09_3 · agg() in Depth

### Why is a single statistic like the mean often not enough to describe a group?
- [x] Two groups with the same mean can differ wildly in spread — you need std, min, max, etc. to see the full picture
- [ ] The mean is always the wrong choice for grouped data
- [ ] pandas cannot compute a mean within a group
- [ ] Computing one statistic takes longer than computing several

### What does `groupby("continent")["lifeExp"].agg(["mean", "median", "std", "min", "max"])` return?
- [x] A DataFrame with one row per continent and one column per requested function
- [ ] Five separate Series objects, one per function
- [ ] Only the first function's result as a Series
- [ ] A single combined summary number per group

### What is the named-aggregation syntax?
- [x] `agg(output_name=("source_column", "function"))` — names each output column and specifies its source column and function
- [ ] `agg("column", "function", "name")` as three positional arguments
- [ ] `agg({name: column})` with a dictionary mapping names to columns
- [ ] `agg(function=column)` with no output name specified

### What is the difference between `size()` and `count()` on a groupby?
- [x] `size()` counts every row in the group including nulls; `count()` counts only non-null values in a column
- [ ] They are identical for any dataset without missing values
- [ ] `size()` counts columns; `count()` counts rows
- [ ] `count()` includes nulls; `size()` excludes them

### Why use `groupby("continent")["country"].nunique()` instead of `count()` to find how many countries are in each continent?
- [x] `nunique()` counts distinct countries; `count()` would count rows (12 years × n countries), a different question
- [ ] `count()` does not work on string-typed columns
- [ ] They give the same answer for this particular dataset
- [ ] `nunique()` is required before any groupby operation

### After a named aggregation, what kind of object do you get back?
- [x] A plain DataFrame you can sort, filter, or pass straight to a chart (after `reset_index()`)
- [ ] A MultiIndex Series that cannot be passed to a chart
- [ ] A Python dictionary of per-group results
- [ ] A NumPy array with no column names

## 09_4 · transform()

### What does `transform()` do differently from `agg()` on a groupby?
- [x] It computes a group statistic and **broadcasts it back to every row** in the group, preserving the original DataFrame's shape
- [ ] It collapses each group down to a single summary row, like `agg`
- [ ] It deletes the grouping column from the result
- [ ] It sorts all rows by their group assignment

### `df2007.groupby("continent")["lifeExp"].mean()` returns 5 rows. What does the same groupby with `.transform("mean")` return?
- [x] 142 rows (one per country), where every country carries its continent's mean
- [ ] 5 rows, identical to the `agg` result
- [ ] 1 row containing the global mean
- [ ] An error — transform cannot accept string function names

### Why can you assign a `transform()` result directly as a new column with no merge?
- [x] It returns a Series aligned to the original index, so the values line up row-for-row automatically
- [ ] Because transform sorts the DataFrame before returning
- [ ] Because transform drops the index to enable alignment
- [ ] You cannot — a merge is always required to add the result

### How would you build a column measuring each country's life expectancy relative to its continent's average?
- [x] Subtract the transformed group mean: `df["lifeExp"] - df.groupby("continent")["lifeExp"].transform("mean")`
- [ ] Use `agg("mean")` and subtract — the shapes align automatically
- [ ] Use `filter()` with a lambda expression
- [ ] This cannot be done in a single pandas operation

### Computing a within-group z-score needs the group mean and group standard deviation. How is that expressed?
- [x] `(value - groupby.transform("mean")) / groupby.transform("std")` — two transforms, both broadcast to every row
- [ ] `groupby.agg(["mean", "std"])` subtracted directly from the column
- [ ] A single `transform("zscore")` call
- [ ] `df.std()` divided by `df.mean()` on the full DataFrame

### Why is a within-group z-score more comparable across continents than a raw deviation in years?
- [x] It rescales each deviation by that group's own standard deviation, so a z-score of 2 means the same "distance from the mean" in every group
- [ ] It converts years into a percentage value
- [ ] It automatically removes outliers from each group
- [ ] Raw deviations are always negative by mathematical definition

## 09_5 · filter()

### What does `groupby().filter()` do?
- [x] Applies a condition to each group as a whole and keeps **all rows** of groups that pass (dropping every row of groups that fail)
- [ ] Keeps individual rows that pass a row-level boolean condition
- [ ] Removes columns that fail a specified condition
- [ ] Fills missing values per group based on a condition

### Why is row-level boolean indexing the wrong tool for "keep continents whose median GDP exceeds 10,000"?
- [x] The condition is a property of the whole group, not of each row — boolean indexing would keep scattered individual rich countries instead of whole qualifying continents
- [ ] Boolean indexing cannot use a median in its condition
- [ ] It would keep entire continents but in the wrong row order
- [ ] There is no difference; both approaches give the same result

### What does the function passed to `filter(lambda g: ...)` receive and return?
- [x] It receives the sub-DataFrame for each group and must return a single boolean (keep or drop the whole group)
- [ ] It receives one individual row and returns a modified version of it
- [ ] It receives a column name string and returns a filtered list
- [ ] It receives the whole DataFrame and returns a summary number

### How do you keep only groups with at least 10 rows?
- [x] `groupby(...).filter(lambda g: len(g) >= 10)`
- [ ] `groupby(...).filter("size >= 10")`
- [ ] `groupby(...).count() >= 10`
- [ ] `df[df.size >= 10]`

### What is a common reason to filter out small groups before computing statistics?
- [x] Statistics like standard deviation are unreliable on very few observations (e.g. Oceania's 2 countries)
- [ ] Small groups in pandas always contain data entry errors
- [ ] pandas refuses to aggregate any group with fewer than 10 rows
- [ ] Small groups slow down the computation significantly

### What can you do with the result of `filter()`?
- [x] It is a plain DataFrame, so you can chain a `groupby().agg()` (filter-then-aggregate is the most common pattern)
- [ ] Nothing — filter results are read-only and cannot be chained
- [ ] Only plot it; further aggregation is not possible
- [ ] It must be converted back with `reset_index()` before any use

## 09_6 · pivot_table()

### What are the four core arguments of `pd.pivot_table()`?
- [x] `values=` (what to aggregate), `index=` (rows), `columns=` (columns), and `aggfunc=` (how to aggregate)
- [ ] `data=`, `x=`, `y=`, and `hue=`
- [ ] `rows=`, `cols=`, `sum=`, and `mean=`
- [ ] `on=`, `how=`, `left=`, and `right=`

### How does `pivot_table` relate to the `groupby(...).mean().unstack()` pattern from 09.2?
- [x] It produces the same wide table in a single call with explicit `index`/`columns`/`values` arguments, no MultiIndex/unstack step needed
- [ ] It produces a completely different result than groupby/unstack
- [ ] It only works on a single grouping dimension
- [ ] It is slower and always discouraged in modern pandas

### What does adding `columns="year"` to a pivot table do?
- [x] Creates a two-dimensional grid — e.g. continents on rows, years across columns
- [ ] Selects only the `year` column for display
- [ ] Sorts the entire table by the year values
- [ ] Raises an error unless `index` is also set to `year`

### What does `margins=True` add to a pivot table?
- [x] A grand-total row and column (labeled `All` by default) computed with the same aggregation function
- [ ] Extra whitespace margin around the displayed table
- [ ] A confidence interval for each individual cell
- [ ] The standard deviation of values in each row

### What is one capability `groupby().agg().unstack()` has that `pivot_table()` lacks?
- [x] Named aggregations — `pivot_table()` does not support the `name=("col","func")` syntax
- [ ] Grouping by more than one column simultaneously
- [ ] Computing a mean across groups
- [ ] Producing a wide table layout

### Why does a pivot table make a natural input to `sns.heatmap()`?
- [x] A pivot table is already a 2-D grid of numbers indexed by two categorical dimensions — exactly what a heatmap visualizes
- [ ] Because heatmaps require a MultiIndex Series as input
- [ ] Because pivot tables always contain exactly one column
- [ ] They are unrelated; heatmaps require raw unaggregated data
