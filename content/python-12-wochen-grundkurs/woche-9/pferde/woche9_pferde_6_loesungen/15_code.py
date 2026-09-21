import os

with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
print(f"Vorhanden: {os.path.exists('stallbuch.txt')}")
os.remove("stallbuch.txt")
print(f"Vorhanden: {os.path.exists('stallbuch.txt')}")
