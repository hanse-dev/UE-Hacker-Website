# 🐴 Exercise 2: Reading line by line and appending

With bigger files you go **line by line** – the file itself is a loop:

```python
with open("stable_book.txt", "r") as f:
    for line in f:
        print(line.strip())        # strip() removes the \n at the end

with open("stable_book.txt", "a") as f:     # "a" = append, nothing is erased
    f.write("Update: Tournament won\n")

parts = "Blitz,8".split(",")   # split text at commas: ["Blitz", "8"]
```

| Mode | Meaning |
|---|---|
| `"r"` | read |
| `"w"` | write, **overwrites** the file |
| `"a"` | append to the end |

`f.readlines()` returns all lines at once as a **list**.
