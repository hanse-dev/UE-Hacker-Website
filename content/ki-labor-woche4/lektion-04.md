# 🧪 Trainieren und testen: alles zusammenfügen

Jetzt fügst du alles zusammen: Daten aufteilen (Lektion 1), Vorhersagen für die Testdaten
sammeln (Lektion 3) und die Genauigkeit berechnen (Lektion 2). Das ist der Standard-Ablauf, mit
dem du jeden Klassifikator ehrlich bewertest.

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

def trainiere_und_teste(daten, split, k):
    trainingsdaten = daten[:split]
    testdaten = daten[split:]

    vorhersagen = []
    for beispiel in testdaten:
        vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, k))

    erwartete_werte = [beispiel["art"] for beispiel in testdaten]
    return genauigkeit(vorhersagen, erwartete_werte)

daten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 3, "art": "Vogel"},
    {"beine": 2, "gewicht": 4, "art": "Vogel"},
    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 20, "art": "Vogel"},
]

print(trainiere_und_teste(daten, 4, 3))
```

Das letzte Testbeispiel (`{"beine": 2, "gewicht": 20, "art": "Vogel"}`) ist ein ungewöhnlich
schwerer Vogel – er liegt näher an den Säugetieren und wird deshalb falsch vorhergesagt. Deshalb
ist die Genauigkeit hier nicht 100%.
