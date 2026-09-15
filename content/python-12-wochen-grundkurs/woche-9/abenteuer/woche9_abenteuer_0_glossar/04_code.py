import json

# Datei schreiben
with open("held.txt", "w") as f:
    f.write("Aria\nLevel 5\n")

# Datei lesen
with open("held.txt", "r") as f:
    inhalt = f.read()
print(inhalt)

# JSON speichern
held = {"name": "Aria", "level": 5}
with open("held.json", "w") as f:
    json.dump(held, f)

# JSON einlesen
with open("held.json", "r") as f:
    geladen = json.load(f)
print(geladen["name"])  # Aria
