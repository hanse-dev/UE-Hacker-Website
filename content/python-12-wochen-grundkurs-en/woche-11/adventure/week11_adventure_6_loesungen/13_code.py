# Solution suggestion Mission 2 – The Polymorphic Arsenal

# Step 1: Three weapon classes
class Sword:
    def __init__(self, name):
        self.name = name

    def use(self):
        print(f"Sword '{self.name}' hits! CLANG!")

class Bow:
    def __init__(self, name):
        self.name = name

    def use(self):
        print(f"Bow '{self.name}': Arrow flies! WHOOSH!")

class Staff:
    def __init__(self, name):
        self.name = name

    def use(self):
        print(f"Staff '{self.name}': Spell fires! ZAP!")

# Step 2: Polymorphic function
def use_weapon(weapon):
    weapon.use()

# Step 3: Test all weapons
blade = Sword("Demon Slayer")
longbow = Bow("Silver Arrow")
staff = Staff("Moonwood Staff")

use_weapon(blade)
use_weapon(longbow)
use_weapon(staff)

# Bonus: Weapon factory
def weapon_factory(type, name):
    if type == "sword":
        return Sword(name)
    elif type == "bow":
        return Bow(name)
    elif type == "staff":
        return Staff(name)
    else:
        print(f"Unknown weapon type: {type}")
        return None

print()
new_weapon = weapon_factory("sword", "Dragon Blade")
use_weapon(new_weapon)
