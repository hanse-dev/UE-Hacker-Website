---
trigger: manual
---

# 🔄 Python-Notebook Workflow: Komplettanleitung

Dieser Guide beschreibt den vollständigen Prozess zur Erstellung einer neuen Woche mit 3 thematischen Jupyter-Notebooks.

## 📋 Übersicht der beteiligten Dateien

| Datei | Zweck | Wann verwenden |
|-------|-------|----------------|
| **@Regeln/12-wochen-kurs-themen-uebersicht.md** | Kurrikulum & Themen | **VORBEGINN** - Thema finden |
| **@Regeln/ordner-und-beschreibung.md** | Ordner & Markdown-Beschreibung | Schritt 1-2 |
| **@Regeln/notebook-erstellung.md** | Notebook-Erstellung | Schritt 3 |
| **@Regeln/vorlagen/vorlage-abenteuer.md** | Fantasy-Template | Schritt 3 |
| **@Regeln/vorlagen/vorlage-pferde.md** | Pferde-Template | Schritt 3 |
| **@Regeln/vorlagen/vorlage-scifi.md** | Sci-Fi-Template | Schritt 3 |

---

## 🎯 Vorbereitung: Thema finden

**BEVOR du starte, prüfe das Kurrikulum:**
1. Öffne @Regeln/12-wochen-kurs-themen-uebersicht.md
2. Finde Woche [X] in der Übersicht
3. Übernehme das exakte Thema und die Kern-Lernpunkte

**Beispiel Woche 7:**
- Thema: "Module und Bibliotheken (math, random)"
- Kern-Lernpunkte: Module importieren, math-Modul, random-Modul

---

## 🎯 Schritt-für-Schritt Anleitung

### Schritt 1: Ordner vorbereiten
```bash
# Prüfen, ob Ordner existiert:
content/python-12-wochen-grundkurs/woche-[X]/

# Falls nicht, erstellen mit Bindestrich!
mkdir content/python-12-wochen-grundkurs/woche-[X]/
```

**Referenz:** Siehe @Regeln/ordner-und-beschreibung.md → Abschnitt "1. Ordner-Struktur prüfen und erstellen"

### Schritt 2: Markdown-Beschreibung erstellen
```bash
# Datei OHNE Bindestrich erstellen:
touch content/python-12-wochen-grundkurs/woche-[X]/woche[X].md
```

**Template:**
```markdown
---
title: '📚 Woche [X] – [Thema]: [Kurzer Untertitel]!'
---

# 🎯 Die Herausforderung: [Kurze Beschreibung]

[2-3 Sätze über das Problem]

[1 Satz über die Python-Lösung]

## 🎮 Themenwelten zur Auswahl

- **🗺️ Abenteuer-Welt:** [Thematische Beschreibung]
- **🐴 Pferdewirtschaft:** [Thematische Beschreibung]
- **🚀 Sci-Fi-Welt:** [Thematische Beschreibung]

# 🎯 Lernziele
- [Lernziel 1 mit Infinitiv]
- [Lernziel 2 mit Infinitiv]
- [Lernziel 3 mit Infinitiv]
- [Lernziel 4 mit Infinitiv]
- [Lernziel 5 mit Infinitiv]
- [Lernziel 6 mit Infinitiv]
```

**Referenz:** Siehe @Regeln/ordner-und-beschreibung.md → Abschnitt "Format für woche[X].md"

### Schritt 3: Drei Jupyter-Notebooks erstellen

#### 3.1 Struktur verstehen
Jedes Notebook hat **11 Abschnitte**:
1. Titel-Zelle (mit XP & Boss)
2. Einführung (mit 3 Lernzielen)
3. 3 Grundlagen-Konzepte (je Theorie + 3 Code-Beispiele)
4. Debug-Quest (3 fehlerhafte Code-Beispiele)
5. Haupt-Missionen (3 Missionen ⭐⭐ bis ⭐⭐⭐⭐)
6. Reflexion (3 Fragen)
7. Lexikon (10-12 Begriffe)
8. Lernziele-Check (6 Punkte)
9. Zusammenfassung (5 Anwendungen)
10. Boss-Kampf (3 Quests ⭐⭐⭐⭐ bis ⭐⭐⭐⭐⭐)
11. Debug-Lösungen (am Ende)

#### 3.2 Themen-Platzhalter vorbereiten
| Platzhalter | Abenteuer | Pferde | Sci-Fi |
|-------------|-----------|--------|--------|
| [Währung] | XP | Huf-Punkte | Cyber Credits |
| [Boss/Herausforderung] | Boss | Herausforderung | Herausforderung |
| [Theme-Name] | Zauberformel | Lektion | Systemprotokoll |
| [Theme-Lexikon] | Zauberspruch-Lexikon | Reiterhof-Lexikon | Tech-Lexikon |
| [Mentor] | alte Magier | erfahrene Reitlehrerin | Missionsleiterin |
| [🐉/🐴/🚀] | 🐉 | 🐴 | 🚀 |

#### 3.3 Notebooks erstellen
```bash
# Drei Dateien erstellen (alle OHNE Bindestrich):
touch content/python-12-wochen-grundkurs/woche-[X]/woche[X]_abenteuer.ipynb
touch content/python-12-wochen-grundkurs/woche-[X]/woche[X]_pferde.ipynb
touch content/python-12-wochen-grundkurs/woche-[X]/woche[X]_scifi.ipynb
```

**Für jedes Notebook:**
1. Template kopieren: @Regeln/vorlagen/vorlage-[theme].md
2. Platzhalter ersetzen:
   - `[X]` → Wochennummer
   - `[THEMA]` → Python-Thema der Woche
   - `[Boss-Namen]` → Thematisch passend
   - Alle Theme-Platzhalter (siehe Tabelle oben)

**Referenzen:**
- Hauptstruktur: @Regeln/notebook-erstellung.md
- Templates: @Regeln/vorlagen/vorlage-abenteuer.md, @Regeln/vorlagen/vorlage-pferde.md, @Regeln/vorlagen/vorlage-scifi.md

---

## ✅ Qualitäts-Checkliste

### Vor der Erstellung:
- [ ] Wochennummer klar?
- [ ] Python-Thema definiert?
- [ ] Boss-Namen für alle 3 Themes überlegt?

### Nach Schritt 1 (Ordner):
- [ ] Ordner `woche-[X]/` existiert mit Bindestrich

### Nach Schritt 2 (Beschreibung):
- [ ] Datei `woche[X].md` erstellt ohne Bindestrich
- [ ] Thema aus @Regeln/12-wochen-kurs-themen-uebersicht.md übernommen
- [ ] Frontmatter mit title vorhanden
- [ ] Alle 3 Themenwelten beschrieben
- [ ] 5-6 Lernziele mit Infinitiv

### Nach Schritt 3 (Notebooks):
- [ ] Alle 3 .ipynb Dateien erstellt
- [ ] Jedes Notebook hat 11 Abschnitte
- [ ] Platzhalter korrekt ersetzt
- [ ] Kern-Lernpunkte aus @Regeln/12-wochen-kurs-themen-uebersicht.md eingebaut
- [ ] Thematische Konsistenz gewahrt
- [ ] Keine `\n` in Print-Statements
- [ ] F-Strings nur ab Woche 2+
- [ ] Debug-Lösungen am Ende

---

## 🔗 Nützliche Verknüpfungen

### Beispiele & Referenzen:
- **Beispiel-Woche:** `content/python-12-wochen-grundkurs/woche-6/`
- **Stil-Beispiele:** Siehe `woche6.md` für Markdown-Stil

### Technische Details:
- **JSON-Format:** Siehe @Regeln/notebook-erstellung.md → "Technische Anforderungen"
- **Code-Stil:** Keine `\n`, separates `print()` für neue Zeilen

### Didaktische Prinzipien:
- Maximal 3 Konzepte pro Woche
- Code-First: Direkt mit Beispielen starten
- Gamification: XP, Schwierigkeitssterne, Boss-Kämpfe

---

## 🚀 Quick-Start Template

Für eine neue Woche `[X]` mit Thema `[THEMA]`:

**1. Thema finden:**
```bash
# Siehe: @Regeln/12-wochen-kurs-themen-uebersicht.md
# Beispiel Woche 7: "Module und Bibliotheken (math, random)"
```

```bash
# 1. Ordner erstellen
mkdir -p content/python-12-wochen-grundkurs/woche-[X]

# 2. Beschreibung erstellen
cat > content/python-12-wochen-grundkurs/woche-[X]/woche[X].md << 'EOF'
---
title: '📚 Woche [X] – [THEMA]: [UNTERTITEL]!'
---

# 🎯 Die Herausforderung: [KURZBESCHREIBUNG]

[2-3 Sätze Problem]

[1 Satz Lösung]

## 🎮 Themenwelten zur Auswahl

- **🗺️ Abenteuer-Welt:** [BESCHREIBUNG]
- **🐴 Pferdewirtschaft:** [BESCHREIBUNG]
- **🚀 Sci-Fi-Welt:** [BESCHREIBUNG]

# 🎯 Lernziele
- [LERNZIEL 1]
- [LERNZIEL 2]
- [LERNZIEL 3]
- [LERNZIEL 4]
- [LERNZIEL 5]
- [LERNZIEL 6]
EOF

# 3. Notebooks erstellen (Templates kopieren und anpassen)
# Siehe @Regeln/vorlagen/ für die vollständigen Templates
```

---

## 💡 Tipps & Tricks

1. **Konsistenz ist alles:** Immer gleiche Struktur, gleiche Stil-Regeln
2. **Themen-Treue:** Jede Welt sollte ihre Metaphern durchhalten
3. **Progression:** Missionen von leicht zu schwer
4. **Qualität vor Quantität:** Lieber 3 gute Konzepte als 5 schlechte
5. **Testen:** Code-Beispiele müssen laufen!

Bei Problemen: Immer die Referenz-Dateien konsultieren und den Workflow Schritt für Schritt durchgehen!
