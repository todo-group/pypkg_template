# 📦 pypkg_template

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/todo-group/pypkg_template/actions/workflows/test.yaml/badge.svg)](https://github.com/todo-group/pypkg_template/actions/workflows/test.yaml)
[![docs](https://github.com/todo-group/pypkg_template/actions/workflows/docs.yaml/badge.svg)](https://github.com/todo-group/pypkg_template/actions/workflows/docs.yaml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Python package template with the modern [toml-based style](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

## ☑ Features

- Modern `pyproject.toml`-based configuration
  - Dynamic versioning with `setuptools_scm`
  - Typing support with `py.typed`
- Testing with `nox`/`pytest`
  - Cross-platform CI integrations
  - Coverage measurement with `pytest-cov`
- Various linters
  - `ruff` for linting, formatting, and import sorting
  - `mypy`/`pyright` for static type checking
- Documentation with `sphinx`
  - Building with CI

## 🛠 How to use

### 🐍 `pip` development

```bash
git clone https://github.com/todo-group/pypkg_template.git
cd pypkg_template
pip install pip -U
pip install -e .[dev]
```

### 🗃 `pipenv` development

```bash
git clone https://github.com/todo-group/pypkg_template.git
cd pypkg_template
pip install pip -U
pip install pipenv
pipenv install --dev
pipenv shell
```

### 🎨 Format/lint

```bash
# Run all linters
pre-commit run -a
```

### 🧪 Test

```bash
# Run unit tests in an isolated venv
nox
```

### 📜 Build docs.

```bash
# Build docs and output to `docs/build`
sphinx-build docs/source docs/build
```

### 📦 Build package

```bash
# Build sdist/wheel and output to `dist`
python3 -m build
```
