"""### ⭐⭐⭐⭐⭐ Boss Quest 2: The Stable Manager

Manage a complete stable with stalls, feed and riders across multiple functions.

**Step 1 – Create stalls:**
Create a function `create_stall(stall_id, size)` that returns a dictionary with ID, size and current feed amount and set up a list with several stalls

**Step 2 – Distribute feed:**
Write a function `distribute_feed(stalls, total_feed)` that distributes feed proportionally to size and update the feed entries in the stall dictionaries

**Step 3 – Plan shifts:**
Create a function `plan_stable_shifts(num_riders, shifts)` that calculates a simple distribution of riders across shifts and return a list with riders per shift

**Step 4 – Generate stable overview:**
Write a function `generate_stable_report(stalls, feed, riders)` that returns a summary as text and use information from the stalls and parameters

**Bonus:** Add a simple emergency function that returns a warning when a stall has too little feed."""
