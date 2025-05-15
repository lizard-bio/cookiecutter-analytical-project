#!/bin/bash

echo "What do you want to add to the project?"
echo "1) Add an R subfolder"
echo "2) Add a Python subfolder"
read -p "Enter your choice [1-2]: " choice

case $choice in
    1)
        cruft create git@github.com:lizard-bio/cookiecutter-analytical-project.git --directory="block/r_general"  --branch="feature/switch_to_functional_setup"
        ;;
    2)
        cruft create git@github.com:lizard-bio/cookiecutter-analytical-project.git --directory="block/python_general"  --branch="feature/switch_to_functional_setup"
        ;;
    *)
        echo "Invalid choice."
        ;;
esac