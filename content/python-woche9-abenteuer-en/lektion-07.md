# ⚔️ Archive Spell 7: CSV with DictReader and switching formats

With **`DictWriter`** and **`DictReader`** you work with **column names** instead of positions – each row is a dictionary from week 8:

```python
import csv

fields = ["name", "class", "level", "hp"]
with open("heroes.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()               # writes the header row
    w.writerows(heroes)           # list of dictionaries

with open("heroes.csv", "r") as f:
    for row in csv.DictReader(f):
        print(row["name"])         # access by column name
```

**Switching formats:** JSON and CSV hold the same data in different forms. You read in one format (a list of dictionaries in memory) and write out in the other. Remember: from CSV all values come as text – convert numbers with `int()`.
