# 📟 Systemprotokoll 6: Rechenoperationen

**Mit Zahlen** kannst du rechnen:

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `+` `-` | addieren, subtrahieren | `8 + 4` → `12` |
| `*` | multiplizieren | `8 * 2` → `16` |
| `/` | teilen (Ergebnis ist ein Float!) | `8 / 2` → `4.0` |

```python
planeten = 8
print(planeten * 2)    # 16
print(planeten / 2)    # 4.0
```

> 💡 Beim Teilen mit `/` kommt immer eine Kommazahl heraus – auch wenn das Ergebnis glatt aufgeht.

> 🧮 Python rechnet wie in Mathe **Punkt vor Strich**: erst `*` und `/`, dann `+` und `-`. Soll etwas zuerst gerechnet werden, setz Klammern: `(2 + 3) * 4` ergibt `20`, aber `2 + 3 * 4` ergibt `14`.
