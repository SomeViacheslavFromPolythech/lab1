---
name: create-actions
description: Add a Windows, Linux, and macOS GitHub Actions CI matrix.
---

Create cross-platform CI by following
`.github/skills/github-actions/SKILL.md`.

## Preconditions

- Work from the repository root.
- Read the skill and inspect the project's existing run/build/test scripts and
  workflow files.
- Require `/create-build` to have established a working local test command.
- Do not assume a branch name that conflicts with the repository or course
  instructions; configure push and pull-request triggers for the agreed target
  branches and report which branches are covered.

## Actions

1. Follow the skill to create `.github/workflows/ci.yml` with one job and a
   matrix containing `ubuntu-latest`, `windows-latest`, and `macos-latest`.
2. Include checkout and the steps needed to select the project's Python version.
3. Ensure the required `ci.sh` and `ci.bat` scripts exist and perform the
   project's setup/build/test steps. Create only missing scripts, following
   the skill and existing project conventions.
4. Have the workflow invoke those scripts rather than duplicating project
   build and test logic inline in YAML.
5. Ensure each runner uses the appropriate script invocation and that failures
   produce a failing job. Do not add secrets or credentials.

## Expected result and verification

- The workflow file exists and contains all three required operating systems.
- `ci.sh` and `ci.bat` exist and run the project setup/build/test steps.
- The workflow invokes those scripts and is triggered by
  pushes and pull requests to the agreed branches.
- Validate the YAML with an available YAML parser and inspect the workflow's
  matrix and script paths. Report any verification tool that is unavailable.

## Errors and repeat runs

- If the skill or required local scripts are missing, stop and report the
  prerequisite; do not create a workflow that calls nonexistent files.
- Preserve existing workflows and unrelated jobs. If the target workflow
  already exists, inspect it and add only missing requirements; do not replace
  conflicting configuration without approval.
- Do not claim CI passed until the workflow has actually run successfully on
  GitHub Actions. A local syntax check is not evidence of a successful hosted
  run.
