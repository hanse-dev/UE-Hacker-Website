date = "Day 42"
with open("diary.txt", "w") as f:
    f.write(date + " Signal received\n")
    f.write(date + " Probe launched\n")
    f.write(date + " Hull repaired\n")
with open("diary.txt", "a") as f:
    f.write(date + " Energy cell charged\n")
with open("diary.txt", "r") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
print(f"Last: {lines[-1].strip()}")
