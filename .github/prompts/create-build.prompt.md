---
name: create-build
description: Configure the Python virtual environment workflow and pytest tests.
---

Configure project setup and unit testing by following
`.github/skills/build-and-test/SKILL.md`.

## Preconditions

- Work from the repository root.
- Read the skill and inspect the existing source, tests, and dependency files.
- Require `/create-project` to have produced a runnable Python Hello World
  entry point.
- Use `venv` and `pytest`, as required for variant 2.

## Actions

1. Follow the skill to document or create repeatable virtual-environment and
   dependency setup, build/run, and test commands.
2. Create a unit test under `tests/` for the app's greeting behavior. Keep tests
   deterministic and independent of network access.
3. Configure a run/build script if the skill calls for one, using a
   cross-platform approach or separate scripts where appropriate.
4. Do not create or modify GitHub Actions files; `/create-actions` owns those.

## Expected result and verification

- A dependency configuration exists with `pytest` as a test dependency.
- `tests/test_main.py` exists and tests the app's greeting behavior.
- The project has a clear way to create/use its virtual environment and install
  test dependencies.
- The tests can be run with `pytest`.
- Run the documented local test command and report its exit status and result.

## Errors and repeat runs

- If the source entry point is missing, stop and report that `/create-project`
  must be completed first.
- If existing dependency or test files conflict, preserve them and report the
  conflict instead of replacing them.
- Keep valid existing configuration and tests; add only missing pieces. Stop
  on any failed test and include the relevant failure output.
