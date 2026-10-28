#!/usr/bin/env python3
"""Zeichnet die Bilder für die micro:bit-Kurse "Erste Schritte" und "Fang den Stern" als SVG.

Aufruf: python3 scripts/build_microbit_bilder.py
Schreibt nach public/microbit/einfuehrung/ (auch die Hilfe beim Verbinden, die alle Kurse zeigen
dürfen) und public/microbit/sterne/. Die SVGs werden mit eingecheckt; wer ein Bild ändert, ändert
es hier und lässt das Skript neu laufen (nie die SVGs von Hand bearbeiten).

Das Spielfeld ist die 5×5-LED-Anzeige: x zählt von links (0) nach rechts (4), y von oben (0) nach
unten (4). Der Korb steht immer in Reihe y = 4, der Stern fällt von y = 0 nach unten. Ab Stufe 4
(und in der Werkstatt) ist der Korb zwei Lampen breit: korb und korb + 1.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'public' / 'microbit'
FONT = 'font-family="Arial, Helvetica, sans-serif"'

BOARD = '#23262b'
LED_OFF = '#4a4f57'
LED_ON = '#ff3030'
LED_DIM = '#8f2a2a'
BUTTON = '#9aa0a8'
PRESSED = '#f28c28'
TEXT = '#222'
MUTED = '#666'
GOOD = '#2e7d32'
BAD = '#c62828'
ACCENT = '#4a2274'

# Zahlen in der Schrift des micro:bit (nur die, die ein Bild braucht)
DIGITS = {
    '3': ['.###.', '....#', '..##.', '....#', '.###.'],
}

# Eingebaute Bilder des micro:bit (Herz, Fröhlich, Traurig)
ICONS = {
    'herz': ['.#.#.', '#####', '#####', '.###.', '..#..'],
    'froehlich': ['.....', '.#.#.', '.....', '#...#', '.###.'],
    'traurig': ['.....', '.#.#.', '.....', '.###.', '#...#'],
}


def pattern(rows):
    return {(x, y): 'on' for y, row in enumerate(rows) for x, c in enumerate(row) if c == '#'}


def svg(width, height, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="{title}">'
        f'<rect width="{width}" height="{height}" fill="#fff"/>'
        + ''.join(body) + '</svg>\n'
    )


def text(x, y, content, size=14, color=TEXT, weight='normal', anchor='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}" '
            f'font-weight="{weight}" {FONT}>{content}</text>')


def display(x0, y0, pixels=None, cell=22, pressed=None, buttons=True, coords=False):
    """Eine micro:bit-Vorderseite. pixels: {(x, y): 'on' | 'dim'}. Breite = 7 * cell + 2 * Knopfrand."""
    pixels = pixels or {}
    pad = cell
    side = 5 * cell + 2 * pad
    knopf = cell * 1.4 if buttons else 0
    width = side + 2 * knopf
    parts = [f'<rect x="{x0}" y="{y0}" width="{width}" height="{side}" rx="{cell * 0.6}" fill="{BOARD}"/>']
    for gx in range(5):
        for gy in range(5):
            state = pixels.get((gx, gy))
            color = LED_ON if state == 'on' else LED_DIM if state == 'dim' else LED_OFF
            cx = x0 + knopf + pad + gx * cell + cell / 2
            cy = y0 + pad + gy * cell + cell / 2
            if state == 'on':
                parts.append(f'<circle cx="{cx}" cy="{cy}" r="{cell * 0.42}" fill="{LED_ON}" opacity="0.35"/>')
            parts.append(f'<rect x="{cx - cell * 0.14}" y="{cy - cell * 0.24}" width="{cell * 0.28}" '
                         f'height="{cell * 0.48}" rx="2" fill="{color}"/>')
    if buttons:
        for name, bx in (('A', x0 + knopf / 2), ('B', x0 + width - knopf / 2)):
            by = y0 + side / 2
            ring = f' stroke="{PRESSED}" stroke-width="4"' if pressed == name else ''
            parts.append(f'<circle cx="{bx}" cy="{by}" r="{cell * 0.42}" fill="{BUTTON}"{ring}/>')
            parts.append(text(bx, by - cell * 0.62, name, size=cell * 0.6, color='#fff', weight='bold'))
    if coords:
        for i in range(5):
            cx = x0 + knopf + pad + i * cell + cell / 2
            parts.append(text(cx, y0 - 8, str(i), size=13, color=ACCENT, weight='bold'))
            cy = y0 + pad + i * cell + cell / 2
            parts.append(text(x0 - 12, cy + 5, str(i), size=13, color=ACCENT, weight='bold'))
    return parts, width, side


def arrow(x1, x2, y, label=None, color=MUTED):
    parts = [f'<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" stroke="{color}" stroke-width="3"/>',
             f'<polygon points="{x2},{y} {x2 - 10},{y - 6} {x2 - 10},{y + 6}" fill="{color}"/>']
    if label:
        parts.append(text((x1 + x2) / 2, y - 10, label, size=13, color=color, weight='bold'))
    return parts


def frames(title, steps, cell=16, gap=56, per_row=2):
    """Bildfolge: steps = [(pixels, pressed, unterschrift, pfeil_zum_nächsten)], höchstens per_row je Zeile."""
    _, w, h = display(0, 0, cell=cell)
    cols = min(len(steps), per_row)
    rows = (len(steps) + per_row - 1) // per_row
    width = 20 + cols * w + (cols - 1) * gap + 20
    row_h = h + 56
    body = [text(width / 2, 26, title, size=17, weight='bold')]
    for i, (pixels, pressed, caption, label) in enumerate(steps):
        x = 20 + (i % per_row) * (w + gap)
        top = 44 + (i // per_row) * row_h
        parts, _, _ = display(x, top, pixels, cell=cell, pressed=pressed)
        body += parts
        if caption:
            color = GOOD if caption.startswith('+') else BAD if caption.startswith('✗') else TEXT
            body.append(text(x + w / 2, top + h + 24, caption, size=13, color=color, weight='bold'))
        if i < len(steps) - 1 and (i + 1) % per_row:
            body += arrow(x + w + 6, x + w + gap - 6, top + h / 2, label)
    return svg(width, 44 + rows * row_h, title, body)


def korb(x, extra=None, breit=1):
    """Korb ab Spalte x, breit Lampen nach rechts (ab Stufe 4 zwei)."""
    pixels = {(x + i, 4): 'on' for i in range(breit)}
    pixels.update(extra or {})
    return pixels


def spielfeld():
    title = 'Das Spielfeld: 5 mal 5 Lampen'
    parts, w, h = display(70, 70, {(2, 0): 'on', (2, 4): 'on'}, cell=40, coords=True)
    body = [text(240, 28, title, size=18, weight='bold')]
    body += parts
    knopf = 40 * 1.4
    body.append(text(70 + knopf + 40 + 5 * 40 + 8, 62, 'x →', size=14, color=ACCENT, weight='bold', anchor='start'))
    body.append(text(58, 70 + 40 + 5 * 40 + 22, 'y ↓', size=14, color=ACCENT, weight='bold'))
    # Beschriftungen Stern und Korb (rechts neben dem micro:bit)
    star_y = 70 + 40 + 20
    korb_y = 70 + 40 + 4 * 40 + 20
    lx = 70 + w + 18
    body.append(f'<line x1="{70 + 56 + 40 + 2 * 40 + 34}" y1="{star_y}" x2="{lx}" y2="{star_y}" stroke="{MUTED}" stroke-dasharray="4 4"/>')
    body.append(f'<line x1="{70 + 56 + 40 + 2 * 40 + 34}" y1="{korb_y}" x2="{lx}" y2="{korb_y}" stroke="{MUTED}" stroke-dasharray="4 4"/>')
    body.append(text(lx + 6, star_y - 4, 'Stern', size=16, weight='bold', anchor='start'))
    body.append(text(lx + 6, star_y + 14, 'x = 2, y = 0', size=13, color=MUTED, anchor='start'))
    body.append(text(lx + 6, korb_y - 4, 'Korb', size=16, weight='bold', anchor='start'))
    body.append(text(lx + 6, korb_y + 14, 'x = 2, y = 4', size=13, color=MUTED, anchor='start'))
    return svg(lx + 120, 70 + h + 30, title, body)


def ziel():
    return frames('So sieht euer Spiel aus', [
        (korb(1, {(3, 0): 'on'}), None, 'Ein Stern fällt', None),
        (korb(2, {(3, 2): 'on'}), 'B', 'Korb hinterher', None),
        (korb(3, {(3, 3): 'on'}), 'B', 'gleich …', None),
        (korb(3), None, '+1 Punkt', None),
    ])


def start():
    title = 'Das soll euer micro:bit zeigen'
    parts, w, h = display(20, 44, {(2, 0): 'on', (2, 4): 'on'}, cell=26)
    return svg(w + 40, h + 64, title, [text((w + 40) / 2, 26, title, size=16, weight='bold')] + parts)


def stufe1():
    return frames('Knopf A schiebt nach links, Knopf B nach rechts', [
        (korb(2), None, 'Start: x = 2', 'A'),
        (korb(1), 'A', 'x = 1', 'A'),
        (korb(0), 'A', 'x = 0', 'B'),
        (korb(1), 'B', 'x = 1', None),
    ])


def rand():
    title = 'Am Rand: Knopf A bei x = 0'
    _, w, h = display(0, 0, cell=16)
    body = [text(330, 26, title, size=17, weight='bold')]
    parts, _, _ = display(20, 56, korb(0), cell=16)
    body += parts
    body.append(text(20 + w / 2, 56 + h + 24, 'x = 0', size=13, weight='bold'))
    for i, (pixels, caption, color) in enumerate([
        ({}, '✗ x = -1: Korb weg', BAD),
        (korb(0), '✓ Korb bleibt stehen', GOOD),
    ]):
        x = 20 + w + 120 + i * (w + 60)
        parts, _, _ = display(x, 56, pixels, cell=16, pressed='A')
        body += parts
        body.append(text(x + w / 2, 56 + h + 24, caption, size=13, color=color, weight='bold'))
    body += arrow(20 + w + 10, 20 + w + 110, 56 + h / 2, 'A')
    width = 20 + w + 120 + 2 * w + 60 + 20
    body[0] = text(width / 2, 26, title, size=17, weight='bold')
    return svg(width, 56 + h + 44, title, body)


def stufe2():
    steps = [(korb(1, {(3, y): 'on'}), None, f'y = {y}', None) for y in range(5)]
    steps.append((korb(1, {(0, 0): 'on'}), None, 'neuer Stern', None))
    return frames('Der Stern fällt, dann kommt der nächste', steps, per_row=3)


def stufe3():
    title = 'Gefangen oder daneben?'
    _, w, h = display(0, 0, cell=16)
    gap = 56
    width = 20 + 3 * w + 2 * gap + 20
    body = [text(width / 2, 26, title, size=17, weight='bold')]
    rows = [
        [(korb(2, {(2, 3): 'on'}), ''), (korb(2), '+1 Punkt'), (korb(2, {(4, 0): 'on'}), 'weiter geht’s')],
        [(korb(0, {(3, 3): 'on'}), ''), (korb(0, {(3, 4): 'on'}), '✗ daneben'),
         ({(x, y): 'on' for y, row in enumerate(DIGITS['3']) for x, c in enumerate(row) if c == '#'},
          'eure Punkte: 3')],
    ]
    for r, row in enumerate(rows):
        top = 44 + r * (h + 56)
        for i, (pixels, caption) in enumerate(row):
            x = 20 + i * (w + gap)
            parts, _, _ = display(x, top, pixels, cell=16)
            body += parts
            if caption:
                color = GOOD if caption.startswith('+') else BAD if caption.startswith('✗') else TEXT
                body.append(text(x + w / 2, top + h + 22, caption, size=13, color=color, weight='bold'))
            if i < 2:
                body += arrow(x + w + 6, x + w + gap - 6, top + h / 2)
    return svg(width, 44 + 2 * (h + 56), title, body)


def breiter_korb():
    title = 'Der Korb ist zwei Lampen breit'
    _, w, h = display(0, 0, cell=16)
    gap = 40
    width = 20 + 3 * w + 2 * gap + 20
    body = [text(width / 2, 26, title, size=17, weight='bold')]
    for i, (stern, caption, detail) in enumerate([
        (2, '+1 Punkt', 'Stern bei x = korb'),
        (3, '+1 Punkt', 'Stern bei x = korb + 1'),
        (4, '✗ daneben', 'Stern bei x = 4'),
    ]):
        x = 20 + i * (w + gap)
        parts, _, _ = display(x, 44, korb(2, {(stern, 3): 'on'}, breit=2), cell=16)
        body += parts
        color = GOOD if caption.startswith('+') else BAD
        body.append(text(x + w / 2, 44 + h + 22, caption, size=13, color=color, weight='bold'))
        body.append(text(x + w / 2, 44 + h + 40, detail, size=12, color=MUTED))
    return svg(width, 44 + h + 56, title, body)


def box(x, y, w, h, lines, fill, stroke, size=14, bold_first=True):
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>']
    total = len(lines) * (size + 6)
    start = y + (h - total) / 2 + size
    for i, line in enumerate(lines):
        parts.append(text(x + w / 2, start + i * (size + 6), line, size=size,
                          weight='bold' if bold_first and i == 0 or bold_first is None else 'normal'))
    return parts


def hilfe():
    """Prüfliste als Ablauf: jede Frage links, bei Nein der Tipp rechts."""
    title = 'Der micro:bit verbindet sich nicht?'
    steps = [
        (['1. Chrome oder Edge?'], ['Seite in Chrome', 'oder Edge öffnen']),
        (['2. Leuchtet hinten', 'die gelbe Lampe?'], ['Kabel fester stecken,', 'anderen USB-Anschluss nehmen']),
        (['3. Zeigt der Computer', 'ein Laufwerk MICROBIT?'], ['Anderes Kabel nehmen', '(manche Kabel laden nur)']),
        (['4. Nur ein Tab', 'mit dem Editor offen?'], ['Andere Tabs schließen,', 'Kabel ab- und anstecken']),
        (['5. Im Fenster den', 'micro:bit ausgewählt?'], ['Noch einmal verbinden,', '„BBC micro:bit“ anklicken']),
    ]
    bw, bh, gap = 230, 62, 26
    left, right = 20, 330
    body = [text(290, 30, title, size=18, weight='bold')]
    y = 52
    for i, (frage, tipp) in enumerate(steps):
        body += box(left, y, bw, bh, frage, '#f3eefa', ACCENT, bold_first=None)
        body += box(right, y, bw, bh, tipp, '#fdecea', BAD, size=13, bold_first=False)
        body += arrow(left + bw + 4, right - 4, y + bh / 2, 'nein', BAD)
        if i < len(steps) - 1:
            body.append(f'<line x1="{left + bw / 2}" y1="{y + bh}" x2="{left + bw / 2}" y2="{y + bh + gap - 6}" stroke="{GOOD}" stroke-width="3"/>')
            body.append(f'<polygon points="{left + bw / 2},{y + bh + gap} {left + bw / 2 - 6},{y + bh + gap - 10} {left + bw / 2 + 6},{y + bh + gap - 10}" fill="{GOOD}"/>')
            body.append(text(left + bw / 2 + 22, y + bh + gap / 2 + 4, 'ja', size=12, color=GOOD, weight='bold'))
        y += bh + gap
    body += box(left, y, 540, 56, ['Immer noch nicht? Plan B: Datei auf MICROBIT ziehen', '(siehe unten)'], '#e8f5e9', GOOD)
    return svg(580, y + 76, title, body)


def plan_b():
    title = 'Plan B: Programm als Datei übertragen'
    body = [text(300, 28, title, size=17, weight='bold')]
    # Datei
    body.append(f'<path d="M40 60 h70 l24 24 v86 h-94 z" fill="#f3eefa" stroke="{ACCENT}" stroke-width="2"/>')
    body.append(f'<path d="M110 60 v24 h24" fill="none" stroke="{ACCENT}" stroke-width="2"/>')
    body.append(text(87, 130, '.hex', size=18, color=ACCENT, weight='bold'))
    body.append(text(87, 196, '1. Herunterladen', size=13, weight='bold'))
    body.append(text(87, 214, 'oder Speichern', size=13))
    body += arrow(150, 260, 115, 'ziehen', ACCENT)
    # Laufwerk
    body.append(f'<rect x="276" y="76" width="150" height="80" rx="10" fill="#eceff1" stroke="#607d8b" stroke-width="2"/>')
    body.append(f'<circle cx="406" cy="140" r="5" fill="{GOOD}"/>')
    body.append(text(351, 122, 'MICROBIT', size=16, weight='bold'))
    body.append(text(351, 196, '2. auf das Laufwerk', size=13, weight='bold'))
    body.append(text(351, 214, 'ziehen', size=13))
    body += arrow(440, 500, 115, None, ACCENT)
    body.append(f'<circle cx="540" cy="115" r="26" fill="#fff8e1" stroke="#f9a825" stroke-width="2"/>')
    body.append(text(540, 122, '…', size=22, color='#f9a825', weight='bold'))
    body.append(text(540, 196, '3. Gelbe Lampe', size=13, weight='bold'))
    body.append(text(540, 214, 'blinkt: fertig!', size=13))
    return svg(600, 236, title, body)


def schneller():
    return frames('Immer schneller', per_row=3, steps=[
        (korb(2, {(2, 1): 'on'}, breit=2), None, '400 ms', None),
        (korb(2, {(2, 1): 'on'}, breit=2), None, '350 ms', None),
        (korb(2, {(2, 1): 'on'}, breit=2), None, '300 ms', None),
    ])


def bombe():
    return frames('Achtung, Bombe! Sie leuchtet schwach.', per_row=3, steps=[
        (korb(1, {(0, 1): 'on', (3, 0): 'dim'}, breit=2), None, 'Stern und Bombe', None),
        (korb(2, {(0, 3): 'on', (3, 2): 'dim'}, breit=2), 'B', 'falsch gelenkt …', None),
        (korb(2, {(3, 4): 'dim'}, breit=2), None, '✗ Bombe gefangen', None),
    ])


def neigen():
    title = 'Steuern durch Neigen'
    parts, w, h = display(0, 0, korb(1, {(3, 1): 'on'}, breit=2), cell=18)
    body = [text(200, 26, title, size=17, weight='bold')]
    body.append(f'<g transform="translate({200 - w / 2} 60) rotate(-12 {w / 2} {h / 2})">' + ''.join(parts) + '</g>')
    body.append(text(200, 60 + h + 40, 'nach links neigen: Korb nach links', size=13, color=ACCENT, weight='bold'))
    return svg(400, 60 + h + 56, title, body)


def vorderseite():
    """Vorderseite mit Beschriftungen links und rechts."""
    title = 'Die Vorderseite des micro:bit'
    cell = 30
    x0, y0 = 170, 70
    parts, w, h = display(x0, y0 + 40, pattern(ICONS['herz']), cell=cell)
    body = [text(340, 30, title, size=18, weight='bold')]
    # Platine nach oben (Logo) und unten (Anschlüsse) verlängern
    body.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h + 110}" rx="18" fill="{BOARD}"/>')
    body += parts
    # Logo: zwei Kreise in einem Oval, wie auf dem micro:bit V2
    lx, ly = x0 + w / 2, y0 + 22
    body.append(f'<rect x="{lx - 26}" y="{ly - 12}" width="52" height="24" rx="12" fill="none" stroke="#d4a017" stroke-width="3"/>')
    body.append(f'<circle cx="{lx - 12}" cy="{ly}" r="5" fill="#d4a017"/><circle cx="{lx + 12}" cy="{ly}" r="5" fill="#d4a017"/>')
    # Anschlüsse unten
    pins_y = y0 + 40 + h + 14
    labels = ['0', '1', '2', '3V', 'GND']
    for i, label in enumerate(labels):
        px = x0 + 22 + i * (w - 44) / 4
        body.append(f'<rect x="{px - 16}" y="{pins_y}" width="32" height="44" rx="4" fill="#d4a017"/>')
        body.append(f'<circle cx="{px}" cy="{pins_y + 16}" r="7" fill="{BOARD}"/>')
        body.append(text(px, pins_y + 40, label, size=11, color=BOARD, weight='bold'))

    def callout(tx, ty, ax, ay, lines, anchor):
        out = [f'<line x1="{tx}" y1="{ty}" x2="{ax}" y2="{ay}" stroke="{ACCENT}" stroke-width="2"/>',
               f'<circle cx="{ax}" cy="{ay}" r="4" fill="{ACCENT}"/>']
        lx2 = tx - 6 if anchor == 'end' else tx + 6
        for i, line in enumerate(lines):
            out.append(text(lx2, ty + 5 + i * 17, line, size=14 if i == 0 else 12,
                            color=TEXT if i == 0 else MUTED, weight='bold' if i == 0 else 'normal', anchor=anchor))
        return out

    knopf = cell * 1.4
    side_y = y0 + 40 + h / 2
    body += callout(150, side_y, x0 + knopf / 2, side_y, ['Knopf A', 'links'], 'end')
    body += callout(x0 + w + 20, side_y, x0 + w - knopf / 2, side_y, ['Knopf B', 'rechts'], 'start')
    body += callout(x0 + w + 20, y0 + 22, lx + 28, ly, ['Logo', 'reagiert auf Berühren'], 'start')
    body += callout(150, y0 + 40 + 40, x0 + knopf + cell, y0 + 40 + cell * 1.5, ['LED-Anzeige', '5 × 5 Lampen'], 'end')
    body += callout(150, pins_y + 22, x0 + 6, pins_y + 22, ['Anschlüsse', 'für Kabel'], 'end')
    return svg(680, pins_y + 70, title, body)


def herz():
    title = 'Das soll euer micro:bit zeigen'
    parts, w, h = display(20, 44, pattern(ICONS['herz']), cell=26)
    return svg(w + 40, h + 64, title, [text((w + 40) / 2, 26, title, size=16, weight='bold')] + parts)


def knoepfe():
    return frames('Knopf A: fröhlich, Knopf B: traurig', [
        (pattern(ICONS['froehlich']), 'A', 'Knopf A', None),
        (pattern(ICONS['traurig']), 'B', 'Knopf B', None),
    ], cell=18)


IMAGES = {
    'einfuehrung/vorderseite': vorderseite,
    'einfuehrung/herz': herz,
    'einfuehrung/knoepfe': knoepfe,
    'einfuehrung/hilfe': hilfe,
    'einfuehrung/plan-b': plan_b,
    'sterne/spielfeld': spielfeld,
    'sterne/ziel': ziel,
    'sterne/start': start,
    'sterne/stufe-1': stufe1,
    'sterne/rand': rand,
    'sterne/stufe-2': stufe2,
    'sterne/stufe-3': stufe3,
    'sterne/breiter-korb': breiter_korb,
    'sterne/schneller': schneller,
    'sterne/bombe': bombe,
    'sterne/neigen': neigen,
}


def main():
    for name, build in IMAGES.items():
        target = OUT / f'{name}.svg'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build(), encoding='utf-8')
        print(f'✓ {name}.svg')


if __name__ == '__main__':
    main()
