# ghscaff-boilerplate

Official boilerplate template registry for [ghscaff](https://github.com/JheisonMB/ghscaff).

This repository contains the source templates that power ghscaff's repository scaffolding. Each template is a complete boilerplate for a specific language, ready to be downloaded and customized during the `ghscaff new` wizard.

---

## Template Structure

Each template is organized as:

```
template-name/
├── template.toml          # Metadata and configuration
├── Cargo.toml             # Package manifest (with {{name}}, {{description}})
├── src/main.rs            # Entry point boilerplate
├── README.md              # Template with placeholders
├── .github/workflows/ci.yml
└── .gitignore
```

### `template.toml`

Metadata file that describes the template:

```toml
[template]
name = "rust"
language = "Rust"
description = "Rust CLI template with cargo, CI/CD, and standard structure"
version = "1.0.0"

[placeholders]
name = "Project name (kebab-case)"
description = "Short description of the project"

[files]
include = [
  "Cargo.toml",
  "src/main.rs",
  "README.md",
  ".github/workflows/ci.yml"
]

[gitignore]
template = "Rust"

[ci]
workflow_name = "CI"
branches = ["main", "develop"]
runs_on = "ubuntu-latest"
```

### Placeholder Syntax

Use `{{placeholder}}` syntax in template files for dynamic content:

```toml
[package]
name = "{{name}}"
version = "0.1.0"
edition = "2021"
description = "{{description}}"
```

```markdown
# {{name}}

> {{description}}
```

```rust
fn main() {
    println!("Hello from {{name}}!");
}
```

Available placeholders:
- `{{name}}` — Project name (kebab-case)
- `{{description}}` — Project description
- `{{author}}` — Author name (from git config or wizard)

---

## Usage in ghscaff

When you run `ghscaff new` and select a language:

1. **Download** — The template is downloaded from this repository (cached locally)
2. **Resolve** — Placeholders are replaced with your answers from the wizard
3. **Commit** — Files are committed to your new GitHub repository

```bash
# Interactive wizard
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
ghscaff

# During the wizard:
# Step 3: Language / template → Choose "Rust"
# Step 1: Repository name → Enter "my-cli"
# Step 1: Description → Enter "A powerful CLI tool"
#
# Result: Repository created with {{name}} → "my-cli", {{description}} → "A powerful CLI tool"
```

---

## Contributing a Template

Thanks for wanting to contribute a template! Follow these steps:

### 1. Template Structure

Create a directory with this layout:

```
my-template/
├── template.toml          ← required: metadata
├── main_file.ext          ← required: entry point
├── src/                   ← optional: additional source files
├── tests/                 ← optional: test files
├── docs/                  ← optional: documentation
└── .github/               ← optional: GitHub Actions workflows
```

### 2. Create `template.toml`

```toml
[template]
name = "my-template"
language = "MyLang"
description = "Short description of the template"
version = "0.1.0"

[placeholders]
name = "Project name"
description = "Project description"

[files]
include = [
  "main_file.ext",
  "src/module.ext",
  "README.md"
]

[gitignore]
template = "MyLanguage"  # GitHub gitignore template name

[ci]
workflow_name = "CI"
branches = ["main", "develop"]
runs_on = "ubuntu-latest"
```

### 3. Add Placeholder Slots

Use `{{variable}}` in all text files:

```
Project: {{name}}
Purpose: {{description}}
```

Binary files are skipped automatically.

### 4. Compatibility Requirements

- All files must be UTF-8 encoded
- `.gitignore` name must match a GitHub API template name
- CI workflow must be compatible with GitHub Actions
- Entry point file must be executable or compilable

### 5. Submit Your Template

1. **Fork** this repository
2. **Create** your template directory
3. **Test** locally with `ghscaff` (if you have it set up)
4. **Open a Pull Request** with:
   - Template directory
   - Clear description of use case
   - Example output

Template reviewers will verify:
- ✅ Metadata completeness
- ✅ Placeholder syntax correctness
- ✅ File structure compliance
- ✅ Language appropriateness

---

## Template Guidelines

### ✅ Do

- Keep templates **minimal** — only essential boilerplate
- Include **CI/CD workflows** — GitHub Actions or equivalent
- Use **meaningful comments** — help users understand the structure
- Support **standard tools** — cargo, npm, python venv, maven, etc.
- Include **LICENSE** — templates should have a license template slot
- Write **clear README** — with {{name}} and {{description}} placeholders

### ❌ Don't

- Include **generated files** — .o, .class, node_modules, __pycache__, etc.
- Use **external binaries** — all tools should be installable via package managers
- Add **huge dependencies** — keep initial boilerplate lightweight
- Hardcode **credentials** — never include API keys or secrets
- Use **uncommon package managers** — stick to standard tools per language

---

## Cache Location

Templates are downloaded and cached locally:

```bash
~/.ghscaff/boilerplate/
├── rust/
│   ├── template.toml
│   ├── Cargo.toml
│   ├── src/main.rs
│   └── ...
└── python/
    ├── template.toml
    ├── pyproject.toml
    └── ...
```

Users can clear the cache anytime:

```bash
rm -rf ~/.ghscaff/boilerplate
```

---

## Versioning

Templates use semantic versioning (`MAJOR.MINOR.PATCH`):

- **MAJOR** — Breaking changes (incompatible with previous versions)
- **MINOR** — New features (backward compatible)
- **PATCH** — Bug fixes (backward compatible)

Update the version in `template.toml` when you make changes.

---

## License

MIT — see [LICENSE](LICENSE) for details.

Templates contributed to this repository are also licensed under MIT unless otherwise specified.

---

Made with ❤️ by [JheisonMB](https://github.com/JheisonMB)
