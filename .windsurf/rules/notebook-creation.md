---
trigger: always_on
---

# 📚 Regeln für Python-Lern-Notebooks

Dieser Ordner enthält die Regeln und Anleitungen für die Erstellung der Python-Lern-Notebooks.

## 📁 Dateien

### 1. `ordner-und-beschreibung.md`
**Zweck:** Vorbereitung vor der Notebook-Erstellung
- Ordner-Struktur anlegen
- Markdown-Beschreibung (`woche[X].md`) erstellen
- Template und Stil-Richtlinien

**Wann verwenden:** ZUERST, bevor du Notebooks erstellst

### 2. `notebook-erstellung.md`
**Zweck:** Hauptregel für die Erstellung der 3 Jupyter-Notebooks
- Detaillierte Struktur für jedes Notebook
- Stil-Richtlinien für Code und Markdown
- Didaktisches Konzept
- Qualitätskriterien

**Wann verwenden:** NACH der Ordner- und Beschreibungs-Erstellung

---

## 🔄 Workflow: Neue Woche erstellen

```
1. 📁 Ordner erstellen
   └─> Siehe:  @Regeln/ordner-und-beschreibung.md
   └─> Erstelle: woche-[X]/

2. 📄 Beschreibung erstellen
   └─> Siehe: @Regeln/ordner-und-beschreibung.md
   └─> Erstelle: woche[X].md

3. 📓 Notebooks erstellen
   └─> Siehe: @Regeln/notebook-erstellung.md
   └─> Erstelle: woche[X]_abenteuer.ipynb
   └─> Erstelle: woche[X]_pferde.ipynb
   └─> Erstelle: woche[X]_scifi.ipynb
```
