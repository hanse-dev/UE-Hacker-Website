# 📖 Spell Formula 3: Docstrings and good names

A good mage writes their spells into the **spell book**. In Python that is a **docstring**: a text in triple quotes right below the `def` line.

```python
def calculate_healing(base, multiplier):
    """Calculates the amount of healing."""
    return base * multiplier

print(calculate_healing.__doc__)
```

`calculate_healing.__doc__` (without parentheses) shows the docstring. That way others – and you yourself in a month – immediately understand what the formula does.

**Good names:**
- **Lowercase with underscores:** `calculate_damage` ✅ – not `CalculateDamage` ❌
- **A verb that says what happens:** `calculate_…`, `show_…`, `check_…`
- **Descriptive but short:** `cd` ❌ (unclear), `calculate_the_whole_damage_result` ❌ (too long)

> 💡 Well-named parameters help just as much: `calculate_damage(base, multiplier)` is more readable than `cd(b, m)`.
