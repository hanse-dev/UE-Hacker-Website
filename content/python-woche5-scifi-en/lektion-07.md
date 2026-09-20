# 📖 System Log 7: Docstrings and good names

Every good protocol has a **manual**. In Python that is a **docstring**: a text in triple quotes right below the `def` line.

```python
def calculate_fuel(distance):
    """Calculates the fuel requirement."""
    return distance * 3

print(calculate_fuel.__doc__)
```

`calculate_fuel.__doc__` (without parentheses) shows the docstring. That way others – and you yourself in a month – immediately understand what the protocol does.

**Good names:**
- **Lowercase with underscores:** `calculate_fuel` ✅ – not `CalculateFuel` ❌
- **A verb that says what happens:** `calculate_…`, `show_…`, `check_…`
- **Descriptive but short:** `cf` ❌ (unclear), `calculate_the_entire_fuel_requirement_of_the_mission` ❌ (too long)

> 💡 Well-named parameters help just as much: `calculate_cargo_space(length, width)` is more readable than `cs(l, w)`.
