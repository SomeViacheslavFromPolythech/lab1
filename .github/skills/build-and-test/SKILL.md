# Skill: `build-and-test`

### Description
Configures project dependencies, builds executable artifacts, and sets up/runs automated unit tests. Can be invoked via subcommands: `setup`, `build`, and `test`.

### Skill Definition (`docs/skills/build-and-test.md`)

```markdown
# Skill: build-and-test

## Purpose
Manages project configuration, executable packaging, and automated unit test execution.

## Subcommands
* `/build-setup` — Creates dependency files (`pyproject.toml` or `requirements.txt`).
* `/build-run` — Runs compilation or packages the Python module.
* `/test-run` — Executes unit tests via `pytest` and checks assertions.

## Input Example
```json
{
  "subcommand": "/test-run",
  "test_framework": "pytest",
  "test_directory": "tests/"
}
