"""### ⭐⭐⭐⭐☆ Boss-Quest 1: Der Protokoll-Generator

Erstelle ein System, das automatisch Systemprotokolle erzeugt, bewertet und in einer kleinen \"Datenbank\" verwaltet.

**Schritt 1 – Protokoll-Namen erstellen:**
Schreibe eine Funktion `generiere_protokoll_name(system_typ, sicherheits_level)`, die aus Typ und Level einen Namen baut (z.B. `\"SEC-ALARM-L3\"`) und gib den Namen als String zurück

**Schritt 2 – Effizienz berechnen:**
Erstelle eine Funktion `berechne_effizienz(komplexitaet, system_typ)`, die einen Wert zwischen 0 und 100 zurückgibt und nutze unterschiedliche Faktoren je nach `system_typ` (z.B. \"Alarm\", \"Scan\", \"Log\")

**Schritt 3 – Protokoll-Daten erstellen:**
Schreibe eine Funktion `erstelle_protokoll(system_typ, sicherheits_level, komplexitaet)`, die ein Dictionary mit Name, Typ, Level und Effizienz zurückgibt und nutze dafür deine beiden vorherigen Funktionen

**Schritt 4 – Protokolle speichern und finden:**
Erstelle eine Liste `protokolle` und schreibe eine Funktion `speichere_protokoll(liste, protokoll)`, die das Protokoll hinzufügt

**Schritt 5 – Generator-System aufbauen:**
Erzeuge im Hauptteil mindestens 5 verschiedene Protokolle und speichere sie in der Liste und gib eine kleine Statistik aus (Anzahl, Durchschnittseffizienz)

**Bonus:** Füge eine Funktion hinzu, die Protokolle nach Effizienz sortiert ausgibt."""
