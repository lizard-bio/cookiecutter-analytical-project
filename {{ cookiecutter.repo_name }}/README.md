{%- if cookiecutter.lizard_code -%}
    {{cookiecutter.lizard_code}} - {{cookiecutter.project_name}}
{% else %}
    {{cookiecutter.project_name}}
{%- endif -%}
==============================

{{cookiecutter.short_description}}

## :notebook: Summary

## :open_file_folder: Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `conda env export --from-history -f environment.yml`
    │
    ├── project.py         <- python script to install new blocks ( r, python or others.)

--------

## :hammer_and_pick: Getting Started

Follow these steps:

### 0. First and foremost, make sure you have your ssh key linked to your github account. Once this has been set for your machine you never have to look back.
    Have a look at our notion page: https://www.notion.so/biolizard/SSH-to-Github-20a7bb9380c080958c30eb5b2552887c

### 1. Create or link up with a git repository

    Make a remote git repository.
    If we are hosting the code: [https://github.com/lizard-bio/](https://github.com/lizard-bio/)
    Remember the standardised naming of the code repo's!
    `<company>-<descriptive-project-name>`
    This is the same name as you have already submitted during initialisation proces.

    ```
    cd {{ cookiecutter.repo_name }}
    git init
    git remote add origin git@github.com:lizard-bio/<your-project-name>.git
    ```

### 2. Install and activate the conda environment.
    ```
    conda env create -f environment.yml
    conda activate {{ cookiecutter.repo_name }}
    ```

### 3. install the pre-commit hooks
    ```
    pre-commit install
    ```
    before doing our first commit.

### 4. first commit and push
    ```
    git add --all
    git commit -m "first commit"
    git push -f origin main
    ```

    The first time this pre-commit is setting up the correct envs. This will speed up for the following commits.

### 5.  (optional) make src/ available as a Python package so that you can include it in your notebooks
    ```
    pip install -e .
    ```

### 6.  run `project.py` to add coding blocks. Rerun as many time as needed.

### 7. Start coding!
