date = "Mar 15"
with open("diary.txt", "w") as f:
    f.write(date + " Entered the dragon cave\n")
    f.write(date + " Found the gold crown\n")
    f.write(date + " Defeated the troll\n")
number = 0
with open("diary.txt", "r") as f:
    for line in f:
        number += 1
        print(f"{number}: {line.strip()}")
