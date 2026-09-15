# Example 1: Level rating
xp = 750
if xp >= 1000:
    print("🏆 Master!")
elif xp >= 500:
    print("⭐ Advanced!")
elif xp >= 100:
    print("🌟 Beginner!")
else:
    print("📚 Still much to learn...")

# Example 2: Elemental spells
element = "Water"
if element == "Fire":
    print("🔥 Fire Strike!")
elif element == "Water":
    print("💧 Water Torrent!")
elif element == "Air":
    print("🌪️ Wind Gust!")
elif element == "Earth":
    print("🗿 Earthquake!")
else:
    print("❓ Unknown element!")

# Example 3: Hero class
strength = 8
intelligence = 12
if strength > 10 and intelligence > 10:
    print("⚔️🧠 Paladin!")
elif strength > 10:
    print("💪 Warrior!")
elif intelligence > 10:
    print("🧙 Mage!")
else:
    print("👤 Adventurer!")