class Alien:
    def __init__(self, name, planet, danger_level, intelligence):
        self.name = name
        self.planet = planet
        self.danger_level = danger_level
        self.intelligence = intelligence

    def analyse(self):
        level = "HIGH" if self.danger_level >= 8 else ("MEDIUM" if self.danger_level >= 5 else "LOW")
        print(f"🔬 {self.name} (Planet: {self.planet}) | Danger: {level} | IQ: {self.intelligence}")

    def communicate(self):
        if self.intelligence >= 7:
            print(f"{self.name} can communicate!")
        else:
            print(f"{self.name} responds instinctively.")

bestiary = [
    Alien("Zorgon", "Kepler-22b", 9, 4),
    Alien("Luminar", "Gliese-667c", 3, 10),
    Alien("Krakon", "HD 40307g", 7, 6),
]

print("=== Alien Bestiary ===")
for alien in bestiary:
    alien.analyse()
    alien.communicate()
    print()

most_dangerous = max(bestiary, key=lambda a: a.danger_level)
print(f"Most dangerous: {most_dangerous.name} (danger level {most_dangerous.danger_level})")

print("🎉 Mission completed!")
print("🏆 You have defeated the Constructor Master!")
print("⭐ Title earned: System Architect")