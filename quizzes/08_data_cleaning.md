# 08 · Data Cleaning

## 08_1 · What Makes Data Messy

### The module organizes messiness into five categories. Which list matches them?
- [x] Wrong types, missing values, inconsistent formatting, structural problems, and date/time encoding
- [ ] Too many rows, too few rows, wrong filename, no header, and bad encoding
- [ ] Outliers, duplicates, typos, nulls, and slow loading
- [ ] Integers, floats, strings, booleans, and dates

### Why is `df.info()` recommended as the very first call on a new dataset?
- [x] In one output it shows row count, column names, non-null counts, and dtypes — enough to spot several problems at once
- [ ] It automatically fixes all the column type problems
- [ ] It is the only way to view the actual data values
- [ ] It removes missing values and duplicate rows automatically

### Why is storing `pclass` (passenger class 1/2/3) as `int64` a "wrong type" problem?
- [x] The numbers are labels, not measurements — averaging them gives a meaningless value like 2.3, with no warning
- [ ] `int64` columns cannot be displayed in the notebook output
- [ ] pandas refuses to group by any integer-typed column
- [ ] Integer columns consume more memory than any other dtype

### How does inconsistent formatting (e.g. `"female"`, `"Female"`, `" male "`) corrupt an analysis?
- [x] A `groupby` or `value_counts` splits logically identical values into separate groups, silently and with no error
- [ ] It raises a `ValueError` immediately when the file is loaded
- [ ] It converts the entire column to a numeric type
- [ ] It deletes the affected rows from the DataFrame

### What kind of problem does the `Name` column ("Mr. Owen Harris Braund") represent?
- [x] A structural problem — multiple distinct pieces (title, first name, last name) packed into one field
- [ ] A missing-value problem where parts of the name are absent
- [ ] A wrong-type problem because names cannot be stored as strings
- [ ] A duplicate-row problem caused by repeated passenger names

### Why are dates stored as strings a problem even when the values look correct?
- [x] String dates cannot be reliably sorted chronologically, filtered by range, or subtracted to find durations
- [ ] Strings take up no memory and therefore lose precision
- [ ] pandas converts string dates to numbers automatically on load
- [ ] String dates are treated as missing values by most operations

## 08_2 · Missing Data

### What is the first diagnostic step before deciding how to handle missing values?
- [x] Measure how much is missing per column, e.g. `df.isnull().sum()` and the percentage of rows
- [ ] Immediately call `dropna()` to remove all rows with any gap
- [ ] Fill every column with its column mean value
- [ ] Delete any column that contains even a single null

### What does a heatmap of `df.isnull().T` help you see?
- [x] **Where** the missing values are — whether scattered randomly or clustered, which can signal a data-source problem
- [ ] The Pearson correlation between pairs of columns
- [ ] The mean value of each column in the dataset
- [ ] How many exact duplicate rows exist

### Why compare survival rates between rows with and without a recorded age?
- [x] To check whether missingness is related to the outcome — if so, dropping those rows would bias the analysis
- [ ] To count the total number of rows with missing age values
- [ ] To fill the missing ages with the survival rate as a proxy
- [ ] To convert the age column to a category type

### What does `df.dropna(thresh=5)` do on a 7-column DataFrame?
- [x] Keeps rows that have at least 5 non-null values, recovering rows that are mostly complete
- [ ] Drops the 5 columns that have the most null values
- [ ] Keeps only the first 5 rows of the DataFrame
- [ ] Fills any null values with the integer 5

### When is forward-fill (`ffill()`) or backward-fill (`bfill()`) an appropriate way to fill gaps?
- [x] When the data has a meaningful order (time series, sensor readings) so a neighboring value is a reasonable estimate
- [ ] In all cases — it is the best default for any column type
- [ ] Only for string-typed columns, not numeric ones
- [ ] Only when more than half the values in the column are missing

### How does `interpolate()` differ from forward-fill for a gradually changing numeric series?
- [x] It estimates gaps by fitting a line between the known values on either side, rather than carrying one constant forward
- [ ] It deletes the rows that contain missing values
- [ ] It fills gaps with the overall column mean
- [ ] It only works correctly on datetime-indexed columns

## 08_3 · Type Problems

### A numeric column read as `str` because one row says `"unknown"` sorts incorrectly. What fixes it?
- [x] `pd.to_numeric(col, errors="coerce")`, which parses valid numbers and turns the rest into `NaN`
- [ ] `col.astype(int)`, which always succeeds without error
- [ ] `col.sort_values()`, which fixes the dtype as a side effect
- [ ] Nothing — string-based sorting is close enough for most purposes

### Why use `errors="coerce"` with `pd.to_numeric()`?
- [x] It converts unparseable values to `NaN` instead of raising an error and stopping
- [ ] It rounds all parsed numbers down to the nearest integer
- [ ] It removes the entire column when any parsing error occurs
- [ ] It is required for every numeric column regardless of content

### A `survived` column stored as `"yes"`/`"no"` can't be averaged. How do you fix it?
- [x] Map the labels to numbers, e.g. `col.map({"yes": 1, "no": 0})`
- [ ] Call `col.mean()` with `errors="ignore"` to suppress the error
- [ ] Sort the column alphabetically to enable numeric operations
- [ ] Cast it directly with `col.astype(float)` without mapping

### Why convert a categorical-but-integer column like `pclass` with `.astype("category")`?
- [x] It tells pandas the values are a fixed set of labels (so arithmetic isn't meaningful), makes intent explicit, and can save memory
- [ ] It lets you finally compute a meaningful average of the class values
- [ ] It is required before any `groupby` operation will work
- [ ] It converts the integer labels into date objects

### For a low-cardinality string column like `sex`, what is a benefit of the `category` dtype?
- [x] Memory savings — pandas stores an integer code per row and maps it back to the string, instead of repeating the full string
- [ ] It forces every value to be unique across the column
- [ ] It converts the strings to floats for arithmetic operations
- [ ] It automatically removes any missing values in the column

### Which tool converts a column of date strings into a proper `datetime64` dtype?
- [x] `pd.to_datetime()`
- [ ] `pd.to_numeric()`
- [ ] `col.astype("category")`
- [ ] `col.str.strip()`

## 08_4 · String Cleaning

### What does the `.str` accessor let you do?
- [x] Apply a string operation to every element of a Series at once, with no explicit loop
- [ ] Convert a string column to numeric values
- [ ] Access a single character from the DataFrame object
- [ ] Sort the strings in the column alphabetically

### A `sex` column shows five values in `value_counts()` instead of two. What is usually the cause?
- [x] Inconsistent capitalization and stray whitespace making logically identical values look distinct
- [ ] The column has been converted to a category dtype
- [ ] The dataset genuinely contains five distinct sex labels
- [ ] `value_counts()` produces incorrect results on string columns

### Which chain normalizes hand-entered values like `" Female"`, `"MALE "`, `"female"` to a clean canonical form?
- [x] `col.str.strip().str.lower()`
- [ ] `col.str.title().str.split()`
- [ ] `col.strip().lower()` without `.str`
- [ ] `col.str.upper()` alone

### Why include `na=False` in `df["name"].str.contains("Mrs", na=False)`?
- [x] So null values evaluate to `False` instead of raising a `TypeError`
- [ ] It makes the pattern search case-insensitive
- [ ] It fills null values with the string `"Mrs"`
- [ ] It limits the search to only the first matching row

### When would you use `.str.startswith()` instead of `.str.contains()`?
- [x] When you want to match only at the beginning of the string (e.g. a title or prefix code), not anywhere inside it
- [ ] When the column contains numeric values
- [ ] When you want to count the number of characters in each string
- [ ] When the pattern is a regular expression

### Why can you chain `.str` methods like `col.str.strip().str.lower().str.replace(...)`?
- [x] Each `.str` method returns a new Series, so the next call operates on the result, left to right
- [ ] Because pandas runs chained `.str` calls in a random order
- [ ] Because `.str` caches the original column values
- [ ] You cannot — only one `.str` method call is allowed per line

## 08_5 · Splitting & Extracting

### What does `df["name"].str.split(". ", expand=True)` return?
- [x] A DataFrame with separate columns for each piece, split at the period-space delimiter
- [ ] A single string with the delimiter character removed
- [ ] A Series of lists that cannot be indexed further
- [ ] The original column unchanged

### Why pass `n=1` to `str.split(". ", expand=True, n=1)`?
- [x] It limits the split to the first occurrence, so other periods (e.g. middle initials) don't break the string into extra pieces
- [ ] It returns only the first row of the result
- [ ] It splits the string into exactly one piece total
- [ ] It removes the first character from every string

### After `str.split()` without `expand=True` you have a Series of lists. How do you pick the first element of each?
- [x] `.str.get(0)`
- [ ] `.str.first()`
- [ ] `[0]` applied to the whole Series
- [ ] `.str.split(0)`

### In `str.extract(r'(\w+)\.')`, what role do the parentheses play?
- [x] They form a **capture group** — `extract` returns only the text matched inside them, ignoring the rest of the pattern
- [ ] They are required syntax with no functional effect
- [ ] They make the match case-insensitive
- [ ] They escape the literal period character

### What advantage do named capture groups `(?P<title>\w+)` give over numbered ones?
- [x] The resulting DataFrame columns get meaningful names automatically, instead of 0, 1, 2
- [ ] They run faster than numbered capture groups
- [ ] They allow more than one match per row
- [ ] They remove the need for any regex pattern at all

### What is the conceptual difference between `str.split()` and `str.extract()`?
- [x] `split` breaks at a delimiter and you take a piece by position; `extract` finds a pattern anywhere and returns the captured portion
- [ ] They are identical in every practical case
- [ ] `split` uses regex; `extract` never does
- [ ] `extract` only works on numeric column values

## 08_6 · Regular Expressions

### In a regex, what do `\d`, `\w`, and `\s` match?
- [x] Any digit, any word character (letter/digit/underscore), and any whitespace, respectively
- [ ] A literal `d`, a literal `w`, and a literal `s`
- [ ] The start, middle, and end of a string
- [ ] Three different date format patterns

### To strip every non-digit character from a phone number, which replacement works?
- [x] `col.str.replace(r'[^\d]', '', regex=True)` — `[^\d]` matches anything that is not a digit
- [ ] `col.str.replace(r'\d', '', regex=True)`
- [ ] `col.str.strip()`
- [ ] `col.str.replace(" ", "")` alone

### Why does the validation pattern use anchors, as in `r'^\d{10}$'`?
- [x] `^` and `$` force the match to span the whole string, so only exactly ten digits qualify (not a 12-digit string)
- [ ] The anchors make the entire pattern case-insensitive
- [ ] They are decorative and have no effect on matching
- [ ] `^` means "not", so it excludes digit characters

### To clean currency strings like `"$71.28"` before `pd.to_numeric()`, which pattern keeps the number intact?
- [x] `r'[^\d.]'` — remove any character that is not a digit or a period
- [ ] `r'[^\d]'` — which would also delete the decimal point
- [ ] `r'\$'` — which only removes the dollar sign
- [ ] `r'.'` — which matches every character in the string

### What do the quantifiers `+`, `*`, and `?` mean in a regex?
- [x] One-or-more, zero-or-more, and zero-or-one of the preceding element, respectively
- [ ] Add, multiply, and question — arithmetic and punctuation operators
- [ ] Exactly one, exactly two, and exactly three of the preceding element
- [ ] Start anchor, middle anchor, and end anchor

### What do `case=False` and `na=False` do in `str.contains(pattern, regex=True, case=False, na=False)`?
- [x] Make the match case-insensitive and treat nulls as non-matching instead of erroring
- [ ] Convert the column to lowercase permanently and drop all null rows
- [ ] Disable regex matching and disable the contains check
- [ ] Sort the matching results and remove any duplicates

## 08_7 · Dates & Times

### Why is sorting a column of string dates unreliable?
- [x] Strings sort alphabetically, not chronologically — it only works for ISO `YYYY-MM-DD` format by coincidence
- [ ] String dates cannot be sorted at all in pandas
- [ ] Sorting strings reverses the chronological order
- [ ] pandas refuses to sort any column with `object` dtype

### How do you parse non-ISO dates like `"03/15/2023"` correctly?
- [x] `pd.to_datetime(col, format="%m/%d/%Y")`, giving the format codes for month, day, and year
- [ ] `col.astype("datetime64")` with no format argument
- [ ] `pd.to_numeric(col)` to convert to a numeric timestamp
- [ ] `col.str.split("/")` and stop there

### When a column mixes several date formats across rows, what helps?
- [x] `pd.to_datetime(col, format="mixed")`, which infers the format row by row (with some ambiguity risk)
- [ ] Dropping every row that contains a date value
- [ ] `col.str.lower()` to normalize the string representation
- [ ] Nothing — mixed formats cannot be parsed in pandas

### Once a column is `datetime64`, how do you extract the month or weekday name?
- [x] The `.dt` accessor, e.g. `col.dt.month` and `col.dt.day_name()`
- [ ] The `.str` accessor, e.g. `col.str.month`
- [ ] `col.month()` called directly on the column
- [ ] You must re-parse the string each time you need a component

### What does subtracting two `datetime64` columns produce, and how do you get minutes from it?
- [x] A `timedelta64` column; convert with `.dt.total_seconds() / 60`
- [ ] A float column already expressed in minutes
- [ ] An error — you cannot subtract two date columns
- [ ] A string column showing the difference as text

### What do `.dt.floor("h")` and `.dt.round("h")` let you do?
- [x] Bucket timestamps to an hour boundary (truncating or rounding) so you can group by time window
- [ ] Convert each timestamp to a count of hours since 1970
- [ ] Remove the time-of-day portion from each timestamp entirely
- [ ] Round the fare column to the nearest whole dollar

## 08_8 · A Complete Pipeline

### Why does the order of cleaning steps matter in a pipeline?
- [x] Steps depend on one another — e.g. you can't parse a date column you haven't loaded, or fill a null in a column you already dropped
- [ ] It doesn't matter — any order produces the identical result
- [ ] Alphabetical order of steps is required by pandas
- [ ] Dropping columns must always be the last step

### How does `raw.nunique()` help diagnose a new dataset?
- [x] Columns with only one unique value carry no information and can be dropped — something `info()` alone wouldn't reveal
- [ ] It counts the total missing values per column
- [ ] It lists all the duplicate rows in the dataset
- [ ] It converts low-cardinality columns to category dtype

### A column is missing 87% of its values. What is the pipeline's recommended action?
- [x] Drop it — a column empty for nearly nine of ten rows is almost never useful and its present rows may be unrepresentative
- [ ] Fill all the gaps with the value 0
- [ ] Forward-fill the entire column from the first non-null value
- [ ] Keep it and ignore the high missingness rate

### The pipeline leaves vehicle fields as `NaN` but drops the few rows missing geographic fields. Why the different treatment?
- [x] Missing vehicle details mean "not available" (inventing values would mislead), while the geographic gaps are tiny enough to drop without affecting the dataset
- [ ] Vehicle fields are numeric and geographic fields are string typed
- [ ] It is an arbitrary choice with no analytical reasoning behind it
- [ ] Dropping is always preferred over leaving `NaN` values

### What is the suggested final check that a dataset is truly clean?
- [x] Run the analysis you actually wanted to do (e.g. a groupby) and confirm it executes correctly on the cleaned data
- [ ] Re-read the raw CSV and compare its byte count to the cleaned version
- [ ] Delete the cleaning code and attempt to re-create it from memory
- [ ] Check that the saved file size shrank after cleaning

### Why package the cleaning steps as a reusable function like `clean_311(raw)`?
- [x] It documents every decision in one place and lets you re-clean an updated dataset in a single call
- [ ] Functions run faster than notebook cells in all circumstances
- [ ] It is required by pandas before changes to the DataFrame are accepted
- [ ] It automatically uploads the cleaned data to a remote location
