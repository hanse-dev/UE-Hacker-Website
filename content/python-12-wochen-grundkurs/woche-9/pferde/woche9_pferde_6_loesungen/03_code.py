with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
with open("stallbuch.txt", "r") as f:
    inhalt = f.read()
print(f"Inhalt: {inhalt.strip()}")
