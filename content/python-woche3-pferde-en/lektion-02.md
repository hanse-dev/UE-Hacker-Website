# 🐴 Lesson 2: Comparison Operators

Conditions often compare two values. Python has six comparison operators, and each gives back `True` or `False`:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal to | `age == 10` |
| `!=` | not equal to | `age != 10` |
| `<` | less than | `age < 5` |
| `<=` | less than or equal | `age <= 5` |
| `>` | greater than | `age > 15` |
| `>=` | greater than or equal | `age >= 3` |

## ⚠️ `=` versus `==`

This is the classic mistake:

- **`=`** (one equals sign) **assigns** a value: `age = 10`
- **`==`** (two equals signs) **compares** two values: `if age == 10:`

In a condition you always need `==` (or another comparison operator), never `=`!

You can even print the result of a comparison:

```python
height = 160
print(f"{height} < 165: {height < 165}")
```
