# Step 1: Create the register
register = [
    {"horse": "Thunder", "rider": "Lena", "discipline": "Dressage"},
    {"horse": "Luna", "rider": "Tom", "discipline": "Cross-Country"},
    {"horse": "Flash", "rider": "Sophie", "discipline": "Jumping"},
    {"horse": "Silver", "rider": "Max", "discipline": "Dressage"}
]

# Step 2: Search by discipline
print("=== RANCH REGISTER ===")
for discipline in ["Dressage", "Jumping"]:
    matches = [e for e in register if e["discipline"] == discipline]
    print(f"\nDiscipline '{discipline}':")
    for e in matches:
        print(f"  {e['rider']} on {e['horse']}")

# Step 3: Statistics
discipline_counter = {}
for e in register:
    d = e["discipline"]
    discipline_counter[d] = discipline_counter.get(d, 0) + 1

print(f"\nNumber of different disciplines: {len(discipline_counter)}")
most_popular = max(discipline_counter, key=discipline_counter.get)
print(f"Most popular discipline: {most_popular} ({discipline_counter[most_popular]}x)")

# Bonus: Last 3 training dates
register[0]["trainings"] = ("2026-06-01", "2026-06-08", "2026-06-15")
print(f"\nBonus – Last trainings of {register[0]['rider']}: {register[0]['trainings']}")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Stable Master of the Infinite Archives!")
print("⭐ Title earned: Master of the Stable Archives")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 8!")
print("📚 Next week: JSON files and I/O!")