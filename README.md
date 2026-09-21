# CS/DS 225: Data Science

Course materials for CS/DS 225 at Illinois Wesleyan University, taught by Brad Sheese. These modules cover the data-analysis core of the course: pandas, visualization, data cleaning, aggregation, SQL, and time series. They assume Python experience but no prior pandas or statistics exposure. Module numbering follows the course schedule; earlier modules of the course are not hosted in this repository.

## Modules

| Module | Topic | Dataset |
|---|---|---|
| [06 · pandas Intro](06_pandas_intro/) | Series, DataFrames, selecting and filtering, cleaning basics, GroupBy, pivot tables | Titanic |
| [07 · Data Visualization](07_data_vis/) | matplotlib and seaborn: distributions, categories, relationships, faceting, polishing | Titanic (seaborn) |
| [08 · Data Cleaning](08_data_cleaning/) | Missing data, type problems, string cleaning, regex, dates, a full cleaning pipeline | Titanic, auto MPG, NYC taxis, Chicago 311 |
| [09 · Data Aggregation](09_data_aggregation/) | GroupBy in depth: multiple keys, `agg`, `transform`, `filter`, `pivot_table` | Gapminder |
| [10 · pandas and SQL](10_pandas_sql/) | SQLite from pandas: SELECT, WHERE, GROUP BY, JOIN, and when to use which tool | Gapminder |
| [11 · Time Series](11_time/) | Datetime indexes, resampling, rolling windows, period comparisons, seasonality | Bike share daily rentals |

Each module folder contains numbered instruction notebooks (`NN_M_Topic.ipynb`), an exercises notebook, a module outline, a glossary, and discussion questions. Work through the instruction notebooks in order; the exercises come last and cover the whole module.

## Using the notebooks

Every notebook opens with an "Open in Colab" badge, so you can run it in the browser with nothing installed. Notebooks are self-contained: each one loads its own data from a public URL, so you can open any single notebook on its own in a fresh runtime.

## Blank notebook

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsheese/225/main?urlpath=lab/tree/notebook_empty_225.ipynb)

Need a scratch notebook with the standard imports (`pandas`, `seaborn`, `matplotlib.pyplot`) and nothing else? Launch [`notebook_empty_225.ipynb`](notebook_empty_225.ipynb) on Binder with the badge above.

## Practice quizzes

Self-serve practice quizzes for every module are published at **https://bsheese.github.io/225/**. They are built from the Markdown in [`quizzes/`](quizzes/) and cover the instruction notebooks section by section.

## Running locally

```bash
git clone https://github.com/bsheese/225.git
cd 225
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

The notebooks were written and executed against the pinned versions in [`requirements.txt`](requirements.txt), including pandas 3.0. Other versions will mostly work, but output details may differ.
