# 🐴 Exercise 1: Writing and reading files

Welcome to the **stable office of the riding farm**! Stable book and filing cabinet are kept here so that nothing gets lost. The stable master says: *"What only lives in the computer's head is gone when it switches off. What is in the stable book stays forever."*

With **`open()`** you open a file. The **mode** says what you plan to do: `"w"` = write (overwrites!), `"r"` = read.

```python
with open("stable_book.txt", "w") as f:      # open the file for writing
    f.write("Stable book of the farm\n")           # \n = new line

with open("stable_book.txt", "r") as f:      # open the file for reading
    content = f.read()              # the whole content as text
print(content)
```

**Step by step:**
1. **`with open(name, mode) as f:`** opens the file and closes it **automatically** at the end of the block
2. **`f.write(text)`** writes text – you must add a line break yourself with `\n`
3. **`f.read()`** returns the whole content as one text

> ⚠️ In mode `"w"` you can only write, in mode `"r"` only read – and `"w"` **erases** the old content.
