# 07 · Data Visualization

## Data Visualization Quiz

### `sns.histplot()` returns a ____; `sns.displot()` returns a ____.
- [x] Axes; FacetGrid
- [ ] FacetGrid; Axes
- [ ] Figure; Axes
- [ ] Axes; Figure

### What does `sns.set_theme(style="whitegrid", context="notebook")` control?
- [ ] The data loaded into the chart and the number of bins
- [x] The background/grid appearance and the scale of text and lines
- [ ] The color palette and the chart type
- [ ] The figure size and the x-axis range

### A distribution with a long tail extending to the right and a mean above the median is called ____.
- [ ] left-skewed
- [ ] symmetric
- [x] right-skewed
- [ ] bimodal

### `sns.histplot(data=df, x="age", hue="survived", common_norm=False)` -- what does `common_norm=False` do?
- [ ] Normalizes all hue groups together so their areas sum to 1
- [x] Normalizes each hue group independently so each group's area sums to 1
- [ ] Disables normalization so the y-axis shows raw counts
- [ ] Removes the color distinction between hue groups

### You want to show the mean survival rate for each passenger class as bars with confidence intervals. Which function is most direct?
- [ ] sns.countplot()
- [x] sns.barplot()
- [ ] sns.histplot()
- [ ] sns.scatterplot()

### `sns.regplot()` adds a line to a scatter plot. What does that line represent?
- [ ] A smoothed KDE of the data
- [x] A linear regression fit
- [ ] The rolling mean of y
- [ ] The median of y within each x bin

### You have a scatter plot of age vs fare and want to encode sex as color. Which argument does this?
- [ ] col="sex"
- [x] hue="sex"
- [ ] style="sex"
- [ ] palette="sex"

### `sns.displot(data=df, x="age", col="pclass")` for a dataset with three classes creates how many panels?
- [ ] 1
- [ ] 2
- [x] 3
- [ ] It depends on col_wrap

### A Pearson correlation of -0.55 between pclass and fare means:
- [x] Higher class number (lower cabin class) is associated with lower fare
- [ ] Higher class number is associated with higher fare
- [ ] Class and fare are unrelated
- [ ] Fare determines class assignment

### Which colormap type is most appropriate for a heatmap showing correlations ranging from -1 to +1?
- [ ] Qualitative (e.g., "Set2")
- [ ] Sequential (e.g., "viridis")
- [x] Diverging (e.g., "vlag")
- [ ] Any colormap works equally well

### After drawing an axes-level chart `ax = sns.histplot(...)`, how do you add a title?
- [ ] plt.title("My title")
- [x] ax.set_title("My title")
- [ ] sns.set_title("My title")
- [ ] g.figure.suptitle("My title")

### You want to save a figure-level chart to PNG at 150 dpi. The chart is stored in `g`. Which call is correct?
- [ ] plt.savefig("chart.png", dpi=150, bbox_inches="tight")
- [x] g.savefig("chart.png", dpi=150, bbox_inches="tight")
- [ ] ax.savefig("chart.png", dpi=150)
- [ ] sns.savefig(g, "chart.png")
