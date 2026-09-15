"""### ⭐⭐⭐☆☆ Mission 2: Das polymorphe Arsenal

Die Waffenschmiede braucht ein System für verschiedene Waffentypen!

**Schritt 1 – Drei Waffen-Klassen anlegen:**
Erstelle `class Schwert:`, `class Bogen:`, `class Zauberstab:` jeweils mit `__init__(self, name)` und einer Methode `anwenden(self)` und jede `anwenden()` gibt eine andere Aktion aus (z.B. \"Schwert trifft!\", \"Pfeil fliegt!\", \"Zauber wirkt!\")

**Schritt 2 – Polymorphe Funktion:**
Erstelle eine Funktion `nutze_waffe(waffe)`, die `waffe.anwenden()` aufruft und die Funktion soll mit allen drei Waffentypen funktionieren

**Schritt 3 – Alle Waffen testen:**
Erstelle je ein Objekt Schwert, Bogen und Zauberstab und rufe `nutze_waffe()` für jede Waffe auf

**Bonus:** Erstelle eine Waffenfabrik-Funktion, die je nach Typ die passende Waffe erzeugt."""
