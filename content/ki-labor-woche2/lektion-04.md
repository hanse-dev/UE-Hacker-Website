# ❓ Datenqualität: Fehlende Werte

Echte Datensätze sind selten perfekt – manchmal fehlt bei einem Beispiel ein Merkmal. Mit
`.get(schluessel, standardwert)` stürzt dein Programm dabei nicht ab, sondern nutzt einen
Standardwert:

```python
tiere = [
    {"name": "Hund", "gewicht": 30},
    {"name": "Spatz"},
]

for tier in tiere:
    gewicht = tier.get("gewicht", "unbekannt")
    print(tier["name"], gewicht)
```

Mit `"merkmal" not in tier` prüfst du direkt, ob ein Merkmal überhaupt vorhanden ist – zum
Beispiel, um zu zählen, wie vielen Beispielen ein Wert fehlt:

```python
tiere = [
    {"name": "Hund", "gewicht": 30},
    {"name": "Spatz"},
    {"name": "Katze", "gewicht": 4},
]

fehlend = 0
for tier in tiere:
    if "gewicht" not in tier:
        fehlend += 1

print(fehlend)
```

> 💡 `tier["gewicht"]` würde bei einem fehlenden Schlüssel abstürzen (`KeyError`).
> `tier.get("gewicht", "unbekannt")` gibt stattdessen einen Standardwert zurück.
