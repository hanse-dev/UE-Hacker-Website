# Example 1: Riding skill level
experience = 750
if experience >= 1000:
    print("🏆 Master Rider!")
elif experience >= 500:
    print("⭐ Advanced Rider!")
elif experience >= 100:
    print("🌟 Beginner!")
else:
    print("📚 Still a lot to practice...")

# Example 2: Horse discipline
discipline = "Jumping"
if discipline == "Dressage":
    print("🎆 Elegant dressage!")
elif discipline == "Jumping":
    print("🏇 Show jumping course!")
elif discipline == "Western":
    print("🤠 Western style!")
elif discipline == "Vaulting":
    print("🤸 Vaulting acrobatics!")
else:
    print("❓ Unknown discipline!")

# Example 3: Horse type
height = 168
temperament = 8
if height > 170 and temperament > 7:
    print("⚔️🧠 Warmblood for sport!")
elif height > 170:
    print("💪 Coldblood for work!")
elif temperament > 7:
    print("🐎 Thoroughbred for racing!")
else:
    print("👤 Pony for leisure!")
