# 📟 Systemprotokoll 2: Strings und type()

Jede Information auf der Nebula-7 hat einen **Quanten-Typ** – wie die vier Aggregatzustände. Python kennt vier Grundtypen:

| Typ | Python-Name | Beispiel |
|---|---|---|
| Text | `str` (String) | `"Starlight"` |
| Ganze Zahl | `int` (Integer) | `250` |
| Kommazahl | `float` (Float) | `2.5` |
| Wahrheitswert | `bool` (Boolean) | `True` |

Die Funktion `type()` zeigt dir den Quanten-Typ jeder Information:

```python
schiff_name = "Starlight"
print(type(schiff_name))   # <class 'str'>
```

## 🔤 Strings – Textdaten

Ein **String** ist jeder Text in Anführungszeichen – auch wenn er wie eine Zahl aussieht: `"250"` ist Text, keine Zahl!
