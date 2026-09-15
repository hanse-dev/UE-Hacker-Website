"""### 🛡️ Catching Errors with try/except

If you try to change an immutable data capsule, Python raises a `TypeError`. With `try`/`except` you catch such errors instead of letting your program crash:

```python
try:
    capsule[0] = \"New\"        # Code that could raise an error
except TypeError as e:
    print(f\"Error: {e}\")      # What happens when the error occurs
```"""
