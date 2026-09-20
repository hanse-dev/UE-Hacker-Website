# 🗂️ Collection Spell 6: Sorting

```python
numbers = [5, 2, 8, 1]
numbers.sort()                      # changes the list: [1, 2, 5, 8]
descending = sorted(numbers, reverse=True)  # new copy: [8, 5, 2, 1]
numbers.reverse()                   # flip the order
```

- **`list.sort()`** sorts the list **itself** (numbers ascending, text alphabetically)
- **`sorted(list)`** returns a **sorted copy** – the original stays as it is
- **`reverse=True`** sorts **descending**: `sort(reverse=True)`
- **`list.reverse()`** just flips the current order (without sorting)
- **`sorted(list, key=len)`** sorts by the **length** of the entries (shortest first) instead of alphabetically

> ⚠️ It is **`reverse=True`** – do not write just `reverse` in the parentheses.
