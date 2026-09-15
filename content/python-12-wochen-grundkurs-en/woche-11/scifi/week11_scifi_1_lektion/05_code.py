# Example 1: Method polymorphism
class LaserWeapon:
    def fire(self):
        print("Laser beam fired! ⚡")

class PlasmaWeapon:
    def fire(self):
        print("Plasma burst fired! 🔥")

class IonWeapon:
    def fire(self):
        print("Ion cannon fired! 💫")

# Example 2: Polymorphic function
def test_weapon(weapon):
    print("Weapon test started:")
    weapon.fire()

# Example 3: Operator polymorphism
class EnergyCell:
    def __init__(self, capacity):
        self.capacity = capacity

    def __add__(self, other):
        return EnergyCell(self.capacity + other.capacity)

    def __str__(self):
        return f"{self.capacity} kWh"