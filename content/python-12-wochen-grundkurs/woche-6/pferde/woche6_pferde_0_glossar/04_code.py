pferde = ["Bobby", "Blitz", "Moritz", "Blitz"]

# Elemente verwalten
pferde.append("Luna")
pferde.insert(1, "Stella")
pferde.remove("Blitz")  # Erstes Vorkommen

# Suchen und zählen
print(pferde.index("Moritz"))   # Position
print(pferde.count("Blitz"))    # 1 (noch eines übrig)
print("Bobby" in pferde)        # True

# Sortieren
print(sorted(pferde))

# enumerate
for i, pferd in enumerate(pferde):
    print(i, pferd)

# break und continue
for pferd in pferde:
    if pferd == "Stella":
        continue   # Stella überspringen
    if pferd == "Luna":
        break      # bei Luna aufhören
    print(pferd)
