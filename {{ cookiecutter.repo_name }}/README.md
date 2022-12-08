{%- if cookiecutter.lizard_code -%}
    {{cookiecutter.lizard_code}} - {{cookiecutter.project_name}}
{% else %}
    {{cookiecutter.project_name}}
{% endif -%}
==============================

{{cookiecutter.short_description}}

## :notebook: Summary

## :open_file_folder: Project Organization
------------

    ├── Makefile           <- Makefile with commands like or `make clean` or `make lint`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
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

## :hammer_and_pick: Getting Started

Follow these steps:

1. Install and activate the conda environment.
    ```
    conda env create -f environment.yml
    conda activate {{ cookiecutter.repo_name }}
    ```

2.  (optional) make src/ available as a Python package so that you can include it in your notebooks
    ```
    pip install -e .
    ```

3. install the pre-commit hooks
    ```
    pre-commit install
    ```

4. Start coding!
