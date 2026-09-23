# 🐴 Exercise 5: JSON files: dump and load

With **`json.dump(data, file)`** you write straight into a file, with **`json.load(file)`** you read it back:

```python
import json

with open("horse.json", "w") as f:
    json.dump(horse, f, indent=2)   # indent makes the file readable

with open("horse.json", "r") as f:
    loaded = json.load(f)
```

**Changing and saving** always takes three steps: **load → change → save again**. Whole lists of dictionaries fit in a JSON file, too.

> 💡 By default `json.dump` writes umlauts like `\u00e4` – when loading, you still get the “ä” back.
