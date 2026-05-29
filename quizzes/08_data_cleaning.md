# 08 · Data Cleaning

## Data Cleaning Quiz

### `df.isnull().sum()` returns 0 for the `age` column. What does this mean?
- [ ] The age column has 0 rows
- [x] The age column has no missing values
- [ ] The age column is not loaded correctly
- [ ] The age column contains only zero values

### You call `df.dropna()` with no arguments. What is the default behavior?
- [ ] Drop any column with at least one null
- [x] Drop any row with at least one null
- [ ] Drop only rows where all values are null
- [ ] Drop only rows where more than 50% of values are null

### `pd.to_numeric(series, errors="coerce")` -- what does `errors="coerce"` do to non-numeric entries?
- [ ] Raises a ValueError immediately
- [ ] Converts them to 0
- [x] Converts them to NaN
- [ ] Leaves them as strings

### A sex column contains "female", "Female", and " female ". After `.str.strip().str.lower()`, how many unique values remain?
- [ ] 3 (unchanged)
- [ ] 2
- [x] 1
- [ ] 0 (all become null)

### What is the main reason to convert `pclass` (values 1, 2, 3) from `int64` to `category` dtype?
- [ ] It makes arithmetic on the column faster
- [x] It signals that the values are labels, not quantities, preventing meaningless averaging
- [ ] It automatically converts the values to strings
- [ ] It sorts the values in the correct order automatically

### `df["name"].str.split(". ", expand=True, n=1)` -- what does `n=1` do?
- [ ] Keeps only the first element of each split
- [x] Limits the split to at most one occurrence, so at most two pieces result
- [ ] Splits on the first character only
- [ ] Returns a Series of length 1

### The regex pattern `[^\d]` matches:
- [ ] Any digit 0-9
- [x] Any character that is NOT a digit
- [ ] The start of a string
- [ ] Any character that is a digit or a letter

### In `pd.to_datetime(series, format="%m/%d/%Y")`, what does `%m` represent?
- [ ] Full month name (e.g., "January")
- [x] Month as a zero-padded number (01-12)
- [ ] Minute as a number
- [ ] Day of the month

### You subtract two `datetime64` columns. The result has dtype:
- [ ] int64 (number of days)
- [ ] float64 (number of seconds)
- [x] timedelta64
- [ ] datetime64

### You have a `timedelta64` column `duration`. How do you convert it to a float column of total seconds?
- [ ] duration.dt.seconds
- [x] duration.dt.total_seconds()
- [ ] duration.astype(float)
- [ ] pd.to_numeric(duration)

### Which `.str` method returns a boolean Series indicating whether each element contains a given substring?
- [ ] .str.equals()
- [x] .str.contains()
- [ ] .str.match()
- [ ] .str.find()

### In a cleaning pipeline, why is renaming columns usually the first step?
- [ ] pandas requires renamed columns before any other operations
- [x] It makes all subsequent code readable and avoids escaping special characters in column names
- [ ] It automatically drops columns with missing values
- [ ] It converts column dtypes to the correct types
