{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    │
    ├── notebooks          <- Notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │   └── python
    │   └── R
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `conda env export --from-history -f environment.yml`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported in notebooks f.e;
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module


--------

## Getting Started

```
make setup_project
```

Alternatively you can follow these steps:

1. Install the conda environment.
```
conda env create -f environment.yml
```

2.  make src/ available as a package so that you can include it in your notebooks
```
pip install -e .
```

3. make sure you have a git repository initialised
```
git init
```

4. install the pre-commit hooks
```
pre-commit install
```
