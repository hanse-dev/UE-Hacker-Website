"""### ⭐⭐⭐⭐☆ Boss-Quest 1: Der Daten-Generator

Baue ein System, das automatisch Datensätze erzeugt, filtert und sortiert.

**Schritt 1 – Datensatz erzeugen:**
Schreibe eine Funktion `generiere_datensatz(datentyp, komplexitaet)`, die eine Liste mit ein paar Einträgen zurückgibt (z.B. Namen oder IDs je nach Typ) und nutze `datentyp` und `komplexitaet`, um die Anzahl oder Art der Einträge zu steuern

**Schritt 2 – Statistik berechnen:**
Erstelle eine Funktion `berechne_statistik(datenliste)`, die Länge und optional Min/Max oder Durchschnitt zurückgibt und gib die Werte als Dictionary oder als ausgedruckte Zeilen zurück

**Schritt 3 – Mehrere Datensätze anlegen:**
Erstelle eine Liste `daten` und füge mit einer Schleife mindestens 10 Datensätze hinzu (z.B. mit `generiere_datensatz(\"sensor\", i)` für verschiedene i) und nutze `append()`, um jeden Datensatz zur Liste hinzuzufügen

**Schritt 4 – Daten filtern und sortieren:**
Schreibe eine Funktion `filtere_daten(datenliste, suchbegriff)`, die nur Einträge zurückgibt, die den Suchbegriff enthalten (z.B. mit `in` oder String-Vergleich) und sortiere die gefilterte oder die gesamte Liste mit `sort()` oder `sorted()` und gib das Ergebnis aus

**Schritt 5 – Generator zusammenbauen:**
Rufe im Hauptteil alle Funktionen auf: Datensätze erzeugen, Statistik ausgeben, filtern, sortieren und gib eine kurze Zusammenfassung (Anzahl, Statistik, gefilterte Anzahl) aus

**Bonus:** Füge zufällige Attribute (z.B. mit `random`) hinzu und prüfe die Daten auf Gültigkeit (Validierung)."""
