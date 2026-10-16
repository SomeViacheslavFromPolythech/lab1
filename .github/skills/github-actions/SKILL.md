# Skill: `github-actions`

### Description
Generates `.github/workflows/ci.yml` supporting a cross-platform matrix (`ubuntu-latest`, `windows-latest`, `macos-latest`). The workflow strictly delegates all build and test logic to executable scripts (`ci.sh` / `ci.bat`).

### Skill Definition (`docs/skills/github-actions.md`)

```markdown
# Skill: github-actions

## Purpose
Configures GitHub Actions CI pipeline across Windows, Linux, and macOS. Delegates execution exclusively to shell scripts (`ci.sh` / `ci.bat`).

## Input Example
```json
{
  "workflow_name": "CI Cross-Platform Pipeline",
  "matrix_os": ["ubuntu-latest", "windows-latest", "macos-latest"],
  "python_version": "3.11"
}
