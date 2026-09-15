# Steps 1–4 – Round through all stalls
for stall in range(1, 11):
    # Step 3 – Skip stall 7 (renovation)
    if stall == 7:
        print("Stall 7: 🔧 Under renovation – skipping!")
        continue

    # Step 1 – Standard message
    print(f"Stall {stall}: Inspection in progress...")

    # Step 2 – Extra inspection at 3, 6, 9
    if stall in [3, 6, 9]:
        print(f"  ⚠️ Stall {stall}: Extra inspection needed!")

    # Step 2 – Bonus at stall 5 and 10
    if stall in [5, 10]:
        print(f"  🎁 Bonus for especially clean stall {stall}!")

    # Step 4 – Stop at stall 10
    if stall == 10:
        break

print()
print("✅ All important stalls checked!")