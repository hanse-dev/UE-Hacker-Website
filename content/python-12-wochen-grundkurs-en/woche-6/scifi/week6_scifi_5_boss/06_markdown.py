"""### ⭐⭐⭐⭐☆ Boss Quest 3: The Mission Database

Manage missions in a list: create, search, filter, and analyze.

**Step 1 – Create mission:**
Create a function `create_mission(name, target, priority)` that returns a dictionary with keys \"name\", \"target\", \"priority\" (and optionally \"status\") and return the dictionary with `return`

**Step 2 – Add mission to list:**
Create a list `missions` and write a function `add_mission(mission, mission_list)` that adds the mission to the list using `append()` and returns or prints a short confirmation

**Step 3 – Search missions:**
Write a function `search_missions(mission_list, search_term)` that returns all missions whose name or target contains the search term (e.g. using `in`) and return the found list

**Step 4 – Filter by status:**
Create a function `filter_by_status(mission_list, status)` that returns only missions with the given status (e.g. \"active\", \"completed\") and return the filtered list

**Step 5 – Print statistics:**
Write a function `mission_statistics(mission_list)` that calculates and prints the number of missions and optionally the distribution by priority or status and call all functions in the main part: create missions, add, search, filter, print statistics

**Bonus:** Add a field \"result\" or \"success\" to each mission and print a success statistic."""
