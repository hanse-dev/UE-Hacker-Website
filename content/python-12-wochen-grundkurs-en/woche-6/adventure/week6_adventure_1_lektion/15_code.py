inventory = ["Potion", "Sword", "Key", "Treasure", "Map"]

# break: stop searching once treasure is found
print("=== Treasure Hunt ===")
for item in inventory:
    print(f"Checking: {item}")
    if item == "Treasure":
        print("🎉 Treasure found! Search complete.")
        break

# continue: skip potions when listing items
print("\n=== Inventory without Potions ===")
for item in inventory:
    if item == "Potion":
        continue
    print(f"  - {item}")
