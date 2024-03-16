# About

Repo for testing testing in Python3.

Had some issue with import when running test files from a `tests/` directory.
Solved by adding `pyproject.toml` file with the following content:

```toml
[tool.pytest.ini_options]
pythonpath = "."
```
