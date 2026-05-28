# 08 — Data Cleaning: Discussion Questions

## What Makes Data Messy (08.1)
1. The notebook identifies five categories of messiness: wrong types, missing values, inconsistent formatting, structural problems, and date encoding. Rank them from most to least likely to cause a *silent* error (one where pandas produces a wrong result without raising an exception). Explain your ranking.
2. The `Pclass` column stores passenger class as integers 1, 2, and 3. What would happen if you computed `df["pclass"].mean()`? Is the result meaningful? What dtype would prevent that calculation from working?

## Missing Data (08.2)
3. The notebook checks whether passengers with missing ages had a different survival rate than those with recorded ages (they did not). What would it mean for the analysis if the survival rates *were* very different? Why would dropping the missing-age rows be more dangerous in that case?
4. `ffill()` and `interpolate()` both fill missing values, but they make different assumptions about the data. Give a concrete example of a dataset where `ffill()` would be the right choice and one where `interpolate()` would be better. What property of the data determines which is appropriate?
5. The notebook fills missing age values with the overall median (28.0). A more sophisticated approach would compute the median separately for each combination of class and sex. What advantage does the group-specific median have? Why might it matter for downstream analysis?

## Type Problems (08.3)
6. A CSV has a column of US zip codes: `["10001", "02134", "94103"]`. If pandas reads this as `int64`, what specific information is lost? How would you detect this problem from `df.dtypes` alone?
7. `pd.to_numeric(series, errors="coerce")` converts unparseable values to `NaN`. An alternative would be `errors="raise"`. When would you prefer `"coerce"`, and when would you prefer `"raise"`? What are the risks of each?

## String Cleaning (08.4)
8. The notebook applies `.str.strip().str.lower()` to normalize a sex column. Does the order of these two operations matter? Construct a specific example where reversing the order produces a different result.
9. `.str.replace(old, new, regex=False)` is described as safer when the replacement string contains characters like `.` or `*`. Why are those characters dangerous without `regex=False`? What would happen if you called `str.replace("1st.", "first", regex=True)` on a column?

## Splitting and Extracting (08.5)
10. `str.split(". ", n=1)` and `str.extract(r'(\w+)\.')` both extract the title from a Titanic name. The results are identical, but the two approaches make different assumptions about the data's structure. What does each approach assume? For which edge cases would `str.split` fail but `str.extract` succeed, or vice versa?
11. After extracting the title from passenger names, the notebook finds a title `"th"` appearing once. What name in the dataset might have produced that result, and why? Does this suggest a problem with the extraction pattern, the data, or both?

## Regular Expressions (08.6)
12. The phone-number cleaning pattern `[^\d]` removes every non-digit character. After cleaning, the notebook validates entries with `^\d{10}$`. Why are the anchors `^` and `$` necessary in the validation step? What false result would you get if you used `\d{10}` without the anchors?
13. The currency-cleaning pattern is `[^\d.]`, which keeps digits and periods. What would go wrong if a value had two decimal points, like `"$71..28"` or `"£7.2.5"`? How would you detect this problem after cleaning?

## Dates and Times (08.7)
14. The notebook shows that ISO 8601 format (`YYYY-MM-DD`) sorts correctly as a string by coincidence, while US format (`MM/DD/YYYY`) does not. Construct a specific counterexample: two US-format dates where alphabetical order gives the wrong chronological order.
15. After subtracting two `datetime64` columns, you have a `timedelta64` column. What is the difference between `.dt.seconds` and `.dt.total_seconds()`? When would they give different results?

## Complete Cleaning Pipeline (08.8)
16. The `clean_311()` function drops `current_activity` and `recent_action` because they appear to be mostly null. What risk does this create? How would you make the function safer against the case where a future version of the dataset has real values in those columns?
17. The pipeline validates by comparing "before" and "after" shapes and null counts. What kinds of errors would this validation NOT catch? Give two specific examples of problems that would pass this check but still leave the data incorrect.
