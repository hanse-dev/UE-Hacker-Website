"""### ⭐⭐⭐☆☆ Mission 2: Der JSON-Konverter

Erstelle ein JSON-Konvertierungssystem!

**Schritt 1 – Schiff-Daten als Dictionary:**
Erstelle ein Dictionary `schiff` mit z.B. `name`, `typ`, `crew`, `systeme` (Liste von Strings) und gib das Dictionary aus

**Schritt 2 – JSON-Export:**
Importiere `json` und speichere `schiff` mit `with open(\"schiff.json\", \"w\") as f: json.dump(schiff, f, indent=2)` in eine Datei und gib eine Bestätigung aus (z.B. „JSON gespeichert“)

**Schritt 3 – JSON-Import:**
Lade die Datei mit `with open(\"schiff.json\", \"r\") as f: daten = json.load(f)` und speichere das Ergebnis in einer Variable und prüfe, ob `daten` ein Dictionary ist und ob z.B. `daten[\"name\"]` existiert; gib den Namen aus

**Schritt 4 – Kurze Statistik:**
Erstelle aus den geladenen Daten eine einfache Statistik (z.B. Anzahl Crew, Anzahl Systeme) und gib sie aus

**Bonus:** Prüfe vor dem Laden, ob bestimmte Schlüssel vorhanden sind (einfache „Validierung“)."""
