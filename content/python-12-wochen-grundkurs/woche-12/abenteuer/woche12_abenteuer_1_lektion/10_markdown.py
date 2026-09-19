"""## ⚔️ Etappe 4: Ein Gegner und ein Kampf

*Wissen aus Woche 7 + 11: Module und Methoden*

Was wäre eine Drachenhöhle ohne Drache? Wir bauen eine Klasse `Gegner` mit einer Methode `ist_besiegt()` (Woche 11). Das Modul `random` (Woche 7) würfelt den Schaden aus.

**So läuft ein Kampf ab:**
1. Der Spieler schlägt zu: 1 bis 6 Schaden – mit dem Gegenstand `Schwert` **+3 Bonus**
2. Ist der Gegner noch nicht besiegt, schlägt er zurück
3. Eine `while`-Schleife (Woche 4) wiederholt das, bis einer keine Lebenspunkte mehr hat

Räume ohne Gegner bekommen den Wert `None` (= „nichts"). Ohne Schwert wird der Kampf ziemlich knapp!"""