# 08 — Data Cleaning: Glossary

**anchor** — A regex symbol that constrains where a match can occur. `^` matches the start of the string; `$` matches the end. Without anchors, a pattern can match anywhere inside a longer string.

**backward-fill (`bfill`)** — A missing-value strategy that replaces each null with the next non-null value in the Series. Appropriate for ordered sequences where a future value is a reasonable estimate.

**capture group** — The portion of a regex pattern enclosed in parentheses `()`. `str.extract()` returns the text that matched inside the capture group, ignoring the rest of the pattern.

**cardinality** — The number of distinct values in a column. A low-cardinality column (e.g., `sex` with 2 values) is a good candidate for the `category` dtype.

**category dtype** — A pandas dtype that represents a column as a fixed set of labels rather than raw strings or integers. Reduces memory for low-cardinality columns and communicates that arithmetic across labels is not meaningful.

**coerce** — The `errors="coerce"` setting in `pd.to_numeric()` and `pd.to_datetime()`: values that cannot be parsed are converted to `NaN` rather than raising an error.

**datetime64** — The pandas dtype for date and time values. Enables chronological sorting, date-range filtering, and subtraction to produce a `timedelta64`.

**dirty data** — A dataset that has one or more of the five problem categories: wrong types, missing values, inconsistent formatting, structural problems, or date encoding issues.

**dtype** — The data type of a pandas column (e.g., `int64`, `float64`, `str`, `category`, `datetime64`, `timedelta64`). Wrong dtypes cause silent errors in sorting, arithmetic, and grouping.

**format string** — A string passed to `pd.to_datetime()` (or `strftime()`) that describes the layout of a date: `%Y` = four-digit year, `%m` = zero-padded month, `%d` = zero-padded day, `%H` = 24-hour hour, `%M` = minute, `%S` = second.

**forward-fill (`ffill`)** — A missing-value strategy that replaces each null with the most recent non-null value in the Series. Appropriate for ordered sequences such as time series or sensor readings.

**imputation** — Replacing missing values with estimated values (e.g., the column median, or a group-specific mean) rather than dropping the rows.

**interpolation** — Estimating a missing value by fitting a line (or curve) through the known values on either side of the gap. More realistic than forward-fill when the data changes gradually.

**metacharacter** — A character in a regex pattern that has special meaning rather than matching itself literally. Examples: `\d` (any digit), `.` (any character), `+` (one or more), `{n}` (exactly n), `[...]` (character class), `^` and `$` (anchors).

**named capture group** — A regex capture group written as `(?P<name>...)`. `str.extract()` uses the name to label the output column automatically.

**NaN** — "Not a Number"; the sentinel value pandas uses to represent a missing entry in a numeric or string column.

**pipeline** — A sequence of cleaning steps applied in a fixed order, typically packaged as a function that takes a raw DataFrame and returns a clean one.

**regex (regular expression)** — A string that describes a pattern. Used in pandas via `.str.replace(regex=True)`, `.str.contains(regex=True)`, and `.str.extract()` to match, filter, and extract text.

**snake_case** — A naming convention where words are separated by underscores and all letters are lowercase (`creation_date`, `zip_code`). Preferred for column names because it avoids spaces and special characters.

**`.str` accessor** — The pandas interface for applying string methods to every element of a Series at once: `.str.lower()`, `.str.strip()`, `.str.replace()`, `.str.contains()`, `.str.split()`, `.str.extract()`.

**`.dt` accessor** — The pandas interface for extracting date and time components from a `datetime64` Series: `.dt.year`, `.dt.month`, `.dt.hour`, `.dt.day_name()`, `.dt.floor()`, `.dt.total_seconds()`.

**timedelta64** — The pandas dtype produced by subtracting two `datetime64` columns. Represents a duration rather than a point in time. Convert to numeric with `.dt.total_seconds()`.

**type coercion** — Converting a column from one dtype to another (e.g., `object` to `float64` via `pd.to_numeric()`). Coercion can be lossy if the source column contains unparseable values.
