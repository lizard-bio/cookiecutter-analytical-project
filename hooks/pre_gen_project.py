import re
import sys


def validate_lizard_code():
    """if there is a lizard code given, make sure it is in the right format (Liz.X.X)"""
    MODULE_REGEX = r"^Liz\.[0-9]+\.[0-9]+$"

    lizard_code = "{{ cookiecutter.lizard_code }}"
    if lizard_code == "lizard_code (f.e. Liz.1.1)":
        lizard_code = ""
    if lizard_code:
        if not re.match(MODULE_REGEX, lizard_code):
            print("ERROR: %s is not a valid lizard code! Format is <Liz.X.X>" % lizard_code)

            # exits with status 1 to indicate failure
            sys.exit(1)


validate_lizard_code()
