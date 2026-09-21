date = "Mar 15"
entries = ["Entered the dragon cave", "Found the gold crown", "Defeated the troll"]
with open("diary.txt", "w") as f:
    for entry in entries:
        f.write(date + " " + entry + "\n")
with open("diary.txt", "r") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
print(f"First line: {lines[0].strip()}")
