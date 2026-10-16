# Lab 1: Python Hello World with a Copilot Agent

**Student:** Batiukov V. O. | **Variant:** 2 — Python, `venv`, run script, and `pytest`

This laboratory project defines a GitHub Copilot agent workflow for creating
and checking a small, cross-platform Python Hello World application. The
intended deliverables are the agent manifest, reusable skills, prompt commands,
application source, tests, local run/CI scripts, and a GitHub Actions matrix for
Windows, Linux, and macOS.

## Using the agent

Open the repository in a Copilot-compatible editor and use Copilot Chat prompt
commands from `.github/prompts/`. Run `/init` to orchestrate project setup and
verification, or run an individual command such as `/check`. See
[`docs/architecture.md`](docs/architecture.md) for the component flow and
[`docs/usage.md`](docs/usage.md) for the project and local verification
instructions once implementation is complete.

The generated application is intended to run from a Python virtual environment
and its unit tests are intended to run with `pytest`. The source, test suite,
setup/run scripts, and GitHub Actions workflow are still to be added; do not
treat this repository as an implemented or passing application yet.
