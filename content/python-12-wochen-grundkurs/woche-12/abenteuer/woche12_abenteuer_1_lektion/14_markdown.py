"""## 💾 Etappe 6: Speichern und Laden

*Wissen aus Woche 9: JSON und Dateien*

Ein gutes Spiel merkt sich den Spielstand. Ein Objekt wie `Spieler` lässt sich nicht direkt als JSON speichern, deshalb bauen wir daraus zuerst ein **Dictionary** mit Name, Position, HP und Inventar (als Liste von Dictionaries).

Beim Laden geht es rückwärts: Aus dem Dictionary entsteht wieder ein `Spieler`-Objekt mit neuen `Gegenstand`-Objekten. Existiert die Datei nicht, fängt ein `try/except` den `FileNotFoundError` ab."""