with open("bordbuch.txt", "w") as f:
    f.write("Bordbuch Nebula-7\n")
with open("bordbuch.txt", "r") as f:
    inhalt = f.read()
print(f"Inhalt: {inhalt.strip()}")
