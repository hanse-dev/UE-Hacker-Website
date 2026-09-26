# Dictionaries

Dictionaries speichern Schlüssel-Wert-Paare. Zugriff über Schlüssel, nicht über Index.

```python
user = {
    "name": "Alex",
    "alter": 16,
    "premium": True
}
print(user["name"])
user["punkte"] = 1500
print(user)
```

Anders als bei Listen spielt bei Dictionaries die Position keine Rolle – du greifst immer über den Schlüssel zu, nicht über eine Zahl. Ein Schlüssel muss dabei eindeutig sein: weist du einem bereits vorhandenen Schlüssel einen neuen Wert zu, wird der alte Wert überschrieben statt ein zweiter Eintrag angelegt.

Fragst du nach einem Schlüssel, der nicht existiert (`user["adresse"]`), wirft Python einen `KeyError`. Willst du das vermeiden, nutzt du `.get(key, default)` – das liefert einen Standardwert zurück, statt abzustürzen:

```python
print(user.get("adresse", "nicht angegeben"))
```

Weitere nützliche Methoden: `.keys()` liefert alle Schlüssel, `.values()` alle Werte, `.items()` alle Schlüssel-Wert-Paare zusammen – praktisch für eine Schleife, die beides gleichzeitig braucht:

```python
for schluessel, wert in user.items():
    print(f"{schluessel}: {wert}")
```
