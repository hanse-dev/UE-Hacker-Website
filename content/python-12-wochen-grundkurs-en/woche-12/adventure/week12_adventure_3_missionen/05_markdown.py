"""### ⭐⭐⭐☆☆ Mission 2: The healing item

The fight against the dragon is tough – a healing potion could help!

**Step 1 – Hide the item:**
Put an `Item("Potion", ...)` into the room `"spring"` (append it to the list `world["spring"]["items"]`).

**Step 2 – New method:**
Write a function `use(self, item_name)` that searches the inventory. If it is `"Potion"`, it raises `self.hp` by 10 and removes the item from the inventory. For other items a message should say that you can't do anything with them. If the item is missing, it also prints a message.

**Step 3 – Attach it to the class:**
With `Player.use = use` the function becomes a method of all players. Test it with a player whose `hp` you set to 5 beforehand.

**Bonus:** The healing item should fill the HP up to 20 at most."""