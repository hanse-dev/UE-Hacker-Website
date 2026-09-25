date = "Mar 15"
with open("diary.txt", "w") as f:
    f.write(date + " Groomed Storm\n")
    f.write(date + " Rode to the forest\n")
    f.write(date + " Finished jump training\n")

entry = input()
with open("diary.txt", "a") as f:
    f.write(date + " " + entry + "\n")

with open("diary.txt") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
