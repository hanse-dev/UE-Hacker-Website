date = "Day 42"
with open("diary.txt", "w") as f:
    f.write(date + " Signal received\n")
    f.write(date + " Probe launched\n")
    f.write(date + " Hull repaired\n")
number = 0
with open("diary.txt", "r") as f:
    for line in f:
        number += 1
        print(f"{number}: {line.strip()}")
