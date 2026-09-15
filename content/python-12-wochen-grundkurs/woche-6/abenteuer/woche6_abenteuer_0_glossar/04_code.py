helden = ["Aria", "Borin", "Lena", "Borin"]

# Elemente verwalten
helden.append("Mira")
helden.insert(1, "Zara")
helden.remove("Borin")  # Erstes Vorkommen

# Suchen und zählen
print(helden.index("Lena"))   # Position
print(helden.count("Borin"))  # 1 (noch eines übrig)
print("Aria" in helden)       # True

# Sortieren
print(sorted(helden))

# enumerate
for i, held in enumerate(helden):
    print(i, held)

# break und continue
for held in helden:
    if held == "Zara":
        continue   # Zara überspringen
    if held == "Mira":
        break      # bei Mira aufhören
    print(held)
