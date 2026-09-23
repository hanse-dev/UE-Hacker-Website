date = "Mar 15"
with open("diary.txt", "w") as f:
    f.write(date + " Groomed Storm\n")
    f.write(date + " Rode to the forest\n")
    f.write(date + " Finished jump training\n")
number = 0
with open("diary.txt", "r") as f:
    for line in f:
        number += 1
        print(f"{number}: {line.strip()}")
