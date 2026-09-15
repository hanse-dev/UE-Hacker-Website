"""### ⭐⭐☆☆☆ Mission 1: The Data Logger

Create your first logging system!

**Step 1 – Write a log file:**
Open a file (e.g. `log.txt`) with `with open(\"log.txt\", \"w\") as f` and write at least 3 lines of text (e.g. system status messages) and use `f.write(\"...\\n\")` for each line

**Step 2 – Add timestamps:**
Import `datetime` and add date and time to each log entry (e.g. `datetime.now().strftime(\"%Y-%m-%d %H:%M\")`) and write the entries with timestamp to the file (mode `\"a\"` for append)

**Step 3 – Use log levels:**
Define entries with different levels: INFO, WARN, ERROR (e.g. as prefix in each line: `[INFO] System starting`) and write 2–3 entries with different levels to the file

**Step 4 – Filter function:**
Write a function `filter_level(filename, level)` that reads the file and returns only lines containing that level (e.g. `\"[INFO]\"` in the line) and call the function for one level and print the filtered lines

**Bonus:** Add a simple \"rotation\": e.g. create new file `log_old.txt` when the current one gets too large."""
