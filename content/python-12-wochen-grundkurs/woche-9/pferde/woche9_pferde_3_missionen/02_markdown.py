"""### ⭐⭐☆☆☆ Mission 1: Der Pferde-Logger

Erstelle dein erstes Pferde-Logging-System!

**Schritt 1 – Log-Datei schreiben:**
Öffne eine Datei (z.B. `stall_log.txt`) mit `with open(\"stall_log.txt\", \"w\") as f`, schreibe mindestens 3 Zeilen (z.B. Pferde-Status, Futterzeiten) mit `f.write(\"...\\n\")` und gib eine Bestätigung aus

**Schritt 2 – Zeitstempel hinzufügen:**
Importiere `datetime`, füge zu jedem Eintrag Datum und Uhrzeit hinzu und schreibe mit Modus `\"a\"` weitere Einträge an, dann gib einen Beispiel-Eintrag aus

**Schritt 3 – Log-Level verwenden:**
Definiere Einträge mit den Leveln `[INFO]`, `[WARN]`, `[ERROR]` (z.B. `[INFO] Luna gefüttert`), schreibe 2–3 Einträge und lies die Datei anschließend mit `open(..., \"r\")` ein und gib den Inhalt aus

**Schritt 4 – Filter-Funktion:**
Schreibe eine Funktion `filter_level(dateiname, level)`, die nur Zeilen mit diesem Level zurückgibt, und rufe sie für ein Level auf und gib die Zeilen aus

**Bonus:** Baue eine einfache Rotation ein (neue Datei, wenn die alte zu groß wird)."""
