# 07 — Data Visualization: Glossary

**aesthetic mapping** — A rule that connects a column of data to a visible property of the chart marks (color, position, size, shape). In seaborn, `hue=`, `size=`, and `style=` are aesthetic mappings.

**axes-level function** — A seaborn function that draws a single chart into one matplotlib `Axes` and returns that `Axes` object. Examples: `sns.histplot()`, `sns.scatterplot()`, `sns.boxplot()`.

**bandwidth** — In a KDE, the parameter that controls how smooth the curve is. A small bandwidth follows every bump in the data; a large bandwidth produces a flatter, more averaged curve.

**bins** — The equal-width intervals used to group values in a histogram. More bins show finer detail; fewer bins show the overall shape. Choice of bins can change the apparent story.

**box plot** — A chart that summarizes a distribution with five numbers: the minimum, 25th percentile (Q1), median (Q2), 75th percentile (Q3), and maximum. Points beyond the whiskers are drawn individually as outliers.

**colormap** — An ordered sequence of colors used to represent numerical values on a continuous scale. Seaborn distinguishes qualitative (unordered categories), sequential (low to high), and diverging (negative to zero to positive) colormaps.

**diverging palette** — A colormap with a neutral midpoint and two hues branching in opposite directions; appropriate for data with a meaningful center, such as correlations ranging from -1 to +1.

**ECDF (empirical cumulative distribution function)** — A chart that shows, for each value x, what fraction of the data falls at or below x. Unlike a histogram, it does not depend on bin width.

**faceting** — Splitting a chart into a grid of small panels, one per category value, so that the same chart type can be compared across groups. Also called "small multiples."

**FacetGrid** — The object returned by seaborn's figure-level functions (`sns.relplot`, `sns.displot`, `sns.catplot`). Used to set labels, titles, and save the figure.

**figure** — In matplotlib, the whole image (the blank sheet of paper). A figure can contain multiple axes panels.

**figure-level function** — A seaborn function that creates a complete figure, potentially with multiple panels, and returns a `FacetGrid`. Examples: `sns.relplot()`, `sns.displot()`, `sns.catplot()`.

**heatmap** — A grid where each cell is colored according to a numeric value; used to visualize matrices such as correlation tables or pivot tables.

**histogram** — A chart that divides a continuous variable into bins and draws a bar whose height represents the count (or density) of values in each bin.

**KDE (kernel density estimate)** — A smoothed continuous curve that approximates the underlying probability distribution of a variable, estimated from the data points.

**pairplot** — A grid of charts showing every pairwise combination of numeric columns in a dataset: scatter plots in the off-diagonal cells, distribution plots on the diagonal.

**qualitative palette** — A colormap for unordered categories; colors should be perceptually distinct but not suggest any ordering.

**right-skewed** — A distribution whose tail extends further to the right than to the left; a small number of very large values pull the mean above the median.

**sequential palette** — A colormap for data that goes from low to high; color smoothly progresses from light to dark (or low-saturation to high-saturation) to suggest magnitude.

**small multiples** — See *faceting*.

**violin plot** — A chart that combines a box plot with a mirrored KDE, showing both the summary statistics and the full shape of the distribution.

**visual channel** — Any perceptual property of a mark that can carry information: position (x, y), color (hue, luminance), size, shape, orientation. Also called an encoding channel.
