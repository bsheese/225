# 07 · Data Visualization

## 07_1 · Why Visualize

### Two columns can have identical means and standard deviations yet look completely different. What does a histogram reveal that those summary numbers cannot?
- [x] The **shape** of the distribution — where values cluster, how skewed it is, and how many peaks there are
- [ ] The exact mean and median calculated to more decimal places
- [ ] The total number of rows in the DataFrame
- [ ] The data type stored in that column

### The fare distribution is described as **right-skewed**. What does that mean?
- [x] Most values are low, but a few very high values stretch a long tail to the right and pull the mean upward
- [ ] The values are spread evenly across the entire range
- [ ] Most values are high, with a few low outliers at the bottom
- [ ] The mean and median happen to be exactly equal

### In the pandas / matplotlib / seaborn stack, what is each library's role?
- [x] pandas holds the data, matplotlib draws the canvas, and seaborn is the high-level statistical interface on top of matplotlib
- [ ] seaborn holds the data, pandas draws the canvas, and matplotlib computes statistics
- [ ] All three are interchangeable ways to accomplish the same thing
- [ ] matplotlib holds the data; seaborn and pandas only handle styling

### What does the typical seaborn call `sns.histplot(data=df, x="age")` expect for `data=` and `x=`?
- [x] A whole DataFrame for `data=`, and a column **name as a string** for `x=`
- [ ] A single column Series for `data=` and an integer for `x=`
- [ ] Two raw NumPy arrays, one for each argument
- [ ] A file path for `data=` and a row index number for `x=`

### What is the practical difference between an **axes-level** function (`sns.histplot`) and a **figure-level** function (`sns.displot`)?
- [x] Axes-level draws into one panel and returns a matplotlib `Axes`; figure-level manages a whole figure (possibly multi-panel) and returns a `FacetGrid`
- [ ] Axes-level is always faster; figure-level is always slower to render
- [ ] Axes-level cannot include titles; figure-level supports them
- [ ] They are aliases that call the same underlying function

### What does `sns.set_theme(style="whitegrid", context="notebook")` control?
- [x] `style=` sets the background/grid appearance; `context=` scales font and line sizes (e.g. `"talk"` for presentations)
- [ ] `style=` chooses the chart type; `context=` chooses which dataset to use
- [ ] Both arguments only affect the color palette used
- [ ] It permanently edits the DataFrame's display formatting

### Why is it easier to color a histogram by survival in seaborn than in raw matplotlib?
- [x] seaborn holds the whole DataFrame, so you just add `hue="survived"`; in matplotlib you'd split the data and loop over groups yourself
- [ ] matplotlib cannot draw colored histograms at all
- [ ] seaborn requires no data argument, so coloring is automatic
- [ ] There is no difference; both require the same amount of manual work

## 07_2 · Distributions

### Why does the number of histogram bins matter?
- [x] Too few bins hide real structure (e.g. a bump of young children); too many make the chart a noisy scatter of thin bars
- [ ] More bins are always strictly better for any dataset
- [ ] Fewer bins are always strictly better for any dataset
- [ ] The bin count has no visible effect on the chart's appearance

### When a variable like `fare` is strongly right-skewed, what does adding `log_scale=True` do?
- [x] Compresses the axis multiplicatively so the squashed low end spreads out and both regions become readable — without changing the data itself
- [ ] Removes the outliers from the dataset permanently
- [ ] Takes the logarithm of every value and stores it in the DataFrame
- [ ] Converts the histogram into a box plot automatically

### What is a kernel density estimate (KDE)?
- [x] A smooth curve fitted through the data that estimates the density, instead of jagged bar counts
- [ ] A table of the five-number summary statistics
- [ ] A scatter plot showing every individual raw data point
- [ ] A correlation coefficient between two numeric variables

### In a box plot, what do the box, the inner line, and the points beyond the whiskers represent?
- [x] The box is the IQR (25th–75th percentile), the line is the median, and the points beyond whiskers are outliers
- [ ] The box is the mean ± standard deviation, the line is the mode, and the points are missing values
- [ ] The box is the full data range, the line is the mean, and the points are duplicates
- [ ] The box is the 10th–90th percentile, the line is the minimum, and the points are the maximum

### How does a violin plot combine the strengths of two other charts?
- [x] It shows the smooth KDE shape on both sides plus an embedded box-plot summary, giving shape and key statistics together
- [ ] It shows raw counts on one side and a regression line on the other
- [ ] It is a scatter plot with a marginal histogram on each axis
- [ ] It is just a box plot rendered with a different color scheme

### When comparing the age distribution of survivors vs non-survivors, why use `common_norm=False` with a KDE?
- [x] It normalizes each group to its own data, so you compare proportions within each group rather than being misled by group size differences
- [ ] It removes the smaller group from the chart entirely
- [ ] It forces both curves to be scaled to identical shapes
- [ ] It converts the density estimates back into raw counts

### A box plot is described as trading shape for summary. What can it NOT show that a histogram or KDE can?
- [x] The shape of the data inside the box (e.g. whether the middle 50% is uniform or clustered to one end)
- [ ] The median value of the distribution
- [ ] The presence of outlier data points
- [ ] The size of the interquartile range

## 07_3 · Comparing Categories

### What does `sns.countplot(data=df, x="pclass")` show?
- [x] One bar per category, with height equal to the number of observations in that category
- [ ] The mean value of `pclass` across all rows
- [ ] The survival rate for each passenger class
- [ ] A scatter plot of class label vs. observation count

### What does the `order=[1, 2, 3]` argument do, and why use it?
- [x] Forces the bars into the sequence you specify, instead of seaborn's default ordering
- [ ] Sorts the underlying DataFrame permanently in that order
- [ ] Limits the chart to displaying only the first three rows
- [ ] Reverses the colors of each bar in the chart

### `sns.barplot(data=df, x="sex", y="survived")` shows survival rate directly. Why?
- [x] `barplot` plots the mean of `y` per category by default, and the mean of a 0/1 column is the proportion who survived
- [ ] `barplot` counts rows, which happens to equal the rate
- [ ] It plots the maximum of `survived`, which is always 1
- [ ] The survival rate appears because `survived` is on the y-axis

### What do the thin vertical lines on top of the bars in a default `sns.barplot()` represent?
- [x] 95% confidence intervals — the range of plausible values for the true group statistic
- [ ] The maximum and minimum values in that group
- [ ] The standard deviation, doubled, of the group values
- [ ] Decorative error markers with no statistical meaning

### In `sns.stripplot(data=df, x="pclass", y="age", jitter=True)`, what does `jitter=True` accomplish?
- [x] Adds a small horizontal wobble so overlapping points separate and become individually visible
- [ ] Randomly removes some points to speed up rendering
- [ ] Adds random noise to the underlying age values in the data
- [ ] Sorts the individual points within each class group

### When would you reach for `sns.swarmplot()` over `sns.stripplot()`, and what is its drawback?
- [x] It arranges points so they never overlap (cleaner for moderate data), but becomes slow above a few thousand points
- [ ] It is always faster than stripplot on any dataset size
- [ ] It hides all the individual data points behind summary statistics
- [ ] It only works correctly when the y-axis is categorical

### How do you split each bar in a count or bar plot by a second categorical variable like `sex`?
- [x] Add `hue="sex"`
- [ ] Add `split="sex"`
- [ ] Add a second `x="sex"` argument
- [ ] Call the plot function twice and overlay the results manually

## 07_4 · Relationships

### In a scatter plot of two numeric variables, what does an upward slope of the point cloud indicate?
- [x] A positive association — as x increases, y tends to increase
- [ ] That the two variables are identical to each other
- [ ] A negative association between the two variables
- [ ] That one of the variables is categorical

### Why set `alpha=0.4` on scatter points when many observations share similar values?
- [x] Transparency reveals density — overlapping regions look darker — addressing overplotting
- [ ] It removes any points that overlap with other points
- [ ] It makes the chart render faster by dropping some points
- [ ] It changes the point color to a gray shade

### `sns.regplot()` draws a fitted line with a shaded band. What does that band represent?
- [x] A 95% confidence interval for the location of the regression line (a wide band means data weakly constrains the line)
- [ ] The range of all individual data points in the dataset
- [ ] One standard deviation of the residuals around the line
- [ ] The prediction interval for a single new observation

### If the relationship between two variables looks curved rather than straight, how can `sns.regplot()` adapt?
- [x] Fit a polynomial with `order=2` or a flexible nonparametric curve with `lowess=True`
- [ ] It cannot adapt — regplot only draws straight lines
- [ ] Set `curved=True` in the function call
- [ ] Switch the x and y axes to straighten the relationship

### How does `sns.lineplot()` differ from a scatter plot of the same two columns?
- [x] It computes the **mean** of y at each x value and connects those means, showing an aggregated trend
- [ ] It draws every raw point and connects them in the original row order
- [ ] It only works correctly when one column is a time variable
- [ ] It is identical to a scatter plot with lines added

### What does adding `hue="sex"` to `sns.lineplot()` produce, and why is it powerful?
- [x] A separate trend line per group, making it easy to compare how the trend differs across categories
- [ ] A single averaged line that ignores the sex grouping
- [ ] A scatter plot rendered with lines instead of points
- [ ] An error, since lineplot does not accept a hue argument

### Quick guide: which function shows individual points, which adds a model fit, and which shows an aggregated trend?
- [x] `scatterplot` shows raw points, `regplot` adds a fitted line, `lineplot` shows the mean trend of y across x
- [ ] `lineplot` shows raw points, `scatterplot` fits a line, `regplot` aggregates by group
- [ ] All three show exactly the same output with different default colors
- [ ] `regplot` shows raw points, `scatterplot` fits a line, `lineplot` does nothing useful

## 07_5 · Third Variable & Faceting

### Besides `hue=` (color), what other visual channels map a data column to a mark's appearance?
- [x] `size=` (marker size) and `style=` (marker shape or line dash pattern)
- [ ] `bins=` (histogram bins) and `order=` (category order)
- [ ] `data=` (the DataFrame) and `x=` (the column name)
- [ ] `dpi=` (resolution) and `figsize=` (figure dimensions)

### The notebook encodes four variables in one scatter plot (`hue`, `size`, `style`) and calls it hard to read. What is the lesson?
- [x] The eye can track only two or three visual properties at once; beyond that the chart becomes noise — use faceting instead
- [ ] seaborn has a known bug when multiple visual channels are specified
- [ ] You should always use all available visual channels for maximum information
- [ ] Size is the only visual channel that ever works well in practice

### What is faceting (small multiples)?
- [x] Breaking a chart into a grid of panels — one per category value — that share the same axes so panels are directly comparable
- [ ] Drawing many variables together in a single crowded panel
- [ ] Overlaying several charts using transparency to show all groups
- [ ] Splitting the underlying data into separate CSV files

### What is the relationship between `sns.scatterplot`/`lineplot` and `sns.relplot()`?
- [x] `relplot` is the figure-level version; its `kind=` switches between scatter and line, and `col=`/`row=` create faceted panels
- [ ] `relplot` only draws bar charts, not scatter or line plots
- [ ] `relplot` is an older, deprecated alias for `scatterplot`
- [ ] They are completely unrelated functions that serve different purposes

### Figure-level functions like `relplot`, `displot`, and `catplot` return a `FacetGrid`. What does that change about customizing the chart?
- [x] You use `g.` methods (`g.set_axis_labels`, `g.set_titles`, `g.figure.suptitle`) instead of `ax.set_*` methods
- [ ] Nothing changes — you still use the standard `ax.set_title` method
- [ ] You cannot customize figure-level charts at all
- [ ] You must convert the FacetGrid back to an Axes object first

### How do you size panels in a figure-level chart, since `figsize=` does not apply?
- [x] With `height=` (height of each panel in inches) and `aspect=` (width-to-height ratio)
- [ ] With `figsize=` exactly as you would in matplotlib
- [ ] Panel size cannot be controlled in figure-level functions
- [ ] With `dpi=` only, which scales all dimensions proportionally

### What does `col_wrap=2` do when faceting by a column with several categories?
- [x] Limits the grid to two columns and wraps additional panels onto new rows
- [ ] Doubles the width of each individual panel in the grid
- [ ] Shows only the first two category values in the facet
- [ ] Merges two adjacent columns into a single wider panel

## 07_6 · Correlation, Heatmaps & Pair Plots

### Why visualize a correlation matrix as a heatmap instead of reading the table of numbers?
- [x] Color lets you spot strong positive and negative correlations at a glance instead of scanning every cell
- [ ] The heatmap computes different, more accurate correlation values
- [ ] The number table cannot display negative correlation values
- [ ] A heatmap removes the diagonal entries automatically

### What do `annot=True` and `fmt=".2f"` add to `sns.heatmap()`?
- [x] They print the numeric value in each cell, formatted to two decimal places
- [ ] They annotate each cell with the column's data type
- [ ] They add a confidence interval band to each cell
- [ ] They format the axis tick labels only, not the cell values

### For a correlation heatmap, why use a **diverging** colormap like `"vlag"` with `center=0` and `vmin=-1, vmax=1`?
- [x] Correlation has a meaningful zero and two directions; diverging colors with white at 0 and fixed ±1 limits make sign and magnitude directly readable
- [ ] Diverging colormaps are the only type that seaborn supports
- [ ] It removes the diagonal line from the heatmap display
- [ ] `center=0` removes any cells with weak correlation values

### A heatmap works on any 2-D numeric table, not just correlations. What is one example from the notebook?
- [x] Visualizing a `pivot_table` of survival rate by class and sex as a colored grid
- [ ] Drawing a single histogram of one numeric column
- [ ] Plotting one numeric column against its own values
- [ ] Showing a scatter plot of two numeric variables

### When should you choose a **sequential** colormap (e.g. `"YlOrRd"`) instead of a diverging one?
- [x] When all values have the same sign and the question is just "how much?" (e.g. a survival rate from 0 to 1, with no meaningful midpoint)
- [ ] Whenever the data contains any negative numbers
- [ ] Only when visualizing correlation matrices
- [ ] Sequential colormaps are unsuitable and should never be used

### What does `sns.jointplot()` show?
- [x] A central scatter (or KDE) of two variables plus marginal histograms on the top and right
- [ ] A full grid of every pairwise relationship in the DataFrame
- [ ] A correlation heatmap of all numeric columns
- [ ] A single box plot for one numeric variable

### What does `sns.pairplot()` produce, and what does `corner=True` do?
- [x] A grid of every pairwise scatter with distributions on the diagonal; `corner=True` shows only the lower triangle to halve the clutter
- [ ] A single scatter plot; `corner=True` moves the legend to a corner
- [ ] A correlation number table; `corner=True` rounds all values
- [ ] One histogram per column stacked vertically in a column

## 07_7 · Polishing

### Which methods set the title and axis labels on an axes-level (matplotlib `Axes`) chart?
- [x] `ax.set_title(...)`, `ax.set_xlabel(...)`, and `ax.set_ylabel(...)`
- [ ] `ax.title(...)` and `ax.labels(...)` called together
- [ ] `sns.set_title(...)` and `sns.set_labels(...)` on the seaborn object
- [ ] `plt.rename(...)` applied to the figure

### How do you label a figure-level chart that returned a `FacetGrid` named `g`?
- [x] `g.set_axis_labels(...)`, `g.set_titles("{col_name}")`, and `g.figure.suptitle(...)`
- [ ] `g.set_xlabel(...)` and `g.set_title(...)` just like a regular Axes object
- [ ] You cannot add labels to figure-level charts at all
- [ ] `ax.set_title(...)` called directly on the grid object

### In `sns.set_theme(style=..., context=...)`, what is the difference between `style` and `context`?
- [x] `style` controls the visual background (grid, ticks); `context` scales text and line sizes for the medium (`notebook`, `talk`, `paper`, `poster`)
- [ ] `style` sets the font size; `context` sets the background color
- [ ] Both arguments control only the color palette used
- [ ] `context` chooses the chart type to render

### Palettes come in three families. Which family fits which data?
- [x] Qualitative for unordered categories, sequential for low→high magnitudes, diverging for data with a meaningful center/zero
- [ ] Qualitative for correlation matrices, sequential for categories, diverging for row counts
- [ ] All three palette families are interchangeable for any data type
- [ ] Sequential for categories, qualitative for magnitudes, diverging for text

### Why might you deliberately choose the `"colorblind"` palette when encoding something important like survival?
- [x] It is designed so readers with common red-green color vision deficiency can still distinguish the categories
- [ ] It uses fewer colors and therefore renders the chart faster
- [ ] It is the only palette that displays a legend correctly
- [ ] It automatically sorts the categories in the best order

### When saving a chart with `plt.savefig("chart.png", dpi=150, bbox_inches="tight")`, what does `bbox_inches="tight"` do?
- [x] Trims extra whitespace around the figure so titles and labels are not cut off
- [ ] Increases the output resolution to 300 dpi automatically
- [ ] Converts the raster figure to a vector format
- [ ] Compresses the file using JPEG lossy compression

### Which file format guidance does the notebook give?
- [x] Use `.png` for web/reports, `.pdf` or `.svg` for scalable vector output, and `.jpg` only when file size is a hard constraint (it adds artifacts)
- [ ] Always use `.jpg` for the smallest and cleanest output
- [ ] `.svg` is a raster format and should be avoided
- [ ] Only `.png` can be saved from matplotlib
