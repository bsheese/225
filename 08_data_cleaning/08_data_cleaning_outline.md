# 08 — Data Cleaning: Module Outline

## Audience
Undergrad CS and data science majors with Python and pandas experience (modules 06 and 07); no prior data cleaning or regex exposure.

## Datasets

| Dataset | Source | Used in | Why |
|---|---|---|---|
| Titanic (bsheese CSV) | course GitHub | 08.1, 08.3, 08.4, 08.5, 08.6, 08.9 | Pre-cleaned; no missing values; familiar from modules 06-07 |
| Titanic (seaborn) | `sns.load_dataset("titanic")` | 08.2, 08.9 | Genuine missing values in `age` and `deck` |
| MPG | `sns.load_dataset("mpg")` | 08.5, 08.9 | `name` column packs manufacturer + model; natural `str.get()` demo |
| Taxis | `sns.load_dataset("taxis")` | 08.7, 08.9 | Pre-parsed datetime columns; clean timedelta demo |
| Chicago 311 | course GitHub | 08.8 | Complex real-world data; motivates multi-step pipeline |
| Synthetic | constructed inline | 08.2, 08.3, 08.4, 08.6, 08.7 | Problems that do not appear in the pre-cleaned datasets |

## Notebooks

| Notebook | Topic | Main Tools |
|---|---|---|
| 08.1 | What Makes Data Messy? | Taxonomy of five problem categories; `.info()`, `.isnull().sum()` |
| 08.2 | Missing Data | `dropna(thresh=, how=, subset=)`, `ffill()`, `bfill()`, `interpolate()` |
| 08.3 | Type Problems | `pd.to_numeric(errors=)`, `.map()`, `.astype("category")`, `pd.to_datetime()` preview |
| 08.4 | String Cleaning | `.str.lower/upper/title()`, `.str.strip()`, `.str.replace()`, `.str.contains()`, `.str.startswith()` |
| 08.5 | Splitting and Extracting | `str.split(expand=True, n=)`, `str.get()`, `str.extract()`, named capture groups |
| 08.6 | Regular Expressions | metacharacters, `[^...]`, `\d{n}`, anchors `^` and `$`; applied to phone, currency, and name problems |
| 08.7 | Dates and Times | `pd.to_datetime(format=)`, `format="mixed"`, `.dt` accessor, `timedelta64`, `.dt.total_seconds()` |
| 08.8 | Complete Cleaning Pipeline | survey → rename → drop → parse → fill → normalize → validate → package as function |

## What Is Intentionally Excluded
- `pd.concat()` and `.merge()` (covered in module 09 aggregation)
- Fuzzy string matching (e.g., `fuzzywuzzy`, `difflib`)
- Schema validation libraries (e.g., `pandera`, `great_expectations`)
- Regular expression lookaheads/lookbehinds and named backreferences
- JSON and XML parsing
- Database loading

## Learning Sequence
Taxonomy (08.1) → missing values (08.2) → type coercion (08.3) → string normalization (08.4) → text extraction (08.5) → regex (08.6) → dates (08.7) → full pipeline (08.8) → exercises (08.9)
