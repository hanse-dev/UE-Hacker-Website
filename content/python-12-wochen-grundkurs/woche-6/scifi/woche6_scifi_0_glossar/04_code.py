planeten = ["Mars", "Venus", "Jupiter", "Venus"]

# Elemente verwalten
planeten.append("Saturn")
planeten.insert(1, "Neptun")
planeten.remove("Venus")  # Erstes Vorkommen

# Suchen und zählen
print(planeten.index("Jupiter"))  # Position
print(planeten.count("Venus"))    # 1 (noch eines übrig)
print("Mars" in planeten)         # True

# Sortieren
print(sorted(planeten))

# enumerate
for i, planet in enumerate(planeten):
    print(i, planet)

# break und continue
for planet in planeten:
    if planet == "Neptun":
        continue   # Neptun überspringen
    if planet == "Saturn":
        break      # bei Saturn aufhören
    print(planet)
