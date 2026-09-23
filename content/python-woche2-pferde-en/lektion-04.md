# 🏇 Lesson 4: Canter – Decimal Numbers

The canter is a flowing three-beat, never quite exactly the same. Fittingly, **floats** (`float`) are **decimal numbers** – like the weight (`550.5`) or a feed amount (`4.25`).

> ⚠️ Python writes the decimal separator as a **point**: `4.25`, not `4,25`!

```python
weight = 550.5
feed_amount = 4.25
print(f"Weight: {weight} kg, feed: {feed_amount} kg")
print(type(weight))   # <class 'float'>
```

As soon as a number has a point, it's a `float` – even `5.0` is a decimal number, while `5` is a whole number.
