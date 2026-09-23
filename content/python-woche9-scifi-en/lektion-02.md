# 🚀 Data Log 2: Reading line by line and appending

With bigger files you go **line by line** – the file itself is a loop:

```python
with open("ship_log.txt", "r") as f:
    for line in f:
        print(line.strip())        # strip() removes the \n at the end

with open("ship_log.txt", "a") as f:     # "a" = append, nothing is erased
    f.write("Update: Probe launched\n")

parts = "Nova,4".split(",")   # split text at commas: ["Nova", "4"]
```

| Mode | Meaning |
|---|---|
| `"r"` | read |
| `"w"` | write, **overwrites** the file |
| `"a"` | append to the end |

`f.readlines()` returns all lines at once as a **list**.
