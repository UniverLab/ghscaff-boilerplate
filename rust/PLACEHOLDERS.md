# Rust Template - Placeholders Reference

This document describes all the placeholders used in the Rust template that `ghscaff` will replace when generating a new project.

## Available Placeholders

### `{{name}}`
**Purpose**: Project name in kebab-case format (used as binary name)  
**Type**: String  
**Used in**:
- `Cargo.toml`: `name = "{{name}}"`
- `src/main.rs`: Comments and binary name references
- `install.sh`: Binary name and messages
- `install.ps1`: Binary name and messages
- `.github/workflows/release.yml`: Archive names and binary packaging

**Example**: `my-awesome-tool`

---

### `{{description}}`
**Purpose**: Short description of the project  
**Type**: String  
**Used in**:
- `Cargo.toml`: `description = "{{description}}"`
- `README.md`: In the opening paragraph

**Example**: `A blazingly fast CLI tool for managing repositories`

---

### `{{github_org}}`
**Purpose**: GitHub organization or username  
**Type**: String  
**Used in**:
- `install.sh`: `REPO="{{github_org}}/{{github_repo}}"`
- `install.ps1`: `$Repo = "{{github_org}}/{{github_repo}}"`
- `README.md`: Installation and documentation links

**Example**: `anomalyco` or `JheisonMB`

---

### `{{github_repo}}`
**Purpose**: GitHub repository name  
**Type**: String  
**Used in**:
- `install.sh`: `REPO="{{github_org}}/{{github_repo}}"`
- `install.ps1`: `$Repo = "{{github_org}}/{{github_repo}}"`
- `README.md`: Installation and documentation links

**Example**: `my-awesome-tool`

---

## File-by-File Placeholder Map

| File | Placeholders | Notes |
|------|-------------|-------|
| `Cargo.toml` | `{{name}}`, `{{description}}` | Standard Rust package metadata |
| `src/main.rs` | `{{name}}` | In comments and binary name |
| `README.md` | `{{name}}`, `{{description}}`, `{{github_org}}`, `{{github_repo}}` | Full documentation |
| `install.sh` | `{{name}}`, `{{github_org}}`, `{{github_repo}}` | Unix installation script |
| `install.ps1` | `{{name}}`, `{{github_org}}`, `{{github_repo}}` | Windows installation script |
| `.github/workflows/ci.yml` | None | Generic, no placeholders needed |
| `.github/workflows/release.yml` | `{{name}}` | Binary name for workflow input |
| `.gitignore` | None | Standard Rust gitignore, no placeholders |

---

## Implementation Notes for ghscaff

When `ghscaff` processes this template, it should:

1. **Read** all files in the template directory
2. **For each file**, replace all occurrences of placeholders with actual values
3. **Handle special cases**:
   - All placeholders use consistent `{{name}}` syntax
   - In shell scripts, ensure placeholders are properly quoted
   - In YAML workflows, placeholders work alongside GitHub Actions context variables like `${{ matrix.target }}`
4. **Preserve** file permissions (especially for `.sh` files)
5. **Create** directory structure (`.github/workflows`, `src/`, etc.)

---

## Example Replacement

**Input values** from user:
```
name: my-cli-tool
description: A CLI tool for managing GitHub repositories
github_org: anomalyco
github_repo: my-cli-tool
```

**Before** (Cargo.toml template):
```toml
[package]
name = "{{name}}"
description = "{{description}}"
```

**After** (Generated Cargo.toml):
```toml
[package]
name = "my-cli-tool"
description = "A CLI tool for managing GitHub repositories"
```

---

## Notes

- All placeholders use the `{{placeholder}}` syntax
- Placeholders are case-sensitive
- Empty placeholders should be handled gracefully (e.g., optional description)
- Some placeholders (like `{{github_org}}` and `{{github_repo}}`) are derived from the GitHub repository information
