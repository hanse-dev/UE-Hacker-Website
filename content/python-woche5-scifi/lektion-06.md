# 🧠 Systemprotokoll 6: Entscheidungen und Schleifen in Funktionen

In eine Funktion darfst du alles packen, was du schon kennst: **`if`/`else`** und **Schleifen**. Mit `return` kannst du je nach Situation ein anderes Ergebnis liefern:

```python
def pruefe_schild(schild):
    if schild >= 50:
        return "Schild stabil!"
    else:
        return f"Noch {50 - schild} % bis stabil"

print(pruefe_schild(20))
print(pruefe_schild(75))
```

Sobald ein `return` ausgeführt wird, endet die Funktion – der Rest wird übersprungen.

Auch eine Schleife passt hinein. Sie rechnet, und am Ende gibt `return` das Ergebnis zurück:

```python
def zaehle_signale(sektoren):
    signale = 0
    for sektor in range(1, sektoren + 1):
        signale += sektor
    return signale
```

> 💡 Das `return` steht **nach** der Schleife (nicht eingerückt) – sonst würde die Funktion schon nach dem ersten Durchlauf enden.
