# Stage 3b: The player – an object that contains other objects
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hp = 20
        self.inventory = []  # a list full of Item objects

    def go(self, direction):
        exits = world[self.position]["exits"]
        if direction in exits:
            self.position = exits[direction]
            describe(self.position)
            self.look_around()
        else:
            print("🚫 You can't go that way!")

    def look_around(self):
        items = world[self.position]["items"]
        if items:
            names = [i.name for i in items]
            print("👀 You see:", ", ".join(names))
        else:
            print("👀 There is nothing here.")

    def take(self, item_name):
        room = world[self.position]
        for item in room["items"]:
            if item.name == item_name:
                room["items"].remove(item)
                self.inventory.append(item)
                print(f"🎒 You take: {item.name} – {item.description}")
                return
        print(f"❓ There is no '{item_name}'.")

    def show_inventory(self):
        if self.inventory:
            names = [i.name for i in self.inventory]
            print("🎒 In your bag:", ", ".join(names))
        else:
            print("🎒 Your bag is empty.")

hero = Player("Mira", "entrance")
hero.look_around()
hero.take("Torch")
hero.go("north")
hero.go("west")
hero.take("Sword")
hero.show_inventory()