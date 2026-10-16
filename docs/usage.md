# Local development and tests

Run these commands from the repository root. Python 3 must be installed.

## Create and activate the virtual environment

Create the project-local environment:

```sh
python -m venv .venv
```

Activate it using the command for your shell:

```sh
# Linux or macOS (bash/zsh)
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat
```

Install the project test dependency:

```sh
python -m pip install -r requirements.txt
```

## Run the application

```sh
python src/main.py
```

Expected output:

```text
Hello, World!
```

## Run tests

Run the complete test suite:

```sh
python -m pytest
```

Run the greeting return-value test alone:

```sh
python -m pytest tests/test_main.py::test_greeting_returns_hello_world
```
