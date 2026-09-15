"""### ⭐⭐⭐☆☆ Mission 2: Das polymorphe Waffensystem

Die Waffenabteilung braucht ein System für verschiedene Waffentypen!

**Schritt 1 – Drei Waffen-Klassen anlegen:**
Erstelle `class Laser:`, `class Plasma:`, `class Ionen:` jeweils mit `__init__(self, name)` und einer Methode `abfeuern(self)` und jede `abfeuern()` gibt eine andere Meldung aus (z.B. \"Pew! Laser feuert!\", \"Zisch! Plasma entladen!\", \"Bzz! Ionenstrahl!\")

**Schritt 2 – Polymorphe Funktion:**
Erstelle eine Funktion `waffe_testen(waffe)`, die `waffe.abfeuern()` aufruft und die Funktion soll mit allen drei Waffentypen funktionieren

**Schritt 3 – Alle Waffen testen:**
Erstelle je ein Objekt Laser, Plasma und Ionen und rufe `waffe_testen()` für jede Waffe auf

**Bonus:** Erstelle eine Waffenfabrik-Funktion, die je nach Typ die passende Waffe erzeugt."""
