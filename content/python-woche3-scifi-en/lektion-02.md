# 📟 Important Operators

## Assignment vs comparison: `=` vs `==`

**This is a crucial difference!**

- **`=` (one equals sign)** assigns a value to a variable:
  ```python
  level = 10      # store the value 10 in level
  ```
- **`==` (two equals signs)** compares two values for equality:
  ```python
  if level == 10:     # check WHETHER level is 10
      print("Access level 10 reached!")
  ```

## The four comparison algorithms

| Operator | Meaning | Example |
|---|---|---|
| `<` | less than | `energy < 20` |
| `<=` | less than or equal | `temperature <= 100` |
| `>` | greater than | `speed > 1000` |
| `>=` | greater than or equal | `shield_strength >= 50` |

There is also `!=` for "not equal". A comparison gives you a Boolean: `True` or `False`.

**Remember:** Always use `==` for comparisons in conditions, never `=`!
