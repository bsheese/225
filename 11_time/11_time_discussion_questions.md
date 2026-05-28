# 11 — Time Series: Discussion Questions

## Time Series Basics (11.1)
1. The notebook converts `dteday` to datetime and then sets it as the index in two separate steps. Why is the order important? What would break if you called `set_index("dteday")` before calling `pd.to_datetime()`?
2. `df.loc["2011"]` returns 365 rows. `df.loc["2011-06"]` returns 30. `df.loc["2011-06-15"]` would return a single row. This is called partial string indexing — the precision of the string controls the size of the selection. What would happen if you used `df.loc["2011-06-15":"2011-06-20"]`? How does this differ from boolean indexing with `(df.index >= "2011-06-15") & (df.index <= "2011-06-20")`? Give one scenario where you would prefer the partial string approach and one where boolean indexing is more flexible.

## Resampling (11.2)
3. `.resample("ME").sum()` and `.resample("ME").mean()` both produce 24 rows, one per month. For the `cnt` column (daily rental count), the sum is roughly 31 times larger than the mean in most months. For a column like `temp` (daily average temperature), which aggregation makes more sense, and why? What information would you lose by summing temperature?
4. The four frequency strings shown in the notebook — `"W"`, `"ME"`, `"QE"`, `"YE"` — all produce different numbers of rows from the same 731-day dataset. If you resampled to `"YE"` and then tried to compute a year-over-year percent change with `.pct_change()`, how many non-NaN values would you get? Why is annual resampling often too coarse for `.pct_change()` analysis?

## Rolling Windows (11.3)
5. A 7-day rolling mean produces `NaN` for the first six rows. A 30-day rolling mean produces `NaN` for the first 29 rows. If your dataset only covered a single month (31 days), how many usable rows would the 30-day rolling mean produce? What does this tell you about choosing a window size relative to dataset length?
6. The notebook overlays the raw daily line and the 7-day rolling mean on the same chart. The raw line is plotted with `alpha=0.4` to make it faint. Why is it useful to show the raw data at all, rather than just the smoothed version? Describe a specific pattern in the bike rental data that would be visible in the raw line but hidden or delayed in the 7-day rolling mean.

## Period-over-Period Comparisons (11.4)
7. `.pct_change()` on raw daily data produces a standard deviation of about 186% because individual days can swing dramatically. `.pct_change()` on monthly totals produces much smaller values. Explain why the aggregation step (daily to monthly) reduces the variability so dramatically. What statistical property does this relate to?
8. The notebook shows year-over-year growth was highest in January through March 2012 (115–157%) and moderated by summer 2012 (41–57%). This pattern is described as "common in young programs." What makes a young program produce this specific shape of year-over-year growth curve? If the program continued into 2013, would you expect the year-over-year percentages to continue declining, stay the same, or rise? What additional data would you need to predict this?

## Seasonal Patterns (11.5)
9. The weekday chart shows total rentals (`cnt`) are nearly flat across the week, because registered and casual riders pull in opposite directions. If you were a city planner trying to decide where to add new docking stations, which breakdown (total vs. by user type) would be more useful, and why? What question would each chart help you answer?
10. The heatmap uses `pivot_table` with `index=df.index.dayofweek` and `columns=df.index.month`. The cell values are means averaged across both years of data. Would the heatmap look different if you plotted 2011 and 2012 separately? Give a specific cell (month + day combination) where you would expect a meaningful difference between the two years, and explain why.

## Comparing Tools (11.1–11.5)
11. Rolling windows and resampling both smooth the time series, but in different ways. Give a concrete example of an analysis question about the bike data that you would answer with resampling, and a different question that you would answer with a rolling window. What is the fundamental difference between the two in terms of what they preserve and what they throw away?
12. The `.dt` accessor and `groupby()` treat time as a categorical variable (month number, day of week). Resampling and rolling windows treat time as a continuous dimension. Give an example of an insight about the bike data that requires the categorical view, and an insight that requires the continuous view. Could you derive either insight from the other representation, or do you genuinely need both?
