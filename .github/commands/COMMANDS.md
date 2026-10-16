# Agent commands

The commands are GitHub Copilot prompt files in `.github/prompts/`. In VS Code,
open Copilot Chat and run `/git-init`, `/create-project`, `/create-build`,
`/create-actions`, `/check`, or `/init`.

Each command is an instruction for the agent, not a standalone executable. It
must inspect the current repository before acting, preserve unrelated work, and
report the files changed and checks performed. If a required skill is missing
or incomplete, the agent must say so rather than claim the skill ran.

## Commands

| Command | Prompt file | Purpose |
| --- | --- | --- |
| `/git-init` | `git-init.prompt.md` | Verify the Git repository and ensure Python ignore rules. |
| `/create-project` | `create-project.prompt.md` | Use `project-scaffold` to create the starter project. |
| `/create-build` | `create-build.prompt.md` | Use `build-and-test` to configure and test the project. |
| `/create-actions` | `create-actions.prompt.md` | Use `github-actions` to add cross-platform CI. |
| `/check` | `check.prompt.md` | Verify deliverables without changing project files. |
| `/init` | `init.prompt.md` | Run the setup commands in order and finish with `/check`. |

## Shared safety and repeat-run rules

- Read the relevant skill and inspect the target files before editing.
- Treat existing user files as authoritative. Do not overwrite a conflicting
  file; stop and report the conflict unless the user explicitly approves it.
- Create only missing required files. When an existing file needs improvement,
  propose the change and obtain user approval before replacing it.
- Do not delete files, expose secrets, install packages globally, change Git
  history, or push/commit changes.
- Stop on the first failed prerequisite, command, or verification. Report the
  failed step, its output, and what remains incomplete; never report success
  after a failure.
- A repeated run must inspect and reuse valid outputs rather than duplicate or
  replace them.

## `/init` execution order

`/init` invokes these prompt commands one at a time:

1. `/git-init`
2. `/create-project`
3. `/create-build`
4. `/create-actions`
5. `/check`

Proceed only when the previous command succeeds. If any step fails or encounters
a conflicting existing file, stop and report the failure; do not continue with
later steps.
