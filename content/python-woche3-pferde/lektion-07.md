# ⚖️ Wichtige Operatoren: `=` oder `==`?

Das ist ein **entscheidender Unterschied**, über den viele Reiter stolpern:

- **`=` (ein Gleichheitszeichen)** *weist zu*: Es legt einen Wert in einer Variable ab.
- **`==` (zwei Gleichheitszeichen)** *vergleicht*: Es fragt: "Sind beide Seiten gleich?" – und liefert `True` oder `False`.

```python
alter = 10        # Zuweisung: alter bekommt den Wert 10
if alter == 10:   # Vergleich: Ist alter gleich 10?
    print("Das Pferd ist 10 Jahre alt!")
```

Ein Vergleich ist selbst ein Wert, den du sogar ausgeben kannst:

```python
alter = 10
print(alter == 10)   # True
print(alter == 12)   # False
```

> 🐴 **Merke:** In einer Bedingung immer `==` zum Vergleichen verwenden, nie `=`! Ein einzelnes `=` in einem `if` ist ein Syntaxfehler.
