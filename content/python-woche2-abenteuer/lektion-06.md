# 💨 Luft: Wahrheitswerte (`bool`)

Das Luft-Element kennt nur **zwei Werte**: `True` (wahr) oder `False` (falsch) – **groß** geschrieben und **ohne** Anführungszeichen. Wie ein Schalter: an oder aus.

```python
magie_aktiv = True
vergiftet = False
print(f"Magie aktiv: {magie_aktiv}")
print(type(magie_aktiv))    # <class 'bool'>
```

Vergleiche liefern automatisch einen Wahrheitswert:

| Vergleich | Bedeutung |
|-----------|-----------|
| `a > b` / `a < b` | größer / kleiner |
| `a >= b` / `a <= b` | größer-gleich / kleiner-gleich |
| `a == b` | gleich (Achtung: **zwei** Gleichheitszeichen!) |
| `a != b` | ungleich |

```python
level = 8
print(level >= 10)    # False
```
