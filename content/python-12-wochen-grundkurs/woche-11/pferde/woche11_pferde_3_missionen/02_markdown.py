"""### ⭐⭐☆☆☆ Mission 1: Die Pferde-Hierarchie

Das Zuchtzentrum braucht eine saubere Hierarchie für alle Pferderassen!

**Schritt 1 – Basisklasse Pferd anlegen:**
Erstelle `class Pferd:` mit `__init__(self, name, alter, geschlecht)`; weise die Attribute zu und füge eine Methode `wiehern()` hinzu, die eine Meldung ausgibt

**Schritt 2 – Kind-Klassen erstellen:**
Erstelle `class Reitpferd(Pferd):`, `class Kaltblut(Pferd):`, `class Pony(Pferd):` und nutze in jedem Konstruktor *(= spezielle Methode, die beim Erstellen eines Objekts automatisch startet)* `super().__init__(name, alter, geschlecht)` und füge ein spezielles Attribut hinzu

**Schritt 3 – Objekt von jeder Klasse erstellen:**
Erstelle je ein Objekt Reitpferd, Kaltblut und Pony und rufe `wiehern()` und die spezielle Methode für jedes Objekt auf

**Bonus:** Füge eine vierte Klasse hinzu, die von einer Kind-Klasse erbt (z.B. Dressurpferd von Reitpferd)."""
