---
name: project-scaffold
description: Create or complete the variant 2 Python Hello World project scaffold. Use when setting up the app source, project directories, README run instructions, or Python ignore rules.
---

# Skill: project-scaffold

## Purpose

Create the minimal, runnable Python Hello World project structure required by
variant 2. Use this skill for `/create-project`; do not configure tests or CI
here.

## Inputs

- `project_name`: short project/package display name.
- `language`: must be `python` for this lab.
- `target_directory`: repository root, normally `.`.
- Existing repository files and Git status, inspected before writing.

Example:

```json
{
  "project_name": "lab1",
  "language": "python",
  "target_directory": "."
}
```

## Procedure

1. Confirm the target is the repository root and the requested language is
   Python. Inspect `README.md`, `.gitignore`, `src/`, and `tests/` before
   changing anything.
2. Create only missing scaffold files. Use `src/main.py` as the runnable
   entry point and expose a small greeting function so behavior can be tested
   independently. Running `python src/main.py` must print `Hello, World!`.
3. Ensure the directory layout includes `src/` and `tests/`. Do not create
   tests or dependency configuration; those are owned by `build-and-test`.
4. Add a short project description and run instructions to `README.md` while
   preserving existing student/course information and unrelated content.
5. Ensure `.gitignore` excludes `.venv/`, `__pycache__/`, `*.py[cod]`,
   `.pytest_cache/`, and `build/`, preserving existing ignore rules.

## Outputs

- `src/main.py` with a callable greeting function and executable entry point.
- `src/` and `tests/` project directories.
- README project/run instructions.
- Python-generated-artifact exclusions in `.gitignore`.
- A report listing created/reused paths and the run command.

## Validation

- Confirm `src/main.py` and both required directories exist.
- Run `python src/main.py`; require exit code zero and exact output
  `Hello, World!`.
- Review the diff to confirm pre-existing content was retained.

## Failure handling and repeat runs

- Stop if the repository root cannot be established, the language is not
  Python, or a skill prerequisite is missing.
- If any target file already contains conflicting user content, do not replace
  it; report the conflict and ask for approval.
- Reuse a valid existing scaffold and add only missing directories/rules.
- If execution fails or output differs, report the command and error/output;
  do not claim the scaffold is verified.
