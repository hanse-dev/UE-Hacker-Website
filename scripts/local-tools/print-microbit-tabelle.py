#!/usr/bin/env python3
"""Druckt die Forscher-Tabelle aus Stufe 8 des micro:bit-Kurses ("Die Linie sehen") zum
Ausfüllen auf einem MXW01-Thermodrucker aus. Läuft nur lokal, nie auf dem Server.

Die Zeilen kommen direkt aus content/microbit-auto/lektion-09.md, der Ausdruck bleibt also
automatisch beim Lektionstext.

Setup: siehe scripts/local-tools/README.md
"""
import argparse
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LESSON_FILE = SCRIPT_DIR.parent.parent / "content" / "microbit-auto" / "lektion-09.md"

# Env-Datei, venv-Pfad und Druckaufruf teilt sich das Skript mit dem Account-Ausdruck.
_spec = importlib.util.spec_from_file_location("account_printout", SCRIPT_DIR / "create-account-printout.py")
account_printout = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(account_printout)

PAPER_WIDTH = 384
DEFAULT_FONT_SCALE = 1.0


def reexec_in_venv() -> None:
    """Wie in create-account-printout.py: im venv (Pillow/bleak/matplotlib) neu starten."""
    venv_python = account_printout.VENV_PYTHON
    if not venv_python.exists() or sys.prefix == str(venv_python.parent.parent):
        return
    os.execv(str(venv_python), [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]])


def read_lesson(path: Path) -> tuple[str, list[str], list[list[str]]]:
    """Liefert Titel, Spaltenköpfe und Zeilen der ersten Markdown-Tabelle der Lektion."""
    title = ""
    table = []
    for line in path.read_text(encoding="utf8").splitlines():
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        elif line.startswith("|"):
            table.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        elif table:
            break
    if len(table) < 3:
        sys.exit(f"Keine Tabelle in {path} gefunden.")
    # table[1] ist die Trennzeile |---|---|
    return title, table[0], table[2:]


def build_table_image(title: str, header: list[str], rows: list[list[str]], font_scale: float, copies: int) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    margin = 10
    cell_pad = 8
    number_col = round(112 * font_scale)  # Spalte zum Eintragen der Zahl
    table_left = margin
    table_right = PAPER_WIDTH - margin
    split_x = table_right - number_col
    text_col = split_x - table_left - 2 * cell_pad

    def font_path(bold: bool) -> str | None:
        try:
            from matplotlib import font_manager
            props = font_manager.FontProperties(family="DejaVu Sans", weight="bold" if bold else "normal")
            return font_manager.findfont(props, fallback_to_default=True)
        except Exception:
            return None

    font_paths = {False: font_path(False), True: font_path(True)}

    def font(size: int, bold: bool = False):
        path = font_paths[bold]
        if path:
            try:
                return ImageFont.truetype(path, round(size * font_scale))
            except OSError:
                pass
        return ImageFont.load_default()

    scratch = ImageDraw.Draw(Image.new("L", (1, 1)))

    def wrap(text: str, f, max_width: int) -> list[str]:
        lines, current = [], ""
        for word in text.split():
            candidate = f"{current} {word}".strip()
            if current and scratch.textlength(candidate, font=f) > max_width:
                lines.append(current)
                current = word
            else:
                current = candidate
        return lines + [current] if current else lines

    def line_height(f) -> int:
        ascent, descent = f.getmetrics()
        return ascent + descent + 2

    title_font = font(22, bold=True)
    head_font = font(15, bold=True)
    body_font = font(17)
    small_font = font(14)

    footer = "Gut aufheben! In Stufe 9 baut ihr damit den Linienfolger."
    title_lines = wrap(title, title_font, PAPER_WIDTH - 2 * margin)
    footer_lines = wrap(footer, small_font, PAPER_WIDTH - 2 * margin)
    head_cells = [wrap(header[0], head_font, text_col), wrap(header[1], head_font, number_col - 2 * cell_pad)]
    body_cells = [wrap(row[0], body_font, text_col) for row in rows]
    # Mindesthöhe, damit eine handgeschriebene Zahl ins Feld passt
    min_row = round(64 * font_scale)

    def draw_copy(draw, y: int) -> int:
        """Zeichnet einen Ausdruck ab y und liefert das neue y. Mit draw=None wird nur gemessen."""
        y += margin
        for line in title_lines:
            if draw:
                draw.text((margin, y), line, font=title_font, fill=0)
            y += line_height(title_font)
        y += 6
        if draw:
            draw.text((margin, y), "Team:", font=small_font, fill=0)
            line_y = y + line_height(small_font) - 4
            draw.line([margin + 60 * font_scale, line_y, table_right, line_y], fill=0, width=1)
        y += line_height(small_font) + 12

        table_top = y
        head_h = max(len(cell) for cell in head_cells) * line_height(head_font) + 2 * cell_pad
        if draw:
            draw.rectangle([table_left, y, table_right, y + head_h], fill=0)
            for x, cell in ((table_left + cell_pad, head_cells[0]), (split_x + cell_pad, head_cells[1])):
                for i, line in enumerate(cell):
                    draw.text((x, y + cell_pad + i * line_height(head_font)), line, font=head_font, fill=255)
        y += head_h

        for cell in body_cells:
            text_h = len(cell) * line_height(body_font)
            row_h = max(min_row, text_h + 2 * cell_pad)
            if draw:
                text_y = y + (row_h - text_h) // 2
                for i, line in enumerate(cell):
                    draw.text((table_left + cell_pad, text_y + i * line_height(body_font)), line, font=body_font, fill=0)
                draw.line([table_left, y + row_h, table_right, y + row_h], fill=0, width=2)
            y += row_h

        if draw:
            draw.rectangle([table_left, table_top, table_right, y], outline=0, width=2)
            draw.line([split_x, table_top, split_x, y], fill=0, width=2)
        y += 10
        for line in footer_lines:
            if draw:
                draw.text((margin, y), line, font=small_font, fill=0)
            y += line_height(small_font)
        return y + margin

    copy_height = draw_copy(None, 0)
    cut_gap = 28  # Platz für die Schnittlinie zwischen zwei Ausdrucken
    total_height = copies * copy_height + (copies - 1) * cut_gap

    img = Image.new("L", (PAPER_WIDTH, total_height), color=255)
    draw = ImageDraw.Draw(img)
    y = 0
    for copy in range(copies):
        y = draw_copy(draw, y)
        if copy < copies - 1:
            for x in range(0, PAPER_WIDTH, 12):
                draw.line([x, y + cut_gap // 2, x + 6, y + cut_gap // 2], fill=0, width=1)
            y += cut_gap

    out_path = Path(tempfile.mkstemp(suffix=".png")[1])
    img.save(out_path)
    return out_path


def main() -> None:
    reexec_in_venv()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--copies", type=int, default=1, help="Anzahl Ausdrucke, eine Tabelle pro Team (Default 1)")
    parser.add_argument("--preview", metavar="DATEI.png", help="Nur das Bild speichern, nicht drucken")
    parser.add_argument("--printer-address", help="Überschreibt MXW01_PRINTER_ADDRESS aus .env")
    parser.add_argument("--font-scale", type=float, default=DEFAULT_FONT_SCALE, help="Skaliert Schrift und Zeilenhöhe (Default 1.0)")
    args = parser.parse_args()
    if args.copies < 1:
        parser.error("--copies muss mindestens 1 sein")

    title, header, rows = read_lesson(LESSON_FILE)
    image_path = build_table_image(title, header, rows, args.font_scale, args.copies)

    if args.preview:
        Path(args.preview).write_bytes(image_path.read_bytes())
        image_path.unlink(missing_ok=True)
        print(f"Vorschau gespeichert: {args.preview}")
        return

    env = account_printout.load_env_file(SCRIPT_DIR / ".env")
    printer_address = args.printer_address or env.get("MXW01_PRINTER_ADDRESS")
    if not printer_address:
        image_path.unlink(missing_ok=True)
        sys.exit("MXW01_PRINTER_ADDRESS fehlt (in scripts/local-tools/.env setzen oder --printer-address übergeben).")
    try:
        account_printout.print_receipt(image_path, printer_address)
    finally:
        image_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
