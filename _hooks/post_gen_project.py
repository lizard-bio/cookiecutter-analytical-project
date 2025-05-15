import os
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.use_R != "yes" %} notebooks/R {% endif %}',
]

def remove_paths(paths):
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                os.unlink(path)

remove_paths(REMOVE_PATHS)