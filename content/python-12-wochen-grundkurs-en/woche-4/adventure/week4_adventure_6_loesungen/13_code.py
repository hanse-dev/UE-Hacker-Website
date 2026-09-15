# Steps 1–4 – Tower ascent through all floors
for floor in range(1, 11):
    # Step 3 – Skip floor 7
    if floor == 7:
        print("Floor 7: 🔧 Closed for magical repairs – skipped!")
        continue

    # Step 2 – Standard message
    print(f"Floor {floor}: All quiet...")

    # Step 2 – Warnings on floors 3, 6, 9
    if floor in [3, 6, 9]:
        print(f"  ⚠️ Magical disturbance on floor {floor}!")

    # Step 2 – Bonus on floors 5 and 10
    if floor in [5, 10]:
        print(f"  🎁 Hidden treasure discovered on floor {floor}!")

    # Step 4 – End at floor 10
    if floor == 10:
        break

print()
print("✅ You have conquered the tower!")