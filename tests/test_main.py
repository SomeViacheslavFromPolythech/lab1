import subprocess
import sys
from pathlib import Path

from src.main import greeting


def test_greeting_returns_hello_world():
    assert greeting() == "Hello, World!"


def test_main_prints_hello_world():
    project_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(project_root / "src" / "main.py")],
        capture_output=True,
        text=True,
        check=True,
        cwd=project_root,
    )

    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ""
