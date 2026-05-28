# 07 — Data Visualization: Module Outline

## Audience
Undergrad CS and data science majors with Python experience and module 06 pandas skills; no prior data visualization exposure.

## Dataset
Titanic passenger data loaded via `sns.load_dataset("titanic")` (891 rows, 7 columns: survived, pclass, sex, age, sibsp, parch, fare). Four rows more than the module 06 CSV; column names are identical.

## Notebooks

| Notebook | Topic | Key Concepts |
|---|---|---|
| 07.1 | Why Visualize? | Motivation for charts, three-library stack (pandas/seaborn/matplotlib), axes-level vs figure-level, `sns.set_theme()` |
| 07.2 | Distributions | `histplot`, `kdeplot`, `ecdf`, `boxplot`, `violinplot`; bins, bandwidth, `hue=`, `common_norm=` |
| 07.3 | Comparing Categories | `barplot`, `countplot`, `stripplot`, `swarmplot`; ordering, confidence intervals, `estimator=` |
| 07.4 | Relationships | `scatterplot`, `regplot`, `lineplot`; `hue=`, `ci=`, choosing between scatter/reg/line |
| 07.5 | Third Variable & Faceting | Visual channels (`hue=`, `size=`, `style=`); figure-level functions (`relplot`, `displot`, `catplot`); `col=`, `row=`, `col_wrap=` |
| 07.6 | Correlation, Heatmaps, Pairplot | `df.corr()`, `sns.heatmap()`, `sns.pairplot()`; `annot=True`, `cmap=`, sequential vs diverging palettes |
| 07.7 | Polishing | `ax.set_title/xlabel/ylabel`, `figsize=`, `height=`/`aspect=`, palette families, `plt.savefig()`, before-vs-after makeover |

## What Is Intentionally Excluded
- pandas `.plot()` method
- Interactive visualization (Plotly, Bokeh, Altair)
- Animation and time-lapse charts
- 3D charts
- Custom matplotlib `Artist` objects below the `Axes` level
- Geographic / map visualizations

## Learning Sequence
Why charts (07.1) → one-variable distributions (07.2) → categorical comparisons (07.3) → two-variable relationships (07.4) → adding a third variable and faceting (07.5) → all-pairs overview (07.6) → polishing and saving (07.7) → exercises (07.9)
