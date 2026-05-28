# 07 — Data Visualization: Discussion Questions

## Why Visualize (07.1)
1. The notebook shows that two distributions can have the same mean and standard deviation but look completely different. Can you construct a small example (by hand or in Python) of two datasets with nearly identical `describe()` output but clearly different shapes? What does this tell you about relying on summary statistics alone?
2. Seaborn sits "on top of" matplotlib. What does that mean technically? If you wanted to change something that seaborn does not expose as a parameter — say, the exact font used for tick labels — where would you have to go? Try to find a concrete example.

## Distributions (07.2)
3. A histogram's shape changes when you change the number of bins. A KDE's shape changes when you change the bandwidth. What is the practical difference between tuning these two parameters? When would you prefer a histogram, and when would you prefer a KDE?
4. `common_norm=True` (the default in `sns.histplot` with `hue=`) normalizes all groups together so their areas sum to 1. `common_norm=False` normalizes each group independently. For the Titanic survival question, which is more informative, and why?
5. A box plot shows the median, Q1, Q3, and whiskers. A violin plot adds the full density shape. When does the extra information in the violin plot justify the added visual complexity? Give an example from the Titanic data where you would choose each.

## Comparing Categories (07.3)
6. `sns.barplot()` with default settings shows a confidence interval around each bar. What does that confidence interval represent? How does increasing the sample size (or simulating more passengers) affect the width of the interval?
7. `sns.countplot()` counts occurrences of a categorical variable. Could you produce the same result using pandas groupby and `sns.barplot()`? Try it. What is different about the two approaches?

## Relationships (07.4)
8. `sns.regplot()` draws a linear regression line through a scatter plot. Before looking at the line, predict: is there a positive or negative relationship between `pclass` and `fare`? Now look at the plot. Does the direction match your prediction? Is the relationship perfectly linear?
9. When would `sns.lineplot()` be misleading? What assumption does it make about how adjacent x-values are related? Name a case in the Titanic dataset where connecting points with a line would not make sense.

## Third Variable and Faceting (07.5)
10. The notebook encodes three variables at once using `hue=`, `size=`, and `style=` and concludes that the result is too noisy to read. At what point does adding more visual channels hurt rather than help? Is there a general principle, or does it depend on the specific chart?
11. Compare a single scatter plot using `hue="pclass"` to a faceted scatter plot using `col="pclass"`. What question does each version answer more easily? What does each version make harder to see?
12. The `col_wrap=` parameter wraps panels to a new row when there are too many to fit in one line. What would happen if you set `col_wrap=1`? Try it and describe the result.

## Correlation, Heatmaps, and Pairplots (07.6)
13. The correlation heatmap in 07.6 shows that `pclass` and `fare` have a strong negative correlation. Interpret this: what does it mean for a correlation to be negative? Does this direction make sense given what you know about the Titanic?
14. A high correlation between two variables does not tell you which one causes the other. The correlation between `pclass` and `survived` is negative (lower class, lower survival). List two possible explanations: one where class is the direct cause, and one where a third variable mediates the relationship.
15. `sns.pairplot()` shows all pairwise relationships at once. What is the downside of looking at all pairs simultaneously? When might it cause you to draw a false conclusion?

## Polishing (07.7)
16. The before-and-after makeover in 07.7 applies several changes: axis labels, a log scale, custom tick labels, and removing outliers. Rank these four changes by how much they improve the chart's readability, and explain your ranking.
17. Choosing a sequential palette for survival rate and a diverging palette for correlations is described as communicating "the nature of the data." What goes wrong if you use a diverging palette for survival rate (which ranges from 0 to 1)? What false impression might a reader form?
