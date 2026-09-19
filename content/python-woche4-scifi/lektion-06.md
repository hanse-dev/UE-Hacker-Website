# 📟 Systemprotokoll 6: Der Schildgenerator

Eine while-Schleife braucht oft **mehrere Variablen**: eine für den Wert, der sich ändert, und eine, die die Durchläufe zählt.

```python
energie = 100
minute = 1
while energie > 20:
    energie -= 15
    print(f"Minute {minute}: Rest: {energie}%")
    minute += 1
print(f"Schild kritisch nach {minute-1} Minuten!")
```

Die Schleife endet, sobald `energie > 20` nicht mehr gilt. Nach der Schleife verrät dir `minute-1`, wie viele Durchläufe es gab.

Werte können sich auch nach anderen Regeln ändern, z. B. verdoppeln mit `signal *= 2`.
