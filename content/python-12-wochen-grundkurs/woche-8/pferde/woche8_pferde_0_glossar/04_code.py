# Dictionary erstellen
pferd = {"name": "Bobby", "alter": 5, "rasse": "Haflinger"}

# Zugriff
print(pferd["name"])           # Bobby
print(pferd.get("gewicht", 0)) # 0 (Standardwert)

# Ändern und löschen
pferd["alter"] = 6
pferd.update({"rasse": "Andalusier"})
pferd.pop("rasse")

# Iteration
for schlüssel, wert in pferd.items():
    print(schlüssel, "→", wert)

# Tupel
koordinate = (10, 20)
x, y = koordinate
print(x, y)  # 10 20
