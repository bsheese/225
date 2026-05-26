# Module 07 — Data Visualization with Seaborn and Pandas

## Planning Document

**Stack:** seaborn 0.13, pandas 3.0, matplotlib 3.10
**Dataset:** Titanic (887 rows, 8 cols: `survived`, `pclass`, `name`, `sex`, `age`, `sibsp`, `parch`, `fare`)
**Audience:** Students who completed module 06 (pandas). No prior visualization experience.

---

## Module Philosophy and Design Notes

- **Question first, chart second.** Every visualization is introduced by posing a concrete question about the Titanic data ("Were younger passengers more likely to survive?"). The chart is the answer.
- **Basic to elaborated within each notebook.** A notebook on histograms starts with one variable, then layers in `hue=`, then faceting. Students see the same call extended, not five new functions.
- **Seaborn-first, matplotlib-second.** We use seaborn for the chart, matplotlib only for titles, axis labels, figure size, and saving. We are explicit about which library owns which piece.
- **Long-form (tidy) data is the seaborn idiom.** We connect every chart back to the columns of a DataFrame and to `x=`, `y=`, `hue=` arguments by name.
- **`.plot()` on pandas objects gets a brief introduction** because students will see it in the wild and it is convenient for quick looks, but seaborn is the primary tool.

---

## Recommended Learning Sequence

| Notebook | Title | Primary chart family |
|---|---|---|
| 07.1 | Why Visualize? Seaborn and the Figure-Level API | orientation, no new charts |
| 07.2 | Distributions of a Single Variable | `histplot`, `kdeplot`, `boxplot`, `violinplot` |
| 07.3 | Comparing Categories | `countplot`, `barplot`, `boxplot` by group |
| 07.4 | Relationships Between Two Numeric Variables | `scatterplot`, `regplot`, `lineplot` |
| 07.5 | Adding a Third Variable: `hue`, `size`, `style`, and Faceting | `relplot`, `catplot`, `displot` |
| 07.6 | Correlation, Heatmaps, and Pair Plots | `heatmap`, `pairplot`, `jointplot` |
| 07.7 | Polishing: Titles, Labels, Themes, Palettes, Saving | matplotlib styling on top of seaborn |
| 07.8 | Quick Plots from pandas: `.plot()` and When to Use It | `DataFrame.plot()` bridge |
| 07.9 | Exercises | mixed, Titanic-only |

The sequence mirrors a real analytical workflow: look at one variable, then compare groups, then look at pairs of variables, then layer in more dimensions, then summarize relationships across many variables, then make it presentable.

---

## 07.1 — Why Visualize? Seaborn and the Figure-Level API

**Central questions**
- What does a chart let us see that `.describe()` and `.value_counts()` do not?
- What is seaborn, and how does it relate to matplotlib and pandas?

**Progression**
1. **Motivation.** Show `df.describe()` for `age` and `fare`. Ask: "What shape is the age distribution? Is it symmetric? Are there outliers?" Then show a single `sns.histplot(df, x="age")` and make the point that the chart answers the question instantly.
2. **The three libraries.** One paragraph each: pandas owns the data, matplotlib owns the canvas, seaborn draws statistical charts on the canvas using DataFrame columns by name.
3. **Loading once.** Read the Titanic CSV from URL into `df`. This is the dataset used for the rest of the module. Show `df.head()`, `df.dtypes`, `df.shape`.
4. **The seaborn call signature.** Every chart takes `data=df` plus column names as strings: `sns.histplot(data=df, x="age")`. Compare to having to pass arrays in raw matplotlib.
5. **Axes-level vs figure-level (gentle).** Name the two families. `sns.histplot` returns an Axes. `sns.displot` returns a FacetGrid (a whole figure). Promise we will see both. Do not drill into `FacetGrid` internals yet.
6. **Themes once.** `sns.set_theme(style="whitegrid")` near the top of the notebook. Explain it changes defaults for everything that follows.

**Key calls introduced**
`sns.set_theme()`, `sns.histplot()` (as a teaser), `pd.read_csv()` (already known).

**Excluded**
No `hue`, no faceting, no styling beyond the default theme, no `.plot()`. This notebook is orientation only.

**Connections**
- *Previous:* Module 06 ended with `.describe()`, `.corr()`, and `pivot_table`. We pick up by asking what these numeric summaries miss.
- *Next:* 07.2 dives into the distribution of a single variable, the simplest possible chart.

---

## 07.2 — Distributions of a Single Variable

**Central questions**
- How is age distributed among Titanic passengers?
- What about fare? Is it skewed?
- Did survivors and non-survivors have different age distributions?

**Progression**
1. **Histogram, one variable.** `sns.histplot(data=df, x="age")`. Introduce `bins=`, then `binwidth=`. Read off shape: roughly symmetric, peak in 20s, tail of children and elderly.
2. **A skewed variable.** `sns.histplot(data=df, x="fare")`. Long right tail. Introduce `log_scale=True` to make the shape readable. Brief note: log scales are for multiplicative spread.
3. **KDE as a smoothed alternative.** `sns.kdeplot(data=df, x="age")`. Explain it estimates a smooth density. Mention bandwidth conceptually, not mathematically. Show `sns.histplot(..., kde=True)` as the combo.
4. **Box plot for one variable.** `sns.boxplot(data=df, x="fare")`. Read off median, IQR, outliers. Compare what the box plot shows vs the histogram (summary vs shape).
5. **Violin plot.** `sns.violinplot(data=df, x="age")`. Hybrid of box and KDE.
6. **Overlapping distributions (the elaborated step).** Did survivors and non-survivors have different ages? `sns.histplot(data=df, x="age", hue="survived", multiple="layer")`, then `multiple="stack"`, then `multiple="dodge"`. Show each and discuss which to pick when. Then `sns.kdeplot(data=df, x="age", hue="survived", common_norm=False, fill=True)` as the cleanest comparison.

**Key parameters to learn**
`x`, `bins`, `binwidth`, `log_scale`, `kde`, `hue`, `multiple` (`layer`/`stack`/`dodge`/`fill`), `common_norm`, `fill`.

**Excluded**
No two-variable charts (saved for 07.4). No faceting into subplots (saved for 07.5). No styling beyond axis labels.

**Connections**
- *Previous:* 07.1 promised that charts reveal what `.describe()` hides; we deliver on that here.
- *Next:* 07.3 moves from "one variable's shape" to "comparing groups," a natural extension of the `hue=` step we just introduced.

---

## 07.3 — Comparing Categories

**Central questions**
- How many passengers were in each class?
- What was the survival rate by sex? By class? By both?
- How did fare vary across classes?

**Progression**
1. **Counts per category.** `sns.countplot(data=df, x="pclass")`. Then `sns.countplot(data=df, x="pclass", hue="sex")`. Read off: most passengers in 3rd class, sex imbalance per class.
2. **Bar plot of a summary statistic.** `sns.barplot(data=df, x="sex", y="survived")`. Explain that with a 0/1 column, the mean is the proportion that survived. Introduce `estimator=` (default `"mean"`, but try `"median"`, `"sum"`). Introduce `errorbar=` (default 95% CI, set `errorbar=None` to hide).
3. **Two categorical splits in one bar plot.** `sns.barplot(data=df, x="pclass", y="survived", hue="sex")`. Now we can see "women in 1st class survived at nearly 100%, men in 3rd class at under 20%." Tie this back to a `groupby(["pclass","sex"])["survived"].mean()` from module 06; the chart is the same numbers.
4. **Box plot by group.** `sns.boxplot(data=df, x="pclass", y="fare")`. Note the heavy outliers; introduce `showfliers=False` and `log_scale=True` on the y-axis.
5. **Violin and strip alternatives.** `sns.violinplot(data=df, x="pclass", y="age", hue="sex", split=True)`. Then `sns.stripplot(...)` and `sns.swarmplot(...)` for showing every observation. Discuss when each is appropriate (sample size, overplotting).
6. **Ordering categories.** `order=["First","Second","Third"]` and `hue_order=`. Why default alphabetical ordering is often wrong.

**Key parameters to learn**
`x`, `y`, `hue`, `order`, `hue_order`, `estimator`, `errorbar`, `showfliers`, `split`, `log_scale`.

**Excluded**
No `catplot` (figure-level version waits for 07.5 where faceting is introduced). No point plots or count-by-time (no time column in this dataset).

**Connections**
- *Previous:* 07.2 introduced `hue=` for overlapping distributions; 07.3 reuses `hue=` for grouped comparisons.
- *Next:* 07.4 leaves categorical comparisons and asks how two numeric variables relate.

---

## 07.4 — Relationships Between Two Numeric Variables

**Central questions**
- Did people who paid more tend to be older?
- Was fare related to survival?
- Is there a trend of survival rate across age?

**Progression**
1. **Basic scatter.** `sns.scatterplot(data=df, x="age", y="fare")`. Read off: no obvious linear pattern, a few extreme fares. Introduce `alpha=` for overplotting.
2. **Scatter with a trend line.** `sns.regplot(data=df, x="age", y="fare")`. Adds linear fit + CI band. Discuss what the band means (uncertainty about the line, not the data). Mention `order=2` for a quadratic and `lowess=True` for a nonparametric smooth.
3. **Residual plot.** `sns.residplot(data=df, x="age", y="fare")` as a one-line check that a linear fit is poor here. Optional aside.
4. **Line plot.** Motivate: "We don't have a time series, but we can ask how the survival rate changes across age." `sns.lineplot(data=df, x="age", y="survived")` — seaborn aggregates y per x value with a CI band. Discuss what `lineplot` is averaging.
5. **Multi-line plot (the elaborated step).** `sns.lineplot(data=df, x="age", y="survived", hue="sex")`. Now we can compare the age-survival curve for men vs women. Then add `style="pclass"`.
6. **When to use which.** Quick decision rule: two raw numeric variables with no aggregation → `scatterplot`; two numeric variables with a model fit → `regplot`; one numeric x with aggregated y across groups → `lineplot`.

**Key parameters to learn**
`x`, `y`, `hue`, `style`, `alpha`, `order` (poly degree in regplot), `lowess`, `errorbar`.

**Excluded**
No `jointplot` (waits for 07.6 where it pairs with `pairplot`). No size mapping yet (waits for 07.5). No log scaling deep-dive.

**Connections**
- *Previous:* 07.3 compared groups on one numeric variable; 07.4 compares two numeric variables.
- *Next:* 07.5 takes the `hue=` and `style=` ideas from this notebook and generalizes them to faceting and figure-level functions.

---

## 07.5 — Adding a Third Variable: `hue`, `size`, `style`, and Faceting

**Central questions**
- How do we show more than two variables in one chart without it becoming a mess?
- When should an extra variable be a color, a marker, a size, or a separate subplot?

**Progression**
1. **Recap of semantic mappings.** `hue=` (color), `size=` (marker size), `style=` (marker shape / line dash). One scatter that uses all three: `sns.scatterplot(data=df, x="age", y="fare", hue="survived", size="pclass", style="sex")`. Then immediately critique it: too many channels, hard to read. Lesson: just because you can map four variables does not mean you should.
2. **Faceting as a cleaner alternative.** Introduce small multiples: one panel per category.
3. **`sns.relplot` — figure-level scatter/line.** `sns.relplot(data=df, x="age", y="fare", hue="survived", col="pclass", kind="scatter")`. Add `row="sex"` to get a 2x3 grid. Explain `col_wrap=` for when you only have `col=`.
4. **`sns.displot` — figure-level distributions.** Revisit 07.2's age histogram, now faceted: `sns.displot(data=df, x="age", hue="survived", col="pclass", kind="hist", multiple="stack")`. Try `kind="kde"`.
5. **`sns.catplot` — figure-level categorical.** Revisit 07.3's survival bars, now faceted by class: `sns.catplot(data=df, x="sex", y="survived", col="pclass", kind="bar")`. Try `kind="box"`, `kind="violin"`, `kind="count"`.
6. **Figure-level return type.** Each of these returns a `FacetGrid`. Show `g = sns.relplot(...)` then `g.set_axis_labels("Age", "Fare")`, `g.set_titles("Class {col_name}")`, `g.figure.suptitle("...")`. Just enough to label things.
7. **Aspect and height.** `height=3, aspect=1.2` to size facets. Why `figsize=` does not apply to figure-level functions.

**Key parameters to learn**
`hue`, `size`, `style`, `col`, `row`, `col_wrap`, `kind`, `height`, `aspect`, `g.set_axis_labels`, `g.set_titles`.

**Excluded**
No custom `FacetGrid` construction with `.map()` (advanced). No `JointGrid`. No `PairGrid` (kept whole in 07.6).

**Connections**
- *Previous:* 07.4 introduced `hue` and `style` on scatter and line; here we generalize.
- *Next:* 07.6 takes faceting to its logical extreme — every pair of variables at once.

---

## 07.6 — Correlation, Heatmaps, and Pair Plots

**Central questions**
- Which numeric variables in the Titanic data move together?
- Can we see all the pairwise relationships at once?

**Progression**
1. **Correlation matrix recap.** `df.select_dtypes("number").corr()` (callback to module 06). A table of numbers; hard to scan.
2. **Heatmap of a correlation matrix.** `sns.heatmap(corr, annot=True, cmap="vlag", vmin=-1, vmax=1, center=0)`. Discuss diverging vs sequential colormaps; why `center=0` matters for correlations.
3. **General heatmap of a pivot table.** Build a `pivot_table(index="pclass", columns="sex", values="survived", aggfunc="mean")` and heatmap it. Heatmaps work for any 2D numeric matrix, not just correlations.
4. **Jointplot — one pair, in depth.** `sns.jointplot(data=df, x="age", y="fare", kind="scatter")`. Then `kind="hex"` for dense data, `kind="kde"` for smoothed density, `kind="reg"` for a fit. Note the marginal histograms on the axes.
5. **Pair plot — every numeric pair at once.** `sns.pairplot(df, vars=["age","fare","sibsp","parch"])`. Diagonal = univariate, off-diagonal = scatter. Then `hue="survived"` to color points by outcome. Then `diag_kind="kde"` and `corner=True`.
6. **Interpreting the grid.** Walk through one row: "Age vs fare — no clear pattern. Age vs sibsp — younger passengers had more siblings aboard, makes sense." This is the payoff: a pair plot is a fast first look at any new dataset.

**Key parameters to learn**
`annot`, `fmt`, `cmap`, `vmin`/`vmax`/`center`, `kind` (in jointplot), `vars`, `hue`, `diag_kind`, `corner`.

**Excluded**
No clustermap (advanced). No custom `PairGrid` with mixed plot types on different cells.

**Connections**
- *Previous:* 07.5 introduced figure-level functions and small multiples; `pairplot` is a specialized small-multiple grid.
- *Next:* 07.7 takes the charts we now know how to make and makes them presentable.

---

## 07.7 — Polishing: Titles, Labels, Themes, Palettes, Saving

**Central questions**
- How do I make a chart that is good enough to put in a report?
- How do I control colors deliberately?

**Progression**
1. **The matplotlib layer underneath.** Capture the Axes from an axes-level call: `ax = sns.histplot(...)`. Then `ax.set_title()`, `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_xlim()`. For figure-level: `g.figure.suptitle()`, `g.set_axis_labels()`.
2. **Figure size.** `plt.figure(figsize=(8,5))` before an axes-level call. For figure-level, use `height=` and `aspect=`.
3. **Themes.** `sns.set_theme(style=...)` with `"darkgrid"`, `"whitegrid"`, `"white"`, `"ticks"`, `"dark"`. `sns.set_context("notebook" | "paper" | "talk" | "poster")` for font scaling.
4. **Palettes.** Three families: qualitative (`"deep"`, `"pastel"`, `"Set2"`) for unordered categories like sex; sequential (`"viridis"`, `"rocket"`) for ordered/numeric like fare; diverging (`"vlag"`, `"coolwarm"`) for data with a meaningful midpoint like correlation. Show `palette=` on `sns.barplot` and `cmap=` on `sns.heatmap`; note which functions take which.
5. **Color blindness and accessibility.** Brief: `"colorblind"` palette exists for a reason. Avoid red-green encoding of meaningful contrasts.
6. **Saving a figure.** `plt.savefig("survival_by_class.png", dpi=150, bbox_inches="tight")`. For figure-level: `g.savefig(...)`. PNG vs PDF vs SVG one-liner.
7. **A worked makeover.** Take an ugly default chart from 07.3 and rebuild it with a title, axis labels, ordered categories, a chosen palette, and a saved PNG. Side-by-side before/after.

**Key calls/parameters**
`ax.set_title`, `ax.set_xlabel`, `ax.set_ylabel`, `ax.set_xlim`, `ax.set_xticks`, `ax.tick_params(rotation=)`, `plt.figure(figsize=)`, `sns.set_theme`, `sns.set_context`, `sns.color_palette`, `palette=`, `cmap=`, `plt.savefig`.

**Excluded**
No custom matplotlib stylesheets (`plt.style.use`). No annotations with `ax.annotate`. No twin axes.

**Connections**
- *Previous:* 07.2–07.6 produced charts that answered questions; here we make those charts presentable.
- *Next:* 07.8 is a short bridge to pandas' built-in `.plot()` so students recognize it in the wild.

---

## 07.8 — Quick Plots from pandas: `.plot()` and When to Use It

**Central questions**
- I have seen `df.plot()` in tutorials. What is it?
- When should I reach for it instead of seaborn?

**Progression**
1. **The pandas plotting bridge.** `df["age"].plot(kind="hist", bins=30)`. Explain that pandas calls matplotlib directly; no seaborn involved. The result is a matplotlib Axes.
2. **Common shortcuts on Series and DataFrame.** `s.plot(kind="hist")`, `s.plot(kind="box")`, `s.plot(kind="kde")`; `df.plot(kind="scatter", x="age", y="fare")`; `df.value_counts().plot(kind="bar")`; `df.groupby("pclass")["survived"].mean().plot(kind="bar")` — note how naturally this chains off module 06's groupby work.
3. **Where pandas wins.** Quick one-line plots during exploration; plotting the result of a groupby/pivot without needing to reshape.
4. **Where seaborn wins.** Anything with `hue=`, anything statistical (CI bands, KDEs, regressions), faceting, polished output.
5. **They share an Axes.** You can call `df["age"].plot(kind="hist", ax=ax)` and then `sns.kdeplot(data=df, x="age", ax=ax)` on the same Axes. They cooperate via matplotlib.

**Key parameters**
`kind` (`"line"`, `"bar"`, `"barh"`, `"hist"`, `"box"`, `"kde"`, `"scatter"`), `ax=`, `figsize=`.

**Excluded**
No `pd.plotting.scatter_matrix` (we have `pairplot`). No `pd.plotting.parallel_coordinates`.

**Connections**
- *Previous:* 07.7 wrapped the seaborn story; 07.8 shows the pandas alternative for completeness.
- *Next:* 07.9 exercises.

---

## 07.9 — Exercises

Use the same Titanic DataFrame. Each exercise asks a question and requires choosing the right chart, not just running a recipe.

**Warm-up (recall a single call)**
1. Plot the distribution of `fare`. Choose appropriate bins and apply a log scale on the x-axis. Add a title.
2. Make a count plot of `pclass`. Order the bars First, Second, Third.
3. Show the mean survival rate by `sex` as a bar plot.

**Comparisons (add a `hue` or a `y`)**
4. On one set of axes, compare the age distribution of survivors vs non-survivors. Choose between `histplot(multiple=...)` and `kdeplot` and justify in a markdown cell.
5. Box plot of `fare` by `pclass`, split by `sex`. Hide outliers and use a log y-axis.
6. Bar plot of survival rate by `pclass` with `sex` as `hue`. Order classes correctly and label axes.

**Relationships (two numeric variables)**
7. Scatter plot of `age` vs `fare` colored by `survived`. Use `alpha=` to handle overplotting.
8. Line plot of survival rate as a function of `age`, with separate lines for each `sex`. Comment on the pattern.

**Faceting (figure-level)**
9. Use `sns.relplot` to make a scatter of `age` vs `fare`, faceted by `pclass` across columns and `sex` across rows.
10. Use `sns.catplot` to make box plots of `age` by `survived`, faceted by `pclass`.

**Synthesis (correlation/pair)**
11. Compute the correlation matrix of all numeric columns and display it as an annotated heatmap with a diverging colormap centered at 0.
12. Make a `pairplot` of `age`, `fare`, `sibsp`, `parch`, colored by `survived`, with KDEs on the diagonal. Write 2 to 3 sentences interpreting what you see.

**Polish (open-ended)**
13. Pick your favorite chart from exercises 1 to 12. Rebuild it with a custom title, axis labels, an appropriate palette, a chosen figure size, and save it to `figures/best_chart.png`.

**Challenge (optional)**
14. Engineer a categorical `age_group` column (Child < 13, Teen 13 to 17, Adult 18 to 59, Senior 60+) using `pd.cut`. Then plot survival rate by `age_group` and `sex` as a grouped bar chart with correct ordering.

Each exercise should have a markdown cell stating the question, an empty code cell for the student, and a "what to look for" hint cell that can be uncommented.

---

## Intentionally Excluded from the Entire Module

These belong in a follow-on visualization module:

| Excluded topic | Why deferred |
|---|---|
| Interactive plots (Plotly, Bokeh, Altair) | Different paradigm; deserves its own module. |
| Geographic / mapping plots | Requires geopandas and a different data shape. |
| Time series charts with date axes | Titanic has no time column; needs a time-indexed dataset. |
| 3D plots | Rarely useful, easy to misread. |
| Animation (`FuncAnimation`) | Not statistical visualization. |
| Custom matplotlib stylesheets and `rcParams` deep-dive | Beyond a first exposure. |
| `JointGrid` and `PairGrid` manual construction with `.map_lower/.map_upper` | Advanced; `jointplot`/`pairplot` cover 95% of needs. |
| `sns.clustermap` and dendrograms | Requires hierarchical clustering concepts. |
| Statistical model output beyond `regplot` | Belongs in a regression/modeling module. |
| Dashboards (Streamlit, Panel) | Application, not visualization fundamentals. |

---

## Cross-Cutting Conventions for All Notebooks

First code cell of every notebook:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid", context="notebook")
URL = "https://.../titanic.csv"   # one canonical URL, defined in 07.1 and reused
df = pd.read_csv(URL)
```

- Every chart cell is preceded by a markdown cell stating the question the chart answers.
- Every new function is introduced with its minimal signature first, then one parameter added per subsequent example.
- Callbacks to module 06 appear whenever a chart is just the visual form of a `.groupby()`, `.value_counts()`, `.corr()`, or `pivot_table` result the students already know how to produce. The chart is "the same numbers, drawn."
