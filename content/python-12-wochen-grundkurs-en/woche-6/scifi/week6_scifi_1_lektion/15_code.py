ships = ["Nebula-Explorer", "Star-Fighter", "Cargo-Hauler", "Science-Vessel"]

# break: stop searching once the ship is found
print("=== Ship Search ===")
for ship in ships:
    print(f"Checking: {ship}")
    if ship == "Cargo-Hauler":
        print("🚀 Cargo-Hauler found! Search stopped.")
        break

# continue: skip damaged ships during launch
print("\n=== Launch-Ready Ships ===")
damaged = ["Star-Fighter"]
for ship in ships:
    if ship in damaged:
        continue
    print(f"  - {ship} is ready for launch")