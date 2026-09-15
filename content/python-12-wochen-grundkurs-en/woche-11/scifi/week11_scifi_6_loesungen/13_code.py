# Solution Suggestion Mission 2 – The Polymorphic Weapon System

# Step 1: Three weapon classes
class Laser:
    def __init__(self, name):
        self.name = name

    def fire(self):
        print(f"Pew! {self.name} fires a laser beam! ⚡")

class Plasma:
    def __init__(self, name):
        self.name = name

    def fire(self):
        print(f"Hiss! {self.name} releases plasma energy! 🔵")

class Ion:
    def __init__(self, name):
        self.name = name

    def fire(self):
        print(f"Bzz! {self.name} hurls an ion beam! ⚪")

# Step 2: Polymorphic function
def test_weapon(weapon):
    print(f"Testing weapon '{weapon.name}':")
    weapon.fire()

# Step 3: Test all weapons
laser_mk2 = Laser("Laser-MK2")
plasma_thrower = Plasma("Plasma Thrower-X")
ion_cannon = Ion("Ion Cannon-3000")

test_weapon(laser_mk2)
test_weapon(plasma_thrower)
test_weapon(ion_cannon)

# Bonus: Weapon factory
def weapon_factory(weapon_type, name):
    if weapon_type == "laser":
        return Laser(name)
    elif weapon_type == "plasma":
        return Plasma(name)
    elif weapon_type == "ion":
        return Ion(name)
    else:
        print(f"Unknown weapon type: {weapon_type}")
        return None

print()
new_weapon = weapon_factory("plasma", "Plasma Prototype")
test_weapon(new_weapon)