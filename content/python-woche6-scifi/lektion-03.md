# ➕ Datenprotokoll 3: Einträge hinzufügen

Eine Liste ist **veränderbar** – du kannst Einträge ergänzen:

```python
module = ["Antrieb", "Sensor", "Schild"]
module.append("Laser")         # ans Ende
module.insert(0, "Kern")   # an eine Position (hier: ganz vorn)
print(module)
```

- **`append(x)`** hängt `x` **ans Ende** an
- **`insert(index, x)`** setzt `x` an die Stelle `index`, die anderen rücken nach hinten
- Zwei Listen verbindest du mit **`+`**: `alles = liste1 + liste2`
- Mit **`extend(liste2)`** hängst du eine ganze Liste an

> ⚠️ `append` und `insert` **verändern** die Liste selbst und geben nichts zurück – schreibe **nicht** `liste = liste.append(x)`, sonst steht in `liste` danach `None`!
