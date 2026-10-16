---
name: init
description: Orchestrate the complete lab project setup and verification.
---

Set up the lab project by invoking the existing prompt commands in this exact
order:

1. `/git-init`
2. `/create-project`
3. `/create-build`
4. `/create-actions`
5. `/check`

Before starting, inspect the repository root, Git status, and the command and
skill files. Confirm that every required skill and prompt command is available.
Do not begin if a prerequisite is missing or if an existing user change would
be overwritten.

Run each command as a separate stage. Wait for its result before starting the
next. After every stage, verify its documented outputs and stop immediately if
it fails, is blocked, or reports a conflicting file. Do not skip failed stages,
claim success, or continue to later commands after a failure.

## Expected outputs and verification

- `/git-init`: repository root is confirmed; `.gitignore` has all required
  Python/cache/build exclusions.
- `/create-project`: the Python entry point `src/main.py` and project
  instructions exist, and the greeting can be run.
- `/create-build`: dependency/test configuration and `tests/test_main.py` exist;
  the documented local test command passes.
- `/create-actions`: `.github/workflows/ci.yml`, `ci.sh`, and `ci.bat` exist;
  YAML and script paths are checked, and the matrix covers all three operating
  systems.
- `/check`: returns a verification report with no failed or blocked required
  checks for `/init` to be considered successful.

## Safety and repeat runs

- Preserve existing files and unrelated user changes. A repeated run should
  reuse valid outputs and add only missing files.
- Do not delete files, expose secrets, install packages globally, commit, push,
  or modify Git history.
- Do not bypass a missing or incomplete skill by improvising its behavior;
  report the blocker.

## Final report

Summarize each completed stage, files created or reused, local checks and their
results, and any blocked/incomplete work. Report GitHub Actions as pending until
the workflow has actually run successfully on GitHub.
