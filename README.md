# pypkg_template

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
