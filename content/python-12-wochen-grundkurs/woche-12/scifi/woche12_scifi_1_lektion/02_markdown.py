"""## 🗺️ Etappe 1: Die Karte der Welt

*Wissen aus Woche 8: Dictionaries*

Eine Raumstation besteht aus Räumen, und jeder Raum hat eine Beschreibung und Ausgänge. Das passt perfekt in ein **Dictionary, das weitere Dictionaries enthält**:

- der äußere Schlüssel ist der Name des Raums (z.B. `"korridor"`)
- der innere Wert ist wieder ein Dictionary mit `"beschreibung"` und `"ausgaenge"`
- die Ausgänge sind selbst ein Dictionary: Richtung → Name des nächsten Raums

Die Funktion `beschreibe()` (Woche 5) schaut den Raum nach und gibt ihn mit einem f-String (Woche 2) aus."""