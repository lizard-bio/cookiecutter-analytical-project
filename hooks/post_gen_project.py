import os
import shutil
import sys
import subprocess

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

# Create conda environment
try:
    subprocess.check_call(["mamba", "env", "create", "-f", "environment.yml"])
except subprocess.CalledProcessError:
    print("Failed to create conda environment")
    sys.exit(1)

# Install additional R packages from GitHub
if "{{ cookiecutter.use_R }}" == "yes":
    # Create R script content
    r_script = """
    setRepositories(ind = c(1:6, 8))
    devtools::install_github("lizard-bio/nature-grade-visualization-playground", subdir="BioLizardStyleR")
    """

    # Write to temporary file
    with open("install_r_packages.R", "w") as f:
        f.write(r_script)

    # Run the R script within the conda environment
    try:
        subprocess.check_call(["Rscript", "install_r_packages.R"])
        # Clean up
        subprocess.check_call(["rm", "install_r_packages.R"])
    except subprocess.CalledProcessError:
        print("Failed to install R packages")
        sys.exit(1)