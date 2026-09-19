"""## Collection Spell 5: List Comprehension – Building Lists in One Go

Often you want to turn a list into a **new** list: change all values or keep only some. With a loop and `append()` that takes several lines. A **list comprehension** does it in one:

```python
new_list = [expression for element in list_]              # transform every element
new_list = [element for element in list_ if condition]    # keep only matching ones
```

Read it from left to right: *"Take `expression` for every `element` in `list_` (if `condition` is true)."*

**Important:** The original list stays unchanged – you always get a new list."""