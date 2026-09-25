date = "Day 42"
with open("diary.txt", "w") as f:
    f.write(date + " Signal received\n")
    f.write(date + " Probe launched\n")
    f.write(date + " Hull repaired\n")

entry = input()
with open("diary.txt", "a") as f:
    f.write(date + " " + entry + "\n")

with open("diary.txt") as f:
    lines = f.readlines()
print(f"Entries: {len(lines)}")
