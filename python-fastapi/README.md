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

### Run

```bash
uv run uvicorn src.main:app --reload
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
│   ├── main.py          # FastAPI app entry point
│   ├── config.py         # Settings via pydantic-settings
│   ├── api/
│   │   └── routes.py     # API routes
│   └── db/
│       └── engine.py     # SQLAlchemy engine
├── tests/
│   └── test_main.py
└── README.md
```

## License

This project is licensed under the MIT License — see LICENSE for details.
