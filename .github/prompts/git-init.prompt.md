---
name: git-init
description: Verify the repository and ensure Python project ignore rules.
---

Verify this repository's Git state and ensure the Python `.gitignore` rules
required by the lab are present.

## Preconditions

- The current working directory must be the repository root.
- Confirm it is a Git work tree with `git rev-parse --show-toplevel`.
- If it is not a Git work tree, stop and explain that this command does not
  initialize repositories or alter Git history.

## Actions

1. Inspect `.gitignore` if it exists; preserve all existing rules and comments.
2. Ensure these rules are present, adding only missing lines:
   - `.venv/`
   - `__pycache__/`
   - `*.py[cod]`
   - `.pytest_cache/`
   - `build/`
3. Do not add broad rules that could hide source, tests, or documentation.
4. Show `git status --short` after the change.

## Expected result and verification

- `.gitignore` exists and contains each required rule exactly once.
- Git reports no `.venv/`, Python cache, pytest cache, or `build/` artifacts as
  untracked when such artifacts are present.
- Report the repository root, whether `.gitignore` changed, and the Git status.

## Errors and repeat runs

- If a matching ignore rule is already present, leave it unchanged.
- If `.gitignore` cannot be read or safely updated, stop and report the error.
- Do not create, remove, or overwrite any other file. A repeated run is a
  no-op when all rules are already present.
