"""### ⭐⭐☆☆☆ Mission 1: Die Charakter-Hierarchie

Die Gilde braucht eine saubere Hierarchie für alle Charakterklassen!

**Schritt 1 – Basisklasse Charakter anlegen:**
Erstelle `class Charakter:` mit `__init__(self, name, level, hp)`; weise die Attribute zu und füge eine Methode `vorstellen()` hinzu, die eine Meldung ausgibt

**Schritt 2 – Kind-Klassen erstellen:**
Erstelle `class Krieger(Charakter):`, `class Magier(Charakter):`, `class Schurke(Charakter):` und nutze in jedem Konstruktor *(= spezielle Methode, die beim Erstellen eines Objekts automatisch startet)* `super().__init__(name, level, hp)` und füge ein spezielles Attribut hinzu

**Schritt 3 – Objekt von jeder Klasse erstellen:**
Erstelle je einen Krieger, Magier und Schurke und rufe `vorstellen()` und die spezielle Methode für jedes Objekt auf

**Bonus:** Füge eine vierte Klasse hinzu, die von einer Kind-Klasse erbt (z.B. Paladin von Krieger)."""
