"""## Important Operators

### Assignment vs Comparison: = vs ==

**This is a crucial difference!**

- **`=` (single equals sign)**: Assigns a value to a variable

```python
age = 10  # Assign the value 10 to age
```

- **`==` (double equals sign)**: Compares two values for equality

```python
if age == 10:  # Check WHETHER age is 10
    print(\"The horse is 10 years old!\")
```

### The Four Comparison Operators

- **`<` (less than)**: Checks if the left value is smaller

```python
if age < 5:
    print(\"Still a foal!\")
```

- **`<=` (less than or equal)**: Checks if the left value is smaller or equal

```python
if age <= 5:
    print(\"Young horse or foal!\")
```

- **`>` (greater than)**: Checks if the left value is larger

```python
if age > 15:
    print(\"An experienced horse!\")
```

- **`>=` (greater than or equal)**: Checks if the left value is larger or equal

```python
if age >= 3:
    print(\"Old enough to ride!\")
```

**Remember:** In conditions always use `==` for comparisons, never `=`!"""
