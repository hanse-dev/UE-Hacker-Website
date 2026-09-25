# 🔍 Der nächste Nachbar

Mit dem Abstand kannst du jetzt den **nächsten Nachbarn** finden: das Trainingsbeispiel mit dem
kleinsten Abstand zu einem neuen Beispiel. Genau wie bei "Maximum finden" in Woche 2 gehst du
dafür einmal durch die Liste und merkst dir laufend das beste (hier: kleinste) Ergebnis.

```python
import math

def abstand(a, b):
    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)

trainingsdaten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.03, "art": "Vogel"},
]
neu = {"beine": 4, "gewicht": 28}

bester_abstand = None
naechster = None
for beispiel in trainingsdaten:
    d = abstand(neu, beispiel)
    if bester_abstand is None or d < bester_abstand:
        bester_abstand = d
        naechster = beispiel

print(naechster["art"])
```

Das Label des nächsten Nachbarn wird zur **Vorhersage** für das neue Beispiel – das ist bereits
ein kompletter Klassifikator mit `k = 1` (auch **1-NN** genannt). Als wiederverwendbare Funktion:

```python
import math

def abstand(a, b):
    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)

def naechster_nachbar(trainingsdaten, neu):
    bester_abstand = None
    naechster = None
    for beispiel in trainingsdaten:
        d = abstand(neu, beispiel)
        if bester_abstand is None or d < bester_abstand:
            bester_abstand = d
            naechster = beispiel
    return naechster["art"]

trainingsdaten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.03, "art": "Vogel"},
    {"beine": 6, "gewicht": 0.001, "art": "Insekt"},
]

print(naechster_nachbar(trainingsdaten, {"beine": 6, "gewicht": 0.002}))
print(naechster_nachbar(trainingsdaten, {"beine": 4, "gewicht": 25}))
```

> 💡 1-NN hat eine Schwäche: Ein einziger untypischer Ausreißer in den Trainingsdaten kann die
> ganze Vorhersage kippen. Deshalb befragst du ab der nächsten Lektion **mehrere** Nachbarn.
