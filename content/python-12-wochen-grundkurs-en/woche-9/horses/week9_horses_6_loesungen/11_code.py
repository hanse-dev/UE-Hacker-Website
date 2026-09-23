with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
    f.write("Status: Open\n")
    f.write("Ride planned\n")
with open("stable_book.txt", "r") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"First: {lines[0].strip()}")
