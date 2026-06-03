# {{name}}

> {{description}}

## Getting started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Install

```bash
uv sync
```

### Run CLI

```bash
uv run python -m src.cli --name world
```

### Test

```bash
uv run pytest
```

## Development

### Format & lint

```bash
uv run ruff format .
uv run ruff check .
```

### Type check

```bash
uv run mypy src/
```

## Project structure

```
{{name}}/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── core.py           # Core logic
│   └── cli.py            # CLI entry point
├── tests/
│   └── test_core.py
└── README.md
```

## License

This project is licensed under the MIT License — see LICENSE for details.
