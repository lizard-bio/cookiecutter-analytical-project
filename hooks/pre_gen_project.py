import re
import sys


def validate_lizard_code():
    MODULE_REGEX = r"^Liz\.[0-9]+\.[0-9]+$"

    lizard_code = "{{ cookiecutter.lizard_code }}"

    if not re.match(MODULE_REGEX, lizard_code):
        print("ERROR: %s is not a valid lizard code!" % lizard_code)

        # exits with status 1 to indicate failure
        sys.exit(1)


validate_lizard_code()
