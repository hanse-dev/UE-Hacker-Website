# Example 1: Simple inheritance
class Robot:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def activate(self):
        print(f"{self.name} is being activated")

class Android(Robot):
    def learn(self, information):
        print(f"{self.name} learns: {information}")

# Example 2: Overriding methods
class CombatRobot(Android):
    def activate(self):
        print(f"{self.name} activated in combat mode!")

    def attack(self, target):
        print(f"{self.name} attacks {target}!")

# Example 3: Using super()
class MedicalRobot(Android):
    def __init__(self, id, name, specialization):
        super().__init__(id, name)
        self.specialization = specialization

    def heal(self, patient):
        print(f"{self.name} treats {patient} with {self.specialization}")