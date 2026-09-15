planets = ["Mars", "Venus", "Jupiter", "Venus"]

# Manage elements
planets.append("Saturn")
planets.insert(1, "Neptune")
planets.remove("Venus")  # First occurrence

# Search and count
print(planets.index("Jupiter"))  # Position
print(planets.count("Venus"))    # 1 (one still remaining)
print("Mars" in planets)         # True

# Sort
print(sorted(planets))

# enumerate
for i, planet in enumerate(planets):
    print(i, planet)

# break and continue
for planet in planets:
    if planet == "Neptune":
        continue   # skip Neptune
    if planet == "Saturn":
        break      # stop at Saturn
    print(planet)
