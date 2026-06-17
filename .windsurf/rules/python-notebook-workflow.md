---
trigger: manual
---

# 🔄 Python-Notebook Workflow: Neue Woche erstellen

Dieser Guide beschreibt den aktuellen Prozess zur Erstellung einer neuen Woche im Python 12-Wochen-Grundkurs.

---

## 📁 Ordnerstruktur (Stand: 2025)

Jede Woche hat **7 Notebooks pro Kurs** in eigenen Unterordnern:

```
content/python-12-wochen-grundkurs/
├── gesamtglossar.ipynb          ← Alle Begriffe aller 12 Wochen
├── woche-X/
│   ├── wocheX.md                ← Wochenbeschreibung (Frontmatter + Inhalt)
│   ├── abenteuer/
│   │   ├── wocheX_abenteuer_0_glossar.ipynb
│   │   ├── wocheX_abenteuer_1_lektion.ipynb
│   │   ├── wocheX_abenteuer_2_debug.ipynb
│   │   ├── wocheX_abenteuer_3_missionen.ipynb
│   │   ├── wocheX_abenteuer_4_reflexion.ipynb
│   │   ├── wocheX_abenteuer_5_loesungen.ipynb
│   │   └── wocheX_abenteuer_6_boss.ipynb
│   ├── pferde/
│   │   └── wocheX_pferde_0_glossar.ipynb  … (gleiche 7 Dateien)
│   └── scifi/
│       └── wocheX_scifi_0_glossar.ipynb   … (gleiche 7 Dateien)
```

---

## 📋 Lehrplan (was wann gelehrt wird)

Immer zuerst `content/python-12-wochen-grundkurs/lehrplan.md` lesen, bevor eine neue Woche erstellt wird. Dort stehen exakt welche Konzepte neu eingeführt werden und was vertieft wird.

**Wichtige Sequenz-Regeln:**
- f-Strings: erst ab Woche 2
- Klassen (`class`): erst ab Woche 10
- break/continue: erst ab Woche 6
- JSON: erst ab Woche 9 (nicht in Woche 7)
- `os`, `shutil`, `pathlib`: NICHT im Kurs

---

## 🗂️ Die 7 Notebook-Typen

| Datei | Inhalt | Besonderheiten |
|-------|--------|----------------|
| `_0_glossar` | Begriffstabelle + Kurzbeispiele + Wiederholung | Format: `Begriff \| Bedeutung \| Beispiel` |
| `_1_lektion` | Lernstoff mit Zauberformel/Lektion/Systemprotokoll-Abschnitten | Kein "Warum nützlich"-Bulletblock |
| `_2_debug` | 3 fehlerhafte Code-Zellen | Vor jeder Bug-Zelle: WHY-Markdown |
| `_3_missionen` | 3 Missionen (⭐⭐ bis ⭐⭐⭐⭐) | Schritt-Format, kein Starter-Code |
| `_4_reflexion` | 3 Reflexionsfragen | Frage IMMER vor Antwort-Platzhalter |
| `_5_loesungen` | Debug-Lösungen + Missions-Lösungsvorschläge | Erst Debug, dann Missionen |
| `_6_boss` | 3 Boss-Quests (⭐⭐⭐⭐ bis ⭐⭐⭐⭐⭐) | Story-getrieben, offen formuliert |

---

## ✍️ Schritt-für-Schritt

### Schritt 1 – Ordner anlegen
```bash
mkdir -p content/python-12-wochen-grundkurs/woche-X/{abenteuer,pferde,scifi}
touch content/python-12-wochen-grundkurs/woche-X/wocheX.md
```

### Schritt 2 – `wocheX.md` erstellen
```markdown
---
title: '📚 Woche X – Thema: Kurzer Untertitel'
---

# 🎯 Die Herausforderung: [Kurzbeschreibung]

[2-3 Sätze über das Problem]

[1 Satz über die Python-Lösung]

## 🎮 Themenwelten zur Auswahl

- **🗺️ Abenteuer-Welt:** [Thematische Beschreibung]
- **🐴 Pferdewirtschaft:** [Thematische Beschreibung]
- **🚀 Sci-Fi-Welt:** [Thematische Beschreibung]

# 🎯 Lernziele
- [Lernziel 1]
- [Lernziel 2]
- [Lernziel 3]
```

### Schritt 3 – 7 × 3 Notebooks erstellen

Für jeden der 7 Typen je 3 thematische Varianten erstellen. Alle Notebooks haben `nbformat: 4`.

---

## 📖 _0_glossar – Format

```markdown
# 📖 Woche X – Glossar
> Dieses Notebook kannst du die ganze Woche offen lassen.

## Begriffe dieser Woche
| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| `print()` | Gibt Text aus | `print("Hallo")` |
...

## Kurzbeispiele
[Code-Zelle mit theme-spezifischen Beispielen]

## Wiederholung – Begriffe aus früheren Wochen
### Aus Woche N
| Begriff | Bedeutung | Beispiel |
...
```

**Themen-spezifische Beispiele:**
- Abenteuer: `held`, `waffe`, `level`, Namen wie "Aria", "Borin"
- Pferde: `pferd`, `reiter`, `stall`, Namen wie "Bobby", "Blitz"
- SciFi: `schiff`, `crew`, `kommandant`, Namen wie "Kirk", "Enterprise"

---

## 📚 _1_lektion – Format

```markdown
# [Emoji] Woche X – Lektion: [Titel]
[Nav-Tabelle]

## [Emoji] Was ist ein/eine [Konzept]?
[1-2 Sätze, einfache Sprache, Alltagsvergleich]

## Zauberformel 1: [Konzeptname]   ← Abenteuer
## Lektion 1: [Konzeptname]        ← Pferde
## Systemprotokoll 1: [Konzeptname]← SciFi

**Was es ist:** [Einfache Erklärung]
[Code-Beispiele]
```

**Sprachregeln:**
- Kein `**Warum nützlich:**`-Bulletblock
- Keine langen metaphorischen Untertitel (`Die Runen des X`)
- Einfache Sprache: `schreiben` statt `implementieren`, `erstellen` statt `instanziieren`
- Fachbegriffe beim ersten Auftreten erklären: `Konstruktor *(= Methode die beim Erstellen automatisch startet)*`

---

## 🐛 _2_debug – Format

```markdown
# 🐛 Debug-Quest – [Theme] Woche X

## 🐛 Debug-Quest: Finde die Fehler!
[Kurze Story-Einleitung]

### 🐛 Bug #1
**Was passiert:** [Erklärung warum der Fehler auftritt – nicht nur was]

[Code-Zelle mit Fehler]

### 🐛 Bug #2
**Was passiert:** ...
[Code-Zelle]

### 🐛 Bug #3
**Was passiert:** ...
[Code-Zelle]
```

**Typische Bug-Typen pro Woche:**
- W1: fehlende Anführungszeichen, str()-Fehler, Tippfehler in Variablen
- W2: f-String Syntax, falscher Typ bei Methoden
- W3: `=` statt `==`, fehlendes `:` bei elif, IndentationError
- W4: falsche Einrückung in Schleifen, range()-Fehler
- W5: fehlende Parameter, falsches return
- W6–W12: passend zum Wochenthema

---

## ⭐ _3_missionen – Format

```markdown
### ⭐⭐☆☆☆ Mission 1: [Titel]

**Belohnung:** 300 [Währung] + [Item]

[1 Satz Story]

**Schritt 1 – [Titel]:**
[Was zu tun ist, 1-2 Sätze]

**Schritt 2 – [Titel]:**
[Was zu tun ist]

**Bonus:** [Optionale Erweiterung]
```

**Regeln:**
- Keine vorgeschriebenen Funktionsnamen (`erstelle_held(name, level)`)
- Kein Starter-Code, keine "Erwartete Ausgabe"
- Mission 3 endet mit: `> 💡 **Tipp:** Du entscheidest selbst, wie du das umsetzt – es gibt keinen einzig richtigen Weg!`
- Schwierigkeit steigt: Mission 1 = ⭐⭐, Mission 2 = ⭐⭐⭐, Mission 3 = ⭐⭐⭐⭐

---

## 🤔 _4_reflexion – Format

```markdown
# 🤔 Reflexion & Zusammenfassung – [Theme] Woche X

## Weisheiten der [Theme-Mentor] (Reflexion)
[Kurze Einleitung]

**1. [Frage?]**

✏️ *Schreibe deine Antwort hier...*

**2. [Frage?]**

✏️ *Schreibe deine Antwort hier...*

**3. [Frage?]**

✏️ *Schreibe deine Antwort hier...*

## 🏆 Zusammenfassung: [Titel]
[Was gelernt wurde + reale Anwendungen + Ausblick auf nächste Woche]
```

**Wichtig:** Frage IMMER vor dem Antwort-Platzhalter (nicht dahinter).

**Theme-Mentoren:** alte Magier (Abenteuer) / erfahrene Reitlehrerin (Pferde) / Missionsleiterin (SciFi)

---

## 🔧 _5_loesungen – Format

```markdown
# 🔧 Lösungen – [Theme] Woche X

## 🐛 Debug-Quest Lösungen

[Code-Zelle mit Lösung Bug #1]
[Code-Zelle mit Lösung Bug #2]
[Code-Zelle mit Lösung Bug #3]

## ⭐ Missions-Lösungsvorschläge

### ⭐⭐☆☆☆ Mission 1: [Titel]
[Code-Zelle: # ✏️ Lösungsvorschlag Mission 1]

### Mission 2 ...
### Mission 3 ...
```

---

## 🐉 _6_boss – Format

```markdown
# 🐉 Boss-Quests – [Theme] Woche X

## 🐉 Boss-Kampf: Hausaufgaben-Quests
[Einleitung + Belohnungshinweis]

### ⭐⭐⭐⭐☆ Boss-Quest 1: [Titel]

**Belohnung:** 500 [Währung] + [Item]

[2-3 Sätze Story-Einleitung mit klarem Ziel]

**Schritt 1 – [Titel]:**
[Was zu tun ist, kein Starter-Code, keine Funktionsnamen]

**Schritt 2 – [Titel]:**
[Was zu tun ist]

**Schritt 3 – [Titel]:**
[Was zu tun ist]

**Bonus:** [Optionale Erweiterung]
```

**Regeln:**
- Story kommt ZUERST, dann Schritte
- Max 3-4 Schritte (nicht 5-6)
- Keine Klassen vor Woche 10
- Kein `os`, `shutil`, `zipfile` (nicht im Lehrplan)
- Offen formulieren: Schüler entscheidet selbst wie, nicht was

---

## 🎨 Themen-Konsistenz

| Element | Abenteuer | Pferde | SciFi |
|---------|-----------|--------|-------|
| Abschnitt-Name | Zauberformel | Lektion | Systemprotokoll |
| Währung | XP | Huf-Punkte | Cyber Credits |
| Lexikon | Zauberspruch-Lexikon | Reiterhof-Lexikon | Tech-Lexikon |
| Mentor | alter Magier | erfahrene Reitlehrerin | Missionsleiterin |
| Code-Variablen | held, waffe, gold | pferd, stall, futter | schiff, crew, energie |
| Beispiel-Namen | Aria, Borin, Gandalf | Bobby, Blitz, Moritz | Kirk, Enterprise, Nebula-7 |
| Boss-Emoji | 🐉 | 🐴 | 🚀 |

---

## ❌ Häufige Fehler vermeiden

| Fehler | Richtig |
|--------|---------|
| `implementieren` | `schreiben` / `einbauen` |
| `instanziieren` | `erstellen` |
| `iterieren` | `durchgehen` |
| `Namenskonvention` | `Schreibregel` |
| `Rückgabewert` | `Ergebnis` |
| `Anatomie einer Liste` | `Aufbau einer Liste` |
| `Buffer` | `Zwischenspeicher` |
| `\n` in `print()` | separates `print()` |
| Klassen vor Woche 10 | ❌ nicht verwenden |
| os/shutil | ❌ nicht im Kurs |

---

## ✅ Qualitäts-Checkliste

### Vor der Erstellung
- [ ] Thema in `lehrplan.md` nachgeschlagen?
- [ ] Welche Konzepte sind NEU, welche sind Vertiefung?
- [ ] Woche-spezifische Einschränkungen beachtet?

### Für jedes Notebook
- [ ] Korrekte Dateinamen: `wocheX_[theme]_[N]_[typ].ipynb`
- [ ] Glossar: Tabelle mit Begriff/Bedeutung/Beispiel + Wiederholung?
- [ ] Lektion: kein "Warum nützlich"-Block, einfache Sprache?
- [ ] Debug: WHY-Markdown vor jeder Bug-Zelle?
- [ ] Missionen: Schritt-Format, kein Starter-Code, kein Funktionsname?
- [ ] Reflexion: Frage VOR Antwort-Platzhalter?
- [ ] Boss: Story zuerst, max 3-4 Schritte, offen formuliert?
- [ ] Themen-Konsistenz: richtige Variablen-Namen je Kurs?
- [ ] Code-Beispiele lauffähig (kein `\n` in `print()`)?

---

## 🔗 Referenzen

- **Lehrplan:** `content/python-12-wochen-grundkurs/lehrplan.md`
- **Gesamtglossar:** `content/python-12-wochen-grundkurs/gesamtglossar.ipynb`
- **Beispiel-Woche:** `content/python-12-wochen-grundkurs/woche-3/`
