# 🔢 Mehrere Merkmale pro Beispiel

Ein Beispiel hat oft nicht nur ein Merkmal, sondern mehrere gleichzeitig. Ein Hund lässt sich zum
Beispiel über seine Beinanzahl, sein Gewicht und sein Fell beschreiben:

```python
tiere = [
    {"name": "Hund", "beine": 4, "gewicht": 30, "fell": True},
    {"name": "Spatz", "beine": 2, "gewicht": 0.03, "fell": False},
]

for tier in tiere:
    print(tier["name"], tier["beine"], tier["gewicht"], tier["fell"])
```

Mit einem f-String lassen sich mehrere Merkmale übersichtlich zu einer Ausgabe zusammensetzen:

```python
tiere = [
    {"name": "Hund", "beine": 4, "gewicht": 30},
    {"name": "Spatz", "beine": 2, "gewicht": 0.03},
]

for tier in tiere:
    print(f"{tier['name']}: {tier['beine']} Beine, {tier['gewicht']}kg")
```

> 💡 Je mehr Merkmale ein Beispiel hat, desto genauer lässt es sich beschreiben – aber auch desto
> schwerer wird es, von Auge Muster zu erkennen. Genau darum geht es gleich.
