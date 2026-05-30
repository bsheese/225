# 11 · Time Series

## 11_1 · Time Series Basics

### When pandas loads a CSV, a date column like `"2011-01-01"` arrives as `object`. Why convert it with `pd.to_datetime()`?
- [x] Until it is `datetime64`, you cannot do date arithmetic, extract components with `.dt`, or compare dates with `<`/`>`
- [ ] `object` columns use too much disk space
- [ ] Conversion sorts the dates automatically
- [ ] It removes invalid rows

### Why set the date column as the DataFrame index for time-series work?
- [x] A `DatetimeIndex` enables partial-string date slicing, automatic time-aware alignment, and date-labeled plots
- [ ] It deletes the date column to save memory
- [ ] It is required before you can call `.mean()`
- [ ] The index must always be a date

### With a `DatetimeIndex`, what does `df.loc["2011-06"]` return?
- [x] All rows from June 2011 — partial-string indexing selects by the precision you give (year, month, etc.)
- [ ] A single row for June 1, 2011
- [ ] A `KeyError`, since the index is dates
- [ ] The column named "2011-06"

### What would `df.loc["2011"]` do if the index were a plain integer range instead of a `DatetimeIndex`?
- [x] Raise a `KeyError` — partial-string date indexing only works on a `DatetimeIndex`
- [ ] Return all 2011 rows anyway
- [ ] Return the row at position 2011
- [ ] Silently return an empty DataFrame

### Why does `df["cnt"].plot()` automatically put dates on the x-axis?
- [x] The index is a `DatetimeIndex`, so pandas/matplotlib draw it as a time axis
- [ ] `.plot()` always uses dates
- [ ] The column `cnt` is a date
- [ ] You must pass `x="date"` for it to work

### The bike dataset has 731 rows for 2011–2012 with no gaps. Why does that matter for this module?
- [x] A clean, gapless daily series is what lets resampling and rolling-window operations work cleanly later
- [ ] 731 is the maximum pandas allows
- [ ] Gaps would make the dates sort incorrectly
- [ ] It proves the data is from a leap year only

## 11_2 · Resampling

### What does `df["cnt"].resample("W").sum()` do?
- [x] Groups the daily rows into 7-day (weekly) bins and totals the rentals in each bin
- [ ] Selects every 7th row
- [ ] Smooths the data without changing the number of rows
- [ ] Drops weekends from the data

### What must always accompany a `resample()` call?
- [x] An aggregation function (e.g. `.sum()` or `.mean()`) describing how to combine the rows in each bin
- [ ] A `hue=` argument
- [ ] A list of columns to drop
- [ ] A boolean mask

### When resampling a daily rental count, when would you use `.sum()` vs `.mean()`?
- [x] `.sum()` for "how many rentals this month" (a total); `.mean()` for a per-day average that isn't inflated by months with more days
- [ ] `.sum()` and `.mean()` always give the same answer
- [ ] `.mean()` for totals, `.sum()` for averages
- [ ] Always use `.sum()`; `.mean()` is invalid on time series

### In current pandas, which frequency strings denote month-end and quarter-end?
- [x] `"ME"` and `"QE"` — the older `"M"` and `"Q"` are deprecated
- [ ] `"M"` and `"Q"` are the current forms
- [ ] `"MONTH"` and `"QUARTER"`
- [ ] `"30D"` and `"90D"` only

### How does resampling change the size of the series?
- [x] It reduces the number of rows — e.g. 731 daily rows become 105 weekly or 24 monthly rows
- [ ] It keeps the same number of rows, filling gaps with NaN
- [ ] It always doubles the number of rows
- [ ] It leaves the row count unchanged

### What is the tradeoff as you resample from daily to weekly to monthly?
- [x] The line gets smoother (less noise, clearer trend) but loses resolution about which specific days/weeks were unusual
- [ ] The data becomes less accurate
- [ ] You gain resolution and lose smoothness
- [ ] There is no tradeoff; coarser is always better

## 11_3 · Rolling Windows

### What does `df["cnt"].rolling(7).mean()` compute?
- [x] For each day, the average of that day and the six days before it — a 7-day moving average
- [ ] The total over every 7-day bin, reducing the row count
- [ ] The average of the next 7 days only
- [ ] A single overall 7-day average

### How does a rolling window differ from resampling in its effect on the row count?
- [x] Rolling preserves the original number of rows; resampling reduces them
- [ ] Rolling reduces rows; resampling preserves them
- [ ] Both reduce the row count equally
- [ ] Both preserve the row count

### Why are the first six values of a 7-day rolling mean `NaN`?
- [x] There aren't yet seven days of data to average until the seventh row
- [ ] The data starts with six missing values
- [ ] Rolling always drops the first row of each month
- [ ] `NaN` marks weekend days

### What is the tradeoff between a 7-day and a 30-day rolling window?
- [x] The 7-day window reacts quickly to changes but is bumpier; the 30-day window is smoother but lags behind sudden shifts
- [ ] The 30-day window reacts faster than the 7-day
- [ ] Larger windows are always better
- [ ] They produce identical lines

### What does `df["cnt"].rolling(30).std()` show?
- [x] The rolling variability — how much the daily count bounces around within each 30-day window
- [ ] The rolling total
- [ ] The trend direction
- [ ] The number of missing values per window

### When should you use a rolling window rather than resampling?
- [x] When you want to overlay a smooth trend line on the raw daily data without changing the time resolution
- [ ] When you want a monthly summary table
- [ ] When you want to reduce the dataset to yearly totals
- [ ] When the data has no datetime index

## 11_4 · Period-over-Period Comparisons

### What does `df["cnt"].diff()` compute, and why is its first value `NaN`?
- [x] The absolute change from the previous row; the first row has no "previous" row to subtract
- [ ] The percent change; the first value is always zero
- [ ] The rolling mean; NaN marks the window start
- [ ] The cumulative sum; NaN means missing data

### Why use `.idxmax()` / `.idxmin()` instead of `.max()` / `.min()` on a time series?
- [x] They return the index label (the date) of the extreme value, telling you *when* it happened, not just the value
- [ ] They are faster versions of max/min
- [ ] They ignore missing values
- [ ] They return the column name instead of the value

### Why prefer `.pct_change()` over `.diff()` when comparing busy and quiet periods?
- [x] Absolute change has a scale problem — a drop of 500 means more in January (low baseline) than July (high baseline); percent change is comparable across scales
- [ ] `.diff()` cannot handle negative numbers
- [ ] `.pct_change()` removes missing values
- [ ] They always give the same ranking

### How do you compute a month-over-month percent change from daily data?
- [x] Resample to monthly totals first, then call `.pct_change()`
- [ ] Call `.pct_change()` directly on the daily data
- [ ] Use `.diff(30)` on the daily data
- [ ] Group by month name and subtract

### On monthly data, what does `.pct_change(12)` measure?
- [x] Year-over-year change — each month compared to the same month one year earlier, which removes the seasonal effect
- [ ] The change over the last 12 days
- [ ] A 12-month rolling average
- [ ] The change since the first month only

### Why is comparing each month to the same month a year earlier (rather than to the prior month) useful?
- [x] It removes the seasonal pattern, isolating true year-over-year growth rather than the expected summer-vs-winter swing
- [ ] It is the only way pct_change works
- [ ] It doubles the number of data points
- [ ] It converts the data to absolute change

## 11_5 · Seasonal Patterns

### With a `DatetimeIndex`, how do you get the month, weekday number, and weekday name?
- [x] `df.index.month`, `df.index.dayofweek` (0 = Monday), and `df.index.day_name()`
- [ ] `df.index.str.month`, `.str.weekday`, `.str.name`
- [ ] `df.month()`, `df.weekday()`, `df.name()`
- [ ] You must re-parse the dates each time

### How do you find the average rentals for each calendar month across both years?
- [x] `df.groupby(df.index.month)["cnt"].mean()`
- [ ] `df.resample("ME").mean()` only
- [ ] `df.index.month.mean()`
- [ ] `df["cnt"].rolling("month").mean()`

### In `df.index.dayofweek`, what does the value 0 represent?
- [x] Monday — the convention runs 0 (Monday) through 6 (Sunday)
- [ ] Sunday
- [ ] The first day in the dataset
- [ ] A missing weekday

### Why does the day-of-week chart for total rentals look fairly flat, while registered and casual riders don't?
- [x] The two user types pull in opposite directions — registered users peak on weekdays, casual users on weekends — so the total evens out
- [ ] The total chart is computed incorrectly
- [ ] Weekends have no data
- [ ] Total rentals are constant every day

### How do you build a month × day-of-week grid of average rentals for a heatmap?
- [x] `df.pivot_table(values="cnt", index=df.index.dayofweek, columns=df.index.month, aggfunc="mean")`
- [ ] `df.groupby("month").groupby("dayofweek").mean()`
- [ ] `df.resample("ME").resample("D").mean()`
- [ ] `df.rolling(7).pivot()`

### The components from `df.index.month` and `df.index.dayofweek` are described as "computed on the fly." What does that mean?
- [x] They are derived from the `DatetimeIndex` when accessed, not stored as separate columns in the DataFrame
- [ ] They are cached to disk on load
- [ ] They require a separate `pd.to_datetime()` call each time
- [ ] They are random until you set them
