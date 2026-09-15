class Monster:
    def __init__(self, name, monster_type, hp, attack_power):
        self.name = name
        self.monster_type = monster_type
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        damage = self.attack_power
        target.hp -= damage
        print(f"{self.name} attacks {target.name}! -{damage} HP. {target.name} has {target.hp} HP left.")

    # Bonus: heal method
    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for {amount} HP. Current HP: {self.hp}")

    def is_defeated(self):
        return self.hp <= 0

goblin = Monster("Grumk", "Goblin", 50, 10)
troll = Monster("Ugrak", "Troll", 120, 25)
dragon = Monster("Smaug", "Dragon", 200, 40)

monster_list = [goblin, troll, dragon]

print("=== Bestiary ===")
for m in monster_list:
    print(f"[{m.monster_type}] {m.name}: {m.hp} HP, {m.attack_power} Attack")

print("\n=== Battle: Goblin vs. Troll ===")
goblin.attack(troll)
troll.attack(goblin)
troll.attack(goblin)

if goblin.is_defeated():
    print(f"{goblin.name} has been defeated!")
    print(f"Winner: {troll.name}")

# Bonus: heal
print("\n=== Dragon heals itself ===")
dragon.heal(50)