# Dictionaries

Dictionaries store key-value pairs. Access by key, not by index.

```python
user = {
    "name": "Alex",
    "age": 16,
    "premium": True
}
print(user["name"])
user["points"] = 1500
print(user)
```

Useful: `.keys()`, `.values()`, `.items()`, `.get(key, default)`
