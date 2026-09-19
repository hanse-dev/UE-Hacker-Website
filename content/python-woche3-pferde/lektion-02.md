# ⚖️ Übung 2: Vergleichsoperatoren

Bedingungen entstehen meist durch **Vergleiche**. Ein Vergleich ergibt immer `True` oder `False`.

## `=` oder `==`?

Das ist ein entscheidender Unterschied!

- **`=`** weist einer Variable einen Wert **zu**: `alter = 10`
- **`==`** **vergleicht** zwei Werte auf Gleichheit: `alter == 10`

```python
alter = 10          # Zuweisung
if alter == 10:     # Vergleich
    print("Das Pferd ist 10 Jahre alt!")
```

> 🐴 **Merke:** In einer Bedingung immer `==` für Vergleiche verwenden, nie `=`!

## Die sechs Vergleichsoperatoren

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `==` | gleich | `alter == 10` |
| `!=` | ungleich | `gangart != "Galopp"` |
| `<` | kleiner als | `alter < 5` |
| `<=` | kleiner oder gleich | `alter <= 5` |
| `>` | größer als | `alter > 15` |
| `>=` | größer oder gleich | `alter >= 3` |

Du kannst einen Vergleich auch direkt ausgeben: `print(160 < 165)` zeigt `True`.
