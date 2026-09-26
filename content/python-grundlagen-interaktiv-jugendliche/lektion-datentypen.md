# Datentypen

Jeder Wert hat einen Typ. Python erkennt ihn automatisch (dynamische Typisierung) – anders als in Sprachen wie Java oder C++, wo du den Typ jeder Variable explizit angeben musst.

| Typ     | Beispiel        | Bedeutung            |
|---------|-----------------|----------------------|
| `int`   | `42`            | Ganze Zahl           |
| `float` | `3.14`          | Dezimalzahl          |
| `str`   | `"Hallo"`       | Text                 |
| `bool`  | `True`, `False` | Wahrheitswert        |

"Dynamisch typisiert" bedeutet außerdem, dass eine Variable im Laufe eines Programms sogar den Typ wechseln kann – dieselbe Variable kann erst eine Zahl, später ein Text sein. In der Praxis macht man das selten bewusst, aber es erklärt, warum Python beim bloßen Zuweisen (`x = 5`) nie nach dem Typ fragt.

Mit `type()` kannst du den Typ jederzeit prüfen. Mit `int()`, `str()`, `float()` konvertierst du zwischen Typen:

```python
alter = "18"
print(type(alter))        # str
print(type(int(alter)))   # int
```

Diese Umwandlung ist besonders wichtig bei Nutzereingaben: `input()` liefert **immer** einen String zurück, selbst wenn jemand eine Zahl eintippt. Willst du mit der Eingabe rechnen, musst du sie also erst mit `int()` oder `float()` umwandeln – sonst führt `"18" + 1` zu einem `TypeError`, weil Python Text und Zahl nicht automatisch verrechnet.
