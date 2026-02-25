# 📋 Plan: Punkte-Sammel-System für den Python 12-Wochen-Kurs

**Stand:** Februar 2025  
**Ziel:** XP / Huf-Punkte / Cyber Credits nachvollziehbar sammeln und speichern

---

## 1. Ausgangslage

- Belohnungen stehen bisher nur im Markdown (z.B. "300 XP + Magischer Schmiedehammer")
- Einige Code-Zellen printen Erfolgsmeldungen, aber es gibt kein Sammel-System
- Notebooks laufen im Browser (Pyodide) oder werden lokal heruntergeladen (Jupyter, VS Code)

---

## 2. Empfohlener Ansatz: Zwei Wege, ein Datenformat

### 2.1 Website (Browser)

- **Speicherort:** `localStorage`
- **Funktionen:** "Mission abgeschlossen" klicken → Punkte addieren → Items sammeln
- **Anzeige:** Fortschritts-Banner mit Gesamt-Punkten und gesammelten Items

### 2.2 Lokal (heruntergeladene Notebooks)

- **Problem:** Kein Vue, kein localStorage, kein Zugriff auf die Website
- **Lösung:** Lokale JSON-Datei + Import auf der Website

---

## 3. Umgang mit lokal heruntergeladenen und ausführbaren Dateien

### 3.1 Szenarien

| Szenario | Wo läuft es? | Tracking möglich? |
|----------|--------------|-------------------|
| Website, interaktives Notebook | Browser (Pyodide) | ✅ Ja, via localStorage |
| Heruntergeladen, Jupyter Lab/Notebook | Lokal auf dem Rechner | ❌ Direkt nein |
| Heruntergeladen, VS Code | Lokal auf dem Rechner | ❌ Direkt nein |

### 3.2 Strategie: Lokale JSON + Import auf der Website

**Idee:** Nutzer, die lokal arbeiten, können Fortschritt in eine lokale Datei schreiben und später auf der Website importieren.

**Ablauf:**

1. Lokal: Nutzer führt ein mitgeliefertes Python-Skript aus oder nutzt eine bereitgestellte Zelle.
2. Es entsteht/aktualisiert sich eine Datei `mein-fortschritt.json` im gleichen Verzeichnis.
3. Auf der Website gibt es einen Button "Fortschritt importieren".
4. Nutzer wählt die lokale `mein-fortschritt.json` → Daten werden mit bestehendem Fortschritt (localStorage) zusammengeführt.

**Vorteile:**

- Kein Backend nötig
- Lokale Nutzer können den gleichen Stand erreichen wie Website-Nutzer
- Freiwillig: Wer lokal kein Tracking will, nutzt es einfach nicht

### 3.3 Technische Umsetzung für lokale Nutzer

**Option A: Kleines CLI-Skript (empfohlen)**

- Datei: `scripts/fortschritt.py` oder als Download auf der Kursseite
- Nutzung: `python fortschritt.py add w10-abenteuer-m1` 
- Schreibt in `mein-fortschritt.json` im aktuellen Verzeichnis
- Mission-IDs müssen dokumentiert sein (siehe Rewards-Manifest)

**Option B: Zelle am Ende jeder Lösungs-Sektion**

- Jede Mission hat eine Code-Zelle mit:
  ```python
  # Fortschritt speichern (optional, für lokale Nutzer)
  # Führe diese Zelle aus, dann findest du fortschritt.json im gleichen Ordner
  import json
  # ... schreibt in fortschritt.json
  ```
- **Nachteil:** 36+ Notebooks müssten angepasst werden

**Option C: Reines Selbst-Tracking auf der Website**

- Lokale Nutzer: Kein Punkte-Tracking
- Klar kommunizieren: "Punkte sammeln nur auf der Website"
- **Vorteil:** Minimaler Implementierungsaufwand

### 3.4 Empfehlung für Phase 1

- **Phase 1:** Nur Website-Tracking (localStorage), keine lokale Unterstützung
- **Phase 2:** CLI-Skript + Import-Funktion auf der Website
- **Phase 3 (optional):** Standard-Zelle in die Notebooks integrieren

---

## 4. Datenstruktur (einheitlich für Website und lokale JSON)

```json
{
  "version": 1,
  "courseId": "python-12-wochen-grundkurs",
  "variants": {
    "abenteuer": {
      "totalPoints": 0,
      "claimedMissions": [],
      "items": []
    },
    "pferde": {
      "totalPoints": 0,
      "claimedMissions": [],
      "items": []
    },
    "scifi": {
      "totalPoints": 0,
      "claimedMissions": [],
      "items": []
    }
  }
}
```

**Mission-IDs (Beispiel):** `w1-m1`, `w1-m2`, `w1-m3`, `w1-boss1`, `w1-boss2`, `w1-boss3`  
Format: `w[Woche]-[m|boss][Nummer]`

---

## 5. Rewards-Manifest (zentrale Konfiguration)

**Datei:** `public/rewards-manifest.json` oder `src/data/rewards-manifest.json`

**Inhalt (Ausschnitt):**

```json
{
  "python-12-wochen-grundkurs": {
    "abenteuer": {
      "w1": {
        "missions": [
          { "id": "w1-m1", "points": 300, "item": "Magischer Grimoire" },
          { "id": "w1-m2", "points": 400, "item": "Schatzkarte" },
          { "id": "w1-m3", "points": 500, "item": "Heldenschwert" }
        ],
        "bossQuests": [
          { "id": "w1-boss1", "points": 500, "item": "Kristallkugel" },
          { "id": "w1-boss2", "points": 600, "item": "Drachenamulett" },
          { "id": "w1-boss3", "points": 400, "item": "Portalschlüssel" }
        ]
      }
    },
    "pferde": { },
    "scifi": { }
  }
}
```

- Alle 36 Notebooks (12 Wochen × 3 Varianten) müssen im Manifest erfasst werden
- Bei Änderungen: nur Manifest anpassen, keine Notebooks nötig

---

## 6. Implementierungs-Schritte (Website)

1. **Rewards-Manifest erstellen** – alle Missionen und Belohnungen eintragen
2. **JupyterNotebook.vue erweitern**
   - Mission-Bereiche im Markdown erkennen (z.B. via Daten-Attribute oder Zell-Reihenfolge)
   - "Punkte einlösen"-Button neben Mission-Titeln
   - `localStorage` lesen/schreiben mit obiger Datenstruktur
3. **Fortschritts-Widget** – z.B. in CourseDetail.vue: Gesamt-Punkte und gesammelte Items
4. **Import-Funktion (Phase 2)** – "Fortschritt importieren"-Button, File-Upload, Merge mit localStorage
5. **Export-Funktion (Phase 2)** – "Fortschritt exportieren" als JSON-Download

---

## 7. Offene Fragen / Entscheidungen

- [ ] Sollen Nutzer Missionen mehrfach einlösen können oder nur einmal?
- [ ] Sollen Punkte beim Wechsel der Variante (Abenteuer ↔ Pferde ↔ Sci-Fi) getrennt sein?
- [ ] Soll es eine Rangliste geben (dann Backend nötig)?
- [ ] Wo genau erscheinen die "Punkte einlösen"-Buttons? (Nur bei Mission-Überschriften im gerenderten Markdown?)

---

## 8. Zusammenfassung: Lokal vs. Website

| Aspekt | Website (Browser) | Lokal (heruntergeladen) |
|--------|-------------------|-------------------------|
| Speicherort | localStorage | Datei `mein-fortschritt.json` |
| Punkte einlösen | Klick auf Button | Ausführen von Skript/Zelle |
| Persistenz | Im Browser, bis Daten gelöscht werden | Im Dateisystem |
| Sync | — | Import der JSON auf der Website |
| Phase 1 | ✅ Voll unterstützt | ❌ Kein Tracking |
| Phase 2 | ✅ + Import/Export | ✅ Via CLI-Skript + Import |

---

## 9. Branch-Strategie für die Implementierung

**Empfehlung:** Neuen Feature-Branch anlegen, z.B.:

```
git checkout -b feature/punkte-sammel-system
```

Erst nach Fertigstellung und Review in den Haupt-Branch mergen.
