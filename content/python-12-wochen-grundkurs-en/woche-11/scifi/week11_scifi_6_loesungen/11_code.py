# Solution Suggestion Mission 1 – The Robot Hierarchy

# Step 1: Base class
class Robot:
    def __init__(self, id, name, energy_status):
        self.id = id
        self.name = name
        self.energy_status = energy_status

    def activate(self):
        print(f"[{self.id}] {self.name} – Energy: {self.energy_status}% – SYSTEM ONLINE")

# Step 2: Child classes
class Android(Robot):
    def __init__(self, id, name, energy_status):
        super().__init__(id, name, energy_status)
        self.languages = ["Galactic", "Terran"]

    def communicate(self):
        print(f"{self.name} speaks: {', '.join(self.languages)}")

class Drone(Robot):
    def __init__(self, id, name, energy_status):
        super().__init__(id, name, energy_status)
        self.max_height_m = 500

    def fly(self):
        print(f"{self.name} climbs up to {self.max_height_m} meters!")

class Cyborg(Robot):
    def __init__(self, id, name, energy_status):
        super().__init__(id, name, energy_status)
        self.is_human = True

    def status(self):
        bio = "biological" if self.is_human else "fully mechanical"
        print(f"{self.name}: Hybrid unit – partly {bio}")

# Step 3: Create objects
seven = Android("AND-007", "Seven", 98)
seven.activate()
seven.communicate()

print()
scout = Drone("DRN-42", "Scout", 85)
scout.activate()
scout.fly()

print()
nexus = Cyborg("CYB-01", "Nexus", 72)
nexus.activate()
nexus.status()

# Bonus: CombatAndroid inherits from Android
print()
class CombatAndroid(Android):
    def __init__(self, id, name, energy_status):
        super().__init__(id, name, energy_status)
        self.weapon = "Plasma Blaster"

    def attack(self):
        print(f"{self.name} fires the {self.weapon}! PEWPEW!")

rex = CombatAndroid("KAD-99", "Rex", 100)
rex.activate()      # inherited from Robot
rex.communicate()   # inherited from Android
rex.attack()