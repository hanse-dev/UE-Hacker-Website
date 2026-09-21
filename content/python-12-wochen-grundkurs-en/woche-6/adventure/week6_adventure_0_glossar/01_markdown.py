"""# 📖 Glossary – 🗡️ Week 6 – Lists: The Treasure Vault of Collections
> You can keep this notebook open all week.

| Term | Meaning | Example |
|------|---------|--------|
| **List** `[]` | Ordered collection of values | `[\"Aria\", \"Borin\", \"Lena\"]` |
| `.append()` | Add an element to the end of a list | `list_.append(\"new\")` |
| **Index** | Position of an element in the list (starts at 0) | `list_[0]` → first element |
| `len()` | Number of elements in a list | `len([1, 2, 3])` → `3` |
| `.insert()` | Insert an element at a specific position | `list_.insert(1, \"x\")` |
| `.remove()` | Remove the first occurrence of an element | `list_.remove(\"x\")` |
| `.pop()` | Remove and return the last (or a specific) element | `list_.pop()` |
| `.index()` | Find the position of an element | `list_.index(\"x\")` |
| `.count()` | How many times an element appears | `list_.count(\"x\")` |
| `in` | Check whether an element is in the list | `\"x\" in list_` |
| `.sort()` | Sort the list in ascending order (modifies the list) | `list_.sort()` |
| `sorted()` | Return a sorted copy (original stays unchanged) | `sorted(list_)` |
| `.reverse()` | Reverse the order of the list | `list_.reverse()` |
| `enumerate()` | Get index and value at the same time when iterating | `for i, x in enumerate(list_):` |
| `break` | Exit the loop immediately | `if x == 5: break` |
| `continue` | Skip the current round and move on to the next | `if x == 0: continue` |
| `set` | A set – like a list but without duplicates and without a fixed order | `set([1,1,2])` → `{1, 2}` |
| **Algorithm** | A step-by-step solution – like a recipe for the computer | `for x in list_: if x > max: max = x` |
| **List Comprehension** | Short syntax to build a new list from an existing one | `[x for x in list_ if x > 5]` |"""