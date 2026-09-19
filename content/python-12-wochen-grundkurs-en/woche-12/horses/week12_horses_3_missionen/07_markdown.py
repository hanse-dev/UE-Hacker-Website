"""### ⭐⭐⭐⭐☆ Mission 3: One-word commands

So far the game only understands two-word commands. If someone types `inventory`, they get the error message from `try/except`. That should get better!

**Step 1 – New commands:**
Extend `execute()`: for `"inventory"` it should run `player.show_inventory()`, for `"help"` a list of all commands should appear. You check both **before** the `try` block.

**Step 2 – Using items:**
Add the command `use` to the `if/elif` chain, which calls `player.use(target)`. For that you need the method from Mission 2!

**Step 3 – Test:**
Use `play(...)` to play through the commands `help`, `take Flashlight`, `inventory` and `dance wildly`.

**Bonus:** Make `help` independent of upper and lower case (`.lower()`)."""