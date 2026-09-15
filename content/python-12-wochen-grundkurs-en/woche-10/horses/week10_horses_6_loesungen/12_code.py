class Rider:
    def __init__(self, name, level=1, favourite_horse="None"):
        self.name = name
        self.level = level
        self.favourite_horse = favourite_horse

    def introduce(self):
        print(f"{self.name} (Level {self.level}) – Favourite horse: {self.favourite_horse}")

    def train(self):
        self.level += 1
        print(f"{self.name} has trained! New level: {self.level}")

lisa = Rider("Lisa", 3, "Thunder")
tom = Rider("Tom", 1)
sarah = Rider("Sarah", 5, "Luna")

print("=== Riding School ===")
for rider in [lisa, tom, sarah]:
    rider.introduce()

tom.train()
print(f"Tom's level after training: {tom.level}")