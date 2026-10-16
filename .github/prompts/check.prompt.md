---
name: check
description: Verify the lab deliverables without editing project files.
---

Perform a read-only verification of the project against the lab requirements.
Do not create, edit, delete, install, commit, or push anything.

## Preconditions

- Work from the repository root and inspect the current Git status first.
- If required project files are absent, report them as missing; do not create
  them during this command.

## Checks

1. **Agent and instructions:** Check that the agent manifest, three required
   skills, six prompt commands, and architecture/usage documentation exist.
   Confirm each skill describes its purpose, inputs, outputs, checks, and
   error handling.
2. **Commands:** Confirm command prerequisites, actions, expected outputs,
   verification, and failure behavior are documented. Confirm `/init` runs
   `/git-init`, `/create-project`, `/create-build`, `/create-actions`, then
   `/check`, stopping on failure.
3. **Project:** Confirm the Python Hello World source, test suite, setup/run
   instructions, dependency configuration, and `.gitignore` are present.
4. **Local verification:** If the documented virtual environment and test
   dependencies already exist, run the documented test command without
   installing dependencies. Disable Python bytecode and pytest cache output
   where possible. If dependencies are unavailable, report the check as
   blocked rather than installing or creating an environment.
5. **CI:** Confirm the workflow YAML parses using an already available parser,
   includes Windows, Linux, and macOS, and invokes existing scripts. Report
   syntax, matrix, or path problems. Do not claim hosted CI success based only
   on local inspection.
6. **Repository hygiene:** Inspect `git status --short` and confirm ignored
   build/venv/cache artifacts are not accidentally tracked. Do not expose
   secret values; report only whether likely secret files or patterns need
   attention.

## Result

Return a concise checklist with `PASS`, `FAIL`, or `BLOCKED` for each category,
include exact failed commands and useful error output, and list missing
deliverables. Return a non-success result if any required check fails or is
blocked. Leave the working tree unchanged.

## Errors and repeat runs

- If a command cannot run, report its error and mark the affected check
  `BLOCKED`; do not install tools or create missing prerequisites.
- If a required file is absent or invalid, mark the relevant check `FAIL` and
  identify the path or requirement.
- This command is read-only, so rerunning it repeats the checks and must not
  change the working tree.
