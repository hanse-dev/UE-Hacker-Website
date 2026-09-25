# 👀 Muster von Auge suchen

Bevor ein Computer aus Daten lernt, lohnt es sich, selbst hinzuschauen: Gibt es ein Merkmal, das
zwei Gruppen von Beispielen unterscheidet?

```python
tiere = [
    {"name": "Hund", "beine": 4},
    {"name": "Spatz", "beine": 2},
    {"name": "Katze", "beine": 4},
    {"name": "Ente", "beine": 2},
]

vierbeiner = [tier["name"] for tier in tiere if tier["beine"] == 4]
print(vierbeiner)
```

Mit einer List Comprehension filterst du in einer Zeile alle Beispiele heraus, die eine Bedingung
erfüllen:

```python
tiere = [
    {"name": "Hund", "gewicht": 30},
    {"name": "Spatz", "gewicht": 0.03},
    {"name": "Elefant", "gewicht": 5000},
]

schwer = [tier["name"] for tier in tiere if tier["gewicht"] > 10]
print(schwer)
```

> 💡 Genau das macht später auch ein trainiertes Modell – nur dass es die Schwelle (hier: `> 10`)
> nicht von dir vorgegeben bekommt, sondern selbst aus den Daten ableitet.
