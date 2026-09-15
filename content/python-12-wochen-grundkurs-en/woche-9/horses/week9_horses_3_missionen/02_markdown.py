"""### ⭐⭐☆☆☆ Mission 1: The Horse Logger

Create your first horse logging system!

**Step 1 – Write a log file:**
Open a file (e.g. `stable_log.txt`) with `with open(\"stable_log.txt\", \"w\") as f`, write at least 3 lines (e.g. horse status, feeding times) with `f.write(\"...\\n\")`, and print a confirmation

**Step 2 – Add timestamps:**
Import `datetime`, add date and time to each entry, and append further entries using mode `\"a\"`, then print a sample entry

**Step 3 – Use log levels:**
Define entries with levels `[INFO]`, `[WARN]`, `[ERROR]` (e.g. `[INFO] Luna fed`), write 2–3 entries, then read the whole file back in with `open(..., \"r\")` and print its contents

**Step 4 – Filter function:**
Write a function `filter_level(filename, level)` that returns only the lines with that level, and call it and print the result

**Bonus:** Add simple rotation (start a new file once the old one gets too large)."""
