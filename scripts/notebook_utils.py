"""Gemeinsame nbformat-Hilfsfunktionen fuer die Notebook-Generatoren (build_lesson_notebook.py,
build_project_notebook.py, build_kilabor_notebook.py) - reine Zellen-/JSON-Bausteine, keine
Content-spezifische Logik."""
import json
import uuid
from pathlib import Path

NBFORMAT_METADATA = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.10.0"},
}


def new_cell_id() -> str:
    """nbformat >= 4.5 verlangt eine id pro Zelle (sonst MissingIDFieldWarning)."""
    return uuid.uuid4().hex[:8]


def to_source(text: str) -> list[str]:
    """Text -> nbformat 'source'-Zeilenliste (jede Zeile inkl. '\\n', letzte ohne)."""
    lines = text.split("\n")
    if not lines:
        return []
    return [line + "\n" for line in lines[:-1]] + [lines[-1]]


def markdown_cell(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": new_cell_id(),
        "metadata": {},
        "source": to_source(text.strip("\n")),
    }


def code_cell(code: str) -> dict:
    return {
        "cell_type": "code",
        "id": new_cell_id(),
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": to_source(code.rstrip("\n")),
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": NBFORMAT_METADATA,
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(path: Path, nb: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
