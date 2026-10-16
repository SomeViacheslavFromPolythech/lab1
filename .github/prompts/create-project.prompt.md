---
name: create-project
description: Scaffold the variant 2 Python Hello World project.
---

Create the starter project by following the `.github/skills/project-scaffold/SKILL.md`
instructions. This repository is variant 2: Python using `venv` and a run script,
with `pytest` for unit tests.

## Preconditions

- Work from the repository root.
- Read the skill and inspect the existing repository, including `README.md`,
  `src/`, and `tests/`.
- Require `/git-init` to have been completed, including the Python `.gitignore`
  rules.
- Use Python; do not substitute a different language or testing framework.

## Actions

1. Use the skill's project-name and target-directory inputs, choosing the
   repository's existing project name when one is clear.
2. Create the minimal Hello World source and the directories required by the
   skill. The app must have a simple, testable greeting function and a runnable
   entry point.
3. Add or update project setup/run instructions in `README.md` only when doing
   so does not discard existing user content. Preserve the student's identity
   and variant information.
4. Do not create build configuration, tests, CI scripts, or a workflow here;
   those belong to `/create-build` and `/create-actions`.

## Expected result and verification

- `src/main.py` and the skill's required project directories exist.
- The documented Python command can run the app and print the greeting.
- Report the created or reused paths and the exact run command.

## Errors and repeat runs

- If the skill is absent/incomplete, or an existing target file conflicts with
  the requested scaffold, stop and report the issue rather than guessing or
  overwriting.
- Reuse a valid existing scaffold. Create only missing files; do not duplicate
  directories or replace existing source without explicit approval.
