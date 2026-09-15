horses = ["Bobby", "Blitz", "Moritz", "Blitz"]

# Managing elements
horses.append("Luna")
horses.insert(1, "Stella")
horses.remove("Blitz")  # First occurrence

# Searching and counting
print(horses.index("Moritz"))   # Position
print(horses.count("Blitz"))    # 1 (one still remaining)
print("Bobby" in horses)        # True

# Sorting
print(sorted(horses))

# enumerate
for i, horse in enumerate(horses):
    print(i, horse)

# break and continue
for horse in horses:
    if horse == "Stella":
        continue   # skip Stella
    if horse == "Luna":
        break      # stop at Luna
    print(horse)
