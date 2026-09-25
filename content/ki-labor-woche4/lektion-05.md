# ⚠️ Overfitting: wenn zu wenig Trainingsdaten reichen

Wenn dein Trainingsdatensatz zu klein oder unrepräsentativ ist, kann dein Klassifikator die
Trainingsdaten zwar perfekt "können" – bei neuen, echten Beispielen aber trotzdem oft
danebenliegen. Das nennt man **Overfitting**: das Modell hat sich an die konkreten
Trainingsbeispiele "überangepasst", statt das dahinterliegende Muster zu lernen.

Ein Trick, um das zu erkennen: die Genauigkeit **auf den Trainingsdaten selbst** mit der
Genauigkeit **auf echten Testdaten** vergleichen.

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

def ist_richtig(vorhersage, erwartet):
    return vorhersage == erwartet

def genauigkeit(vorhersagen, erwartete_werte):
    richtig = 0
    for i in range(len(vorhersagen)):
        if ist_richtig(vorhersagen[i], erwartete_werte[i]):
            richtig += 1
    return round(richtig / len(vorhersagen) * 100)

# Absichtlich winzige, unrepräsentative Trainingsdaten: zwei Ausreißer statt typischer Beispiele.
trainingsdaten = [
    {"beine": 4, "gewicht": 5, "art": "Saeugetier"},   # ungewöhnlich leichtes Saeugetier
    {"beine": 2, "gewicht": 30, "art": "Vogel"},        # ungewöhnlich schwerer Vogel
]

# "Test" mit den Trainingsdaten selbst - jedes Beispiel ist sein eigener naechster Nachbar.
vorhersagen_training = [knn_klassifiziere(trainingsdaten, b, 1) for b in trainingsdaten]
erwartete_training = [b["art"] for b in trainingsdaten]
print(genauigkeit(vorhersagen_training, erwartete_training))

# Echte, typische Testdaten - vom Modell nie gesehen.
testdaten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 3, "art": "Vogel"},
]
vorhersagen_test = [knn_klassifiziere(trainingsdaten, b, 1) for b in testdaten]
erwartete_test = [b["art"] for b in testdaten]
print(genauigkeit(vorhersagen_test, erwartete_test))
```

100% auf den Trainingsdaten, aber 0% auf echten Testdaten – eine riesige Lücke. Das Modell hat
sich zwei Ausreißer gemerkt, statt zu lernen, dass Saeugetiere meist schwerer sind als Vögel.
**Genug und repräsentative Trainingsdaten** helfen dagegen (siehe die Extra-Herausforderungen).
