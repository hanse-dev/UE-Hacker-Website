"""### ⭐⭐⭐⭐☆ Mission 3: Einwort-Befehle

Bisher versteht das Spiel nur Zwei-Wort-Befehle. Tippt jemand `inventar`, gibt es die Fehlermeldung aus `try/except`. Das soll besser werden!

**Schritt 1 – Neue Befehle:**
Erweitere `fuehre_aus()`: Bei `"inventar"` soll `spieler.zeige_inventar()` laufen, bei `"hilfe"` eine Liste aller Befehle erscheinen. Beide prüfst du **vor** dem `try`-Block.

**Schritt 2 – Benutzen:**
Ergänze in der `if/elif`-Kette den Befehl `benutze`, der `spieler.benutze(ziel)` aufruft. Dafür brauchst du die Methode aus Mission 2!

**Schritt 3 – Testen:**
Spiele mit `spiele(...)` die Befehle `hilfe`, `nimm Taschenlampe`, `inventar` und `tanze wild` durch.

**Bonus:** Mache `hilfe` unabhängig von Groß- und Kleinschreibung (`.lower()`)."""