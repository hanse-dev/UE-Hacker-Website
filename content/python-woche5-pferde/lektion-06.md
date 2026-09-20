# 🧠 Übung 6: Entscheidungen und Schleifen in Funktionen

In eine Funktion darfst du alles packen, was du schon kennst: **`if`/`else`** und **Schleifen**. Mit `return` kannst du je nach Situation ein anderes Ergebnis liefern:

```python
def pruefe_tempo(tempo):
    if tempo >= 20:
        return "Galopp!"
    else:
        return f"Noch {20 - tempo} km/h bis zum Galopp"

print(pruefe_tempo(12))
print(pruefe_tempo(25))
```

Sobald ein `return` ausgeführt wird, endet die Funktion – der Rest wird übersprungen.

Auch eine Schleife passt hinein. Sie rechnet, und am Ende gibt `return` das Ergebnis zurück:

```python
def zaehle_spruenge(runden):
    spruenge = 0
    for runde in range(1, runden + 1):
        spruenge += runde
    return spruenge
```

> 💡 Das `return` steht **nach** der Schleife (nicht eingerückt) – sonst würde die Funktion schon nach dem ersten Durchlauf enden.
