"""
Migriert den kompletten 12-Wochen-Kurs (alle 3 Varianten, DE+EN, alle 6 Notebook-Typen) vom
.ipynb-Format auf das Zellen-Format: jede Zelle eines Notebooks wird zu einer eigenen,
numerierten .py-Datei in einem gleichnamigen Ordner, der die alte .ipynb-Datei ersetzt.

- Markdown-Zellen: ein alleinstehendes String-Literal in drei Anfuehrungszeichen
  (gueltiges, wirkungsloses Python)
- Code-Zellen: der Original-Code unveraendert, Byte-fuer-Byte

Nach dem Schreiben wird sofort zurueckgelesen und gegen die Original-Zelle verglichen
(Round-Trip-Check). Erst wenn das fuer alle Zellen eines Notebooks passt, wird die alte
.ipynb-Datei geloescht - bei einer Abweichung bleibt die Original-Datei unangetastet.

Idempotent: bereits migrierte Notebooks (keine .ipynb mehr, Ziel-Ordner existiert schon)
werden uebersprungen, nicht als Fehler gezaehlt.
"""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TYPES = ["0_glossar", "1_lektion", "2_debug", "3_missionen", "5_boss", "6_loesungen"]

# (Kurs-Ordner, Variante-Ordner, Datei-Praefix)
VARIANTS = [
    ("python-12-wochen-grundkurs", "abenteuer", "woche"),
    ("python-12-wochen-grundkurs", "pferde", "woche"),
    ("python-12-wochen-grundkurs", "scifi", "woche"),
    ("python-12-wochen-grundkurs-en", "adventure", "week"),
    ("python-12-wochen-grundkurs-en", "horses", "week"),
    ("python-12-wochen-grundkurs-en", "scifi", "week"),
]


def cell_text(cell):
    source = cell["source"]
    return "".join(source) if isinstance(source, list) else source


def split_notebook(src_path: Path, dest_dir: Path):
    nb = json.loads(src_path.read_text(encoding="utf-8"))
    cells = nb["cells"]

    dest_dir.mkdir(parents=True, exist_ok=True)
    for f in dest_dir.glob("*.py"):
        f.unlink()

    for i, cell in enumerate(cells, start=1):
        text = cell_text(cell)
        cell_type = cell["cell_type"]
        fname = dest_dir / f"{i:02d}_{cell_type}.py"

        if cell_type == "markdown":
            # Backslash zuerst escapen, dann JEDES Anfuehrungszeichen (nicht nur exakte
            # """-Sequenzen) - sonst kann Text, der zufaellig mit " endet, mit dem
            # schliessenden """ kollidieren. Kein zusaetzliches Zeilenumbruch-Padding um
            # den Text herum, sonst weicht der extrahierte Wert vom Original ab.
            escaped = text.replace("\\", "\\\\").replace('"', '\\"')
            content = f'"""{escaped}"""\n'
        else:
            # Keine Padding-Zeilenumbrueche - Byte-fuer-Byte identisch zum Original.
            content = text

        fname.write_text(content, encoding="utf-8")

    return cells


def verify_round_trip(dest_dir: Path, original_cells):
    files = sorted(dest_dir.glob("*.py"))
    assert len(files) == len(original_cells), (
        f"{dest_dir}: {len(files)} Dateien, aber {len(original_cells)} Original-Zellen"
    )
    for f, cell in zip(files, original_cells):
        text = f.read_text(encoding="utf-8")
        if cell["cell_type"] == "markdown":
            tree = ast.parse(text)
            value = tree.body[0].value.value
            expected = cell_text(cell)
            assert value == expected, f"{f}: Markdown weicht vom Original ab"
        else:
            expected = cell_text(cell)
            assert text == expected, f"{f}: Code weicht vom Original ab"


def already_migrated(dest_dir: Path) -> bool:
    return dest_dir.is_dir() and any(dest_dir.glob("[0-9][0-9]_*.py"))


def main():
    total = 0
    skipped = 0
    failures = []
    for course, variant, prefix in VARIANTS:
        for week in range(1, 13):
            for typ in TYPES:
                base = f"{prefix}{week}_{variant}_{typ}"
                src = ROOT / "content" / course / f"woche-{week}" / variant / f"{base}.ipynb"
                dest = ROOT / "content" / course / f"woche-{week}" / variant / base

                if not src.exists():
                    if already_migrated(dest):
                        skipped += 1
                        continue
                    failures.append(f"FEHLT: {src}")
                    continue

                try:
                    cells = split_notebook(src, dest)
                    verify_round_trip(dest, cells)
                    src.unlink()
                    total += 1
                except Exception as e:
                    failures.append(f"{src}: {e}")

    print(f"{total} Notebooks migriert und Round-Trip-verifiziert, {skipped} bereits migriert.")
    if failures:
        print(f"\n{len(failures)} Fehler:")
        for f in failures:
            print(" -", f)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
