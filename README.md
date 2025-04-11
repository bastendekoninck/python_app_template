# Python App Template

A starter template with Poetry, pre-commit, pytest, GitHub Actions CI, and linting.

## Setup

```bash
poetry install
pre-commit install
```


Run tests:
```bash
pytest
```

Run the app:
```bash
poetry run python app/main.py
```

## Lint and format
```bash
pre-commit run --all-files
```