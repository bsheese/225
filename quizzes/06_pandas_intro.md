# 06 · Pandas Intro

## 06_1 · Series

### What problem does a pandas Series solve that two parallel Python lists do not?
- [x] Values stay permanently paired with their index labels through any sort or filter
- [ ] It uses less memory per element than an equivalent Python list
- [ ] It allows values of several different types in one column
- [ ] It automatically detects and removes any duplicate values on creation

### When you extract a column with `ages = df["age"]`, what is the index of the resulting Series?
- [x] An automatically generated 0-based `RangeIndex` of row numbers
- [ ] The passenger name column from the parent DataFrame
- [ ] A second copy of the age values, mirrored from the original column
- [ ] Nothing — a Series has no index until you assign one

### `s.loc[5]` and `s.iloc[5]` return the same row when the index is `0, 1, 2, …`. When do they start to diverge?
- [x] After filtering or sorting, when index labels no longer match positions
- [ ] Never — both `.loc[]` and `.iloc[]` are completely interchangeable
- [ ] Only when the Series contains missing or null values in the data
- [ ] Only for Series that contain more than 1,000 elements

### How do `s.loc[0:4]` and `s.iloc[0:4]` differ when slicing?
- [x] `.loc[]` includes the end label, giving five rows; `.iloc[]` excludes it, giving four
- [ ] Both include the end label by convention, returning five rows total
- [ ] Both exclude the end position by default, returning only four rows
- [ ] `.loc[]` excludes the end label; `.iloc[]` includes the end position instead

### What does the vectorized expression `fares * 1.27` do?
- [x] Multiplies every element and returns a new Series, with no explicit loop
- [ ] Multiplies only the first element of the Series by 1.27
- [ ] Raises an error because a Series cannot be multiplied by a number
- [ ] Modifies the `fares` Series in place and returns `None`

### In `ages[ages < 18]`, what is the expression `ages < 18` by itself?
- [x] A boolean Series of `True`/`False` values, one per element
- [ ] A single `True` or `False` describing the whole Series
- [ ] A Python list containing only the ages that are below 18
- [ ] The total count of passengers whose age is under 18

### Which expression correctly keeps passengers between 18 and 60 inclusive?
- [x] `ages[(ages >= 18) & (ages <= 60)]`
- [ ] `ages[ages >= 18 and ages <= 60]`
- [ ] `ages[ages >= 18 & ages <= 60]`
- [ ] `ages[18 <= ages <= 60]`

### The `name` column holds strings like `"Mr. Owen Harris Braund"`. Which tool extracts the title (`Mr.`) from every row at once?
- [x] The `.str` accessor, e.g. `names.str.extract(r'^(\w+\.)')`
- [ ] A `for` loop over `names`, manually slicing each string one at a time
- [ ] `names.extract('title')`
- [ ] `names.split('.')` applied to the entire Series object directly

## 06_2 · DataFrame Basics

### How is a DataFrame related to a Series?
- [x] A DataFrame is a collection of Series columns that all share the same row index
- [ ] A DataFrame is a single Series with more than one value stored per row
- [ ] A DataFrame and a Series are completely unrelated data structures
- [ ] A Series is built by stacking several DataFrames vertically

### What does `df.shape` return for the Titanic data?
- [x] A tuple `(rows, columns)` — here `(887, 8)`
- [ ] The number of rows only, as a single integer
- [ ] A list of the column names in order
- [ ] The total number of cells (rows × columns)

### `df.dtypes` shows `survived` and `pclass` as `int64`. Why does the notebook flag this as something to fix later?
- [x] They represent categories (0/1 and 1/2/3), not magnitudes — pandas treats them as plain integers until told otherwise
- [ ] `int64` columns cannot be used in filtering operations
- [ ] pandas cannot group by any integer column
- [ ] `int64` uses more memory than any other available dtype

### Why is `df.info()` recommended as your standard first call on a new dataset?
- [x] It combines shape, column names, dtypes, and non-null counts — missing data shows up immediately
- [ ] It deletes any rows that contain missing values automatically
- [ ] It is the only way to view the first few rows of data
- [ ] It converts every column to its correct data type automatically

### What is the difference between `df["age"]` and `df[["age"]]`?
- [x] `df["age"]` returns a Series; `df[["age"]]` (a list of names) returns a one-column DataFrame
- [ ] They are identical — the extra brackets are silently ignored
- [ ] `df["age"]` returns a DataFrame; `df[["age"]]` returns a Series
- [ ] `df[["age"]]` raises a syntax error in current pandas

### `df["has_family"] = (df["sibsp"] > 0) | (df["parch"] > 0)` is an example of what?
- [x] Feature engineering — deriving a new column from existing ones
- [ ] Filtering rows by a boolean condition
- [ ] Dropping an unwanted column from the DataFrame
- [ ] Renaming an existing column to a new label

### After `df_trimmed = df.drop(columns=["has_family"])`, why does `df` still contain `has_family`?
- [x] `.drop()` returns a new DataFrame and leaves the original unchanged; assign the result back to make it permanent
- [ ] `.drop()` only hides the column temporarily until the next cell
- [ ] `has_family` cannot be dropped because it was computed from other columns
- [ ] You must call `.drop()` twice before the change takes effect

### In `df.describe()`, the `survived` column has a mean of about 0.38. What does that mean represent?
- [x] The proportion of passengers who survived — the mean of a 0/1 column equals the survival rate
- [ ] The average passenger ID number in the dataset
- [ ] The number of survivors divided by the number of columns
- [ ] A meaningless value, since you cannot average a categorical variable

## 06_3 · Selecting & Filtering

### What is the core difference between `.loc[]` and `.iloc[]`?
- [x] `.loc[]` selects by index label; `.iloc[]` selects by integer position (0-based)
- [ ] `.loc[]` selects rows only; `.iloc[]` selects columns only
- [ ] `.loc[]` is for Series; `.iloc[]` is only for DataFrames
- [ ] `.loc[]` always returns a copy; `.iloc[]` always returns a view

### What does `df.loc[0:5]` return compared with `df.iloc[0:5]`?
- [x] `.loc[0:5]` includes label 5 (six rows); `.iloc[0:5]` stops before position 5 (five rows)
- [ ] Both return exactly five rows in all cases
- [ ] Both return exactly six rows in all cases
- [ ] `.loc[0:5]` returns five rows; `.iloc[0:5]` returns six rows

### How do you keep only the rows where `survived` equals 1?
- [x] `df.loc[df["survived"] == 1]` — pass a boolean mask to `.loc[]`
- [ ] `df.loc[survived = 1]`
- [ ] `df[survived == 1]` without referencing `df` inside the brackets
- [ ] `df.filter("survived == 1")`

### Why must each condition be parenthesized in `df.loc[(df["pclass"] == 1) & (df["survived"] == 1)]`?
- [x] `&` binds more tightly than `==`, so without parentheses pandas evaluates the wrong thing
- [ ] Parentheses are only a style preference and change nothing here
- [ ] `&` requires exactly one space on each side, supplied by the parentheses
- [ ] Without them pandas treats the conditions as literal column names

### What is the cleanest way to keep rows whose `pclass` is 1 or 2?
- [x] `df.loc[df["pclass"].isin([1, 2])]`
- [ ] `df.loc[df["pclass"] == [1, 2]]`
- [ ] `df.loc[df["pclass"] = 1 or 2]`
- [ ] `df.loc[df["pclass"].contains(1, 2)]`

### What does the `~` operator do in `df.loc[~(df["survived"] == 1)]`?
- [x] It negates the boolean mask — keeping rows where the condition is `False`
- [ ] It sorts the result in reverse alphabetical order
- [ ] It selects only the last row that matches the condition
- [ ] It drops the `survived` column from the result

### Which statement about `.query()` is correct?
- [x] It accepts a plain-string condition like `df.query("pclass == 1 and age > 40")`, but struggles with column names containing spaces
- [ ] It is always faster and more flexible than a boolean mask approach
- [ ] It permanently modifies the DataFrame it is called on
- [ ] It cannot combine more than one condition at a time

### After filtering, why call `.copy()` as in `survivors = df[df["survived"] == 1].copy()` before adding a column?
- [x] It makes the result an independent DataFrame so modifying it cannot affect the original
- [ ] It makes the filtering operation run faster
- [ ] It is required or the filter returns `None`
- [ ] It permanently deletes the filtered-out rows from `df`

## 06_4 · Data Cleaning

### What is the standard first step for finding missing data, and what does it return?
- [x] `df.isnull().sum()` — the count of missing (`NaN`) values in each column
- [ ] `df.dropna()` — returns the rows that contain missing values
- [ ] `df.missing()` — returns a list of columns that have missing values
- [ ] `df.describe()` — returns the percentage of missing values per column

### What does a plain `df.dropna()` do, and how does `subset=` change it?
- [x] It drops any row with a `NaN` in *any* column; `subset=["age"]` drops only rows missing in `age`
- [ ] It drops only fully empty rows; `subset=` has no effect on the behavior
- [ ] It fills missing values with a default; `subset=` chooses the fill value
- [ ] It drops columns rather than rows; `subset=` selects which columns to drop

### Why is the **median** often preferred over the mean when filling a missing numeric column like `age`?
- [x] The median is more robust to outliers and skew than the mean
- [ ] The median is always a whole number, making it easier to store
- [ ] `.fillna()` cannot accept a mean value as its argument
- [ ] The mean cannot be computed when any missing values are present

### When filling missing values for a model, why compute the fill statistic from the **training set only**?
- [x] Computing it from the full dataset leaks test-set information into training, a subtle but real bug
- [ ] The test set has no missing values that need to be filled
- [ ] Training-set medians are faster to compute than full-dataset medians
- [ ] pandas requires the training and test fill values to be different

### How do you find and remove exact duplicate rows?
- [x] `df.duplicated().sum()` counts them; `df.drop_duplicates()` removes them, keeping the first occurrence
- [ ] `df.unique()` removes duplicate rows automatically
- [ ] `df.dropna()` removes duplicate rows as well as missing values
- [ ] `df.duplicated(drop=True)` both finds and deletes them in one call

### Why convert `survived`, `pclass`, and `sex` with `.astype("category")`?
- [x] They hold a small set of distinct labels, not quantities — `category` reflects their meaning and saves memory
- [ ] It converts them into numbers so they can be averaged
- [ ] It is required before you can group by those columns
- [ ] It removes any missing values present in those columns

### A numeric column loaded as text contains a stray `"unknown"`. What does `pd.to_numeric(col, errors="coerce")` do?
- [x] Converts valid strings to numbers and turns unparseable values like `"unknown"` into `NaN` instead of crashing
- [ ] Deletes every row that contains any non-numeric value
- [ ] Raises an error on the first bad value it encounters
- [ ] Replaces the string `"unknown"` with the integer 0

### A hand-entered `sex` column contains `"  Male"`, `"female"`, `"MALE"`, `"Female "`. Which chain normalizes them to two clean values?
- [x] `col.str.strip().str.lower()`
- [ ] `col.str.upper().str.split()`
- [ ] `col.strip().lower()` (without `.str`)
- [ ] `col.replace("MALE", "male")` alone

## 06_5 · GroupBy

### What three steps make up the split–apply–combine pattern behind GroupBy?
- [x] Split the rows into groups by a key, apply a function within each group, combine the results
- [ ] Sort the data by key, apply a filter condition, then plot the result
- [ ] Split each column in half, apply a join operation, combine the halves back
- [ ] Sample the data randomly, apply a model, combine the predictions

### Which call answers "what was the survival rate for each sex?"
- [x] `df.groupby("sex")["survived"].mean()`
- [ ] `df.groupby("survived")["sex"].mean()`
- [ ] `df.groupby("sex").mean("survived")["rate"]`
- [ ] `df["sex"].groupby("survived").count()`

### Why does taking `.mean()` of the 0/1 `survived` column within each group give a survival *rate*?
- [x] The mean of a column of 0s and 1s equals the proportion of 1s, i.e. the fraction who survived
- [ ] `.mean()` is specially defined to compute rate statistics
- [ ] pandas rescales 0/1 columns to percentages automatically on groupby
- [ ] It only works because the column happens to be named `survived`

### How do you get several summaries per group at once, e.g. count, mean, min, and max of `fare`?
- [x] `df.groupby("pclass")["fare"].agg(["count", "mean", "min", "max"])`
- [ ] `df.groupby("pclass")["fare"].describe(["count", "mean"])`
- [ ] `df.groupby("pclass").fare.count().mean().min().max()`
- [ ] You must run four separate `.groupby()` calls and join them

### What do named aggregations like `df.groupby("pclass").agg(avg_fare=("fare", "mean"))` give you?
- [x] Output columns with names you choose, each defined as a `(column, function)` pair
- [ ] A faster but unlabeled version of the standard `.agg()` call
- [ ] A plot of the aggregation result
- [ ] The same result as `.describe()` with different column names

### What does grouping by two keys, `df.groupby(["pclass", "sex"])["survived"].mean()`, produce?
- [x] A survival rate for every class-and-sex combination
- [ ] An error — groupby only accepts a single column at a time
- [ ] The survival rate for `pclass` only, ignoring `sex`
- [ ] Two separate DataFrames, one per grouping key

### After `df.groupby("pclass")["survived"].mean()`, `pclass` is the index. What does `.reset_index()` do?
- [x] Promotes `pclass` back to a regular column, so you can sort, rename, or filter the result
- [ ] Deletes the `pclass` values from the result
- [ ] Re-runs the groupby operation from scratch
- [ ] Renumbers the rows but removes the survival rate values

## 06_6 · Pivot Tables & Crosstabs

### What question does `pd.crosstab(df["sex"], df["survived"])` answer?
- [x] How many passengers fall into each combination of sex and survival (a count table)
- [ ] What was the average fare paid by each sex group
- [ ] What is the Pearson correlation between sex and survival
- [ ] Which rows have both sex and survived missing

### In `pd.crosstab(df["sex"], df["survived"], normalize="index")`, what does `normalize="index"` make each row do?
- [x] Each row sums to 1, answering "of all people of this sex, what fraction survived?"
- [ ] Each column sums to 1, answering "of all survivors, what fraction were this sex?"
- [ ] The whole table sums to 1 across every individual cell
- [ ] Nothing changes — raw counts are still displayed

### What does adding `margins=True` to a crosstab or pivot table do?
- [x] Adds row and column totals (an `All` line) alongside the per-group values
- [ ] Removes any group that has too few observations
- [ ] Normalizes the table to show proportions instead of counts
- [ ] Sorts the table by its margin totals

### When would you reach for `pd.pivot_table()` instead of `pd.crosstab()`?
- [x] When you want any aggregation (e.g. mean fare) of a numeric column displayed as a 2-D grid, not just counts
- [ ] When you only need raw counts of two categorical columns
- [ ] When the data has missing values that need to be handled
- [ ] When you want a single summary number rather than a table

### Which statement about `.corr()` and the values it returns is correct?
- [x] Pearson correlation ranges from −1 to +1 and measures linear association — it does not establish causation
- [ ] Correlation ranges from 0 to 100 and proves one variable causes the other
- [ ] A correlation of 0 means the two columns are identical
- [ ] `.corr()` only works on a single column at a time

### The notebook finds `fare` and `survived` correlate at about +0.26, but warns this is "entangled." Why?
- [x] First-class passengers both paid more and survived more, so fare is largely a proxy for class — correlation is not causation
- [ ] A correlation of +0.26 is mathematically impossible and signals a calculation bug
- [ ] The fare directly caused the survival, which the notebook confirms
- [ ] The two columns have different numbers of non-null rows

### Which methods quickly surface the extremes, e.g. the eight highest fares or the eight youngest passengers?
- [x] `df.nlargest(8, "fare")` and `df.nsmallest(8, "age")`
- [ ] `df.max(8)` and `df.min(8)`
- [ ] `df.sort_values().head(8)` is the only correct option
- [ ] `df.top(8, "fare")` and `df.bottom(8, "age")`
