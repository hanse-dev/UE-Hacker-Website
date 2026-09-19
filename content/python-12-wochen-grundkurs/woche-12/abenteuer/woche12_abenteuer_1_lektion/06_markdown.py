"""## 🎒 Etappe 3: Gegenstände und Inventar

*Wissen aus Woche 6 + 10: Listen und Klassen*

Jeder **Gegenstand** hat einen Namen und eine Beschreibung. Dafür bauen wir eine Klasse `Gegenstand` (Woche 10). Jeder Raum bekommt eine Liste seiner Gegenstände (Woche 6).

### 💡 Neu: Objekte in Objekten (Komposition)

Bisher haben Objekte nur einfache Werte gespeichert (Texte, Zahlen). Ein Objekt kann aber auch **andere Objekte enthalten**. Der `Spieler` hat ein Inventar – und das ist eine Liste voller `Gegenstand`-Objekte.

Das nennt man **Komposition** und sie beantwortet die Frage: *„Hat das Objekt ein anderes Objekt?"*

| Beziehung | Frage | Beispiel |
|-----------|-------|----------|
| Vererbung (Woche 11) | Ist ein Krieger **ein** Held? | `class Krieger(Held):` |
| Komposition | **Hat** der Spieler einen Gegenstand? | `self.inventar = [Gegenstand(...)]` |

Beide Ideen sind wichtig: Vererbung sagt „ist ein", Komposition sagt „hat ein"."""