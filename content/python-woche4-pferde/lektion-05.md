## ⏳ Übung 5: Schleife – Der Ausdauer-Test

Eine **while-Schleife** wiederholt Code, **solange** eine Bedingung wahr ist:

```python
zaehler = 1
while zaehler <= 5:
    print(f"Hufschlag {zaehler}")
    zaehler += 1
```

1. `zaehler` startet bei 1.
2. Solange `zaehler <= 5` stimmt, wird der eingerückte Code ausgeführt.
3. `zaehler += 1` erhöht den Wert bei jedem Durchlauf um 1.
4. Bei `zaehler = 6` ist die Bedingung falsch – die Schleife endet.

> ⚠️ **Vorsicht:** Vergisst du `zaehler += 1`, wird die Bedingung nie falsch – dann läuft die Schleife **endlos**!
