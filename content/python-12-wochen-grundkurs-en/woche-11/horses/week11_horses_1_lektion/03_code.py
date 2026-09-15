# Example 1: Simple inheritance
class Horse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} eats hay")

class RidingHorse(Horse):
    def ride(self, speed):
        print(f"{self.name} rides at {speed} km/h")

# Example 2: Overriding methods
class Thoroughbred(RidingHorse):
    def eat(self):
        print(f"{self.name} eats special high-energy feed")

    def gallop(self):
        print(f"{self.name} gallops like the wind! 🐎")

# Example 3: Using super()
class Coldblood(Horse):
    def __init__(self, name, age, pulling_force):
        super().__init__(name, age)
        self.pulling_force = pulling_force

    def pull(self, load):
        print(f"{self.name} pulls {load} with {self.pulling_force}kg of force")
