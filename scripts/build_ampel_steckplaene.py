#!/usr/bin/env python3
"""Zeichnet die Steckpläne für den micro:bit-Kurs "Die Ampelanlage" als SVG.

Aufruf: python3 scripts/build_ampel_steckplaene.py
Schreibt nach public/microbit/ampel/. Die SVGs werden mit eingecheckt; wer den Aufbau ändert,
ändert ihn hier und lässt das Skript neu laufen (nie die SVGs von Hand bearbeiten).

Vorbild ist das Mini-Breadboard (17 Reihen) an der T-förmigen "micro:bit GPIO Board"-Platine:
Die Lücke läuft senkrecht, links sind nur die zwei Löcher direkt an der Lücke frei (der Rest liegt
unter der Platine), rechts sind es fünf. Reihen werden von oben (an der Platine) gezählt.

Erreichbar ist nur eine Stiftleiste: 3.3V, GND, GND, P20, P19, P16, P15, P14, P13, P12, P11, P10, 3.3V.
Pins: Autoampel P16/P15/P14, Fußgänger P13/P12 (in Leisten-Reihenfolge), Taster P20. P10 (LED-Anzeige),
P11 (Knopf B) und P19 bleiben frei. Nur zwei GND-Stifte: Jede Ampel hat eine GND-Reihe mit einem Kabel
zu GND, das kurze Bein jeder LED ist mit einer Brücke (Kabel Stecker auf Stecker) dorthin verbunden.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'public' / 'microbit' / 'ampel'

ROWS = 17
PITCH = 28
TOP = 84
LEFT_HOLES = [150, 178, 206, 234, 262]   # die ersten drei liegen unter der Platine
FREE_LEFT = LEFT_HOLES[3:]
RIGHT_HOLES = [338, 366, 394, 422, 450]
WIDTH = 620
HEIGHT = TOP + (ROWS - 1) * PITCH + 46

LED_COLORS = {'rot': '#e53935', 'gelb': '#fdd835', 'gruen': '#43a047'}
WIRE = '#f28c28'
GND_WIRE = '#222'
BRIDGE = '#1e88e5'
FONT = 'font-family="Arial, Helvetica, sans-serif"'


def y(row):
    return TOP + (row - 1) * PITCH


def board(title):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'width="{WIDTH}" height="{HEIGHT}" role="img" aria-label="{title}">',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#fff"/>',
        f'<text x="{WIDTH / 2}" y="26" text-anchor="middle" font-size="18" font-weight="bold" {FONT}>{title}</text>',
        # Breadboard
        f'<rect x="124" y="{TOP - 22}" width="352" height="{(ROWS - 1) * PITCH + 44}" rx="10" fill="#f7f4ec" stroke="#c9c2b0"/>',
        # Lücke
        f'<rect x="282" y="{TOP - 22}" width="36" height="{(ROWS - 1) * PITCH + 44}" fill="#e2dccb"/>',
        f'<text x="300" y="{TOP - 30}" text-anchor="middle" font-size="12" fill="#555" {FONT}>Lücke</text>',
    ]
    for row in range(1, ROWS + 1):
        parts.append(f'<text x="22" y="{y(row) + 4}" text-anchor="middle" font-size="12" fill="#777" {FONT}>{row}</text>')
        for x in LEFT_HOLES + RIGHT_HOLES:
            parts.append(f'<rect x="{x - 4}" y="{y(row) - 4}" width="8" height="8" fill="#555"/>')
    parts.append(f'<text x="22" y="{TOP - 30}" text-anchor="middle" font-size="11" fill="#777" {FONT}>Reihe</text>')
    # Platine deckt die ersten drei Löcher links ab
    parts.append(f'<rect x="124" y="{TOP - 22}" width="96" height="{(ROWS - 1) * PITCH + 44}" fill="#1d4e89" opacity="0.92"/>')
    parts.append(f'<text x="172" y="{y(8) + 4}" text-anchor="middle" font-size="11" fill="#fff" {FONT} '
                 f'transform="rotate(-90 172 {y(8)})">micro:bit-Platine</text>')
    return parts


def dot(x, yy, color='#000'):
    return f'<circle cx="{x}" cy="{yy}" r="5" fill="{color}" stroke="#fff" stroke-width="1.5"/>'


def signal_wire(row, label, target_x=FREE_LEFT[0]):
    yy = y(row)
    return [
        f'<text x="104" y="{yy + 5}" text-anchor="end" font-size="14" font-weight="bold" {FONT}>{label}</text>',
        # Endet das Kabel rechts der Lücke, springt es im Bogen über die linken Löcher (nicht eingesteckt).
        (f'<line x1="108" y1="{yy}" x2="{target_x}" y2="{yy}" stroke="{WIRE}" stroke-width="5" stroke-linecap="round"/>'
         if target_x in FREE_LEFT else
         f'<path d="M 108 {yy} L 214 {yy} Q 300 {yy - 26} {target_x} {yy}" fill="none" stroke="{WIRE}" '
         f'stroke-width="5" stroke-linecap="round"/>'),
        dot(target_x, yy, WIRE),
    ]


def bridge(from_row, to_row, end_hole, lane):
    """Brücke (Kabel Stecker auf Stecker) vom äußersten Loch der Reihe `from_row` in Loch
    `end_hole` (Index rechts) der GND-Reihe. `lane` = 0: kurzer, direkter Weg; sonst läuft die
    Brücke auf einer eigenen Spur rechts neben dem Breadboard (weiter außen je höher `lane`)."""
    x1, y1 = RIGHT_HOLES[-1], y(from_row)
    x2, y2 = RIGHT_HOLES[end_hole], y(to_row)
    if lane == 0:
        d = f'M {x1} {y1} L {x2} {y2}'
    else:
        side = -1 if to_row > from_row else 1   # kommt von oben bzw. von unten in die GND-Reihe
        lx = x1 + 15 + lane * 15
        if end_hole == len(RIGHT_HOLES) - 1:
            d = f'M {x1} {y1} L {lx} {y1} L {lx} {y2} L {x2} {y2}'
        else:
            d = f'M {x1} {y1} L {lx} {y1} L {lx} {y2 + side * 14} L {x2} {y2}'
    return [
        f'<path d="{d}" fill="none" stroke="{BRIDGE}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
        dot(x1, y1, BRIDGE), dot(x2, y2, BRIDGE),
    ]


def resistor(row):
    yy = y(row)
    x1, x2 = FREE_LEFT[1], RIGHT_HOLES[0]
    bands = ['#7b4a12', '#2e7d32', '#111', '#111', '#7b4a12']   # 150 Ω: braun grün schwarz schwarz braun
    parts = [
        f'<line x1="{x1}" y1="{yy}" x2="{x2}" y2="{yy}" stroke="#999" stroke-width="3"/>',
        f'<rect x="278" y="{yy - 7}" width="44" height="14" rx="6" fill="#9ec5e8" stroke="#6a8fb0"/>',
    ]
    for i, color in enumerate(bands):
        parts.append(f'<rect x="{283 + i * 7 + (4 if i == 4 else 0)}" y="{yy - 7}" width="3.5" height="14" fill="{color}"/>')
    parts += [dot(x1, yy, '#999'), dot(x2, yy, '#999')]
    return parts


def led(row, color):
    """Langes Bein (+) in `row`, kurzes Bein (-) in der Reihe darunter, beide rechts im zweiten Loch."""
    x = RIGHT_HOLES[1]
    ya, yk = y(row), y(row + 1)
    cx, cy = x + 46, (ya + yk) / 2
    fill = LED_COLORS[color]
    return [
        f'<line x1="{x}" y1="{ya}" x2="{cx - 10}" y2="{cy - 6}" stroke="#999" stroke-width="3"/>',
        f'<line x1="{x}" y1="{yk}" x2="{cx - 10}" y2="{cy + 6}" stroke="#999" stroke-width="3"/>',
        f'<circle cx="{cx}" cy="{cy}" r="15" fill="{fill}" stroke="#333" stroke-width="1.5"/>',
        f'<circle cx="{cx - 5}" cy="{cy - 5}" r="4" fill="#fff" opacity="0.6"/>',
        dot(x, ya, '#999'), dot(x, yk, '#999'),
        f'<text x="{x - 2}" y="{ya - 8}" text-anchor="middle" font-size="13" font-weight="bold" fill="#c62828" {FONT}>+</text>',
    ]


def ampel_led(row, color, pin):
    return signal_wire(row, pin) + resistor(row) + led(row, color)


def gnd_row(row, cathode_rows):
    """GND-Reihe: ein Kabel von einem GND-Stift der Platine ins innerste Loch, dazu eine Brücke
    von jeder Reihe in `cathode_rows`. Nähere Reihen enden weiter außen, so kreuzt sich nichts."""
    yy = y(row)
    parts = [f'<rect x="{RIGHT_HOLES[0] - 12}" y="{yy - 10}" width="{RIGHT_HOLES[-1] - RIGHT_HOLES[0] + 24}" '
             f'height="20" rx="10" fill="#ececec" stroke="{GND_WIRE}" stroke-width="1.5" stroke-dasharray="4 3"/>']
    for x in RIGHT_HOLES:
        parts.append(f'<rect x="{x - 4}" y="{yy - 4}" width="8" height="8" fill="#555"/>')
    parts += [
        f'<text x="104" y="{yy + 5}" text-anchor="end" font-size="14" font-weight="bold" {FONT}>GND</text>',
        # Kabel von der Platine: läuft über die linken Löcher hinweg (nicht eingesteckt) bis rechts in Loch 1.
        f'<path d="M 108 {yy} L 214 {yy} Q 300 {yy - 26} {RIGHT_HOLES[0]} {yy}" fill="none" stroke="{GND_WIRE}" '
        f'stroke-width="5" stroke-linecap="round"/>',
        dot(RIGHT_HOLES[0], yy, GND_WIRE),
    ]
    # Von oben: die nächste Reihe direkt ins Loch 2, weiter entfernte über Spuren in Loch 3, 4.
    # Von unten (Taster): danach, ebenfalls über eine Spur.
    above = sorted((c for c in cathode_rows if c < row), key=lambda c: row - c)
    below = sorted((c for c in cathode_rows if c > row), key=lambda c: c - row)
    for i, cathode in enumerate(above + below):
        parts += bridge(cathode, row, 2 + i, i)
    return parts


def taster(row_top, row_bottom):
    x1, x2 = RIGHT_HOLES[1], RIGHT_HOLES[3]
    y1, y2 = y(row_top), y(row_bottom)
    parts = [
        f'<rect x="{x1 - 2}" y="{y1 - 2}" width="{x2 - x1 + 4}" height="{y2 - y1 + 4}" rx="4" fill="#444"/>',
        f'<circle cx="{(x1 + x2) / 2}" cy="{(y1 + y2) / 2}" r="15" fill="#222" stroke="#888"/>',
    ]
    parts += [dot(x, yy, '#bbb') for x in (x1, x2) for yy in (y1, y2)]
    parts += signal_wire(row_top, 'P20', RIGHT_HOLES[0])
    return parts


def save(name, parts):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text('\n'.join(parts + ['</svg>']) + '\n', encoding='utf-8')


FUSS_ROT = (10, 'rot', 'P13')
FUSS_GRUEN = (12, 'gruen', 'P12')
AUTO = [(2, 'rot', 'P16'), (4, 'gelb', 'P15'), (6, 'gruen', 'P14')]
AUTO_GND = 8
FUSS_GND = 14
TASTER = (15, 17)


def plan(title, leds, extra=(), extra_gnd=()):
    """`extra_gnd`: weitere Reihen, die mit der GND-Reihe der Fußgänger verbunden werden (Taster)."""
    parts = board(title)
    for row, color, pin in leds:
        parts += ampel_led(row, color, pin)
    auto = [row + 1 for row, _, _ in leds if row < AUTO_GND]
    fuss = [row + 1 for row, _, _ in leds if AUTO_GND < row < FUSS_GND]
    if auto:
        parts += gnd_row(AUTO_GND, auto)
    parts += gnd_row(FUSS_GND, fuss + list(extra_gnd))
    parts += list(extra)
    return parts


def breadboard_explained():
    parts = board('So ist das Breadboard verbunden')
    for row in range(1, ROWS + 1):
        yy = y(row)
        parts.append(f'<rect x="{FREE_LEFT[0] - 8}" y="{yy - 6}" width="{FREE_LEFT[1] - FREE_LEFT[0] + 16}" height="12" rx="6" fill="#43a047" opacity="0.35"/>')
        parts.append(f'<rect x="{RIGHT_HOLES[0] - 8}" y="{yy - 6}" width="{RIGHT_HOLES[-1] - RIGHT_HOLES[0] + 16}" height="12" rx="6" fill="#43a047" opacity="0.35"/>')
    hint = [
        (y(3), 'Löcher in einer Reihe'),
        (y(3) + 18, 'sind verbunden'),
        (y(9), 'links und rechts'),
        (y(9) + 18, 'der Lücke: getrennt'),
        (y(15), 'Reihe unter Reihe:'),
        (y(15) + 18, 'getrennt'),
    ]
    for yy, text in hint:
        parts.append(f'<text x="{RIGHT_HOLES[-1] + 36}" y="{yy}" font-size="13" fill="#2e7d32" {FONT}>{text}</text>')
    return parts


if __name__ == '__main__':
    save('breadboard.svg', breadboard_explained())
    save('stufe-0.svg', plan('Startklar: die erste LED', [FUSS_ROT]))
    save('stufe-1.svg', plan('Stufe 1: Fußgängerampel', [FUSS_ROT, FUSS_GRUEN]))
    save('stufe-2.svg', plan('Stufe 2 und 3: Fußgänger- und Autoampel', AUTO + [FUSS_ROT, FUSS_GRUEN]))
    save('taster.svg', plan('Werkstatt: echter Ampeldrücker', AUTO + [FUSS_ROT, FUSS_GRUEN], taster(*TASTER), [TASTER[1]]))
    print(f'Steckpläne geschrieben nach {OUT}')
