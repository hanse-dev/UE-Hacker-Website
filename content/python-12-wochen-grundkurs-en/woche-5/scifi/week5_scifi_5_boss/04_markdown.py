"""### ⭐⭐⭐⭐⭐ Boss Quest 2: The Space Station Manager

Build a system that manages the most important areas of a space station: sectors, energy and personnel.

**Step 1 – Create sectors:**
Create a function `create_sector(sector_id, size)` that returns a dictionary with ID, size and initial energy and set up a list with several sectors

**Step 2 – Distribute energy:**
Write a function `distribute_energy(sectors, total_energy)` that distributes energy proportionally to size and update the entries in the sector dictionaries

**Step 3 – Simplify shift planning:**
Create a function `plan_shifts(num_personnel, shifts)` that calculates a simple distribution (e.g. evenly) and return a list with personnel numbers per shift

**Step 4 – Generate station overview:**
Write a function `generate_station_report(sectors, energy, personnel)` that returns an overview as text and use information from the sectors, total energy and personnel count

**Bonus:** Add a simple emergency function that returns a warning when a sector has too little energy."""
