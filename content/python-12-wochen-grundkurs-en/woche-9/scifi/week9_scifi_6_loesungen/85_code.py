import json
quests = [
    {"name": "Locate the signal", "difficulty": 1, "status": "open"},
    {"name": "Launch the probe", "difficulty": 2, "status": "open"},
    {"name": "Repair the hull", "difficulty": 3, "status": "open"},
]
quests[0]["status"] = "done"
with open("questlog.json", "w") as f:
    json.dump(quests, f)
with open("questlog.json", "r") as f:
    loaded = json.load(f)
finished = 0
for quest in loaded:
    if quest["status"] == "done":
        finished += 1
with open("report.txt", "w") as f:
    f.write(f"Completed: {finished}\n")
with open("report.txt", "r") as f:
    content = f.read()
print(f"Report: {content.strip()}")
