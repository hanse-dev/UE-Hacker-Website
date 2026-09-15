"""### ⭐⭐⭐⭐☆ Boss Quest 1: The Data Generator

Build a system that automatically generates, filters, and sorts datasets.

**Step 1 – Generate dataset:**
Write a function `generate_dataset(data_type, complexity)` that returns a list with a few entries (e.g. names or IDs depending on the type) and use `data_type` and `complexity` to control the number or kind of entries

**Step 2 – Calculate statistics:**
Create a function `calculate_statistics(data_list)` that returns the length and optionally min/max or average and return the values as a dictionary or as printed lines

**Step 3 – Create multiple datasets:**
Create a list `data` and use a loop to add at least 10 datasets (e.g. with `generate_dataset(\"sensor\", i)` for different i) and use `append()` to add each dataset to the list

**Step 4 – Filter and sort data:**
Write a function `filter_data(data_list, search_term)` that returns only entries containing the search term (e.g. using `in` or string comparison) and sort the filtered or entire list with `sort()` or `sorted()` and print the result

**Step 5 – Assemble the generator:**
Call all functions in the main part: generate datasets, print statistics, filter, sort and print a short summary (count, statistics, filtered count)

**Bonus:** Add random attributes (e.g. using `random`) and validate the data (check for correctness)."""
