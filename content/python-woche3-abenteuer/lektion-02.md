# ⚖️ Wichtige Operatoren: `=` oder `==`?

Das ist ein **entscheidender Unterschied**, an dem viele Abenteurer scheitern:

- **`=` (ein Gleichheitszeichen)** *weist zu*: Es legt einen Wert in einer Variable ab.
- **`==` (zwei Gleichheitszeichen)** *vergleicht*: Es fragt: "Sind beide Seiten gleich?" – und liefert `True` oder `False`.

```python
level = 10        # Zuweisung: level bekommt den Wert 10
if level == 10:   # Vergleich: Ist level gleich 10?
    print("Level 10 erreicht!")
```

Ein Vergleich ist selbst ein Wert, den du sogar ausgeben kannst:

```python
level = 10
print(level == 10)   # True
print(level == 99)   # False
```

> **Merke:** In einer Bedingung immer `==` zum Vergleichen verwenden, nie `=`! Ein einzelnes `=` in einem `if` ist ein Syntaxfehler.
