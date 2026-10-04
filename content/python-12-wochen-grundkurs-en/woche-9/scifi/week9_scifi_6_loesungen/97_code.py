import os

with open("cleanup.txt", "w") as f:
    f.write("Test")
os.remove("cleanup.txt")
print(f"Deleted: {not os.path.exists('cleanup.txt')}")
