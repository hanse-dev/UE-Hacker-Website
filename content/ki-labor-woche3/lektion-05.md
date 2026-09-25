# 🤖 Der komplette k-NN-Klassifikator

Jetzt fügst du alles zu einem einzigen Klassifikator zusammen: Abstand berechnen, die k nächsten
Nachbarn holen, ihre Labels zählen, und das häufigste Label zurückgeben (**Mehrheitsentscheid**).

```python
import math

def abstand(a, b):
    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)

def knn_klassifiziere(trainingsdaten, neu, k):
    def abstand_zu_neu(beispiel):
        return abstand(neu, beispiel)

    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)
    naechste = sortiert[:k]
    labels = [beispiel["art"] for beispiel in naechste]

    anzahl_je_kategorie = {}
    for label in labels:
        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1

    beste_kategorie = None
    bester_wert = -1
    for kategorie in anzahl_je_kategorie:
        anzahl = anzahl_je_kategorie[kategorie]
        if anzahl > bester_wert:
            bester_wert = anzahl
            beste_kategorie = kategorie
    return beste_kategorie

trainingsdaten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.03, "art": "Vogel"},
    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.02, "art": "Vogel"},
]

print(knn_klassifiziere(trainingsdaten, {"beine": 3, "gewicht": 20}, 3))
print(knn_klassifiziere(trainingsdaten, {"beine": 2, "gewicht": 0.01}, 1))
```

Herzlichen Glückwunsch – das ist dein erster kompletter, selbst geschriebener Klassifikator!

> 💡 Woher weißt du, ob `k = 1` oder `k = 3` (oder ein ganz anderer Wert) die bessere Wahl ist?
> Genau das lernst du in Woche 4: Trainings- und Testdaten trennen und die Genauigkeit selbst
> messen.
