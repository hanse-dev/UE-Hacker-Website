import os

with open("aufraeumen.txt", "w") as f:
    f.write("Test")
os.remove("aufraeumen.txt")
print(f"Gelöscht: {not os.path.exists('aufraeumen.txt')}")
