---
name: build-and-test
description: Configure the project-local Python virtual environment, pytest dependency, app run instructions, and unit tests. Use when setting up or verifying local project execution and tests.
---

# Skill: build-and-test

## Purpose

Configure and verify local Python setup, application execution, and unit tests
for variant 2. Python is interpreted, so this skill does not introduce a
compiled binary build. Use it for `/create-build`; CI workflow generation is
owned by `github-actions`.

## Inputs

- Repository root and current Git status.
- Runnable Python entry point, expected at `src/main.py`.
- Python version selected for the project and workflow.
- Existing dependency configuration, tests, and run scripts.

Example:

```json
{
  "python_version": "3.11",
  "entry_point": "src/main.py",
  "test_framework": "pytest",
  "test_directory": "tests"
}
```

## Procedure

1. Confirm the scaffold exists and inspect existing source, tests,
   `requirements.txt`, `pyproject.toml`, and usage documentation.
2. Use the repository's existing dependency convention. If none exists, add a
   minimal `requirements.txt` declaring `pytest`; do not add a second
   dependency manager or unnecessary runtime dependencies.
3. Document commands to create and activate `.venv`, install dependencies,
   run the app, and run tests. Include platform-appropriate activation
   commands, and provide a direct single-test command such as
   `python -m pytest tests/test_main.py`.
4. Add `tests/test_main.py` with deterministic tests for both the greeting
   function's return value and the entry point's printed output. Tests must
   not access the network.
5. Keep app execution as `python src/main.py`. Do not create CI scripts or
   workflow YAML; those belong to `github-actions`.

## Outputs

- A minimal dependency configuration containing the test dependency.
- `tests/test_main.py` covering the greeting behavior.
- Documented `.venv` setup, app run, full test, and single-test commands.
- Test command output and exit status.

## Validation

- Create/use the project-local virtual environment only when the user invokes
  this setup operation; do not install packages globally.
- Confirm the app runs with the documented command.
- Run the full suite with `python -m pytest`.
- Run at least one focused test with
  `python -m pytest tests/test_main.py::test_greeting_returns_hello_world`.
- Report exact commands, test counts/results, and exit codes. Do not claim
  success if dependencies are unavailable or a command fails.

## Failure handling and repeat runs

- Stop if the entry point is missing or not runnable; report that
  `/create-project` must be completed.
- Preserve valid existing dependency files, tests, and documentation. If a
  change would replace conflicting user content, stop and request approval.
- Reuse a compatible dependency setup and existing tests; add only missing
  configuration or coverage.
- If environment creation or dependency installation fails, report the failed
  command and error. Do not silently switch package managers or skip tests.
