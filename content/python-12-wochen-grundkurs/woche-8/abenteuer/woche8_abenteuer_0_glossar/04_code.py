# Dictionary erstellen
held = {"name": "Aria", "level": 5, "gold": 100}

# Zugriff
print(held["name"])          # Aria
print(held.get("xp", 0))    # 0 (Standardwert)

# Ändern und löschen
held["level"] = 6
held.pop("gold")

# Iteration
for schlüssel, wert in held.items():
    print(schlüssel, "→", wert)

# Tupel
koordinate = (10, 20)
x, y = koordinate
print(x, y)  # 10 20
