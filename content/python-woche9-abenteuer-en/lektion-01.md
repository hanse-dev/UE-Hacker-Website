# ⚔️ Archive Spell 1: Writing and reading files

Welcome to the **great scriptorium of Pyralia**! Scrolls and books are stored here that are never lost. The scribe says: *"What only lives in the computer's head is gone when it switches off. What is written on a scroll stays forever."*

With **`open()`** you open a file. The **mode** says what you plan to do: `"w"` = write (overwrites!), `"r"` = read.

```python
with open("quest_log.txt", "w") as f:      # open the file for writing
    f.write("Pyralia Quest Log\n")           # \n = new line

with open("quest_log.txt", "r") as f:      # open the file for reading
    content = f.read()              # the whole content as text
print(content)
```

**Step by step:**
1. **`with open(name, mode) as f:`** opens the file and closes it **automatically** at the end of the block
2. **`f.write(text)`** writes text – you must add a line break yourself with `\n`
3. **`f.read()`** returns the whole content as one text

> ⚠️ In mode `"w"` you can only write, in mode `"r"` only read – and `"w"` **erases** the old content.
