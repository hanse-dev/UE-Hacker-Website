# 🔄 Übung 8: Typen umwandeln

Nicht alle Typen passen zusammen – `"5" * 2` ergibt `"55"`, aber `5 * 2` ergibt `10`. Zum Glück gibt es vier **Umwandlungs-Funktionen**, eine pro Hufschlag-Typ. Du gibst ihnen einen Wert, sie geben ihn im neuen Typ zurück:

| Funktion | macht daraus … | Beispiel | Ergebnis |
|----------|----------------|----------|----------|
| `int()` | ganze Zahl | `int("5")` | `5` |
| `float()` | Kommazahl | `float("4.5")` | `4.5` |
| `str()` | Text | `str(5)` | `"5"` |
| `bool()` | Wahrheitswert | `bool(1)` | `True` |

```python
alter_text = "5"
alter_zahl = int(alter_text)
print(type(alter_text))   # <class 'str'>
print(type(alter_zahl))   # <class 'int'>
```

> 🐴 **Merke:** `int("abc")` klappt nicht – nur Text, der wirklich wie eine Zahl aussieht, lässt sich umwandeln.
