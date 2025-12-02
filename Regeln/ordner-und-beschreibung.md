# 📁 Ordner-Struktur und Markdown-Beschreibung

## 🎯 Vorbereitung vor der Notebook-Erstellung

**Bevor du die 3 Jupyter-Notebooks erstellst, führe diese Schritte aus:**

### 1. Ordner-Struktur prüfen und erstellen

- **Prüfe:** Existiert der Ordner `content/python-12-wochen-grundkurs/woche-[X]/`?
- **Falls nicht:** Erstelle den Ordner `woche-[X]` (mit Bindestrich!)
- **Alle Dateien** werden in diesem Ordner gespeichert:
  - `woche[X].md` (Beschreibung, ohne Bindestrich!)
  - `woche[X]_abenteuer.ipynb`
  - `woche[X]_pferde.ipynb`
  - `woche[X]_scifi.ipynb`

**Beispiel für Woche 7:**
```
content/python-12-wochen-grundkurs/
└── woche-7/              ← Ordner mit Bindestrich
    ├── woche7.md         ← Beschreibung ohne Bindestrich
    ├── woche7_abenteuer.ipynb
    ├── woche7_pferde.ipynb
    └── woche7_scifi.ipynb
```

### 2. Markdown-Beschreibung erstellen

**Erstelle zuerst die Datei `woche[X].md`** (ohne Bindestrich im Dateinamen!)

Diese Datei enthält eine kurze Übersicht über die Woche und dient als Einstiegsseite.

---

## 📄 Format für woche[X].md

**Orientiere dich am Format von `woche6.md` – halte es kurz und einfach!**

### Template:

```markdown
---
title: '📚 Woche [X] – [Thema]: [Kurzer Untertitel]!'
---

# 🎯 Die Herausforderung: [Kurze Beschreibung]

[2-3 Sätze über die Herausforderung und warum das Thema wichtig ist. 
Beschreibe das Problem, das gelöst werden soll.]

[1 Satz über die Lösung in Python. Was ist das Konzept/die Struktur?]

## 🎮 Themenwelten zur Auswahl

Wähle deine bevorzugte Lernumgebung:
- **🗺️ Abenteuer-Welt:** [Kurze thematische Beschreibung]
- **🐴 Pferdewirtschaft:** [Kurze thematische Beschreibung]
- **🚀 Sci-Fi-Welt:** [Kurze thematische Beschreibung]

Alle Welten vermitteln dieselben Python-Kenntnisse – nur mit unterschiedlichem Flair!

# 🎯 Lernziele
- [Lernziel 1 mit Infinitiv, z.B. "Listen zu erstellen"]
- [Lernziel 2 mit Infinitiv]
- [Lernziel 3 mit Infinitiv]
- [Lernziel 4 mit Infinitiv]
- [Lernziel 5 mit Infinitiv]
- [Lernziel 6 mit Infinitiv]
```

---

## ✅ Stil-Richtlinien für woche[X].md

### Länge und Struktur
- **Kurz und prägnant:** Ca. 20-30 Zeilen insgesamt
- **Keine ausführlichen Erklärungen:** Nur Übersicht und Orientierung
- **Gleiche Struktur wie woche6.md:** Konsistenz ist wichtig

### Inhalt
- **Titel:** Emoji + Wochennummer + Thema + Untertitel
- **Herausforderung:** 2-3 Sätze über das Problem
- **Lösung:** 1 Satz über das Python-Konzept
- **Themenwelten:** Kurze Beschreibung jeder Welt (1 Zeile)
- **Lernziele:** 5-6 Punkte mit Infinitiv-Form

### Sprache
- **Einfach und direkt:** Keine komplexen Sätze
- **Motivierend:** Zeige, warum das Thema wichtig ist
- **Konsistent:** Verwende die gleichen Formulierungen wie in woche6.md

---

## 📋 Beispiel: woche7.md

```markdown
---
title: '📚 Woche 7 – Module und Bibliotheken: Die Werkzeugkiste nutzen!'
---

# 🎯 Die Herausforderung: Nutze fertige Werkzeuge

Du stehst vor komplexen Aufgaben: Präzise mathematische Berechnungen, Zufallsgenerierung für Spiele, oder physikalische Simulationen. Müsstest du all diese Funktionen selbst programmieren, würde das Wochen dauern!

Zum Glück gibt es **Module und Bibliotheken** – vorgefertigte Sammlungen von Funktionen, die andere Entwickler bereits geschrieben haben. In Python nennen wir diese Werkzeugkisten **Module**.

## 🎮 Themenwelten zur Auswahl

Wähle deine bevorzugte Lernumgebung:
- **🗺️ Abenteuer-Welt:** Magische Archive und Zauberspruch-Bibliotheken
- **🐴 Pferdewirtschaft:** Werkzeugkisten für Reiterhof-Berechnungen
- **🚀 Sci-Fi-Welt:** Galaktische Datenbanken und Raumfahrt-Algorithmen

Alle Welten vermitteln dieselben Python-Kenntnisse – nur mit unterschiedlichem Flair!

# 🎯 Lernziele
- Module mit `import` zu laden
- Mathematische Berechnungen mit `math` durchzuführen
- Zufallszahlen mit `random` zu erzeugen
- Verschiedene Import-Methoden zu nutzen
- Module zu kombinieren für komplexe Aufgaben
- Trigonometrische Funktionen anzuwenden
```

---

## 🔄 Workflow-Übersicht

**Reihenfolge beim Erstellen einer neuen Woche:**

1. ✅ **Ordner erstellen:** `woche-[X]/` (falls nicht vorhanden)
2. ✅ **Beschreibung erstellen:** `woche[X].md` im einfachen Stil
3. ✅ **Notebooks erstellen:** Die 3 thematischen Jupyter-Notebooks
4. ✅ **Qualitätsprüfung:** Alle Dateien vorhanden und korrekt benannt

---

## 📌 Wichtige Hinweise

### Namenskonvention
- **Ordner:** `woche-7` (mit Bindestrich)
- **Beschreibung:** `woche7.md` (ohne Bindestrich)
- **Notebooks:** `woche7_abenteuer.ipynb` (ohne Bindestrich, mit Unterstrich)

### Qualitätskriterien für woche[X].md
- [ ] Frontmatter mit `title` vorhanden
- [ ] Überschrift "Die Herausforderung" vorhanden
- [ ] 2-3 Sätze Problembeschreibung
- [ ] 1 Satz Lösungsbeschreibung
- [ ] Alle 3 Themenwelten beschrieben
- [ ] 5-6 Lernziele mit Infinitiv-Form
- [ ] Gesamtlänge ca. 20-30 Zeilen
- [ ] Gleicher Stil wie woche6.md

### Referenz-Datei
- **Orientiere dich immer an:** `content/python-12-wochen-grundkurs/woche-6/woche6.md`
- Diese Datei zeigt den gewünschten Stil und die Struktur
