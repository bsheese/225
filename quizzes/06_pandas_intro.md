# 06 · Pandas Intro

## Pandas Intro Quiz

### What does `pd.Series([10, 20, 30]).iloc[1]` return?
- [ ] 10
- [x] 20
- [ ] 30
- [ ] An error; iloc requires a label

### You run `s = pd.Series({'a': 1, 'b': 2, 'c': 3})`. What is `s.loc['b']`?
- [ ] 1
- [x] 2
- [ ] 3
- [ ] KeyError

### Which method produces a statistical summary (count, mean, std, min, max) of a Series?
- [ ] .info()
- [x] .describe()
- [ ] .summary()
- [ ] .stats()

### What does `df[['name', 'age']]` return?
- [ ] A Series with two elements
- [x] A DataFrame with two columns
- [ ] A list of two Series
- [ ] An error; use .loc[] for multiple columns

### Which selector always uses integer positions, regardless of the index?
- [ ] .loc[]
- [x] .iloc[]
- [ ] .at[]
- [ ] []

### You want rows where age > 30 AND pclass == 1. Which expression is correct?
- [ ] df[df['age'] > 30 and df['pclass'] == 1]
- [x] df[(df['age'] > 30) & (df['pclass'] == 1)]
- [ ] df[(df['age'] > 30) | (df['pclass'] == 1)]
- [ ] df.filter(age > 30, pclass == 1)

### After filtering a DataFrame, you want to add a new column to the result without affecting the original. What should you do first?
- [ ] Use inplace=True
- [x] Call .copy() on the filtered result
- [ ] Assign directly; pandas handles this automatically
- [ ] Reset the index before assigning

### Which method fills missing values with the string 'Unknown'?
- [ ] df['col'].dropna('Unknown')
- [ ] df['col'].replace(NaN, 'Unknown')
- [x] df['col'].fillna('Unknown')
- [ ] df['col'].isnull() = 'Unknown'

### What does `df.groupby('sex')['survived'].mean()` compute?
- [ ] The average survival value for the entire dataset
- [ ] The mean of the 'sex' column
- [x] The survival rate for each unique value of 'sex'
- [ ] The number of survivors grouped by sex

### You have a GroupBy result where 'pclass' is the index. You want it as a regular column. What do you call?
- [ ] .set_index()
- [x] .reset_index()
- [ ] .reindex()
- [ ] .drop_index()

### What is the main difference between pd.crosstab() and pd.pivot_table()?
- [ ] crosstab is faster; pivot_table is slower
- [x] crosstab counts observations; pivot_table aggregates any numeric column with any function
- [ ] pivot_table only works with dates; crosstab works with any data
- [ ] They are identical; just different syntax

### What does pd.crosstab(df['sex'], df['survived'], normalize='index') produce?
- [ ] Counts of each sex/survived combination
- [ ] Proportions across the entire table summing to 1
- [x] Proportions within each sex group: each row sums to 1
- [ ] Proportions within each survived group: each column sums to 1
