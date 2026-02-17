#!/usr/bin/env python3
"""
Convert wissens_cheat_sheet.md to Jupyter notebook format.
Creates markdown cells for explanations and code cells for Python examples.
"""
import json
import re
from pathlib import Path


def parse_markdown(content: str) -> list[dict]:
    """Parse markdown into notebook cells."""
    cells = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Code block
        if line.strip().startswith('```python'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```
            if code_lines:
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'outputs': [],
                    'source': [l + '\n' for l in code_lines]
                })
            continue

        # Markdown content - collect until next ### or ## or ``` or ---
        md_lines = []
        while i < len(lines):
            line = lines[i]
            if line.strip().startswith('```python'):
                break
            if line.strip() == '---':
                i += 1
                continue
            md_lines.append(line)
            i += 1

        # Trim trailing empty lines
        while md_lines and not md_lines[-1].strip():
            md_lines.pop()

        if md_lines:
            cells.append({
                'cell_type': 'markdown',
                'metadata': {},
                'source': [l + '\n' for l in md_lines]
            })

    return cells


def convert_md_to_notebook(md_path: Path, output_path: Path) -> None:
    """Convert markdown file to Jupyter notebook."""
    content = md_path.read_text(encoding='utf-8')
    cells = parse_markdown(content)

    notebook = {
        'cells': cells,
        'metadata': {
            'kernelspec': {
                'display_name': 'Python 3',
                'language': 'python',
                'name': 'python3'
            },
            'language_info': {
                'name': 'python',
                'version': '3.10.0'
            }
        },
        'nbformat': 4,
        'nbformat_minor': 5
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False), encoding='utf-8')
    print(f"Created: {output_path}")


def main():
    base = Path(__file__).parent.parent / 'content' / 'python-12-wochen-grundkurs'
    for week in range(2, 13):
        md_path = base / f'woche-{week}' / 'wissens_cheat_sheet.md'
        if md_path.exists():
            output_path = base / f'woche-{week}' / 'wissens_cheat_sheet.ipynb'
            convert_md_to_notebook(md_path, output_path)


if __name__ == '__main__':
    main()
