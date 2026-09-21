date = "Mar 15"
with open("diary.txt", "w") as f:
    f.write(date + " Entered the dragon cave\n")
    f.write(date + " Found the gold crown\n")
    f.write(date + " Defeated the troll\n")
with open("diary.txt", "a") as f:
    f.write(date + " Rested by the campfire\n")
with open("diary.txt", "r") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
print(f"Last: {lines[-1].strip()}")
