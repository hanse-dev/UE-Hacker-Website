date = "Mar 15"
entries = ["Groomed Storm", "Rode to the forest", "Finished jump training"]
with open("diary.txt", "w") as f:
    for entry in entries:
        f.write(date + " " + entry + "\n")
with open("diary.txt", "r") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
print(f"First line: {lines[0].strip()}")
