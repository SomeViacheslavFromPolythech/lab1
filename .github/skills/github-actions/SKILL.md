---
name: github-actions
description: Configure the repository's GitHub Actions CI matrix for Ubuntu, Windows, and macOS using the project's CI scripts. Use when adding or checking cross-platform CI.
---

# Skill: github-actions

## Purpose

Configure repeatable GitHub Actions CI for the Python variant on Ubuntu,
Windows, and macOS. Use this skill for `/create-actions` after local project
setup and tests are defined.

## Inputs

- Repository root and existing workflows/scripts.
- Python version used by the project.
- Verified local setup and test commands from `build-and-test`.
- Target branch names for push and pull-request triggers.
- Existing `.gitignore` and Git status.

Example:

```json
{
  "python_version": "3.11",
  "matrix_os": ["ubuntu-latest", "windows-latest", "macos-latest"],
  "push_branches": ["develop", "master"],
  "pull_request_branches": ["develop", "master"],
  "test_command": "python -m pytest"
}
```

## Procedure

1. Confirm the app, dependency setup, and local test command exist and inspect
   existing workflow files before editing. Confirm the target branches with
   the user if repository/course requirements do not establish them.
2. Create `ci.sh` for Linux/macOS and `ci.bat` for Windows. Each script must
   create or use the project-local `.venv`, install the declared dependencies,
   run the app, and run the full test suite. Propagate errors/non-zero exit
   codes. Do not hide test output or failures.
3. Create `.github/workflows/ci.yml` with one job and a matrix for
   `ubuntu-latest`, `windows-latest`, and `macos-latest`.
4. Configure push and pull-request triggers for the supplied target branches.
   The workflow may check out the repository and select the Python version;
   delegate project setup, run, and tests to `ci.sh` or `ci.bat`.
5. Use the platform-appropriate script invocation. Do not add tokens, secrets,
   credentials, unrelated jobs, or branch protection changes.

## Outputs

- `ci.sh` and `ci.bat` with matching setup, app-run, and test behavior.
- `.github/workflows/ci.yml` with a single three-OS matrix job.
- Workflow syntax/matrix/script-path verification results.

## Validation

- Confirm both scripts exist and are invoked by the workflow on the correct
  platforms.
- Confirm the matrix includes all three required runner labels and triggers
  cover the supplied push and pull-request branches.
- Parse the workflow YAML with an available validator. If none is available,
  report that limitation and still inspect the file structurally.
- Run the appropriate CI script locally when possible and report its exact
  command and result.
- Report hosted GitHub Actions status separately; local validation does not
  prove a hosted run passed.

## Failure handling and repeat runs

- If local setup/test commands are not defined, stop and report that
  `build-and-test` must be completed first.
- If branch targets are unclear, ask rather than inventing a branch policy.
- Preserve unrelated existing workflows and scripts. If an existing target
  conflicts, report it and request approval before replacement.
- Reuse valid scripts/workflow and add only missing requirements. Stop on
  syntax, script, or test failure; preserve the error and do not report CI
  success.
