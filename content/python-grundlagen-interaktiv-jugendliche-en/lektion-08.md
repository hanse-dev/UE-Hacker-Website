# Functions

Functions encapsulate reusable code. `return` gives back a value.

```python
def speed(distance, time):
    return distance / time

result = speed(150, 2.5)
print(f"Speed: {result:.1f} km/h")
```

Without `return` the function returns `None`. Parameters can have default values.
