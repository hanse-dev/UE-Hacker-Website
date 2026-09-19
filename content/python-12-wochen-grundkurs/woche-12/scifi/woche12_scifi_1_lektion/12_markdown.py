"""## 🛡️ Etappe 5: Falsche Eingaben abfangen

*Wissen aus Woche 8: try/except*

Spieler tippen manchmal Unsinn. Der Befehl `gehe norden` besteht aus zwei Wörtern, die `split()` (Woche 2) in `aktion` und `ziel` zerlegt. Bei `hallo` oder `gehe nach norden` passt die Anzahl nicht, und Python wirft einen `ValueError`.

Statt abzustürzen fängt `try/except` den Fehler ab und zeigt eine freundliche Meldung. So bleibt das Spiel stabil!"""