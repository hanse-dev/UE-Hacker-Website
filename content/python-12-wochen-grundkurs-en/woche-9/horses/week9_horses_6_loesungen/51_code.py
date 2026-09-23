with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
    f.write("Status: Open\n")
    f.write("Ride planned\n")
with open("stable_book.txt", "a") as f:
    f.write("Update: Tournament won\n")
with open("stable_book.txt", "r") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"Last: {lines[-1].strip()}")
