# 🚀 Data Log 1: Writing and reading files

Welcome to the **data store of space station Nebula-7**! The ship AI says: *"What only lives in working memory is gone when the station shuts down. What is written to a file stays forever."*

With **`open()`** you open a file. The **mode** says what you plan to do: `"w"` = write (overwrites!), `"r"` = read.

```python
with open("ship_log.txt", "w") as f:      # open the file for writing
    f.write("Ship log Nebula-7\n")           # \n = new line

with open("ship_log.txt", "r") as f:      # open the file for reading
    content = f.read()              # the whole content as text
print(content)
```

**Step by step:**
1. **`with open(name, mode) as f:`** opens the file and closes it **automatically** at the end of the block
2. **`f.write(text)`** writes text – you must add a line break yourself with `\n`
3. **`f.read()`** returns the whole content as one text

> ⚠️ In mode `"w"` you can only write, in mode `"r"` only read – and `"w"` **erases** the old content.
