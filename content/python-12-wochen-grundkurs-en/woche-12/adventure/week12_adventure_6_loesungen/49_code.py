class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.inventory = []

    def take(self, item_name):
        self.inventory.append(item_name)

player = Player("Mira", "entrance")
player.take("Torch")
print(f"Count: {len(player.inventory)}")
