"""### ⭐⭐⭐⭐☆ Boss Quest 1: The Spell Generator

Build a system that automatically generates spells with element, tier and power and stores them in a spellbook.

**Step 1 – Generate spell names:**
Write a function `generate_spell_name(element_type, tier)` that forms a name from element and tier (e.g. `\"FIRE-T3\"`) and return the name as a string

**Step 2 – Calculate spell power:**
Create a function `calculate_power(complexity, element_type)` that returns a value between 0 and 100 and use different factors per `element_type` (e.g. Fire stronger, Water balanced, Earth defensive)

**Step 3 – Create spell data:**
Write a function `create_spell(element_type, tier, complexity)` that returns a dictionary with name, element, tier and power and use your two previous functions

**Step 4 – Manage spellbook:**
Create a list `spellbook` and write a function `save_spell(book, spell)` that appends the spell

**Step 5 – Use the generator:**
Generate at least 5 different spells in the main section and save them in the spellbook and print a small statistic (count, average power)

**Bonus:** Add a function that prints all spells sorted by power."""
