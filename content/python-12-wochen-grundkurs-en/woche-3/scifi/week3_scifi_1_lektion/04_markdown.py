"""## Important Operators

### Assignment vs Comparison: = vs ==

**This is a crucial difference!**

- **`=` (one equals sign)**: Assigns a value to a variable
  ```python
  level = 10  # Assign the value 10 to level
  ```

- **`==` (two equals signs)**: Compares two values for equality
  ```python
  if level == 10:  # Check WHETHER level is 10
      print(\"Access level 10 reached!\")
  ```

### The Four Comparison Algorithms

- **`<` (less than)**: Checks if the left value is smaller
  ```python
  if energy < 20:
      print(\"⚠️ Low energy!\")
  ```

- **`<=` (less than or equal)**: Checks if the left value is smaller or equal
  ```python
  if temperature <= 100:
      print(\"🌡️ Normal temperature!\")
  ```

- **`>` (greater than)**: Checks if the left value is larger
  ```python
  if speed > 1000:
      print(\"💨 Faster than light!\")
  ```

- **`>=` (greater than or equal)**: Checks if the left value is larger or equal
  ```python
  if shield_strength >= 50:
      print(\"🛡️ Shields stable!\")
  ```

**Remember:** Always use `==` for comparisons in conditions, never `=`!"""
