import json

# Datei schreiben
with open("pferd.txt", "w") as f:
    f.write("Bobby\n5 Jahre\n")

# Datei lesen
with open("pferd.txt", "r") as f:
    inhalt = f.read()
print(inhalt)

# JSON speichern
pferd = {"name": "Bobby", "alter": 5}
with open("pferd.json", "w") as f:
    json.dump(pferd, f)

# JSON einlesen
with open("pferd.json", "r") as f:
    geladen = json.load(f)
print(geladen["name"])  # Bobby
