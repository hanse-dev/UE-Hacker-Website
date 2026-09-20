# 📖 Lesson 7: Docstrings and good names

A good rider keeps a **training diary**. In Python that is a **docstring**: a text in triple quotes right below the `def` line.

```python
def calculate_feed(horses):
    """Calculates the daily amount of feed."""
    return horses * 8

print(calculate_feed.__doc__)
```

`calculate_feed.__doc__` (without parentheses) shows the docstring. That way others – and you yourself in a month – immediately understand what the routine does.

**Good names:**
- **Lowercase with underscores:** `calculate_feed` ✅ – not `CalculateFeed` ❌
- **A verb that says what happens:** `calculate_…`, `show_…`, `check_…`
- **Descriptive but short:** `cf` ❌ (unclear), `calculate_the_whole_daily_amount_of_feed` ❌ (too long)

> 💡 Well-named parameters help just as much: `calculate_area(length, width)` is more readable than `ar(l, w)`.
