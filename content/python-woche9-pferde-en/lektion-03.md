# 🐴 Exercise 3: When the file is missing

If you try to read a file that does not exist, you get a **FileNotFoundError**. You know that from week 8: catch it with `try`/`except`.

```python
try:
    with open("missing.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("File missing")

import os
print(os.path.exists("stable_book.txt"))   # True or False
os.remove("stable_book.txt")               # delete the file
```

With **`os.path.exists(name)`** you ask beforehand whether the file exists. The module **`os`** comes ready-made like `math` and `random` from week 7.
