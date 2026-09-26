# ⚖️ Ausgewogene Daten dagegen

Eine gängige Gegenmaßnahme: die Trainingsdaten **ausgewogen** machen, bevor der Baum überhaupt
gebaut wird. Die einfachste Variante heißt **Undersampling** – von der großen Klasse nur so viele
Beispiele behalten, wie die kleine Klasse hat.

```python
tickets_ausgewogen = [
    {"wartezeit": 5, "dringend": "nein"},
    {"wartezeit": 10, "dringend": "nein"},
    {"wartezeit": 22, "dringend": "ja"},
    {"wartezeit": 27, "dringend": "ja"},
]
baum2 = baue_baum(tickets_ausgewogen, "wartezeit", "dringend")
print(baum2)
print(genauigkeit_je_klasse(tickets, "dringend", lambda b: klassifiziere(baum2, b)))
```

Wichtig: Trainiert wird nur mit den vier ausgewogenen Beispielen – **getestet** wird trotzdem mit
allen zehn ursprünglichen Tickets, damit der Vergleich zu vorher fair bleibt. Jetzt findet der Baum
einen Trennwert, der wirklich zwischen "dringend" und "nicht dringend" unterscheidet: Er erkennt
jetzt **alle** dringenden Tickets richtig (100%) – dafür sinkt seine Genauigkeit bei den
nicht-dringenden Tickets deutlich. Ausgewogene Daten machen ein Modell also nicht "besser an sich",
sondern verschieben, **worauf** es achtet. Ob das gewünscht ist, hängt vom Ziel ab: Bei einem
Dringlichkeits-Filter ist es meist wichtiger, kein dringendes Ticket zu übersehen, als gelegentlich
ein normales Ticket fälschlich als dringend einzustufen.
