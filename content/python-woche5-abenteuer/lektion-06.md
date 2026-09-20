# 🧠 Zauberformel 2: Entscheidungen und Schleifen in Funktionen

In eine Funktion darfst du alles packen, was du schon kennst: **`if`/`else`** und **Schleifen**. Mit `return` kannst du je nach Situation ein anderes Ergebnis liefern:

```python
def pruefe_level(level):
    if level >= 10:
        return "Bereit für die Quest!"
    else:
        return f"Noch {10 - level} Level nötig"

print(pruefe_level(5))
print(pruefe_level(12))
```

Sobald ein `return` ausgeführt wird, endet die Funktion – der Rest wird übersprungen.

Auch eine Schleife passt hinein. Sie rechnet, und am Ende gibt `return` das Ergebnis zurück:

```python
def summe_bis(n):
    summe = 0
    for zahl in range(1, n + 1):
        summe += zahl
    return summe
```

> 💡 Das `return` steht **nach** der Schleife (nicht eingerückt) – sonst würde die Funktion schon nach dem ersten Durchlauf enden.
