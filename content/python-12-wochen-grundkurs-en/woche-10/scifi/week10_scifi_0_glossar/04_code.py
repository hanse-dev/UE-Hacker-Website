class Spaceship:
    def __init__(self, name, ship_type="Standard"):
        self.name = name
        self.ship_type = ship_type

    def introduce(self):
        print(f"I am {self.name}, type: {self.ship_type}!")

    def launch(self):
        print(f"{self.name} is launching!")

# Create objects
ship1 = Spaceship("Enterprise")
ship2 = Spaceship("Voyager", ship_type="Intrepid")

ship1.introduce()   # I am Enterprise, type: Standard!
ship1.launch()      # Enterprise is launching!
print(ship2.ship_type)  # Intrepid
