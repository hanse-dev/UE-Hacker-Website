# Example 1: Rank rating
points = 750
if points >= 1000:
    print("🏆 Fleet Commander!")
elif points >= 500:
    print("⭐ Captain!")
elif points >= 100:
    print("🌟 Lieutenant!")
else:
    print("📚 Cadet!")

# Example 2: Weapon system
weapon = "Laser"
if weapon == "Laser":
    print("🔥 Laser activated!")
elif weapon == "Plasma":
    print("💧 Plasma cannon loaded!")
elif weapon == "Quantum":
    print("🌪️ Quantum torpedo ready!")
elif weapon == "Ion":
    print("⚡ Ion cannon online!")
else:
    print("❓ Unknown weapon!")

# Example 3: Ship class
shield = 8
weapons = 12
if shield > 10 and weapons > 10:
    print("⚔️🧠 Battleship!")
elif shield > 10:
    print("💪 Cruiser!")
elif weapons > 10:
    print("🧙 Destroyer!")
else:
    print("👤 Frigate!")