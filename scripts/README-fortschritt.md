# Fortschritt lokal tracken

Wenn du die Jupyter-Notebooks **lokal** ausführst (z.B. in Jupyter Lab oder VS Code), kannst du trotzdem Punkte und Belohnungen sammeln.

## Ablauf

1. **Skript ausführen**, wenn du eine Mission gemeistert hast:
   ```bash
   python fortschritt.py
   ```
   Das Skript fragt dich interaktiv:
   - Welche Questreihe? (Abenteuer / Pferde / Sci-Fi)
   - Welche Woche? (1–12)
   - Was hast du beendet? (Mission 1–3 oder Boss-Quest 1–3)

   Alternativ mit direkten Argumenten:
   ```bash
   python fortschritt.py add abenteuer w10-m1
   ```
   (Falls nötig: `python3` statt `python`)
   Das erstellt bzw. aktualisiert `mein-fortschritt.json` im aktuellen Verzeichnis.

2. **Auf der Website importieren**: Öffne den Python-Kurs, klappe „Deine gesammelten Belohnungen“ auf und klicke auf „📥 Importieren“. Wähle deine `mein-fortschritt.json` – die Missionen werden mit deinem Stand zusammengeführt.

## Befehle

| Befehl | Beispiel | Beschreibung |
|--------|----------|--------------|
| (ohne) | `python fortschritt.py` | **Interaktiv** – fragt, was du beendet hast |
| `add` | `python fortschritt.py add abenteuer w10-m1` | Mission direkt einlösen |
| `unclaim` | `python fortschritt.py unclaim abenteuer w10-m1` | Einlösen rückgängig machen |
| `show` | `python fortschritt.py show` | Aktuellen Stand anzeigen |

## Mission-IDs

Format: `w[Woche]-[m|boss][Nummer]`

- **Missionen 1–3:** `w1-m1`, `w1-m2`, `w1-m3`, …
- **Boss-Quests 1–3:** `w1-boss1`, `w1-boss2`, `w1-boss3`, …

Beispiele: `w5-m2` = Mission 2 in Woche 5, `w10-boss3` = Boss-Quest 3 in Woche 10.

## Varianten

- `abenteuer` – XP & Abenteuer-Items
- `pferde` – Huf-Punkte & Pferde-Items
- `scifi` – Cyber Credits & Sci-Fi-Items

## Dateien

- `fortschritt.py` – dieses Skript
- `rewards-manifest.json` – muss im gleichen Ordner liegen (oder im Projekt unter `public/`)
- `mein-fortschritt.json` – wird automatisch erstellt (im aktuellen Verzeichnis)

## Export von der Website

Nutze „📤 Exportieren“ auf der Kursseite, um deinen Fortschritt als JSON herunterzuladen – z.B. als Backup oder zum Übertragen auf einen anderen Rechner.
