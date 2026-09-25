# ✂️ Merkmale und Label trennen

Wenn ein Modell später etwas vorhersagen soll, darf es die Antwort (das **Label**, siehe Woche 1)
nicht schon vorher sehen. Darum trennst du einen Datensatz oft in zwei Teile: die Merkmale
(*Features*) und die Labels.

```python
tiere = [
    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},
    {"beine": 2, "gewicht": 0.03, "art": "Vogel"},
]

merkmale = [{"beine": t["beine"], "gewicht": t["gewicht"]} for t in tiere]
labels = [t["art"] for t in tiere]

print(merkmale)
print(labels)
```

Aus den getrennten Labels lässt sich zum Beispiel zählen, wie oft eine Kategorie vorkommt:

```python
tiere = [
    {"beine": 4, "art": "Saeugetier"},
    {"beine": 2, "art": "Vogel"},
    {"beine": 6, "art": "Insekt"},
]

labels = [t["art"] for t in tiere]
anzahl_saeugetiere = labels.count("Saeugetier")
print(anzahl_saeugetiere)
```

> 💡 Ab Woche 3 baust du deinen ersten Klassifikator: Er bekommt nur die Merkmale eines neuen
> Beispiels zu sehen und soll daraus das Label vorhersagen.
