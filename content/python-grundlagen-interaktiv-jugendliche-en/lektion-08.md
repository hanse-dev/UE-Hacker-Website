# Functions

Functions encapsulate reusable code. `return` gives back a value.

```python
def bmi(weight, height):
    return weight / (height ** 2)

result = bmi(70, 1.75)
print(f"BMI: {result:.1f}")
```

Without `return` the function returns `None`. Parameters can have default values.
