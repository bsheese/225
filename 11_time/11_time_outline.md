# 11 — Time Series: Module Outline

## Audience
Undergrad CS and data science majors with Python, pandas, groupby, and SQL experience (modules 06–10); no prior time-series exposure.

## Dataset

| Dataset | Source | Used in | Why |
|---|---|---|---|
| UCI Bike Sharing (daily) | repo `data/bike_daily.csv` via raw GitHub URL | 11.1–11.9 | One row per day for 731 consecutive days; clear seasonal and weekly structure; multiple numeric columns (cnt, casual, registered) that tell different stories |

Every notebook is self-contained: each loads the bike data from the source URL and rebuilds the datetime index in its first code cell so it can be opened on its own through its Colab badge. Notebook 11.1 explains the parse and indexing step by step; 11.2–11.9 repeat a compact `read_csv` load with `parse_dates` and `index_col` and do not re-teach it. The dataset switches from the Gapminder data used in modules 09–10; the switch is acknowledged explicitly at the top of 11.1.

Columns used: `dteday`, `season`, `yr`, `mnth`, `holiday`, `weekday`, `workingday`, `weathersit`, `temp`, `casual`, `registered`, `cnt`.

## Notebooks

| Notebook | Topic | Main Tools |
|---|---|---|
| 11.1 | Time Series Basics | `pd.to_datetime()`, `set_index()`, `sort_index()`, `DatetimeIndex`, partial string indexing with `.loc` |
| 11.2 | Resampling | `resample("W").sum()`, `resample("ME").mean()`, `resample("QE")`, `resample("YE")`, sum vs. mean choice, frequency strings |
| 11.3 | Rolling Windows | `rolling(7).mean()`, `rolling(30).mean()`, `rolling(30).std()`, overlay plot of raw + smoothed |
| 11.4 | Period Comparisons | `.diff()`, `.pct_change()`, `.pct_change(12)` for year-over-year, `.idxmin()`, `.idxmax()` |
| 11.5 | Seasonal Patterns | `index.month`, `index.dayofweek`, `index.day_name()`, groupby time components, `pivot_table` + `sns.heatmap` |
| 11.9 | Exercises | All module 11 tools |

## What Is Intentionally Excluded
- Upsampling (only downsampling is covered; upsampling introduces interpolation complexity)
- Time zone handling (`tz_localize`, `tz_convert`)
- Irregular time series and gap filling (`asfreq`, `ffill`, `bfill` for missing dates)
- Forecasting and predictive modeling (out of course scope)
- `pd.Period` and `PeriodIndex`
- `pd.Timedelta` arithmetic beyond what DatetimeIndex subtraction produces implicitly
- `DateOffset` objects
- `resample().apply()` with custom aggregation functions
- `rolling(min_periods=...)` and other rolling parameters beyond `window`
- Multivariate time series alignment

## Learning Sequence
Parse and index dates (11.1) → change time resolution with resampling (11.2) → overlay smoothed trend with rolling windows (11.3) → measure rate and direction of change (11.4) → group by time components for seasonal patterns (11.5) → exercises (11.9)
