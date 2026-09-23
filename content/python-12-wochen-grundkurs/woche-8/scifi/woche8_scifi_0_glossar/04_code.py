# Dictionary erstellen
schiff = {"name": "Enterprise", "crew": 150, "klasse": "Galaxy"}

# Zugriff
print(schiff["name"])            # Enterprise
print(schiff.get("waffen", 0))   # 0 (Standardwert)

# Ändern und löschen
schiff["crew"] = 160
schiff.pop("klasse")

# Iteration
for schlüssel, wert in schiff.items():
    print(schlüssel, "→", wert)

# Tupel
koordinate = (10, 20)
x, y = koordinate
print(x, y)  # 10 20
