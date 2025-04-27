# Python package template

A python package template that contains everything you need to create a package.

- a very basic function (`add_digit`) and tests
- a `.gitignore` with all the basic stuff we don't want to track
- 3 github actions:
  - format the code with `ruff`
  - run the tests with `pytest`
  - deploy documentation website with `mkdocs`
- a `pyproject.toml` with all the basic elements
- a `.pre-commit-config.yaml` which checks the formatting of the code
- a licence file (MIT)

<br>

## How to use this template

- Click on `Use this template` and `Create a new repository`
- Clone your repo

```bash
git clone https://github.com/your_name/package_name.git
```

- Replace info in `pyproject.toml`
- Replace **all** `package_name` to your actual package
- Replace **all** `your_name` to your Github username/organization
- Change the `LICENSE` file to your actual license (optional)
- Ensure everything works well

```bash
uv sync --all-extras --dev
uv run pytest
```

- Preview the documentation website

```bash
uv run mkdocs serve
```
