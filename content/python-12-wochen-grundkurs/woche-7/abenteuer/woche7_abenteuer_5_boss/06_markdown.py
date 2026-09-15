"""### ⭐⭐⭐⭐☆ Boss-Quest 3: Der Zufalls-Dungeon

Kein Abenteuer gleicht dem anderen – jedes Mal ein neuer Dungeon!

**Schritt 1 – Räume erschaffen:**
Erstelle Listen mit möglichen Raum-Typen (z.B. \"Schatzkammer\", \"Falle\", \"Leerer Raum\") und Monstern. Wähle zufällig 5 Räume.

**Schritt 2 – Monster verteilen:**
Weise jedem Raum zufällig ein Monster zu (oder keines – manche Räume sind sicher).

**Schritt 3 – Dungeon ausgeben:**
Gib den Dungeon Raum für Raum aus: Nummer, Typ und Inhalt. Berechne am Ende, wie viele Leben der Held bräuchte (1 Leben pro 2 Monster, aufgerundet – z.B. mit `(monster_anzahl + 1) // 2`).

**Bonus:** Lass den Spieler mit `input()` entscheiden, ob er einen gefährlichen Raum betreten will."""
