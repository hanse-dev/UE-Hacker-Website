# Funktionen

Funktionen kapseln wiederverwendbaren Code. `return` gibt einen Wert zurück.

```python
def bmi(gewicht, groesse):
    return gewicht / (groesse ** 2)

ergebnis = bmi(70, 1.75)
print(f"BMI: {ergebnis:.1f}")
```

Ohne `return` gibt die Funktion `None` zurück. Parameter können Standardwerte haben.
