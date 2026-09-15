heroes = ["Aria", "Borin", "Lena", "Borin"]

# Manage elements
heroes.append("Mira")
heroes.insert(1, "Zara")
heroes.remove("Borin")  # First occurrence

# Search and count
print(heroes.index("Lena"))   # Position
print(heroes.count("Borin"))  # 1 (one still remaining)
print("Aria" in heroes)       # True

# Sorting
print(sorted(heroes))

# enumerate
for i, hero in enumerate(heroes):
    print(i, hero)

# break and continue
for hero in heroes:
    if hero == "Zara":
        continue   # skip Zara
    if hero == "Mira":
        break      # stop at Mira
    print(hero)
