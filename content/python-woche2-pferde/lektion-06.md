# 🧮 Übung 6: Rechnen mit Zahlen

Mit `int` und `float` rechnet Python wie ein Taschenrechner:

| Zeichen | Bedeutung | Beispiel | Ergebnis |
|---------|-----------|----------|----------|
| `+` | plus | `12 + 8` | `20` |
| `-` | minus | `12 - 8` | `4` |
| `*` | mal | `12 * 2` | `24` |
| `/` | geteilt | `12 / 4` | `3.0` |

> 🐴 **Merke:** Eine Division mit `/` ergibt **immer** einen `float` – auch wenn das Ergebnis glatt aufgeht (`12 / 4` ist `3.0`).

```python
pferde_a = 12
pferde_b = 8
print(f"Gesamte Pferde: {pferde_a + pferde_b}")
print(f"Pferde pro Box: {pferde_a / 4}")
```
