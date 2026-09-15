"""### ⭐⭐☆☆☆ Mission 1: Der Quest-Logger

Erstelle dein erstes Quest-Logging-System!

**Schritt 1 – Quest-Log schreiben:**
Öffne eine Datei (z.B. `quest_log.txt`) mit `with open(..., \"w\")`, schreibe mindestens 3 Zeilen (Quest-Status) hinein und gib eine Bestätigung aus

**Schritt 2 – Zeitstempel:**
Nutze das `datetime`-Modul und hänge mit dem Modus `\"a\"` einen neuen Eintrag mit Zeitstempel an die Datei an und gib den Beispiel-Eintrag aus

**Schritt 3 – Log-Level:**
Schreibe Einträge mit den Markierungen `[INFO]`, `[WARN]` oder `[ERROR]` und lies die Datei anschließend vollständig ein und gib den Inhalt aus

**Schritt 4 – Filter-Funktion:**
Schreibe eine Funktion `filter_level(dateiname, level)`, die nur die Zeilen mit diesem Log-Level zurückgibt, und rufe sie auf und gib das Ergebnis aus

**Beispiel-Code:** `with open(\"quest_log.txt\", \"w\") as f: f.write(...)`, `datetime.now()` für den Zeitstempel.

**Bonus:** Baue eine einfache Rotation ein (neue Datei, wenn ein Größenlimit erreicht ist)."""
