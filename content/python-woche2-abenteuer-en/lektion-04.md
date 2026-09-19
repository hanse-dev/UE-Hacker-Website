# 💧 Element 3: Water – Decimal Numbers (`float`)

**Water** flows and is never quite exact: damage values, percentages, speeds. A decimal number has a **decimal point** (not a comma!).

```python
damage = 23.5
percent = 87.25
print(f"Damage: {damage}, hit chance: {percent}%")
print(type(damage))   # <class 'float'>
```

Calculating with a Water element always gives Water:

```python
print(23.5 * 2)   # 47.0
print(10 / 4)     # 2.5
```

> 💡 Even `5.0` is Water – the decimal point decides, not the value.
