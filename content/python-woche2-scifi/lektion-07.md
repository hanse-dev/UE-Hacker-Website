# 📟 Systemprotokoll 7: Typumwandlung

Sensordaten kommen oft als **Text** an. Um damit zu rechnen, musst du sie umwandeln. Vier Funktionen übernehmen das:

| Funktion | Wandelt um in | Beispiel |
|---|---|---|
| `int()` | ganze Zahl | `int("273")` → `273` |
| `float()` | Kommazahl | `float("42.5")` → `42.5` |
| `str()` | Text | `str(5)` → `"5"` |
| `bool()` | Wahrheitswert | `bool(1)` → `True`, `bool(0)` → `False` |

```python
temperatur_str = "273"                   # Text!
temperatur_int = int(temperatur_str)     # jetzt eine Zahl
print(temperatur_int + 10)               # 283
```

Und umgekehrt: Um eine Zahl mit `+` in einen Text einzufügen, brauchst du `str()`:

```python
crew = 12
print("Crew: " + str(crew))
```

> 💡 Bei f-Strings brauchst du kein `str()` – sie wandeln automatisch um.
