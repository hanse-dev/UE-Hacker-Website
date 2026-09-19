# 📟 System Protocol 3: if-elif-else

`if-elif-else` checks **several conditions one after another**.

```python
points = 750
if points >= 1000:
    print("Fleet Commander!")
elif points >= 500:
    print("Captain!")
elif points >= 100:
    print("Lieutenant!")
else:
    print("Cadet!")
```

> ⚠️ **Important:** `elif` always needs a condition, `else` never does. Only the **first true** path is executed – the rest is skipped.
