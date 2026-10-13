"""Forscher-Tabelle aus Stufe 8 des micro:bit-Kurses ("Die Linie sehen") zum Ausfüllen.
Die Zeilen kommen direkt aus dem Lektionstext, der Ausdruck bleibt also automatisch aktuell.
"""
from pathlib import Path

from druck import PAPER_WIDTH, REPO_ROOT, DruckerError, load_font, save_printout

LESSON_FILE = REPO_ROOT / "content" / "microbit-auto" / "lektion-09.md"
DEFAULT_TABLE_FONT_SCALE = 1.0


def read_lesson_table(path: Path) -> tuple[str, list[str], list[list[str]]]:
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
        raise DruckerError(f"Keine Tabelle in {path} gefunden.")
    # table[1] ist die Trennzeile |---|---|
    return title, table[0], table[2:]


def build_table_image(title: str, header: list[str], rows: list[list[str]], font_scale: float, copies: int):
    from PIL import Image, ImageDraw

    margin = 10
    cell_pad = 8
    number_col = round(112 * font_scale)  # Spalte zum Eintragen der Zahl
    table_left = margin
    table_right = PAPER_WIDTH - margin
    split_x = table_right - number_col
    text_col = split_x - table_left - 2 * cell_pad

    def font(size: int, bold: bool = False):
        return load_font(round(size * font_scale), bold)

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

    return img


def save_table(copies: int, font_scale: float = DEFAULT_TABLE_FONT_SCALE) -> Path:
    """Baut `copies` Tabellen untereinander (mit Schnittlinien) und speichert sie unter ausdrucke/."""
    if copies < 1:
        raise DruckerError("Die Anzahl muss mindestens 1 sein.")
    title, header, rows = read_lesson_table(LESSON_FILE)
    return save_printout(build_table_image(title, header, rows, font_scale, copies), f"tabelle_{copies}x")
