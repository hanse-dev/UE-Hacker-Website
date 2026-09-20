# 🚀 Data Log 4: JSON text: dumps and loads

**JSON** is a text format that looks almost like a Python dictionary. Almost every program in the world understands it. The module **`json`** translates in both directions:

```python
import json

member = {"name": "Nova", "rank": 4}
text = json.dumps(member)      # dictionary → JSON text (string)
back = json.loads(text)         # JSON text → dictionary
print(back["name"])             # Nova
```

**Memory aid:** the **s** in `dumps`/`loads` stands for **string**. The versions without s (`dump`/`load`) work with files – those come in the next lesson.

> 💡 JSON has **no tuples**: `(3, 4)` becomes the **list** `[3, 4]` when read back. A value `True` becomes `true` in the text.
