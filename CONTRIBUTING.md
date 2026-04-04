# Contributing to ghscaff-boilerplate

Thanks for wanting to contribute a template to ghscaff-boilerplate! This guide explains how to create and submit a high-quality template.

---

## Quick Start

1. Clone this repository
2. Create a template directory following the structure below
3. Test it locally (see [Testing](#testing))
4. Open a Pull Request

---

## Template Structure

Every template must follow this layout:

```
my-language-template/
├── template.toml          ← required: metadata and configuration
├── src/
│   └── main.ext           ← required: entry point for the language
├── README.md              ← required: template with placeholders
├── .github/
│   └── workflows/
│       └── ci.yml         ← required: GitHub Actions CI workflow
├── .gitignore             ← recommended: language-specific
└── LICENSE                ← optional: license file
```

### Minimal Example

```
rust/
├── template.toml
├── Cargo.toml
├── src/main.rs
├── README.md
├── .github/workflows/ci.yml
└── .gitignore
```

---

## `template.toml` Format

This is the most important file — it tells ghscaff how to handle your template:

```toml
[template]
name = "my-template"
language = "MyLang"
description = "Short description (1 line)"
version = "0.1.0"

[placeholders]
# Define which placeholders are available
name = "Project name (kebab-case)"
description = "Project description"

[files]
# List files to include in the generated repo
include = [
  "Cargo.toml",
  "src/main.rs",
  "README.md",
  ".github/workflows/ci.yml"
]

[gitignore]
# GitHub's gitignore template name
template = "Rust"

[ci]
# CI workflow configuration
workflow_name = "CI"
branches = ["main", "develop"]
runs_on = "ubuntu-latest"
```

### `[template]` Section

| Key | Type | Required | Example |
|-----|------|----------|---------|
| `name` | string | ✅ | `"rust"`, `"python"`, `"node"` |
| `language` | string | ✅ | `"Rust"`, `"Python"`, `"Node.js"` |
| `description` | string | ✅ | `"Rust CLI with Cargo and CI"` |
| `version` | string | ✅ | `"0.1.0"` |

### `[placeholders]` Section

Define what placeholders are available:

```toml
[placeholders]
name = "Project name (kebab-case)"
description = "Project description"
author = "Author name"
```

These placeholders can be used in any text file with `{{placeholder_name}}` syntax.

### `[files]` Section

List the files to include. Paths are relative to the template directory:

```toml
[files]
include = [
  "Cargo.toml",
  "src/main.rs",
  "README.md",
  ".github/workflows/ci.yml",
  ".gitignore"
]
```

Binary files (images, PDFs, etc.) are automatically excluded even if listed.

### `[gitignore]` Section

GitHub provides pre-made `.gitignore` templates. Specify which one:

```toml
[gitignore]
template = "Rust"  # GitHub's template name
```

Common values:
- `"Rust"` — for Rust projects
- `"Python"` — for Python projects
- `"Node"` — for Node.js projects
- `"Java"` — for Java projects

See [GitHub's gitignore templates](https://api.github.com/repos/github/gitignore/contents) for valid names.

### `[ci]` Section

Describe the CI workflow:

```toml
[ci]
workflow_name = "CI"           # Name in the workflow file
branches = ["main", "develop"]  # Trigger branches
runs_on = "ubuntu-latest"       # GitHub Actions runner
```

---

## Placeholder Usage

### Available Placeholders

By default, these placeholders are always available:

| Placeholder | Source | Example |
|-------------|--------|---------|
| `{{name}}` | User's repo name | `"my-cli"` |
| `{{description}}` | User's repo description | `"A powerful CLI"` |
| `{{author}}` | Git config or wizard | `"John Doe"` |

Define custom placeholders in `template.toml`:

```toml
[placeholders]
organization = "Your organization name"
```

Then use `{{organization}}` in your template files.

### Using Placeholders

Add placeholders to **any text file** using `{{placeholder_name}}`:

**Cargo.toml:**
```toml
[package]
name = "{{name}}"
description = "{{description}}"
```

**src/main.rs:**
```rust
//! {{description}}
//! 
//! Author: {{author}}

fn main() {
    println!("Welcome to {{name}}!");
}
```

**README.md:**
```markdown
# {{name}}

> {{description}}

**Author:** {{author}}
```

**.github/workflows/ci.yml:**
```yaml
name: CI
jobs:
  test:
    name: Test {{name}}
    runs-on: ubuntu-latest
```

**Binary files** are never processed for placeholders (images, fonts, .pyc, etc.).

---

## CI Workflow Best Practices

### 1. Minimal and Fast

Keep the workflow lightweight:

```yaml
name: CI
on:
  pull_request:
    branches: [main, develop]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
      - run: cargo fmt --check
      - run: cargo clippy -- -D warnings
      - run: cargo test
```

### 2. Standard Checks

Include:
- ✅ Format check (fmt, prettier, black, etc.)
- ✅ Linting (clippy, eslint, pylint, etc.)
- ✅ Tests (unit and integration)
- ✅ Build verification

### 3. Use Official Actions

Prefer official GitHub Actions:
- `actions/checkout@v4`
- `actions/setup-python@v4`
- `actions/setup-node@v4`
- `actions-rs/toolchain@v1` (for Rust)

### 4. Cache Dependencies

For faster runs, cache package manager output:

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cargo/registry
    key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.lock') }}
```

---

## README Template Guidelines

Your `README.md` should:

1. **Use placeholders:**
   ```markdown
   # {{name}}
   
   > {{description}}
   ```

2. **Include setup instructions:**
   ```markdown
   ## Getting Started
   
   ### Requirements
   - Rust 1.70+
   
   ### Build
   ```bash
   cargo build --release
   ```
   ```

3. **Document the structure:**
   ```markdown
   ## Project Structure
   
   ```
   {{name}}/
   ├── Cargo.toml
   ├── src/
   │   └── main.rs
   ├── tests/
   └── README.md
   ```
   ```

4. **Include development guide:**
   ```markdown
   ## Development
   
   ```bash
   cargo test
   cargo fmt
   cargo clippy
   ```
   ```

---

## Testing Your Template

### Local Testing

1. **Verify placeholders are replaced:**
   ```bash
   grep -r "{{" my-template/
   # Should return empty if all placeholders are inside template.toml or properly used
   ```

2. **Check file syntax:**
   - TOML files: use a TOML validator
   - YAML files: use yamllint
   - Rust files: `rustfmt` should parse them

3. **Validate `template.toml`:**
   ```bash
   cat my-template/template.toml
   # Should have all required sections: [template], [placeholders], [files], [gitignore], [ci]
   ```

### Integration Testing with ghscaff

If you have ghscaff installed:

```bash
# Create a test template directory
cd ghscaff-boilerplate
mkdir -p test-output

# Manually copy your template to the cache
mkdir -p ~/.ghscaff/boilerplate/my-template
cp -r my-template/* ~/.ghscaff/boilerplate/my-template/

# Run ghscaff and test the template
export GITHUB_TOKEN=test_token
ghscaff new --dry-run
# Select your template language during the wizard
```

---

## Submission Checklist

Before opening a PR, verify:

- [x] Template directory structure follows the guidelines
- [x] `template.toml` has all required sections
- [x] All placeholders are defined in `template.toml`
- [x] Placeholders are used correctly in files (e.g., `{{name}}`)
- [x] `.gitignore` references a valid GitHub template
- [x] CI workflow is valid GitHub Actions YAML
- [x] No sensitive data (API keys, passwords, credentials)
- [x] No generated artifacts (`.o`, `.pyc`, `node_modules`, etc.)
- [x] Files are UTF-8 encoded
- [x] README has clear instructions
- [x] License (MIT or compatible) is included

---

## Example: Python Template Submission

```
python/
├── template.toml
├── pyproject.toml
├── src/{{name}}/__init__.py
├── src/{{name}}/main.py
├── tests/test_main.py
├── README.md
├── .github/workflows/ci.yml
└── .gitignore
```

**template.toml:**
```toml
[template]
name = "python"
language = "Python"
description = "Python package with poetry and pytest"
version = "0.1.0"

[placeholders]
name = "Package name (snake_case)"
description = "Package description"

[files]
include = [
  "pyproject.toml",
  "src/{{name}}/__init__.py",
  "src/{{name}}/main.py",
  "tests/test_main.py",
  "README.md"
]

[gitignore]
template = "Python"

[ci]
workflow_name = "CI"
branches = ["main", "develop"]
runs_on = "ubuntu-latest"
```

**pyproject.toml:**
```toml
[project]
name = "{{name}}"
description = "{{description}}"
version = "0.1.0"
```

**README.md:**
```markdown
# {{name}}

> {{description}}

## Installation

```bash
pip install -e .
```

## Development

```bash
pytest
```
```

---

## Questions?

- 📖 Check [README.md](README.md)
- 💬 Open an [issue](https://github.com/JheisonMB/ghscaff-boilerplate/issues)
- 🐦 Reach out on Twitter: [@JheisonMB](https://twitter.com/JheisonMB)

---

## Code of Conduct

Be respectful, inclusive, and professional. We're building something awesome together.

---

Thanks for contributing! 🎉
