"""### ⭐⭐⭐☆☆ Mission 2: The JSON Converter

Create a JSON conversion system!

**Step 1 – Ship data as dictionary:**
Create a dictionary `ship` with e.g. `name`, `type_`, `crew`, `systems` (list of strings) and print the dictionary

**Step 2 – JSON export:**
Import `json` and save `ship` with `with open(\"ship.json\", \"w\") as f: json.dump(ship, f, indent=2)` to a file and print a confirmation

**Step 3 – JSON import:**
Load the file with `with open(\"ship.json\", \"r\") as f: data = json.load(f)` and store the result in a variable and check whether `data[\"name\"]` exists; print the name

**Step 4 – Short statistics:**
Create a simple statistic from the loaded data (e.g. crew count, number of systems) and print it

**Bonus:** Check before loading whether certain keys are present (simple \"validation\")."""
