# pypkg_template

[![CI](https://github.com/todo-group/pypkg_template/actions/workflows/pytest.yaml/badge.svg)](https://github.com/todo-group/pypkg_template/actions/workflows/pytest.yaml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Python package template with the modern toml-based style.

See [here](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) for more details.

## How to use

### `pip` development

```bash
git clone https://github.com/todo-group/pypkg_template.git
cd pypkg_template
pip install pip -U
pip install -e .[dev]
```

### `pipenv` development

```bash
git clone https://github.com/todo-group/pypkg_template.git
cd pypkg_template
pip install pip -U
pip install pipenv
pipenv install --dev
pipenv shell
```
