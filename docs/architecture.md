# AI Agent Architecture

## Purpose and scope

The Build Engineer agent guides creation and verification of the lab's variant
2 deliverable: a minimal Python Hello World application using `venv` and
`pytest`, together with a repeatable local run/test path and cross-platform
GitHub Actions CI. The agent configuration is instructional: Copilot Chat
prompt files define the user-invoked operations, while skills provide reusable
procedures. There is no separate executable agent or command-line orchestrator
in this repository.

## Components

| Component | Location | Responsibility |
| --- | --- | --- |
| Agent manifest | `.github/agents/build-engineer.agent.md` | Defines the agent's role, scope, safety rules, and completion criteria. |
| Skills | `.github/skills/*/SKILL.md` | Define reusable scaffold, build/test, and CI procedures with inputs, outputs, validation, and failure behavior. |
| Prompt commands | `.github/prompts/*.prompt.md` | Define user-invoked operations, their prerequisites, and actions. |
| Command index | `.github/commands/COMMANDS.md` | Lists prompt commands and their shared safety and repeat-run rules. |
| Application and tests | `src/`, `tests/` | Hold the generated Python application and its `pytest` tests. |
| CI scripts and workflow | `ci.sh`, `ci.bat`, `.github/workflows/ci.yml` | Run setup/tests consistently on local machines and the three CI operating systems. |

## Skills and data flow

1. **`project-scaffold`** receives a project name, Python language, and target
   directory. It creates the minimal Hello World source, project structure,
   run instructions, and initial ignore rules. It reports the paths created
   and a command to run the app.
2. **`build-and-test`** receives the source layout, Python version, and chosen
   dependency/test configuration. It defines `venv` setup, dependencies,
   application run, and `pytest` execution, and creates a focused unit test.
   Its result is the reproducible local test command and its verification
   output.
3. **`github-actions`** receives the local setup/test commands and agreed
   target branches. It creates `ci.sh`, `ci.bat`, and a workflow matrix for
   Ubuntu, Windows, and macOS. The workflow invokes the scripts instead of
   duplicating project test logic in YAML.

The expected end-to-end flow is:

```text
User → /init → /git-init → /create-project → /create-build
                         → /create-actions → /check
                 prompts call the corresponding skills
```

Each stage reports its files and verification result to the orchestrating
`/init` prompt. `/init` proceeds only after a successful stage and stops at the
first missing prerequisite, conflict, or failed check. `/check` is read-only
and reports `PASS`, `FAIL`, or `BLOCKED` for required areas; it must not repair
files or install dependencies.

## Commands

| Command | Responsibility |
| --- | --- |
| `/git-init` | Confirm repository root, ensure Python/cache/build ignore rules, and report Git status. |
| `/create-project` | Apply `project-scaffold` to create the Python Hello World starter. |
| `/create-build` | Apply `build-and-test` to define environment setup and tests. |
| `/create-actions` | Apply `github-actions` to add scripts and cross-platform CI. |
| `/check` | Verify agent files, project, local checks, CI configuration, and repository hygiene without edits. |
| `/init` | Run the preceding commands in order, including `/check`, stopping on failure. |

## Safety and idempotency

Commands inspect the repository before editing, preserve user files and
unrelated changes, and add only missing outputs. A conflicting existing file
must be reported instead of silently overwritten. Commands do not delete
project files, expose secrets, install packages globally, commit, push, or
rewrite Git history. A failed command or test remains a failure in the final
report; later orchestration steps must not run after a failure.

## Completion criteria

The lab implementation is complete when the agent and all three skills are
documented, all six prompt commands are available, the Python application and
unit test run locally with the documented `venv`/`pytest` commands, and the
workflow delegates to project scripts across Ubuntu, Windows, and macOS.
Hosted CI success must be verified in GitHub Actions rather than inferred from
local YAML inspection.
