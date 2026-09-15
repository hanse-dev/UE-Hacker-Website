def create_tournament(name, discipline, difficulty):
    return {"name": name, "discipline": discipline, "difficulty": difficulty, "status": "open"}

tournaments = [
    create_tournament("Spring Cup", "Dressage", 3),
    create_tournament("Summer Tournament", "Show Jumping", 4),
    create_tournament("Autumn Cup", "Eventing", 5),
]

print("=== Tournament Database ===")
for t in tournaments:
    print(f"  {t['name']} | {t['discipline']} | Difficulty: {t['difficulty']}")

# Search
hard = [t for t in tournaments if t["difficulty"] >= 4]
print(f"\nHard tournaments: {[t['name'] for t in hard]}")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Stable Master of Infinite Lists!")
print("⭐ Title earned: Master of Training Collections")