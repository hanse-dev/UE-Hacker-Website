# Bedingungen mit if

`if` führt Code nur aus, wenn eine Bedingung wahr ist. `elif` prüft weitere Bedingungen, `else` fängt den Rest ab.

```python
alter = 16
if alter >= 18:
    print("Zugang erlaubt")
elif alter >= 16:
    print("Eingeschränkter Zugang")
else:
    print("Kein Zugang")
```

Vergleichsoperatoren: `==`, `!=`, `<`, `>`, `<=`, `>=`
