from pathlib import Path
from subprocess import check_output


CC_TEMPLATE_ROOT = Path(__file__).parents[1].resolve()


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


def check_environment(path) -> None:
    reqs_path = path / "environment.yml"
    assert reqs_path.exists()
    assert no_curlies(reqs_path)


def check_r_install(path: Path, use_R: str) -> bool:
    """check if R is in the environment.yml file if "use_R" == "yes" """
    reqs_path = path / "environment.yml"
    use_R_ = True if use_R == "yes" else False
    # read in file and check if
    with open(reqs_path, "r") as file:
        data = file.read().replace("\n", "")
    return ("r-essentials" in data) == use_R_


def check_makefile(path: Path):
    makefile_path = path / "Makefile"
    assert makefile_path.exists()
    assert no_curlies(makefile_path)


def check_author(path: Path, author_name: str) -> bool:
    setup_ = path / "setup.py"
    args = ["python", str(setup_), "--author"]
    p = check_output(args).decode("ascii").strip()
    return p == author_name


def check_readme(path: Path, liz_code: str, project_name: str) -> bool:
    """Generate a README.md file with the project code and name"""
    readme_path = path / "README.md"
    assert readme_path.exists()
    assert no_curlies(readme_path)
    with open(readme_path) as fin:
        return liz_code + " - " + project_name == next(fin).strip()


def check_folders(path: Path, use_R: str) -> None:
    expected_dirs = [
        "data",
        "data/external",
        "data/interim",
        "data/processed",
        "data/raw",
        "notebooks",
        "notebooks/python",
        "references",
        "reports",
        "reports/figures",
        "src",
    ]
    expected_dirs += ["notebooks/R"] if use_R == "yes" else []

    abs_expected_dirs = [path / d for d in expected_dirs]
    abs_dirs = list(path.glob("**"))
    abs_dirs.remove(path)  # remove root dir
    if path / "src/__pycache__" in abs_dirs:
        abs_dirs.remove(path / "src/__pycache__")

    assert set(abs_dirs) == set(abs_expected_dirs)


def test_bake_python_project(cookies):
    args = {
        "lizard_code": "Liz.0.0",
        "project_name": "Google",
        "author_name": "Jeff Bezos",
        "use_R": "no",
    }

    result = cookies.bake(template=str(CC_TEMPLATE_ROOT), extra_context=args)

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == args["project_name"].lower()
    assert result.project_path.is_dir()
    path_ = result.project_path

    assert check_readme(path_, args["lizard_code"], args["project_name"])
    check_environment(path_)
    assert check_r_install(path_, args["use_R"])
    check_makefile(path_)
    assert check_author(path_, args["author_name"])
    check_folders(path_, args["use_R"])


def test_bake_python_and_R_project(cookies):
    args = {
        "lizard_code": "Liz.10.0",
        "project_name": "Microsoft ChatGPT implementation",
        "author_name": "Ronald Ronalds",
        "use_R": "yes",
    }

    result = cookies.bake(template=str(CC_TEMPLATE_ROOT), extra_context=args)

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.is_dir()
    path_ = result.project_path

    assert check_readme(path_, args["lizard_code"], args["project_name"])
    check_environment(path_)
    assert check_r_install(path_, args["use_R"])
    check_makefile(path_)
    assert check_author(path_, args["author_name"])
    check_folders(path_, args["use_R"])
