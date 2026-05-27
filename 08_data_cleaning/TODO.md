# Module 08: Data Cleaning with pandas

## Module goal

Build a systematic, hands-on understanding of how to take raw, messy data and make it analysis-ready. The emphasis is on pandas string methods — the most common real-world cleaning challenge — backed by a full treatment of missing data, type coercion, and date handling. The module closes with a complete end-to-end pipeline on a dataset students have not seen before.

## What 06.4 already covered (do not repeat)

- `isnull().sum()`, `notna()`, `isnull().any(axis=1)`
- `dropna()`, `dropna(subset=)`, `fillna()` with scalar and dict
- `duplicated()`, `drop_duplicates()`
- `rename(columns={})`, `columns.str.lower()`
- `astype("category")`, `pd.to_numeric(errors="coerce")` — introduced but not explored in depth
- Brief `str.extract()` and `str.strip().str.lower()` — introduced but not taught as a system
- A complete `prepare_titanic()` function as a capstone

Every 08 notebook should open with an explicit "06.4 covered X; here we go deeper into Y" framing so students understand the progression.

---

## Notebook plan

### 08.1 — What Makes Data Messy?

**Goal:** taxonomy of messiness, motivate the module, survey the tools students will learn.

**Primary calls:** `df.info()`, `df.dtypes`, `df.describe()`, `df.head()`, `.value_counts()` on a dirty column.

**Content:**
- The five categories of messiness: wrong types, missing values, inconsistent formatting, structural problems, encoding errors.
- Show each category with a real example from the bsheese Titanic CSV (e.g., the Name column is a string needing parsing, fare is numeric but stored fine, age has NaN).
- A visual map of which notebook covers which category.
- Keep this short — it is orientation, not instruction.

---

### 08.2 — Missing Data in Depth

**Goal:** go far beyond 06.4's introduction to dropna/fillna. Teach students to diagnose missing-data patterns and choose the right strategy.

**Primary calls:** `df.isnull().sum()`, `df.isnull().mean()`, `dropna(thresh=, how="all")`, `fillna(method=)` (deprecated path — use `ffill()`/`bfill()`), `interpolate()`.

**Content:**
- Diagnosing: how much is missing? Which rows? Which columns? Is it random or systematic?
- Dropping strategies: `thresh=` to keep rows/columns with enough non-null data, `how="all"` for entirely-null rows.
- Filling strategies: forward-fill (`ffill()`) and backward-fill (`bfill()`) for ordered/time data; `interpolate()` for numeric sequences.
- The missing-data analysis pipeline: check → visualize with a heatmap of nulls → decide → act.
- When dropping is legitimate vs. when it biases the analysis (brief, conceptual).

**Dataset:** bsheese Titanic CSV.

---

### 08.3 — Type Problems and Conversions

**Goal:** teach students to recognize and fix the most common dtype mismatches: numbers stored as strings, booleans encoded as 0/1 or Y/N, datetimes stored as strings, and object columns that should be category.

**Primary calls:** `pd.to_numeric(errors="coerce")`, `astype()`, `pd.to_datetime(format=)`, `pd.Categorical()`.

**Content:**
- Why dtypes matter: a ">" comparison on an object column with numbers stored as strings silently sorts lexicographically instead of numerically. Show the broken result, then the fix.
- Numeric-as-string: construct a column with values like `["22", "35", "missing", "41"]` and demonstrate `pd.to_numeric(errors="coerce")` producing NaN for non-numeric values.
- Boolean encoding: pclass stored as 1/2/3 already works numerically, but survived stored as "yes"/"no" needs a map. Use `map({"yes": True, "no": False})` or `replace`.
- Category type: when to use it (fixed, low-cardinality text like sex, pclass) and what memory savings look like.
- Datetimes are introduced here conceptually but handled fully in 08.7.

**Dataset:** bsheese Titanic CSV for most examples; a small synthetic DataFrame for the numeric-as-string demonstration.

---

### 08.4 — String Cleaning: The `.str` Accessor

**Goal:** teach the `.str` accessor systematically as a vectorized toolkit for normalizing and filtering text columns.

**Primary calls:** `str.lower()`, `str.upper()`, `str.title()`, `str.strip()`, `str.lstrip()`, `str.rstrip()`, `str.replace()`, `str.contains()`, `str.startswith()`, `str.endswith()`, `str.len()`, `str.count()`.

**Content:**
- Motivation: the Name column has values like `"Mr. Owen Harris Braund"` — case-inconsistent cabin codes, whitespace-padded ticket strings. Show how equality checks fail without normalization.
- Case normalization: `.str.lower()` before any groupby or comparison.
- Whitespace: `.str.strip()` catches leading/trailing spaces from CSV exports.
- Simple replacement: `.str.replace("Mrs.", "")` vs. `str.replace(r'\bMrs\.\b', '', regex=True)` — show why the plain version can have unexpected matches.
- Filtering rows: `df[df["name"].str.contains("Mrs")]` to subset.
- Measuring: `str.len()` on a column to find unusually long or short values; `str.count("a")` to count occurrences.
- Chain example: normalize a ticket column from raw → stripped → lowercased → deduplicated.

**Dataset:** bsheese Titanic CSV (Name, Ticket columns).

---

### 08.5 — Splitting and Extracting Text

**Goal:** teach students to pull structured information out of free-text fields using `str.split()` and `str.extract()`.

**Primary calls:** `str.split(expand=True)`, `str.get(n)`, `str.extract(r'pattern')` with named groups.

**Content:**
- Motivation: the Name column contains title (Mr., Mrs., Miss., Master.), first name, and last name packed into one string. The MPG dataset's car name column contains make and model. Students need each piece separately.
- `str.split(expand=True)`: split on a delimiter into multiple columns. Use the MPG car name to extract make in one line: `.str.split(expand=True).str.get(0)`.
- `str.get(n)`: index into a list column (after split) to get the nth element.
- `str.extract(r'pattern')`: use a capture group to extract the title from Titanic names. Single capture group → one new column.
- Named capture groups: `str.extract(r'(?P<title>\w+)\.')` produces a column named `title` directly.
- Multiple capture groups in one call: extract last name and title at once.

**Dataset:** bsheese Titanic CSV (Name column) + `sns.load_dataset("mpg")` (name column for make extraction).

---

### 08.6 — Regular Expressions for Data Cleaning

**Goal:** apply regular expressions to concrete data-cleaning problems — not as a regex tutorial, but as a practical tool for the patterns that come up most often.

**Primary calls:** `str.contains(regex=True)`, `str.replace(regex=True)`, `str.extract()` with complex patterns.

**Content:**
- Anchor every regex to a concrete cleaning problem. Do not introduce syntax divorced from a real task.
- Problem 1: phone numbers. A column has values like `"(555) 867-5309"`, `"555.867.5309"`, `"5558675309"`. Extract the 10 digits: `str.replace(r'[\D]', '', regex=True)` then validate with `str.contains(r'^\d{10}$', regex=True)`.
- Problem 2: currency. A fare column stored as strings: `"$71.28"`, `"£7.25"`, `"22.00"`. Strip the currency symbol: `str.replace(r'[^\d.]', '', regex=True)`, then `pd.to_numeric()`.
- Problem 3: extracting name components. The Titanic Name column has the pattern `"Last, Title. Rest"`. Use `str.extract(r'^(?P<last>[^,]+),\s*(?P<title>\w+)\.')` to get both columns in one call.
- Key metacharacters covered: `.`, `*`, `+`, `?`, `[]`, `^`, `$`, `\d`, `\w`, `\s`, `{n}`, named groups. Introduce each one only when the problem demands it.
- Note what is out of scope: `str.findall`, `str.extractall` (these are analytical, not cleaning-oriented).

**Dataset:** bsheese Titanic CSV; synthetic DataFrames for the phone and currency examples.

---

### 08.7 — Dates and Times

**Goal:** teach `pd.to_datetime()` for parsing, the `.dt` accessor for extraction, and timedelta arithmetic.

**Primary calls:** `pd.to_datetime(format=)`, `dt.year`, `dt.month`, `dt.day`, `dt.dayofweek`, `dt.hour`, `pd.Timedelta`, arithmetic on datetime columns.

**Content:**
- Motivation: dates stored as strings can't be sorted, filtered by range, or differenced. Show the comparison failure, then the fix.
- Parsing: construct a synthetic DataFrame with mixed-format date strings (`"2023-01-15"`, `"01/15/2023"`, `"January 15, 2023"`). Use `pd.to_datetime()` with explicit `format=` where possible; use `dateutil` parsing (no `format=`) as a fallback with its caveats.
- The `.dt` accessor: extract components from a datetime column — year, month, day, weekday (name via `dt.day_name()`), hour. Show a practical aggregation: count bookings by weekday.
- Timedelta: subtract two datetime columns to get a duration. Example with the taxis dataset: `dropoff - pickup` gives ride duration; compute mean duration by payment type.
  - Note: seaborn's taxis pickup/dropoff are already `datetime64[us]` — no parsing needed. Use `dt.strftime("%Y-%m-%d %H:%M:%S")` → `pd.to_datetime()` as a round-trip to demonstrate the parsing step explicitly.
- `dt.floor()`, `dt.round()` for bucketing timestamps to the nearest hour.

**Dataset:** taxis (`sns.load_dataset("taxis")`) for the dt accessor and timedelta; synthetic DataFrame for the mixed-format parsing demonstration.

---

### 08.8 — A Complete Cleaning Pipeline

**Goal:** synthesize all prior tools into a documented, reproducible cleaning pipeline on a dataset students have not seen.

**Dataset:** a real-world CSV from a public source that is messy enough to require all the tools: missing values, type problems, string normalization, date parsing, duplicates. Candidate: FiveThirtyEight's `steak-survey.csv` (has "How do you like your steak prepared?", messy categorical columns, missing values) or a similar publicly accessible dataset. Verify the URL works before writing the notebook.

**Content:**
- Load the raw dataset. Show `df.info()` and `df.head()` to survey the damage.
- Work through the cleaning checklist in order:
  1. Rename columns (snake_case, no spaces).
  2. Fix dtypes (to_numeric, to_datetime, category).
  3. Handle missing values (diagnose → drop or fill with justified choice).
  4. Normalize strings (strip, lower, replace inconsistent values).
  5. Parse and extract structured fields.
  6. Drop duplicates.
  7. Validate: shape, dtypes, null counts after cleaning.
- Write the whole pipeline as a single function: `def clean_dataset(df) -> pd.DataFrame`.
- Show a before-and-after summary table.

---

### 08.9 — Exercises

**Goal:** apply all module tools to a mix of short and multi-step problems.

**Structure:** same as 07.9 — markdown question, blank `# your code here` cell, hidden solution cell with `#@title Solution` and `"cellView": "form"` metadata.

**Exercise topics to cover (at minimum):**
1. Diagnose missing data: counts, percentages, heatmap.
2. Drop rows/columns using `thresh=` and `how="all"`.
3. Forward-fill a column in a sorted DataFrame.
4. Fix a numeric-as-string column with `pd.to_numeric(errors="coerce")`.
5. Normalize a string column: strip, lowercase, replace a value.
6. Filter rows using `str.contains()`.
7. Extract a title from the Titanic Name column using `str.extract()`.
8. Split the MPG car name to create a "make" column.
9. Clean a currency-formatted string column and convert to float.
10. Parse a column of mixed-format date strings to datetime.
11. Extract the month and weekday from a datetime column.
12. Compute a duration in minutes from two datetime columns.
13. Write a `clean()` function that applies at least 5 of the above steps to a given DataFrame.

---

## Scope exclusions

The following are intentionally out of scope for module 08:

- Outlier and anomaly detection (statistics-first topic, belongs in a later module)
- Validation frameworks (pandera, great_expectations)
- Tidy-data reshaping (melt, pivot, stack/unstack — separate module)
- Unicode and encoding deep dives
- `str.extractall`, `str.findall` (analytical, not cleaning-oriented)
- Fuzzy matching / record linkage

---

## Datasets to use

| Dataset | Source | Why |
|---|---|---|
| bsheese Titanic CSV | `https://raw.githubusercontent.com/bsheese/CSDS125ExampleData/master/data_titanic.csv` | Has `Name` column: "Mr. Owen Harris Braund". Primary dataset throughout. |
| MPG | `sns.load_dataset("mpg")` | `name` column (e.g., "chevrolet chevelle malibu") good for `str.split().str.get(0)` to extract make. Note: `horsepower` is already `float64` with 6 NaN — `to_numeric` demo needs a synthetic column instead. |
| Taxis | `sns.load_dataset("taxis")` | `pickup`/`dropoff` are already `datetime64[us]`. Use `dt.strftime()→parse` round-trip to demonstrate datetime parsing. |
| New dataset for 08.8 | `https://raw.githubusercontent.com/bsheese/CSDS125ExampleData/refs/heads/master/data_311_Service_Requests_small.csv` | Verify URL before writing the notebook. |

---

## Writing and pedagogy reminders

- Read `writing_sample.md` before writing any prose.
- No em-dashes anywhere.
- Every notebook opens with the Colab badge cell (before title, before everything).
- Every code cell is preceded by a markdown cell that earns it.
- Every output is interpreted in prose immediately after.
- Show the broken case first, then the fix.
- Introduce each function at its minimum; add one parameter per subsequent example.
- Close each notebook with a bridge to the next.
