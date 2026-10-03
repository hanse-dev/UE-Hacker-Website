date = "Mar 15"
with open("diary.txt", "w") as f:
    f.write(date + " Entered the dragon cave\n")
    f.write(date + " Found the gold crown\n")
    f.write(date + " Defeated the troll\n")

entry = input()
with open("diary.txt", "a") as f:
    f.write(date + " " + entry + "\n")

with open("diary.txt") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
