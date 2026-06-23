# Dictionaries

Dictionaries speichern Schlüssel-Wert-Paare. Zugriff über Schlüssel, nicht über Index.

```python
user = {
    "name": "Alex",
    "alter": 16,
    "premium": True
}
print(user["name"])
user["punkte"] = 1500
print(user)
```

Nützlich: `.keys()`, `.values()`, `.items()`, `.get(key, default)`
