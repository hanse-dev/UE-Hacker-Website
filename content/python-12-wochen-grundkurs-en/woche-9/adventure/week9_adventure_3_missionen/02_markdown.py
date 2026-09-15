"""### ⭐⭐☆☆☆ Mission 1: The Quest Logger

Create your first quest logging system!

**Step 1 – Write the quest log:**
Open a file (e.g. `quest_log.txt`) with `with open(..., \"w\")`, write at least 3 lines (quest status) into it, and print a confirmation

**Step 2 – Timestamp:**
Use the `datetime` module and append a new entry with a timestamp to the file using mode `\"a\"`, then print the sample entry

**Step 3 – Log level:**
Write entries tagged with `[INFO]`, `[WARN]` or `[ERROR]`, then read the whole file back in and print its contents

**Step 4 – Filter function:**
Write a function `filter_level(filename, level)` that returns only the lines with that log level, and call it and print the result

**Example code:** `with open(\"quest_log.txt\", \"w\") as f: f.write(...)`, `datetime.now()` for the timestamp.

**Bonus:** Add simple rotation (start a new file once a size limit is reached)."""
