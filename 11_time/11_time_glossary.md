# 11 — Time Series: Glossary

**DatetimeIndex** — A pandas index where each label is a timestamp. Created by `set_index()` on a datetime column. Enables partial string indexing, resampling, and rolling operations that require rows to be understood as points in time.

**`.diff()`** — A Series method that subtracts the previous row from the current row, producing the absolute change between consecutive periods. The first row is always `NaN` because there is no "previous row." The pandas equivalent of "how much did this change from yesterday?"

**`.dt` accessor** — Syntax for extracting time components from a datetime **column** (a Series), as in `df["dteday"].dt.month`. When the timestamps are in the **index** instead, drop the `.dt` and read the attribute directly: `df.index.month`, `df.index.dayofweek`, `df.index.day_name()`. Both return integers or strings suitable for groupby.

**frequency string** — A short code passed to `resample()` that specifies the time period for grouping. Common values: `"W"` (week ending Sunday), `"ME"` (month end), `"QE"` (quarter end), `"YE"` (year end). Pandas 3.0 uses `"ME"` and `"QE"` rather than the deprecated `"M"` and `"Q"`.

**`.idxmax()` / `.idxmin()`** — Series methods that return the index label of the maximum or minimum value. On a `DatetimeIndex`, the label is a timestamp. Call `.date()` on the result to display just the calendar date. The pandas complement to `.max()` and `.min()` when location matters more than value.

**month-over-month change** — The percent change in a monthly series computed with `.pct_change()` (default `periods=1`). Answers "how did this month compare to last month?" Seasonal effects are visible because adjacent months differ by season.

**partial string indexing** — Selecting rows from a `DatetimeIndex` using a string that names a year (`"2011"`) or year-month (`"2011-06"`). Pandas matches all rows whose timestamp falls within the named period. Only works when the index is a `DatetimeIndex`.

**`.pct_change()`** — A Series method that computes the fractional change between consecutive rows: `(current - previous) / previous`. Pass an integer `periods` argument to compare against a row further back (e.g., `.pct_change(12)` on monthly data gives year-over-year change). The first `periods` rows are `NaN`.

**resample()** — A pandas method for grouping time-series rows by a time period and reducing each group to a single value. Analogous to `groupby().agg()` except that the grouping key is time itself. Always requires a chained aggregation: `.resample("ME").sum()`, `.resample("W").mean()`, etc.

**rolling window** — A calculation that moves a fixed-length window across the series one row at a time, computing an aggregate within each window position. `.rolling(7).mean()` produces a series of the same length as the input, where each value is the average of that row and the six preceding rows. The first `n-1` rows are `NaN`.

**rolling mean (moving average)** — The most common rolling calculation: `.rolling(n).mean()`. Smooths short-term noise while preserving the trend. A 7-day window removes the weekly cycle; a 30-day window removes monthly fluctuations as well. Shorter windows react faster to change; longer windows show the slow seasonal arc.

**rolling standard deviation** — `.rolling(n).std()`: measures how much the series is bouncing around within each window. High values mean the series is volatile during that period; low values mean it is stable.

**seasonal pattern** — A repeating structure in a time series tied to a calendar period (season, month, day of week). Identified by grouping on a time component extracted with the `.dt` accessor and computing a mean per group.

**year-over-year change** — `.pct_change(12)` on monthly data: each month is compared to the same month one year earlier, removing the seasonal effect and isolating true growth. The first 12 values are `NaN` because there is no year-ago baseline for the first year.
