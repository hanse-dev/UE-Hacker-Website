# ✂️ Trainings- und Testdaten trennen

Bisher hast du deinen k-NN-Klassifikator immer mit denselben Daten getestet, mit denen du ihn
auch "trainiert" hast (also den Trainingsdaten selbst als Vergleich benutzt). Das verrät dir
aber nicht, ob dein Klassifikator auch bei **neuen, unbekannten** Beispielen richtig liegt – er
könnte die Trainingsdaten einfach "auswendig gelernt" haben.

Deshalb teilt man einen Datensatz in zwei Teile:
- **Trainingsdaten** – damit lernt der Klassifikator (bzw. speichert er die Beispiele)
- **Testdaten** – die werden zurückgehalten und erst danach benutzt, um ehrlich zu prüfen, wie
  gut die Vorhersage bei unbekannten Beispielen funktioniert

Mit **Slicing** kannst du eine Liste einfach in zwei Teile zerlegen:

```python
daten = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.03, "art": "Vogel"},
    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.02, "art": "Vogel"},
    {"beine": 8, "gewicht": 0.0002, "art": "Spinnentier"},
    {"beine": 6, "gewicht": 0.001, "art": "Insekt"},
]

trainingsdaten = daten[:4]
testdaten = daten[4:]

print(len(trainingsdaten))
print(len(testdaten))
```
