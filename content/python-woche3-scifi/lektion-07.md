# ⚖️ Wichtige Operatoren: `=` oder `==`?

Das ist ein **entscheidender Unterschied**, über den viele Kadetten stolpern:

- **`=` (ein Gleichheitszeichen)** *weist zu*: Es legt einen Wert in einer Variable ab.
- **`==` (zwei Gleichheitszeichen)** *vergleicht*: Es fragt: "Sind beide Seiten gleich?" – und liefert `True` oder `False`.

```python
energie = 100        # Zuweisung: energie bekommt den Wert 100
if energie == 100:   # Vergleich: Ist energie gleich 100?
    print("Volle Energie!")
```

Ein Vergleich ist selbst ein Wert, den du sogar ausgeben kannst:

```python
energie = 100
print(energie == 100)   # True
print(energie == 50)   # False
```

> 📡 **Merke:** In einer Bedingung immer `==` zum Vergleichen verwenden, nie `=`! Ein einzelnes `=` in einem `if` ist ein Syntaxfehler.
