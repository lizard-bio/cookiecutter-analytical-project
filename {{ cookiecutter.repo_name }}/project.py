import questionary
from cookiecutter.main import cookiecutter

base_choices = [
    questionary.Choice('Add a general python submodule', value=0),
    questionary.Choice('Add a general R submodule', value=1),
#    questionary.Choice('Add a spatial submodule', value=2)
]

base_selection = questionary.select(
    "What do you want to do?",
    choices=base_choices
).ask()

if base_selection == 0:
    cookiecutter()
elif base_selection == 1:
    cookiecutter()
