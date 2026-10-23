# ⚖️ Wichtige Operatoren: `=` oder `==`?

Das ist ein **entscheidender Unterschied**, an dem viele Abenteurer scheitern:

- **`=` (ein Gleichheitszeichen)** *speichert*: Es legt einen Wert in eine Variable.
- **`==` (zwei Gleichheitszeichen)** *vergleicht*: Es fragt: "Sind beide Seiten gleich?" – und liefert `True` oder `False`.

```python
level = 10        # speichern: level bekommt den Wert 10
if level == 10:   # Vergleich: Ist level gleich 10?
    print("Level 10 erreicht!")
```

Ein Vergleich ist selbst ein Wert, den du sogar ausgeben kannst:

```python
level = 10
print(level == 10)   # True
print(level == 99)   # False
```

Auch in die `{}` eines f-Strings darfst du einen Vergleich schreiben: `print(f"Level 10: {level == 10}")` gibt `Level 10: True` aus.

> **Merke:** In einer Bedingung immer `==` zum Vergleichen verwenden, nie `=`! Ein einzelnes `=` in einem `if` ist ein Syntaxfehler.
