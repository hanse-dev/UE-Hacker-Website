date = "Mar 15"
with open("diary.txt", "w") as f:
    f.write(date + " Groomed Storm\n")
    f.write(date + " Rode to the forest\n")
    f.write(date + " Finished jump training\n")
with open("diary.txt", "a") as f:
    f.write(date + " Cleaned the hooves\n")
with open("diary.txt", "r") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
print(f"Last: {lines[-1].strip()}")
