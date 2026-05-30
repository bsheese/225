# 08 · Data Cleaning

## 08_1 · What Makes Data Messy

### The module organizes messiness into five categories. Which list matches them?
- [x] Wrong types, missing values, inconsistent formatting, structural problems, and date/time encoding
- [ ] Too many rows, too few rows, wrong filename, no header, and bad encoding
- [ ] Outliers, duplicates, typos, nulls, and slow loading
- [ ] Integers, floats, strings, booleans, and dates

### Why is `df.info()` recommended as the very first call on a new dataset?
- [x] In one output it shows row count, column names, non-null counts, and dtypes — enough to spot several problems at once
- [ ] It automatically fixes the column types
- [ ] It is the only way to view the data values
- [ ] It removes missing values and duplicates

### Why is storing `pclass` (passenger class 1/2/3) as `int64` a "wrong type" problem?
- [x] The numbers are labels, not measurements — averaging them gives a meaningless value like 2.3, with no warning
- [ ] `int64` columns cannot be displayed
- [ ] pandas refuses to group by integer columns
- [ ] Integers always use too much memory

### How does inconsistent formatting (e.g. `"female"`, `"Female"`, `" male "`) corrupt an analysis?
- [x] A `groupby` or `value_counts` splits logically identical values into separate groups, silently and with no error
- [ ] It raises a `ValueError` immediately on load
- [ ] It converts the column to numbers
- [ ] It deletes the affected rows

### What kind of problem does the `Name` column ("Mr. Owen Harris Braund") represent?
- [x] A structural problem — multiple distinct pieces (title, first name, last name) packed into one field
- [ ] A missing-value problem
- [ ] A wrong-type problem
- [ ] A duplicate-row problem

### Why are dates stored as strings a problem even when the values look correct?
- [x] String dates cannot be reliably sorted chronologically, filtered by range, or subtracted to find durations
- [ ] Strings take up no memory
- [ ] pandas converts them to numbers automatically
- [ ] String dates are always missing

## 08_2 · Missing Data

### What is the first diagnostic step before deciding how to handle missing values?
- [x] Measure how much is missing per column, e.g. `df.isnull().sum()` and the percentage of rows
- [ ] Immediately call `dropna()` to remove all gaps
- [ ] Fill every column with its mean
- [ ] Delete any column that has a single null

### What does a heatmap of `df.isnull().T` help you see?
- [x] **Where** the missing values are — whether they're scattered randomly or clustered (which can signal a data-source problem)
- [ ] The correlation between columns
- [ ] The mean of each column
- [ ] How many duplicate rows exist

### Why compare survival rates between rows with and without a recorded age?
- [x] To check whether the missingness is related to the outcome — if it is, dropping those rows would bias the analysis
- [ ] To count how many rows are missing
- [ ] To fill the missing ages with the survival rate
- [ ] To convert age to a category

### What does `df.dropna(thresh=5)` do on a 7-column DataFrame?
- [x] Keeps rows that have at least 5 non-null values, recovering rows that are mostly complete
- [ ] Drops the 5 columns with the most nulls
- [ ] Keeps only the first 5 rows
- [ ] Fills nulls with the value 5

### When is forward-fill (`ffill()`) or backward-fill (`bfill()`) an appropriate way to fill gaps?
- [x] When the data has a meaningful order (time series, sensor readings) so a neighboring value is a reasonable estimate
- [ ] Always — it is the best default for any column
- [ ] Only for string columns
- [ ] Only when more than half the values are missing

### How does `interpolate()` differ from forward-fill for a gradually changing numeric series?
- [x] It estimates gaps by fitting a line between the known values on either side, rather than carrying one constant forward
- [ ] It deletes the rows with gaps
- [ ] It fills gaps with the column mean
- [ ] It only works on datetime columns

## 08_3 · Type Problems

### A numeric column read as `object` because one row says `"unknown"` sorts incorrectly. What fixes it?
- [x] `pd.to_numeric(col, errors="coerce")`, which parses valid numbers and turns the rest into `NaN`
- [ ] `col.astype(int)`, which always succeeds
- [ ] `col.sort_values()`, which fixes the dtype
- [ ] Nothing — string sorting is fine

### Why use `errors="coerce"` with `pd.to_numeric()`?
- [x] It converts unparseable values to `NaN` instead of raising an error and stopping
- [ ] It rounds the numbers to integers
- [ ] It removes the entire column on any error
- [ ] It is required for every numeric column

### A `survived` column stored as `"yes"`/`"no"` can't be averaged. How do you fix it?
- [x] Map the labels to numbers, e.g. `col.map({"yes": 1, "no": 0})`
- [ ] Call `col.mean()` with `errors="ignore"`
- [ ] Sort the column alphabetically
- [ ] Cast it directly with `col.astype(float)`

### Why convert a categorical-but-integer column like `pclass` with `.astype("category")`?
- [x] It tells pandas the values are a fixed set of labels (so arithmetic isn't meaningful), makes intent explicit, and can save memory
- [ ] It lets you finally compute a meaningful average of the classes
- [ ] It is required before `groupby` will work
- [ ] It converts the labels into dates

### For a low-cardinality string column like `sex`, what is a benefit of the `category` dtype?
- [x] Big memory savings — pandas stores an integer code per row and maps it back to the string, instead of repeating the full string
- [ ] It makes every value unique
- [ ] It converts the strings to numbers for arithmetic
- [ ] It removes missing values

### Which tool converts a column of date strings into a proper `datetime64` dtype?
- [x] `pd.to_datetime()`
- [ ] `pd.to_numeric()`
- [ ] `col.astype("category")`
- [ ] `col.str.strip()`

## 08_4 · String Cleaning

### What does the `.str` accessor let you do?
- [x] Apply a string operation to every element of a Series at once, with no explicit loop
- [ ] Convert a string column to numbers
- [ ] Access a single character of the DataFrame
- [ ] Sort the strings alphabetically

### A `sex` column shows five values in `value_counts()` instead of two. What is usually the cause?
- [x] Inconsistent capitalization and stray whitespace making logically identical values look distinct
- [ ] The column has been converted to a category
- [ ] There are genuinely five sexes in the data
- [ ] `value_counts()` is broken on string columns

### Which chain normalizes hand-entered values like `" Female"`, `"MALE "`, `"female"` to a clean canonical form?
- [x] `col.str.strip().str.lower()`
- [ ] `col.str.title().str.split()`
- [ ] `col.strip().lower()` without `.str`
- [ ] `col.str.upper()` alone

### Why include `na=False` in `df["name"].str.contains("Mrs", na=False)`?
- [x] So null values evaluate to `False` instead of raising a `TypeError`
- [ ] It makes the search case-insensitive
- [ ] It fills nulls with the string "Mrs"
- [ ] It limits the search to the first row

### When would you use `.str.startswith()` instead of `.str.contains()`?
- [x] When you want to match only at the beginning of the string (e.g. a title or a prefix code), not anywhere inside it
- [ ] When the column contains numbers
- [ ] When you want to count characters
- [ ] When the pattern is a regular expression

### Why can you chain `.str` methods like `col.str.strip().str.lower().str.replace(...)`?
- [x] Each `.str` method returns a new Series, so the next call operates on the result, left to right
- [ ] Because pandas runs them in random order
- [ ] Because `.str` caches the original column
- [ ] You cannot — only one `.str` call is allowed per line

## 08_5 · Splitting & Extracting

### What does `df["name"].str.split(". ", expand=True)` return?
- [x] A DataFrame with separate columns for each piece, split at the period-space delimiter
- [ ] A single string with the delimiter removed
- [ ] A Series of lists that you cannot index
- [ ] The original column unchanged

### Why pass `n=1` to `str.split(". ", expand=True, n=1)`?
- [x] It limits the split to the first occurrence, so other periods (e.g. middle initials) don't break the string into extra pieces
- [ ] It returns only the first row
- [ ] It splits the string into exactly 1 piece
- [ ] It removes the first character

### After `str.split()` without `expand=True` you have a Series of lists. How do you pick the first element of each?
- [x] `.str.get(0)`
- [ ] `.str.first()`
- [ ] `[0]` on the whole Series
- [ ] `.str.split(0)`

### In `str.extract(r'(\w+)\.')`, what role do the parentheses play?
- [x] They form a **capture group** — `extract` returns only the text matched inside them, ignoring the rest of the pattern
- [ ] They are required syntax with no effect
- [ ] They make the match case-insensitive
- [ ] They escape the period

### What advantage do named capture groups `(?P<title>\w+)` give over numbered ones?
- [x] The resulting DataFrame columns get meaningful names automatically, instead of 0, 1, 2
- [ ] They run faster than numbered groups
- [ ] They allow more than one match per row
- [ ] They remove the need for a pattern

### What is the conceptual difference between `str.split()` and `str.extract()`?
- [x] `split` breaks at a delimiter and you take a piece by position; `extract` finds a pattern anywhere and returns the captured portion
- [ ] They are identical in every case
- [ ] `split` uses regex; `extract` never does
- [ ] `extract` only works on numbers

## 08_6 · Regular Expressions

### In a regex, what do `\d`, `\w`, and `\s` match?
- [x] Any digit, any word character (letter/digit/underscore), and any whitespace, respectively
- [ ] A literal `d`, `w`, and `s`
- [ ] The start, middle, and end of a string
- [ ] Three different date formats

### To strip every non-digit character from a phone number, which replacement works?
- [x] `col.str.replace(r'[^\d]', '', regex=True)` — `[^\d]` matches anything that is not a digit
- [ ] `col.str.replace(r'\d', '', regex=True)`
- [ ] `col.str.strip()`
- [ ] `col.str.replace(" ", "")` only

### Why does the validation pattern use anchors, as in `r'^\d{10}$'`?
- [x] `^` and `$` force the match to span the whole string, so only exactly ten digits qualify (not a 12-digit string containing ten)
- [ ] The anchors make the pattern case-insensitive
- [ ] They are decorative and optional
- [ ] `^` means "not", so it excludes digits

### To clean currency strings like `"$71.28"` before `pd.to_numeric()`, which pattern keeps the number intact?
- [x] `r'[^\d.]'` — remove any character that is not a digit or a period
- [ ] `r'[^\d]'` — which would also delete the decimal point
- [ ] `r'\$'` — which only removes the dollar sign
- [ ] `r'.'` — which matches everything

### What do the quantifiers `+`, `*`, and `?` mean in a regex?
- [x] One-or-more, zero-or-more, and zero-or-one of the preceding element, respectively
- [ ] Add, multiply, and question — arithmetic operators
- [ ] Exactly one, exactly two, exactly three
- [ ] Start, middle, and end anchors

### What do `case=False` and `na=False` do in `str.contains(pattern, regex=True, case=False, na=False)`?
- [x] Make the match case-insensitive and treat nulls as non-matching instead of erroring
- [ ] Convert the column to lowercase permanently and drop nulls
- [ ] Disable regex and disable matching
- [ ] Sort the results and remove duplicates

## 08_7 · Dates & Times

### Why is sorting a column of string dates unreliable?
- [x] Strings sort alphabetically, not chronologically — it only works for ISO `YYYY-MM-DD` format by coincidence
- [ ] String dates cannot be sorted at all
- [ ] Sorting strings always reverses the order
- [ ] pandas refuses to sort object columns

### How do you parse non-ISO dates like `"03/15/2023"` correctly?
- [x] `pd.to_datetime(col, format="%m/%d/%Y")`, giving the format codes for month, day, and year
- [ ] `col.astype("datetime64")` with no format
- [ ] `pd.to_numeric(col)`
- [ ] `col.str.split("/")` and stop there

### When a column mixes several date formats across rows, what helps?
- [x] `pd.to_datetime(col, format="mixed")`, which infers the format row by row (with some ambiguity risk)
- [ ] Dropping every row with a date
- [ ] `col.str.lower()`
- [ ] Nothing — mixed formats cannot be parsed

### Once a column is `datetime64`, how do you extract the month or weekday name?
- [x] The `.dt` accessor, e.g. `col.dt.month` and `col.dt.day_name()`
- [ ] The `.str` accessor, e.g. `col.str.month`
- [ ] `col.month()` directly
- [ ] You must re-parse the string each time

### What does subtracting two `datetime64` columns produce, and how do you get minutes from it?
- [x] A `timedelta64` column; convert with `.dt.total_seconds() / 60`
- [ ] A float column already in minutes
- [ ] An error — you cannot subtract dates
- [ ] A string showing the difference

### What do `.dt.floor("h")` and `.dt.round("h")` let you do?
- [x] Bucket timestamps to an hour boundary (truncating or rounding) so you can group by time window
- [ ] Convert the timestamp to a number of hours since 1970
- [ ] Remove the time portion entirely
- [ ] Round the fare column to the nearest hour

## 08_8 · A Complete Pipeline

### Why does the order of cleaning steps matter in a pipeline?
- [x] Steps depend on one another — e.g. you can't parse a date column you haven't loaded, or fill a null in a column you already dropped
- [ ] It doesn't — any order produces the same result
- [ ] Alphabetical order of steps is required
- [ ] Dropping must always come last

### How does `raw.nunique()` help diagnose a new dataset?
- [x] Columns with only one unique value carry no information and can be dropped — something `info()` alone wouldn't reveal
- [ ] It counts the missing values per column
- [ ] It lists the duplicate rows
- [ ] It converts columns to categories

### A column is missing 87% of its values. What is the pipeline's recommended action?
- [x] Drop it — a column empty for nearly nine of ten rows is almost never useful and its present rows may be unrepresentative
- [ ] Fill all the gaps with 0
- [ ] Forward-fill the entire column
- [ ] Keep it and ignore the missingness

### The pipeline leaves vehicle fields as `NaN` but drops the few rows missing geographic fields. Why the different treatment?
- [x] Missing vehicle details mean "not available" (inventing values would mislead), while the geographic gaps are tiny enough to drop without affecting the dataset
- [ ] Vehicle fields are numeric and geographic fields are strings
- [ ] It is an arbitrary choice with no reasoning
- [ ] Dropping is always preferred over leaving NaN

### What is the suggested final check that a dataset is truly clean?
- [x] Run the analysis you actually wanted to do (e.g. a groupby) and confirm it executes correctly on the cleaned data
- [ ] Re-read the raw CSV and compare byte counts
- [ ] Delete the cleaning code and start over
- [ ] Check that the file size shrank

### Why package the cleaning steps as a reusable function like `clean_311(raw)`?
- [x] It documents every decision in one place and lets you re-clean an updated dataset (or share it) in a single call
- [ ] Functions run faster than cells in all cases
- [ ] It is required for pandas to accept the changes
- [ ] It automatically uploads the data somewhere
