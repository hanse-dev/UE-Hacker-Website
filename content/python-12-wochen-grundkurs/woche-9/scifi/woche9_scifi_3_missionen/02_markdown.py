"""### ⭐⭐☆☆☆ Mission 1: Der Daten-Logger

Erstelle dein erstes Logging-System!

**Schritt 1 – Log-Datei schreiben:**
Öffne eine Datei (z.B. `log.txt`) mit `with open(\"log.txt\", \"w\") as f` und schreibe mindestens 3 Zeilen Text hinein (z.B. System-Status-Meldungen) und nutze `f.write(\"...\\n\")` für jede Zeile

**Schritt 2 – Zeitstempel hinzufügen:**
Importiere `datetime` und füge zu jedem Log-Eintrag Datum und Uhrzeit hinzu (z.B. `datetime.now().strftime(\"%Y-%m-%d %H:%M\")`) und schreibe die Einträge mit Zeitstempel in die Datei (Modus `\"a\"` für Anhängen)

**Schritt 3 – Log-Level verwenden:**
Definiere Einträge mit verschiedenen Leveln: INFO, WARN, ERROR (z.B. als Präfix in jeder Zeile: `[INFO] System startet`) und schreibe 2–3 Einträge mit unterschiedlichen Leveln in die Datei

**Schritt 4 – Filter-Funktion:**
Schreibe eine Funktion `filter_level(dateiname, level)`, die die Datei liest und nur Zeilen zurückgibt, die dieses Level enthalten (z.B. `\"[INFO]\"` in der Zeile) und rufe die Funktion für ein Level auf und gib die gefilterten Zeilen aus

**Bonus:** Füge eine einfache „Rotation“ hinzu: z.B. neue Datei `log_alt.txt` anlegen, wenn die aktuelle zu groß wird."""
