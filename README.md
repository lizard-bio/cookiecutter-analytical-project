# Cookiecutter Analytical Project

_A logical, reasonably standardized, but flexible project structure for working on and sharing an analytical project._

_(inspired by https://drivendata.github.io/cookiecutter-data-science/)_

## :muscle: Features
- Scaffolding an analytical project with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://cruft.github.io/cruft/)
- Code linting / formatting with [pre-commit](https://pre-commit.com/)
- Environment management through Conda's [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) file

## :sparkles: Using the template

1. Install [Cruft](https://cruft.github.io/cruft/) in your environment if you haven't done so.
This can be installed with [Conda](https://github.com/conda/conda-docs/blob/master/docs/source/miniconda.rst)/[Mamba](https://github.com/mamba-org/mamba) or pip depending on how you manage your Python packages:
    ``` bash
    conda config --add channels conda-forge
    conda install cruft
    ```
    or
    ``` bash
    pip install cruft
    ```

2. Create a new project on your workstation by running:
    ``` bash
    cruft create -f https://github.com/lizard-bio/cookiecutter-analytical-project
    ```

3.  Make sure you have a git repository initialized and linked to the remote upstream
    ```
    cd <your-project-name>
    git init
    git remote add github git@github.com:lizard-bio/<your-project-name>.git
    git add --all
    git commit -m "first commit"
    git push -f github main
    ```

4. Dive into the README.md of your new project for the next steps!

## :raised_hands: Contributing

This template is opinionated, but not afraid to be wrong. Best practices change, tools evolve, and lessons are learned. The goal of this project is to make it easier to start, structure, and share an analysis. Starting a discussion, filing an issue or even a pull request is encouraged!
