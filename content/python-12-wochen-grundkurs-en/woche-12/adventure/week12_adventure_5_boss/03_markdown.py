"""### ⭐⭐⭐⭐☆ Boss Quest 1: The complete game state

The game state from the lesson has a weakness: it does not remember **which items are still lying in the rooms** and how much life the enemy has left. After loading, `Sword` would be back again!

**Step 1 – Saving:**
Write `save_full(player)`. The dictionary contains the player (as before) **and** the state of every room: the names and descriptions of its items as well as the HP of the enemy (or `None` if there is none).

**Step 2 – Loading:**
Write `load_full()`, which restores all rooms and returns the `Player`. If the file is missing, it should return `None`.

**Step 3 – Prove it:**
Let a player take `Sword`, save, deliberately wreck the contents of the room `"spring"`, load – and check that the room is right again.

**Bonus:** Also save how often the player has saved already."""