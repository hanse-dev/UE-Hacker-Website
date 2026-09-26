# ⚖️ Wenn Trainingsdaten schief sind

Jedes Modell, das du diese Wochen gebaut hast (k-NN, Entscheidungsbaum), lernt **ausschließlich
aus seinen Trainingsdaten**. Wenn eine Klasse darin sehr viel häufiger vorkommt als eine andere,
nennt man den Datensatz **schief** oder **unausgewogen** (englisch: *imbalanced*). Das Modell hat
dann kaum eine Chance, die seltene Klasse wirklich zu lernen – einfach, weil es fast nichts davon
gesehen hat.

Ein Beispiel: Ein Support-Team möchte automatisch erkennen, ob ein Ticket **dringend** ist. In den
meisten Betrieben ist die überwältigende Mehrheit der Tickets **nicht** dringend – nur wenige
wirklich. Zähle zuerst, wie schief so ein Datensatz sein kann:

```python
def anzahl_je_klasse(daten, label_feld):
    anzahl = {}
    for beispiel in daten:
        anzahl[beispiel[label_feld]] = anzahl.get(beispiel[label_feld], 0) + 1
    return anzahl

tickets = [
    {"wartezeit": 5, "dringend": "nein"},
    {"wartezeit": 10, "dringend": "nein"},
    {"wartezeit": 22, "dringend": "ja"},
]
print(anzahl_je_klasse(tickets, "dringend"))
```

`anzahl_je_klasse()` zählt für jede Klasse (hier `"ja"`/`"nein"`), wie oft sie in den Daten
vorkommt – genau wie `anzahl_je_klasse()` in `mehrheitsklasse()` aus Woche 5, nur diesmal mit
einem **Parameter** für das Label-Feld, statt es fest einzubauen. So funktioniert die Funktion für
jeden Datensatz, egal wie das Label-Feld heißt.
