# ➕ Systemprotokoll 3: Rechnen mit Zahlen

Mit Integern und Floats kannst du rechnen – wie mit einem Taschenrechner:

| Zeichen | Bedeutung | Beispiel | Ergebnis |
|---|---|---|---|
| `+` | Addition | `8 + 4` | `12` |
| `-` | Subtraktion | `8 - 4` | `4` |
| `*` | Multiplikation | `8 * 2` | `16` |
| `/` | Division | `8 / 2` | `4.0` |

> 📡 **Achtung:** Eine Division mit `/` liefert **immer einen Float** – auch wenn die Zahl aufgeht: `8 / 2` ergibt `4.0`, nicht `4`.

Ergebnisse kannst du in Variablen speichern und in f-Strings ausgeben:

```python
planeten = 8
pro_sektor = planeten / 2
print(f"Pro Sektor: {pro_sektor}")
```
