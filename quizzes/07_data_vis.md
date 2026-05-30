# 07 · Data Visualization

## 07_1 · Why Visualize

### Two columns can have identical means and standard deviations yet look completely different. What does a histogram reveal that those summary numbers cannot?
- [x] The **shape** of the distribution — where values cluster, skew, and how many peaks there are
- [ ] The exact mean and median to more decimal places
- [ ] The number of rows in the DataFrame
- [ ] The data type of the column

### The fare distribution is described as **right-skewed**. What does that mean?
- [x] Most values are low, but a small number of very high values stretch a long tail to the right and pull the mean upward
- [ ] The values are spread evenly across the whole range
- [ ] Most values are high, with a few low outliers
- [ ] The mean and median are exactly equal

### In the pandas / matplotlib / seaborn stack, what is each library's role?
- [x] pandas holds the data, matplotlib draws the canvas, and seaborn is the high-level statistical interface on top of matplotlib
- [ ] seaborn holds the data, pandas draws the canvas, matplotlib computes statistics
- [ ] All three are interchangeable ways to do the same thing
- [ ] matplotlib holds the data; seaborn and pandas just style it

### What does the typical seaborn call `sns.histplot(data=df, x="age")` expect for `data=` and `x=`?
- [x] A whole DataFrame for `data=`, and a column **name as a string** for `x=`
- [ ] A single column for `data=` and a number for `x=`
- [ ] Two raw NumPy arrays
- [ ] A file path for `data=` and a row index for `x=`

### What is the practical difference between an **axes-level** function (`sns.histplot`) and a **figure-level** function (`sns.displot`)?
- [x] Axes-level draws into one panel and returns a matplotlib `Axes`; figure-level manages a whole figure (possibly multiple panels) and returns a `FacetGrid`
- [ ] Axes-level is always faster; figure-level is always slower
- [ ] Axes-level cannot show titles; figure-level can
- [ ] They are aliases for the same function

### What does `sns.set_theme(style="whitegrid", context="notebook")` control?
- [x] `style=` sets the background/grid appearance; `context=` scales the font and line sizes (e.g. `"talk"` for presentations)
- [ ] `style=` chooses the chart type; `context=` chooses the dataset
- [ ] Both arguments only affect color
- [ ] It permanently edits the DataFrame's formatting

### Why is it easier to color a histogram by survival in seaborn than in raw matplotlib?
- [x] Because seaborn holds the whole DataFrame, you just add `hue="survived"`; in matplotlib you'd split the data and loop over groups yourself
- [ ] matplotlib cannot draw colored histograms at all
- [ ] seaborn requires no data, so coloring is automatic
- [ ] There is no difference; both need a manual loop

## 07_2 · Distributions

### Why does the number of histogram bins matter?
- [x] Too few bins hide real structure (e.g. a bump of young children); too many make the chart a noisy scatter of thin bars
- [ ] More bins are always strictly better
- [ ] Fewer bins are always strictly better
- [ ] The bin count has no visible effect on the chart

### When a variable like `fare` is strongly right-skewed, what does adding `log_scale=True` do?
- [x] Compresses the axis multiplicatively so the squashed low end spreads out and both regions become readable — without changing the data itself
- [ ] Removes the outliers from the dataset
- [ ] Takes the logarithm of every value permanently in the DataFrame
- [ ] Converts the histogram into a box plot

### What is a kernel density estimate (KDE)?
- [x] A smooth curve fitted through the data that estimates density, instead of the jagged bar counts of a histogram
- [ ] A table of the five-number summary
- [ ] A scatter plot of every raw point
- [ ] A correlation coefficient between two variables

### In a box plot, what do the box, the inner line, and the points beyond the whiskers represent?
- [x] The box is the interquartile range (25th–75th percentile), the line is the median, and the points beyond the whiskers are outliers
- [ ] The box is the mean ± standard deviation, the line is the mode, the points are missing values
- [ ] The box is the full range, the line is the mean, the points are duplicates
- [ ] The box is the 10th–90th percentile, the line is the minimum, the points are the maximum

### How does a violin plot combine the strengths of two other charts?
- [x] It shows the smooth KDE shape on both sides plus an embedded box-plot summary, giving shape and five-number summary together
- [ ] It shows raw counts plus a regression line
- [ ] It is a scatter plot with a histogram on each axis
- [ ] It is just a box plot with a different color

### When comparing the age distribution of survivors vs non-survivors, why use `common_norm=False` with a KDE?
- [x] It normalizes each group to its own data, so you compare proportions within each group rather than being misled by one group having more passengers
- [ ] It removes the smaller group from the chart
- [ ] It forces both curves to have identical shapes
- [ ] It converts the densities back into raw counts

### A box plot is described as trading shape for summary. What can it NOT show that a histogram or KDE can?
- [x] The shape of the data inside the box (e.g. whether the middle 50% is uniform or clustered to one end)
- [ ] The median value
- [ ] The presence of outliers
- [ ] The interquartile range

## 07_3 · Comparing Categories

### What does `sns.countplot(data=df, x="pclass")` show?
- [x] One bar per category, with height equal to the number of observations in that category
- [ ] The mean of `pclass`
- [ ] The survival rate for each class
- [ ] A scatter plot of class vs count

### What does the `order=[1, 2, 3]` argument do, and why use it?
- [x] Forces the bars into the sequence you specify, instead of seaborn's arbitrary default ordering
- [ ] Sorts the underlying DataFrame permanently
- [ ] Limits the chart to only the first three rows
- [ ] Reverses the colors of the bars

### `sns.barplot(data=df, x="sex", y="survived")` shows survival rate directly. Why?
- [x] `barplot` plots the mean of `y` per category by default, and the mean of the 0/1 `survived` column is the proportion who survived
- [ ] `barplot` counts rows, which happens to equal the rate
- [ ] It plots the maximum of `survived`, which is always 1
- [ ] Because `survived` is the x-axis

### What do the thin vertical lines on top of the bars in a default `sns.barplot()` represent?
- [x] 95% confidence intervals — the range of plausible values for the true group statistic
- [ ] The maximum and minimum values
- [ ] The standard deviation doubled
- [ ] Decorative error markers with no meaning

### In `sns.stripplot(data=df, x="pclass", y="age", jitter=True)`, what does `jitter=True` accomplish?
- [x] Adds a small horizontal wobble so overlapping points separate and become individually visible
- [ ] Randomly removes points to speed up rendering
- [ ] Adds random noise to the actual age values
- [ ] Sorts the points within each class

### When would you reach for `sns.swarmplot()` over `sns.stripplot()`, and what is its drawback?
- [x] It arranges points so they never overlap (cleaner for moderate data), but it becomes slow above a few thousand points
- [ ] It is always faster than stripplot
- [ ] It hides the individual points entirely
- [ ] It only works on categorical y-axes

### How do you split each bar in a count or bar plot by a second categorical variable like `sex`?
- [x] Add `hue="sex"`
- [ ] Add `split="sex"`
- [ ] Add a second `x="sex"`
- [ ] Call the plot function twice and overlay manually

## 07_4 · Relationships

### In a scatter plot of two numeric variables, what does an upward slope of the point cloud indicate?
- [x] A positive association — as x increases, y tends to increase
- [ ] That the two variables are identical
- [ ] A negative association
- [ ] That one variable is categorical

### Why set `alpha=0.4` on scatter points when many observations share similar values?
- [x] Transparency reveals density — overlapping regions look darker — which addresses overplotting
- [ ] It removes points that overlap
- [ ] It makes the chart render faster by dropping points
- [ ] It changes the points' color to gray

### `sns.regplot()` draws a fitted line with a shaded band. What does that band represent?
- [x] A 95% confidence interval for the location of the regression line itself (a wide band means the data weakly constrains the line)
- [ ] The range of all individual data points
- [ ] One standard deviation of the residuals
- [ ] The prediction for a single new observation

### If the relationship between two variables looks curved rather than straight, how can `sns.regplot()` adapt?
- [x] Fit a polynomial with `order=2` or a flexible nonparametric curve with `lowess=True`
- [ ] It cannot — regplot only draws straight lines
- [ ] Set `curved=True`
- [ ] Switch the x and y axes

### How does `sns.lineplot()` differ from a scatter plot of the same two columns?
- [x] It computes the **mean** of y at each x value and connects those means, showing an aggregated trend rather than individual points
- [ ] It draws every raw point and connects them in row order
- [ ] It only works with a time column
- [ ] It is identical to a scatter plot

### What does adding `hue="sex"` to `sns.lineplot()` produce, and why is it powerful?
- [x] A separate trend line per group, making it easy to compare how the trend differs across categories
- [ ] A single averaged line ignoring sex
- [ ] A scatter plot instead of lines
- [ ] An error, since lineplot does not accept hue

### Quick guide: which function shows individual points, which adds a model fit, and which shows an aggregated trend?
- [x] `scatterplot` shows raw points, `regplot` adds a fitted line, `lineplot` shows the mean trend of y across x
- [ ] `lineplot` shows raw points, `scatterplot` fits a line, `regplot` aggregates
- [ ] All three show the same thing with different colors
- [ ] `regplot` shows raw points, `scatterplot` fits a line, `lineplot` does nothing

## 07_5 · Third Variable & Faceting

### Besides `hue=` (color), what other visual channels map a data column to a mark's appearance?
- [x] `size=` (marker size) and `style=` (marker shape or line dash pattern)
- [ ] `bins=` and `order=`
- [ ] `data=` and `x=`
- [ ] `dpi=` and `figsize=`

### The notebook encodes four variables in one scatter plot (`hue`, `size`, `style`) and calls it hard to read. What is the lesson?
- [x] The eye can comfortably track only two or three visual properties at once; beyond that the chart becomes noise — use faceting instead
- [ ] seaborn has a bug with multiple channels
- [ ] You should always use all available channels
- [ ] Size is the only channel that ever works

### What is faceting (small multiples)?
- [x] Breaking a chart into a grid of panels — one per category value — that share the same axes so panels are directly comparable
- [ ] Drawing many variables in a single crowded panel
- [ ] Overlaying several charts with transparency
- [ ] Splitting the data into separate files

### What is the relationship between `sns.scatterplot`/`lineplot` and `sns.relplot()`?
- [x] `relplot` is the figure-level version; its `kind=` switches between scatter and line, and `col=`/`row=` create faceted panels
- [ ] `relplot` only draws bar charts
- [ ] `relplot` is an older, deprecated alias for scatterplot
- [ ] They are unrelated functions

### Figure-level functions like `relplot`, `displot`, and `catplot` return a `FacetGrid`. What does that change about customizing the chart?
- [x] You use `g.` methods (`g.set_axis_labels`, `g.set_titles`, `g.figure.suptitle`) instead of `ax.set_*` methods
- [ ] Nothing — you still use `ax.set_title`
- [ ] You cannot customize them at all
- [ ] You must convert the FacetGrid to an Axes first

### How do you size panels in a figure-level chart, since `figsize=` does not apply?
- [x] With `height=` (height of each panel in inches) and `aspect=` (width-to-height ratio)
- [ ] With `figsize=` exactly as in matplotlib
- [ ] You cannot control panel size
- [ ] With `dpi=` only

### What does `col_wrap=2` do when faceting by a column with several categories?
- [x] Limits the grid to two columns and wraps additional panels onto new rows
- [ ] Doubles the width of each panel
- [ ] Shows only the first two categories
- [ ] Merges two columns into one

## 07_6 · Correlation, Heatmaps & Pair Plots

### Why visualize a correlation matrix as a heatmap instead of reading the table of numbers?
- [x] Color lets you spot strong positive and negative correlations at a glance instead of scanning every cell
- [ ] The heatmap computes different, more accurate correlations
- [ ] The table cannot show negative values
- [ ] A heatmap removes the diagonal automatically

### What do `annot=True` and `fmt=".2f"` add to `sns.heatmap()`?
- [x] They print the numeric value in each cell, formatted to two decimal places
- [ ] They annotate the chart with the column dtypes
- [ ] They add a confidence interval to each cell
- [ ] They format the axis tick labels only

### For a correlation heatmap, why use a **diverging** colormap like `"vlag"` with `center=0` and `vmin=-1, vmax=1`?
- [x] Correlation has a meaningful zero and two directions; diverging colors (blue↔red) with white at 0 and fixed ±1 limits make sign and magnitude directly readable
- [ ] Diverging colormaps are the only ones seaborn supports
- [ ] It makes the diagonal disappear
- [ ] `center=0` deletes weak correlations

### A heatmap works on any 2-D numeric table, not just correlations. What is one example from the notebook?
- [x] Visualizing a `pivot_table` of survival rate by class and sex as a colored grid
- [ ] Drawing a single histogram
- [ ] Plotting one numeric column against itself
- [ ] Showing a scatter plot of two variables

### When should you choose a **sequential** colormap (e.g. `"YlOrRd"`) instead of a diverging one?
- [x] When the values all have the same sign and the question is just "how much?" (e.g. a survival rate from 0 to 1, with no meaningful midpoint)
- [ ] Whenever the data contains negative numbers
- [ ] Only for correlation matrices
- [ ] Sequential colormaps should never be used

### What does `sns.jointplot()` show?
- [x] A central scatter (or KDE) of two variables plus marginal histograms of each variable on the top and right
- [ ] A full grid of every pairwise relationship
- [ ] A correlation heatmap
- [ ] A single box plot

### What does `sns.pairplot()` produce, and what does `corner=True` do?
- [x] A grid of every pairwise scatter with distributions on the diagonal; `corner=True` shows only the lower triangle to halve the clutter
- [ ] A single scatter plot; `corner=True` moves the legend to a corner
- [ ] A correlation table; `corner=True` rounds the values
- [ ] One histogram per column stacked vertically

## 07_7 · Polishing

### Which methods set the title and axis labels on an axes-level (matplotlib `Axes`) chart?
- [x] `ax.set_title(...)`, `ax.set_xlabel(...)`, and `ax.set_ylabel(...)`
- [ ] `ax.title(...)` and `ax.labels(...)`
- [ ] `sns.set_title(...)` and `sns.set_labels(...)`
- [ ] `plt.rename(...)`

### How do you label a figure-level chart that returned a `FacetGrid` named `g`?
- [x] `g.set_axis_labels(...)`, `g.set_titles("{col_name}")`, and `g.figure.suptitle(...)`
- [ ] `g.set_xlabel(...)` and `g.set_title(...)` just like an Axes
- [ ] You cannot label figure-level charts
- [ ] `ax.set_title(...)` on the grid object

### In `sns.set_theme(style=..., context=...)`, what is the difference between `style` and `context`?
- [x] `style` controls the visual background (grid, ticks); `context` scales text and line sizes for the medium (`notebook`, `talk`, `paper`, `poster`)
- [ ] `style` sets font size; `context` sets the background
- [ ] Both set the color palette
- [ ] `context` chooses the chart type

### Palettes come in three families. Which family fits which data?
- [x] Qualitative for unordered categories, sequential for low→high magnitudes, diverging for data with a meaningful center/zero
- [ ] Qualitative for correlations, sequential for categories, diverging for counts
- [ ] All three are interchangeable
- [ ] Sequential for categories, qualitative for magnitudes, diverging for text

### Why might you deliberately choose the `"colorblind"` palette when encoding something important like survival?
- [x] It is designed so readers with common red-green color vision deficiency can still distinguish the categories
- [ ] It uses fewer colors so it renders faster
- [ ] It is the only palette that supports a legend
- [ ] It automatically sorts the categories

### When saving a chart with `plt.savefig("chart.png", dpi=150, bbox_inches="tight")`, what does `bbox_inches="tight"` do?
- [x] Trims extra whitespace around the figure so titles and labels are not cut off
- [ ] Increases the resolution to 300 dpi
- [ ] Converts the figure to a vector format
- [ ] Compresses the file using JPEG

### Which file format guidance does the notebook give?
- [x] Use `.png` for web/reports, `.pdf` or `.svg` for scalable vector output, and `.jpg` only when file size is a hard constraint (it adds artifacts)
- [ ] Always use `.jpg` for the smallest, cleanest charts
- [ ] `.svg` is raster and should be avoided
- [ ] Only `.png` can be saved from matplotlib
