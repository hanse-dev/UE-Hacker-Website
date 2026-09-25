# 🔁 Vorhersagen für den ganzen Testdatensatz sammeln

Um die Genauigkeit deines k-NN-Klassifikators zu messen, brauchst du für **jedes** Beispiel in
den Testdaten eine Vorhersage. Du gehst also mit einer Schleife über die Testdaten, rufst für
jedes Beispiel `knn_klassifiziere()` (aus Woche 3) auf, und sammelst die Ergebnisse in einer
Liste.

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
    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 3, "art": "Vogel"},
    {"beine": 2, "gewicht": 4, "art": "Vogel"},
]
testdaten = [
    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 5, "art": "Vogel"},
]

vorhersagen = []
for beispiel in testdaten:
    vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, 3))

print(vorhersagen)
```

Mit `erwartete_werte = [beispiel["art"] for beispiel in testdaten]` bekommst du die passende
Liste der richtigen Antworten – genau das Format, das `genauigkeit()` aus Lektion 2 braucht.
