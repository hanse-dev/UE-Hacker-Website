# 🛡️ Zauberformel 2: Die while-Schleife

Am zweiten Tor steht der **Wächter der Bedingung**. Er lässt dich so lange im Kreis laufen, *solange* seine Bedingung wahr ist. Eine `while`-Schleife wiederholt Code, **solange** eine Bedingung `True` ist:

```python
zaehler = 0
while zaehler <= 5:
    print(f"Zaehler: {zaehler}")
    zaehler += 1
```

**Schritt für Schritt:**
1. `zaehler` startet bei 0
2. Solange `zaehler <= 5` stimmt, läuft der eingerückte Code
3. `zaehler += 1` erhöht den Wert bei jedem Durchlauf
4. Bei `zaehler = 6` ist die Bedingung falsch – die Schleife endet

> ⚠️ **Vorsicht:** Vergisst du `zaehler += 1`, wird die Bedingung nie falsch – die Schleife läuft **endlos**! Die Bedingung muss sich irgendwann ändern.

| Schleife | Wann? |
|----------|-------|
| `for` | Du weißt, **wie oft** |
| `while` | Du wiederholst, **solange** etwas gilt |
