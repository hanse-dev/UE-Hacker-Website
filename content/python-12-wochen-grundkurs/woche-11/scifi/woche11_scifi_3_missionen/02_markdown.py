"""### ⭐⭐☆☆☆ Mission 1: Die Roboter-Hierarchie

Die Robotik-Abteilung braucht eine saubere Hierarchie für alle Robotertypen!

**Schritt 1 – Basisklasse Roboter anlegen:**
Erstelle `class Roboter:` mit `__init__(self, id, name, energiestatus)`; weise die Attribute zu und füge eine Methode `aktivieren()` hinzu, die eine Statusmeldung ausgibt

**Schritt 2 – Kind-Klassen erstellen:**
Erstelle `class Android(Roboter):`, `class Drohne(Roboter):`, `class Cyborg(Roboter):` und nutze in jedem Konstruktor *(= spezielle Methode, die beim Erstellen eines Objekts automatisch startet)* `super().__init__(id, name, energiestatus)` und füge ein spezielles Attribut hinzu

**Schritt 3 – Objekt von jeder Klasse erstellen:**
Erstelle je ein Objekt Android, Drohne und Cyborg und rufe `aktivieren()` und die spezielle Methode für jedes Objekt auf

**Bonus:** Füge eine vierte Klasse hinzu, die von einer Kind-Klasse erbt (z.B. Kampfandroid von Android)."""
