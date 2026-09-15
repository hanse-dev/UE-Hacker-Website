# Example 1: Method polymorphism
class DressageHorse:
    def special_ability(self):
        print("Elegant Piaffe! 💃")

class JumpingHorse:
    def special_ability(self):
        print("High Jump! 🦘")

class WesternHorse:
    def special_ability(self):
        print("Sliding Stop! 🤠")

# Example 2: Polymorphic function
def complete_training(horse):
    print(f"Training for {horse.name}:")
    horse.special_ability()

# Example 3: Operator polymorphism
class Horsepower:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Horsepower(self.value + other.value)

    def __str__(self):
        return f"{self.value} horsepowers"
