# 📟 Systemprotokoll 2: Vergleichsoperatoren

Bedingungen entstehen meist durch **Vergleiche**. Ein Vergleich ergibt immer `True` oder `False`.

## Zuweisung vs. Vergleich: `=` und `==`

Das ist ein entscheidender Unterschied:

- **`=` (ein Gleichheitszeichen)** speichert einen Wert in einer Variable: `level = 10`
- **`==` (zwei Gleichheitszeichen)** vergleicht zwei Werte: `if level == 10:`

> 📡 **Merke:** In Bedingungen immer `==` zum Vergleichen – nie `=`!

## Die Vergleichsoperatoren

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `==` | ist gleich | `befehl == "START"` |
| `!=` | ist **nicht** gleich | `befehl != "START"` |
| `<` | kleiner als | `energie < 20` |
| `<=` | kleiner oder gleich | `temperatur <= 100` |
| `>` | größer als | `geschwindigkeit > 1000` |
| `>=` | größer oder gleich | `schildstaerke >= 50` |

```python
energie = 15
if energie < 20:
    print("Niedrige Energie!")
```

Du kannst einen Vergleich auch einfach ausgeben und siehst dann `True` oder `False`:

```python
print(42 <= 42)   # True
```

Das klappt auch in den `{}` eines f-Strings: `print(f"Genug Energie: {energie >= 10}")` zeigt `Genug Energie: True`.
