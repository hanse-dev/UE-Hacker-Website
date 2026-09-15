"""### ⭐⭐⭐⭐☆ Mission 3: The Rune Forge

The final trial: forge a rune key and find the right hour to finally open the archive.

**Step 1 – Rune alphabet:**
Build an alphabet from `string.ascii_letters` and `string.digits` (joined together) and print it

**Step 2 – Forge the rune key:**
Use a loop or a list comprehension to draw 8 random characters from your alphabet (with `random.choice()`) and join them with `\"\".join()` into a key

**Step 3 – The right hour:**
Check with `datetime.now().hour` whether it's currently day (6–18) or night, and print a matching message

**Step 4 – Open the archive:**
Combine the rune key and the time-of-day message into a closing message (e.g. \"The archive opens for you!\")

**Bonus:** Use `random.seed()` before step 2 to generate the same rune key reproducibly – a trick real archivists use for testing."""
