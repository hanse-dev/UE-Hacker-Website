class Player:
    inventory = []

    def __init__(self, name):
        self.name = name

    def take(self, thing):
        self.inventory.append(thing)

mira = Player("Mira")
ben = Player("Ben")
mira.take("Flashlight")
print("Mira:", mira.inventory)
print("Ben:", ben.inventory)