import os

with open("bordbuch.txt", "w") as f:
    f.write("Bordbuch Nebula-7\n")
print(f"Vorhanden: {os.path.exists('bordbuch.txt')}")
os.remove("bordbuch.txt")
print(f"Vorhanden: {os.path.exists('bordbuch.txt')}")
