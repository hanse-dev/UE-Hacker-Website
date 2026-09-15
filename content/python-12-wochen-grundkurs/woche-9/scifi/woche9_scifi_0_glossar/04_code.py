import json

# Datei schreiben
with open("schiff.txt", "w") as f:
    f.write("Enterprise\nKlasse: Galaxy\n")

# Datei lesen
with open("schiff.txt", "r") as f:
    inhalt = f.read()
print(inhalt)

# JSON speichern
schiff = {"name": "Enterprise", "crew": 150}
with open("schiff.json", "w") as f:
    json.dump(schiff, f)

# JSON einlesen
with open("schiff.json", "r") as f:
    geladen = json.load(f)
print(geladen["name"])  # Enterprise
