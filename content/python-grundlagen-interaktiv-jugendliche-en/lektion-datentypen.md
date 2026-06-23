# Data Types

Every value has a type. Python detects it automatically (dynamic typing).

| Type    | Example         | Meaning              |
|---------|-----------------|----------------------|
| `int`   | `42`            | Integer              |
| `float` | `3.14`          | Decimal number       |
| `str`   | `"Hello"`       | Text                 |
| `bool`  | `True`, `False` | Boolean value        |

Use `type()` to check the type. Use `int()`, `str()`, `float()` to convert between types.

```python
age = "18"
print(type(age))        # str
print(type(int(age)))   # int
```
