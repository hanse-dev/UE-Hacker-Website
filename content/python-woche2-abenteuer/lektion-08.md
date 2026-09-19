# 🔄 Zauberformeln zum Umwandeln

Die Umwandlungen sind ebenfalls **Zauberformeln (Funktionen)** – du rufst sie mit Klammern auf und gibst den Wert hinein, der umgewandelt werden soll. Sie liefern den umgewandelten Wert zurück.

| Zauberformel | Wandelt in ... um | Beispiel |
|--------------|-------------------|----------|
| `int()` | 🪨 ganze Zahl | `int("25")` → `25` |
| `float()` | 💧 Kommazahl | `float("3.5")` → `3.5` |
| `str()` | 🔥 Text | `str(50)` → `"50"` |
| `bool()` | 💨 Wahrheitswert | `bool(0)` → `False` |

```python
alter_text = "25"                # Feuer
alter = int(alter_text)          # Feuer -> Erde
print(alter + 5)                 # 30

gold = 50
print("Gold: " + str(gold))      # Erde -> Feuer, jetzt passt es zu Text
```

**Gut zu wissen:**
- `int(3.9)` schneidet die Nachkommastellen ab und ergibt `3` (es wird **nicht** gerundet).
- `int("abc")` geht nicht – nur Text, der wirklich wie eine Zahl aussieht, lässt sich umwandeln.
- `bool()` ergibt `False` für `0` und den leeren Text `""`, sonst `True`.
