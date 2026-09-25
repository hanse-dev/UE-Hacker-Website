# 📊 Ein Datensatz ist eine Liste von Beispielen

In Woche 1 hast du gesehen: Statt Regeln zu schreiben, sammelst du Beispiele. So eine Sammlung
nennt man einen **Datensatz** – eine Liste, in der jedes Element ein einzelnes Beispiel ist.

Ein Beispiel besteht meistens aus mehreren Werten, die zusammengehören. Dafür eignet sich ein
Dictionary gut:

```python
tiere = [
    {"name": "Hund", "beine": 4, "gewicht": 30},
    {"name": "Spatz", "beine": 2, "gewicht": 0.03},
    {"name": "Biene", "beine": 6, "gewicht": 0.001},
]

for tier in tiere:
    print(tier["name"])
```

Jedes Dictionary in der Liste ist ein Beispiel, jeder Schlüssel ein **Merkmal** (englisch:
*Feature*) dieses Beispiels. Du kannst gezielt auf einzelne Merkmale zugreifen:

```python
tiere = [
    {"name": "Hund", "beine": 4},
    {"name": "Spatz", "beine": 2},
]

for tier in tiere:
    print(tier["name"], "hat", tier["beine"], "Beine")
```

> 💡 Diese Struktur – eine Liste von Dictionaries – wirst du den ganzen Kurs über als Datensatz
> verwenden. Ab Woche 3 lässt du den Computer aus genau solchen Daten Vorhersagen treffen.
