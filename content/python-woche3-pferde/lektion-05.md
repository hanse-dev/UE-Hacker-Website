# 🔗 Übung 5: Logische Verknüpfungen (and, or, not)

Mit **`and`**, **`or`** und **`not`** kombinierst du mehrere Bedingungen:

| Operator | Bedeutung |
|----------|-----------|
| `and` | **beide** Bedingungen müssen wahr sein |
| `or` | **mindestens eine** muss wahr sein |
| `not` | kehrt einen Wahrheitswert um (`True` ↔ `False`) |

```python
hat_sattel = True
hat_helm = True
if hat_sattel and hat_helm:
    print("Du bist bereit zum Reiten!")
```

```python
hat_trense = False
hat_halfter = True
if hat_trense or hat_halfter:
    print("Du kannst das Pferd führen!")
```

```python
ist_krank = False
if not ist_krank:
    print("Das Pferd ist gesund!")
```

> 💡 Bei mehreren Verknüpfungen helfen **Klammern**, z.B. `a or (b and c)` – so ist klar, was zusammengehört.
