with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
    f.write("Status: Open\n")
with open("stable_book.txt", "a") as f:
    f.write("Ride planned\n")
with open("stable_book.txt", "r") as f:
    for line in f:
        print(line.strip())
