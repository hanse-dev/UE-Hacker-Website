# 🗳️ Zählen mit einem Dictionary & die k nächsten Nachbarn

Bevor du mehrere Nachbarn befragst, brauchst du eine Zähl-Technik: Mit einem Dictionary kannst du
zählen, wie oft jeder Wert in einer Liste vorkommt – der Schlüssel ist der Wert, der zugehörige
Wert im Dictionary die Anzahl. `.get(schluessel, 0)` liefert 0, wenn der Schlüssel noch nicht
vorkommt (siehe Woche 2).

```python
labels = ["Saeugetier", "Vogel", "Saeugetier", "Saeugetier", "Vogel"]

anzahl_je_kategorie = {}
for label in labels:
    anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1

print(anzahl_je_kategorie)
```

Damit kannst du jetzt die **k** nächsten Nachbarn statt nur des einen nächsten holen: Du
sortierst die Trainingsdaten nach ihrem Abstand zum neuen Beispiel (`sorted(..., key=...)`, aus
Woche 11 des 12-Wochen-Kurses) und nimmst mit Slicing die ersten `k` davon.

```python
import math

def abstand(a, b):
    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)

trainingsdaten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.03, "art": "Vogel"},
    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},
]
neu = {"beine": 4, "gewicht": 28}

def abstand_zu_neu(beispiel):
    return abstand(neu, beispiel)

sortiert = sorted(trainingsdaten, key=abstand_zu_neu)
k = 2
naechste = sortiert[:k]

for beispiel in naechste:
    print(beispiel["art"])
```

> 💡 Als Nächstes verbindest du beide Techniken: die k nächsten Nachbarn holen, ihre Labels
> zählen, und das häufigste Label als Mehrheitsentscheid ausgeben – dein kompletter k-NN.
