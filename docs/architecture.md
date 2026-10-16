# Agent Architecture: AI Code Reviewer & pytest Generator

This document defines the architecture, core modules, data flow, user commands, and error handling strategies for the **AI Code Reviewer & pytest Generator Agent**.

---

## 1. Problems Solved by the Agent

1. **High Overhead in Manual Code Reviews:**
   Automates static code analysis to instantly detect PEP 8 non-compliance, potential runtime errors, anti-patterns, and security code smells.
2. **Low Unit Test Coverage:**
   Eliminates the friction of manual test creation by automatically generating `pytest`-compliant test suites covering happy paths, edge cases, and exception handling.
3. **Early Bug Identification:**
   Executes generated tests in an isolated environment immediately after creation, detecting logical flaws prior to code merge or deployment.
4. **Cross-Platform Execution Consistency:**
   Ensures deterministic behavior and execution across Windows, Linux, and macOS environments through path abstraction and standardized environment invocation.

---

## 2. Agent Skills

The agent uses a modular architecture where discrete tasks are encapsulated into reusable skills:

| Skill Name | Responsibility | Input Data | Output Data |
| :--- | :--- | :--- | :--- |
| **`HelloSkill`** | Minimal status and health check verification skill used for basic environment validation and testing. | None or Command Args | Status String (`Hello World` payload) |
| **`CodeParserSkill`** | Reads Python source files, builds Abstract Syntax Trees (AST), and extracts signatures, functions, and imports. | Source File Path (`pathlib.Path`) | `CodeContext` (JSON/AST metadata) |
| **`CodeReviewSkill`** | Performs static code analysis, evaluates code metrics, and flags code smells or style violations. | `CodeContext` | `ReviewReport` (List of issues, severity, line numbers) |
| **`TestGeneratorSkill`** | Synthesizes `pytest` test code based on extracted function signatures, edge cases, and fixtures. | `CodeContext`, `ReviewReport` | `TestCode` (`test_*.py` content) |
| **`TestExecutorSkill`** | Invokes `pytest` in a cross-platform `subprocess`, captures execution logs, exit codes, and coverage metrics. | Path to test file | `ExecutionResult` (Status, stdout, stderr, coverage) |
| **`ReportGeneratorSkill`** | Consolidates analysis and execution results into formatted user reports. | `ReviewReport`, `ExecutionResult` | `SummaryReport` (Markdown / CLI output) |

---

## 3. User Commands

Users interact with the agent using structured CLI commands:

* **`/hello`** *(Minimal Initial Command)*  
  Executes `HelloSkill` to verify orchestrator availability, environment setup, and CLI output sanity.
* **`/review <path>`**  
  Executes static code analysis on the specified `.py` file or directory and outputs a detailed review report.
* **`/generate-tests <path>`**  
  Generates `pytest` test suites and saves them inside the `tests/` directory without running them.
* **`/run-tests <path>`**  
  Triggers `pytest` execution for existing or generated test files and outputs stdout/stderr logs.
* **`/run-all <path>`** *(Default Pipeline)*  
  Executes the full end-to-end flow: Code Parsing -> Review -> Test Generation -> Test Execution -> Final Reporting.
* **`/fix <path>`**  
  Generates refactored code proposals addressing issues identified during code review or test execution failures.

---

## 4. Data Flow Pipeline

Data flows sequentially through the central Orchestrator, which manages state transitions between skills:

```text
[User / CLI Input]
        │
        ▼
1. Orchestrator (Command Parsing & Pipeline Control)
        │
        ├──► Command: /hello ──► [HelloSkill] ──► Status Message ("Hello World")
        │
        └──► Command: /run-all
                 │
                 ├─► [CodeParserSkill] ────► Output: CodeContext (AST / Signatures)
                 │                                 │
                 │                                 ▼
                 ├─► [CodeReviewSkill] ────► Output: ReviewReport (Issues / Line numbers)
                 │                                 │
                 │                                 ▼
                 ├─► [TestGeneratorSkill] ─► Output: Generated test_*.py file
                 │                                 │
                 │                                 ▼
                 ├─► [TestExecutorSkill] ──► Output: ExecutionResult (Passed/Failed, Traceback)
                 │                                 │
                 │                                 ▼
                 └─► [ReportGeneratorSkill]► Output: Final Markdown Summary Report
