# 🚀 KI-Modul 5: __str__ und __repr__

**Magic Methods** haben zwei Unterstriche vor und nach dem Namen. Python ruft sie **von selbst** auf. `__init__` kennst du schon – jetzt kommen die für die **Textdarstellung**:

```python
class Roboter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __repr__(self):
        return f"Roboter('{self.name}', {self.level})"

k = Roboter("Nova", 5)
print(k)
print([k])
```

1. **`__str__`** liefert den Text für `print(objekt)` – mit **`return`**, nicht mit `print`!
2. **`__repr__`** ist die „Entwickler-Darstellung“; Python nutzt sie z. B. in Listen
3. Ohne `__str__` würde `print(k)` nur etwas wie `<__main__.Roboter object at 0x…>` zeigen
