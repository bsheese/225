# 06 · Pandas Intro

## 06_1 · Series

### What problem does a pandas Series solve that two parallel Python lists do not?
- [x] Each value stays permanently paired with its index label, so sorting or filtering never silently desyncs the data
- [ ] It uses far less memory than a Python list
- [ ] It allows values of several different types in one column
- [ ] It automatically removes duplicate values

### When you extract a column with `ages = df["age"]`, what is the index of the resulting Series?
- [x] An automatically generated 0-based `RangeIndex` of row numbers
- [ ] The passenger names
- [ ] A second copy of the age values
- [ ] Nothing — a Series has no index until you assign one

### `s.loc[5]` and `s.iloc[5]` return the same row when the index is `0, 1, 2, …`. When do they start to diverge?
- [x] After filtering or sorting, once the index labels no longer line up with positions
- [ ] Never — `.loc[]` and `.iloc[]` are interchangeable
- [ ] Only when the Series contains missing values
- [ ] Only for Series with more than 1,000 rows

### How do `s.loc[0:4]` and `s.iloc[0:4]` differ when slicing?
- [x] `.loc[]` includes the end label (rows 0–4, five rows); `.iloc[]` excludes the end position (four rows)
- [ ] Both include the end label, returning five rows
- [ ] Both exclude the end, returning four rows
- [ ] `.loc[]` excludes the end; `.iloc[]` includes it

### What does the vectorized expression `fares * 1.27` do?
- [x] Applies the multiplication to every element and returns a new Series, with no explicit loop
- [ ] Multiplies only the first element by 1.27
- [ ] Raises an error because a Series cannot be multiplied by a number
- [ ] Modifies `fares` in place and returns `None`

### In `ages[ages < 18]`, what is the expression `ages < 18` by itself?
- [x] A boolean Series of `True`/`False` values, one per element
- [ ] A single `True` or `False` describing the whole Series
- [ ] A list containing only the ages below 18
- [ ] The number of passengers under 18

### Which expression correctly keeps passengers between 18 and 60 inclusive?
- [x] `ages[(ages >= 18) & (ages <= 60)]`
- [ ] `ages[ages >= 18 and ages <= 60]`
- [ ] `ages[ages >= 18 & ages <= 60]`
- [ ] `ages[18 <= ages <= 60]`

### The `name` column holds strings like `"Mr. Owen Harris Braund"`. Which tool extracts the title (`Mr.`) from every row at once?
- [x] The `.str` accessor, e.g. `names.str.extract(r'^(\w+\.)')`
- [ ] A `for` loop over `names`, slicing each string
- [ ] `names.extract('title')`
- [ ] `names.split('.')` applied to the Series directly

## 06_2 · DataFrame Basics

### How is a DataFrame related to a Series?
- [x] A DataFrame is a collection of Series columns that all share the same row index
- [ ] A DataFrame is a single Series with more than one value per row
- [ ] A DataFrame and a Series are unrelated structures
- [ ] A Series is built by stacking several DataFrames

### What does `df.shape` return for the Titanic data?
- [x] A tuple `(rows, columns)` — here `(887, 8)`
- [ ] The number of rows only
- [ ] A list of the column names
- [ ] The total number of cells (rows × columns)

### `df.dtypes` shows `survived` and `pclass` as `int64`. Why does the notebook flag this as something to fix later?
- [x] They represent categories (0/1 and 1/2/3), not magnitudes — pandas treats them as plain integers until you tell it otherwise
- [ ] `int64` columns cannot be filtered
- [ ] pandas cannot group by integer columns
- [ ] `int64` uses more memory than any other type

### Why is `df.info()` recommended as your standard first call on a new dataset?
- [x] It combines shape, column names, dtypes, and non-null counts — so missing data shows up immediately
- [ ] It deletes any rows that contain missing values
- [ ] It is the only way to see the first few rows
- [ ] It converts every column to its correct type automatically

### What is the difference between `df["age"]` and `df[["age"]]`?
- [x] `df["age"]` returns a Series; `df[["age"]]` (a list of names) returns a one-column DataFrame
- [ ] They are identical — the extra brackets are ignored
- [ ] `df["age"]` returns a DataFrame; `df[["age"]]` returns a Series
- [ ] `df[["age"]]` raises a syntax error

### `df["has_family"] = (df["sibsp"] > 0) | (df["parch"] > 0)` is an example of what?
- [x] Feature engineering — deriving a new column from existing ones
- [ ] Filtering rows by a condition
- [ ] Dropping a column from the DataFrame
- [ ] Renaming an existing column

### After `df_trimmed = df.drop(columns=["has_family"])`, why does `df` still contain `has_family`?
- [x] `.drop()` returns a new DataFrame and leaves the original unchanged; you must assign the result back to make it permanent
- [ ] `.drop()` only hides columns temporarily
- [ ] `has_family` cannot be dropped because it was computed
- [ ] You must call `.drop()` twice for it to take effect

### In `df.describe()`, the `survived` column has a mean of about 0.38. What does that mean represent?
- [x] The proportion of passengers who survived — because the column is 0/1, the mean equals the survival rate
- [ ] The average passenger ID number
- [ ] The number of survivors divided by the number of columns
- [ ] A meaningless value, since you cannot average a category

## 06_3 · Selecting & Filtering

### What is the core difference between `.loc[]` and `.iloc[]`?
- [x] `.loc[]` selects by index label; `.iloc[]` selects by integer position (0-based)
- [ ] `.loc[]` selects rows; `.iloc[]` selects columns
- [ ] `.loc[]` is for Series; `.iloc[]` is for DataFrames
- [ ] `.loc[]` returns a copy; `.iloc[]` returns a view

### What does `df.loc[0:5]` return compared with `df.iloc[0:5]`?
- [x] `.loc[0:5]` includes label 5 (six rows); `.iloc[0:5]` stops before position 5 (five rows)
- [ ] Both return exactly five rows
- [ ] Both return exactly six rows
- [ ] `.loc[0:5]` returns five rows; `.iloc[0:5]` returns six

### How do you keep only the rows where `survived` equals 1?
- [x] `df.loc[df["survived"] == 1]` — pass a boolean mask to `.loc[]`
- [ ] `df.loc[survived = 1]`
- [ ] `df[survived == 1]` without referencing `df` inside the brackets
- [ ] `df.filter("survived == 1")`

### Why must each condition be parenthesized in `df.loc[(df["pclass"] == 1) & (df["survived"] == 1)]`?
- [x] `&` binds more tightly than `==`, so without parentheses pandas evaluates the wrong thing
- [ ] Parentheses are only a style preference and change nothing
- [ ] `&` requires exactly one space on each side, supplied by the parentheses
- [ ] Without them pandas treats the conditions as column names

### What is the cleanest way to keep rows whose `pclass` is 1 or 2?
- [x] `df.loc[df["pclass"].isin([1, 2])]`
- [ ] `df.loc[df["pclass"] == [1, 2]]`
- [ ] `df.loc[df["pclass"] = 1 or 2]`
- [ ] `df.loc[df["pclass"].contains(1, 2)]`

### What does the `~` operator do in `df.loc[~(df["survived"] == 1)]`?
- [x] It negates the boolean mask — keeping rows where the condition is `False`
- [ ] It sorts the result in reverse order
- [ ] It selects the last matching row
- [ ] It drops the `survived` column

### Which statement about `.query()` is correct?
- [x] It accepts a plain-string condition like `df.query("pclass == 1 and age > 40")`, but struggles with column names containing spaces
- [ ] It is always faster and more flexible than a boolean mask
- [ ] It permanently modifies the DataFrame it is called on
- [ ] It cannot combine more than one condition

### After filtering, why call `.copy()` as in `survivors = df[df["survived"] == 1].copy()` before adding a column?
- [x] It makes the result an independent DataFrame, so modifying it can never affect the original and the intent is explicit
- [ ] It makes the filter run faster
- [ ] It is required or the filter returns `None`
- [ ] It permanently deletes the filtered-out rows from `df`

## 06_4 · Data Cleaning

### What is the standard first step for finding missing data, and what does it return?
- [x] `df.isnull().sum()` — the count of missing (`NaN`) values in each column
- [ ] `df.dropna()` — the rows that are missing values
- [ ] `df.missing()` — a list of missing columns
- [ ] `df.describe()` — the percentage of missing values

### What does a plain `df.dropna()` do, and how does `subset=` change it?
- [x] It drops any row with a `NaN` in *any* column; `subset=["age"]` drops only rows missing in `age`
- [ ] It drops only fully empty rows; `subset=` has no effect
- [ ] It fills missing values; `subset=` chooses the fill value
- [ ] It drops columns rather than rows; `subset=` selects which columns

### Why is the **median** often preferred over the mean when filling a missing numeric column like `age`?
- [x] The median is more robust to outliers and skew than the mean
- [ ] The median is always a whole number
- [ ] `.fillna()` cannot accept a mean
- [ ] The mean cannot be computed when values are missing

### When filling missing values for a model, why compute the fill statistic from the **training set only**?
- [x] Computing it from the full dataset leaks test-set information into training, a subtle but real bug
- [ ] The test set has no missing values to worry about
- [ ] Training-set medians are faster to compute
- [ ] pandas requires the training and test fills to be different

### How do you find and remove exact duplicate rows?
- [x] `df.duplicated().sum()` counts them; `df.drop_duplicates()` removes them, keeping the first occurrence
- [ ] `df.unique()` removes them automatically
- [ ] `df.dropna()` removes duplicates as well as missing values
- [ ] `df.duplicated(drop=True)` both finds and deletes them

### Why convert `survived`, `pclass`, and `sex` with `.astype("category")`?
- [x] They hold a small set of distinct labels, not quantities — `category` reflects their meaning and is more memory-efficient
- [ ] It converts them into numbers so they can be averaged
- [ ] It is required before you can group by them
- [ ] It removes any missing values in those columns

### A numeric column loaded as text contains a stray `"unknown"`. What does `pd.to_numeric(col, errors="coerce")` do?
- [x] Converts valid strings to numbers and turns unparseable values like `"unknown"` into `NaN` instead of crashing
- [ ] Deletes every row that contains a non-numeric value
- [ ] Raises an error on the first bad value
- [ ] Replaces `"unknown"` with 0

### A hand-entered `sex` column contains `"  Male"`, `"female"`, `"MALE"`, `"Female "`. Which chain normalizes them to two clean values?
- [x] `col.str.strip().str.lower()`
- [ ] `col.str.upper().str.split()`
- [ ] `col.strip().lower()` (without `.str`)
- [ ] `col.replace("MALE", "male")` alone

## 06_5 · GroupBy

### What three steps make up the split–apply–combine pattern behind GroupBy?
- [x] Split the rows into groups by a key, apply a function within each group, combine the per-group results into one output
- [ ] Sort the data, apply a filter, then plot the result
- [ ] Split each column in half, apply a join, combine the halves
- [ ] Sample the data, apply a model, combine the predictions

### Which call answers "what was the survival rate for each sex?"
- [x] `df.groupby("sex")["survived"].mean()`
- [ ] `df.groupby("survived")["sex"].mean()`
- [ ] `df.groupby("sex").mean("survived")["rate"]`
- [ ] `df["sex"].groupby("survived").count()`

### Why does taking `.mean()` of the 0/1 `survived` column within each group give a survival *rate*?
- [x] The mean of a column of 0s and 1s equals the proportion of 1s, i.e. the fraction who survived
- [ ] `.mean()` is specially defined to compute rates
- [ ] pandas rescales 0/1 columns to percentages automatically
- [ ] It only works because the column is named `survived`

### How do you get several summaries per group at once, e.g. count, mean, min, and max of `fare`?
- [x] `df.groupby("pclass")["fare"].agg(["count", "mean", "min", "max"])`
- [ ] `df.groupby("pclass")["fare"].describe(["count", "mean"])`
- [ ] `df.groupby("pclass").fare.count().mean().min().max()`
- [ ] You must run four separate `.groupby()` calls and join them

### What do named aggregations like `df.groupby("pclass").agg(avg_fare=("fare", "mean"))` give you?
- [x] Output columns with names you choose, each defined as a `(column, function)` pair
- [ ] A faster but unnamed version of `.agg()`
- [ ] A plot of the aggregation
- [ ] The same result as `.describe()`

### What does grouping by two keys, `df.groupby(["pclass", "sex"])["survived"].mean()`, produce?
- [x] A survival rate for every class-and-sex combination
- [ ] An error — you can only group by one column
- [ ] The survival rate for `pclass` only, ignoring `sex`
- [ ] Two separate DataFrames, one per key

### After `df.groupby("pclass")["survived"].mean()`, `pclass` is the index. What does `.reset_index()` do?
- [x] Promotes `pclass` back to a regular column, so you can sort, rename, or filter the result
- [ ] Deletes the `pclass` values
- [ ] Re-runs the groupby from scratch
- [ ] Renumbers the rows but removes the survival rates

## 06_6 · Pivot Tables & Crosstabs

### What question does `pd.crosstab(df["sex"], df["survived"])` answer?
- [x] How many passengers fall into each combination of sex and survival (a count table)
- [ ] What was the average fare for each sex
- [ ] What is the correlation between sex and survival
- [ ] Which rows have both sex and survived missing

### In `pd.crosstab(df["sex"], df["survived"], normalize="index")`, what does `normalize="index"` make each row do?
- [x] Each row sums to 1, answering "of all people of this sex, what fraction survived?"
- [ ] Each column sums to 1, answering "of all survivors, what fraction were this sex?"
- [ ] The whole table sums to 1 across every cell
- [ ] Nothing changes; raw counts are still shown

### What does adding `margins=True` to a crosstab or pivot table do?
- [x] Adds row and column totals (an `All`/overall line) alongside the per-group values
- [ ] Removes any group with too few observations
- [ ] Normalizes the table to proportions
- [ ] Sorts the table by its margins

### When would you reach for `pd.pivot_table()` instead of `pd.crosstab()`?
- [x] When you want any aggregation (e.g. mean fare) of a numeric column displayed as a 2-D grid, not just counts or proportions
- [ ] When you only need raw counts of two categories
- [ ] When the data has missing values
- [ ] When you want a single number rather than a table

### Which statement about `.corr()` and the values it returns is correct?
- [x] Pearson correlation ranges from −1 to +1 and measures linear association — it does not establish causation
- [ ] Correlation ranges from 0 to 100 and proves one variable causes the other
- [ ] A correlation of 0 means the two columns are identical
- [ ] `.corr()` only works on a single column at a time

### The notebook finds `fare` and `survived` correlate at about +0.26, but warns this is "entangled." Why?
- [x] First-class passengers both paid more and survived more, so fare is largely standing in for class — correlation is not causation
- [ ] A correlation of +0.26 is mathematically impossible and signals a bug
- [ ] Fare directly caused survival, which the warning confirms
- [ ] The two columns have different numbers of rows

### Which methods quickly surface the extremes, e.g. the eight highest fares or the eight youngest passengers?
- [x] `df.nlargest(8, "fare")` and `df.nsmallest(8, "age")`
- [ ] `df.max(8)` and `df.min(8)`
- [ ] `df.sort_values().head(8)` is the only option
- [ ] `df.top(8, "fare")` and `df.bottom(8, "age")`
