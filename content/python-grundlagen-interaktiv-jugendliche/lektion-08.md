# Funktionen

Funktionen kapseln wiederverwendbaren Code. `return` gibt einen Wert zurück.

```python
def bmi(gewicht, groesse):
    return gewicht / (groesse ** 2)

ergebnis = bmi(70, 1.75)
print(f"BMI: {ergebnis:.1f}")
```

`gewicht` und `groesse` sind **Parameter** – Platzhalter, die beim Aufruf mit konkreten Werten (**Argumenten**) gefüllt werden. Die Funktion selbst weiß beim Definieren noch nicht, mit welchen Zahlen sie später aufgerufen wird.

`return` unterscheidet sich von `print()`: `print()` gibt nur etwas auf dem Bildschirm aus, `return` liefert einen Wert zurück, mit dem das restliche Programm weiterarbeiten kann – z.B. um ihn in einer Variable zu speichern (`ergebnis = bmi(70, 1.75)`) oder direkt in einen f-String einzubauen. Eine Funktion ohne `return`-Anweisung gibt automatisch `None` zurück, auch wenn sie intern `print()` aufruft.

Parameter können Standardwerte haben, die verwendet werden, wenn beim Aufruf kein Wert übergeben wird:

```python
def begruessung(name, gruss="Hallo"):
    return f"{gruss}, {name}!"

print(begruessung("Alex"))            # "Hallo, Alex!"
print(begruessung("Alex", "Servus"))  # "Servus, Alex!"
```
