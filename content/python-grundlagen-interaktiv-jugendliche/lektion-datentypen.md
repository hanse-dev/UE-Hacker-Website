# Datentypen

Jeder Wert hat einen Typ. Python erkennt ihn automatisch (dynamische Typisierung).

| Typ     | Beispiel        | Bedeutung            |
|---------|-----------------|----------------------|
| `int`   | `42`            | Ganze Zahl           |
| `float` | `3.14`          | Dezimalzahl          |
| `str`   | `"Hallo"`       | Text                 |
| `bool`  | `True`, `False` | Wahrheitswert        |

Mit `type()` kannst du den Typ prüfen. Mit `int()`, `str()`, `float()` konvertierst du zwischen Typen.

```python
alter = "18"
print(type(alter))        # str
print(type(int(alter)))   # int
```
