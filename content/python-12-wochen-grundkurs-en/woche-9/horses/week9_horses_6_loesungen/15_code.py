import os

with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
print(f"Exists: {os.path.exists('stable_book.txt')}")
os.remove("stable_book.txt")
print(f"Exists: {os.path.exists('stable_book.txt')}")
