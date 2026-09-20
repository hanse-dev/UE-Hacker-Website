# 🐴 Exercise 6: CSV tables: writer and reader

**CSV** stores a table as text: one line per table row, columns separated by commas. The module **`csv`** does the splitting for you:

```python
import csv

with open("horses.csv", "w", newline="") as f:     # newline="" prevents empty lines
    writer = csv.writer(f)
    writer.writerow(["name", "age"])          # header row
    writer.writerow(["Blitz", 8])

with open("horses.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)                  # skip the first row
    for row in reader:
        print(row[0], row[1])               # each row is a list
```

> ⚠️ When reading, **all values are text**, even numbers! `"8"` is a string – for calculations you need `int(row[1])`.
