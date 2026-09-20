# ➕ Übung 3: Einträge hinzufügen

Eine Liste ist **veränderbar** – du kannst Einträge ergänzen:

```python
pferde = ["Sturmwind", "Blitz", "Luna"]
pferde.append("Nova")         # ans Ende
pferde.insert(0, "Stella")   # an eine Position (hier: ganz vorn)
print(pferde)
```

- **`append(x)`** hängt `x` **ans Ende** an
- **`insert(index, x)`** setzt `x` an die Stelle `index`, die anderen rücken nach hinten
- Zwei Listen verbindest du mit **`+`**: `alles = liste1 + liste2`
- Mit **`extend(liste2)`** hängst du eine ganze Liste an

> ⚠️ `append` und `insert` **verändern** die Liste selbst und geben nichts zurück – schreibe **nicht** `liste = liste.append(x)`, sonst steht in `liste` danach `None`!
