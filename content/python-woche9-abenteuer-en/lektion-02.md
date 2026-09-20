# ⚔️ Archive Spell 2: Reading line by line and appending

With bigger files you go **line by line** – the file itself is a loop:

```python
with open("quest_log.txt", "r") as f:
    for line in f:
        print(line.strip())        # strip() removes the \n at the end

with open("quest_log.txt", "a") as f:     # "a" = append, nothing is erased
    f.write("Update: Treasure found\n")

parts = "Aria,15".split(",")   # split text at commas: ["Aria", "15"]
```

| Mode | Meaning |
|---|---|
| `"r"` | read |
| `"w"` | write, **overwrites** the file |
| `"a"` | append to the end |

`f.readlines()` returns all lines at once as a **list**.
