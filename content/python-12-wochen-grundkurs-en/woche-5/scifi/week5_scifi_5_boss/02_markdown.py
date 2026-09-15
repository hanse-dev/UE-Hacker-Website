"""### ⭐⭐⭐⭐☆ Boss Quest 1: The Protocol Generator

Create a system that automatically generates, rates and manages system protocols in a small database.

**Step 1 – Create protocol names:**
Write a function `generate_protocol_name(system_type, security_level)` that builds a name from type and level (e.g. `\"SEC-ALARM-L3\"`) and return the name as a string

**Step 2 – Calculate efficiency:**
Create a function `calculate_efficiency(complexity, system_type)` that returns a value between 0 and 100 and use different factors per `system_type` (e.g. `\"Alarm\"`, `\"Scan\"`, `\"Log\"`)

**Step 3 – Create protocol data:**
Write a function `create_protocol(system_type, security_level, complexity)` that returns a dictionary with name, type, level and efficiency and use your two previous functions

**Step 4 – Save and find protocols:**
Create a list `protocols` and write a function `save_protocol(list_, protocol)` that appends the protocol

**Step 5 – Build generator system:**
Generate at least 5 different protocols and save them in the list and print a small statistic (count, average efficiency)

**Bonus:** Add a function that prints protocols sorted by efficiency."""
