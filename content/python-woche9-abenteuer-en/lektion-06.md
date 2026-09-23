# ⚔️ Archive Spell 6: CSV tables: writer and reader

**CSV** stores a table as text: one line per table row, columns separated by commas. The module **`csv`** does the splitting for you:

```python
import csv

with open("heroes.csv", "w", newline="") as f:     # newline="" prevents empty lines
    writer = csv.writer(f)
    writer.writerow(["name", "level"])          # header row
    writer.writerow(["Aria", 15])

with open("heroes.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)                  # skip the first row
    for row in reader:
        print(row[0], row[1])               # each row is a list
```

> ⚠️ When reading, **all values are text**, even numbers! `"15"` is a string – for calculations you need `int(row[1])`.
