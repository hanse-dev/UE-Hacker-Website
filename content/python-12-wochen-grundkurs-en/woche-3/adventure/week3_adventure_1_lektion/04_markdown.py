"""## Important Operators

### Assignment vs Comparison: = vs ==

**This is a crucial difference!**

- **`=` (single equals sign)**: Assigns a value to a variable
  ```python
  level = 10  # Assign the value 10 to level
  ```

- **`==` (double equals sign)**: Compares two values for equality
  ```python
  if level == 10:  # Check WHETHER level is 10
      print(\"Level 10 reached!\")
  ```

### The Four Comparison Runes

- **`<` (less than)**: Checks if the left value is smaller
  ```python
  if level < 10:
      print(\"Not yet Level 10\")
  ```

- **`<=` (less than or equal)**: Checks if the left value is smaller or equal
  ```python
  if level <= 10:
      print(\"Level 10 or lower\")
  ```

- **`>` (greater than)**: Checks if the left value is larger
  ```python
  if level > 10:
      print(\"Above Level 10!\")
  ```

- **`>=` (greater than or equal)**: Checks if the left value is larger or equal
  ```python
  if level >= 10:
      print(\"Level 10 or higher\")
  ```

**Remember:** Always use `==` for comparisons in conditions, never `=`!"""
