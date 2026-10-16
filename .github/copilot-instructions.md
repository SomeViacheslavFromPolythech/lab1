# Repository instructions

## Project and current implementation

This is variant 2 of the lab: a Python Hello World project using `venv` and
`pytest`, with an AI-assisted setup workflow and cross-platform GitHub Actions.
The current repository contains agent/prompt documentation, but not the Python
application, tests, dependency configuration, run scripts, or CI workflow.

There are no project build, test, or lint commands available yet. The slash
commands in `.github/prompts/` are Copilot prompt commands, not shell commands.
Do not report builds or tests as passing until the project and its documented
commands exist and have actually been run. When adding them, document exact
setup, full-test, and single-test commands in the project usage documentation.

## Agent workflow

The intended setup flow is coordinated by `.github/prompts/init.prompt.md`:
`/git-init` → `/create-project` → `/create-build` → `/create-actions` →
`/check`. Each stage must finish and verify its outputs before the next begins;
stop on failure or a conflicting file. `/check` is read-only.

The prompt files define user-invoked operations; `.github/skills/` is intended
to provide the reusable procedures those operations follow. Keep those
responsibilities aligned: prompts orchestrate a specific operation and skills
define its inputs, outputs, validation, and failure handling. `COMMANDS.md`
indexes the prompt commands. The agent manifest and `docs/architecture.md`
describe the project-scaffolding workflow; keep both aligned with the
variant 2 Python deliverable and the operations defined in the prompts/skills.

## Project and CI conventions

- Keep the application in `src/` and pytest tests in `tests/`; use Python and
  `pytest` as required by variant 2.
- Use the standard GitHub Copilot locations already established here:
  `.github/agents/`, `.github/skills/`, and `.github/prompts/`.
- The CI target is a single GitHub Actions job with a matrix for
  `ubuntu-latest`, `windows-latest`, and `macos-latest`. The workflow should
  delegate project setup/build/test work to the repository scripts (the lab
  specifies `ci.sh` and `ci.bat`) rather than maintaining a second test
  implementation in YAML.
- Keep `.venv/`, Python bytecode/cache, `.pytest_cache/`, and `build/` out of
  version control, as specified by the prompt workflow.
- Setup prompts are designed to preserve existing user files, add only missing
  outputs, avoid destructive or Git-history-changing actions, and report
  failures rather than claiming success.
