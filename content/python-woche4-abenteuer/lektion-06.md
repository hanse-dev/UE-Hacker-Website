# 💀 Die Spiel-Schleife

Fast jedes Spiel nutzt eine `while`-Schleife: Es läuft weiter, **solange** der Held noch Leben hat.

```python
leben = 100
runde = 1

while leben > 0:
    schaden = 20
    leben -= schaden
    print(f"Runde {runde}: -{schaden} Leben, übrig: {leben}")
    runde += 1
```

Die Bedingung `leben > 0` wird durch `leben -= schaden` irgendwann falsch – so endet die Schleife von allein.

Du kannst Bedingungen auch mit `and` verbinden, zum Beispiel `while leben > 0 and mana > 0:` – dann läuft die Schleife nur weiter, wenn **beides** noch stimmt.
