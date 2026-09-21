world = {
    "airlock": {
        "description": "You stand in the airlock. Red warning lights flash and the station hums ominously.",
        "exits": {"north": "corridor"},
    },
    "corridor": {
        "description": "A long corridor with many doors. Emergency lighting bathes everything in red light.",
        "exits": {"south": "airlock", "east": "reactor", "west": "lab"},
    },
    "lab": {"description": "A lab full of equipment. Tools are ready on a table.", "exits": {"east": "corridor"}},
    "reactor": {"description": "The reactor room! The reactor hums – and in front of it stands a broken maintenance robot!", "exits": {"west": "corridor"}},
}

def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

def go(position, direction):
    exits = world[position]["exits"]
    if direction in exits:
        new_position = exits[direction]
        describe(new_position)
        return new_position
    print("🚫 You can't go that way!")
    return position

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["airlock"]["items"] = [Item("Keycard", "It opens secured doors.")]
world["corridor"]["items"] = []
world["lab"]["items"] = [Item("Welder", "A tool that can also stop broken robots.")]
world["reactor"]["items"] = [Item("Switch", "The red emergency stop switch of the reactor.")]

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hp = 20
        self.inventory = []

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
            names = [g.name for g in items]
            print("👀 You see:", ", ".join(names))
        else:
            print("👀 Nothing lies here.")

    def take(self, item_name):
        room = world[self.position]
        for item in room["items"]:
            if item.name == item_name:
                room["items"].remove(item)
                self.inventory.append(item)
                print(f"🎒 You take: {item.name} – {item.description}")
                return
        print(f"❓ There is no '{item_name}' here.")

    def show_inventory(self):
        if self.inventory:
            names = [g.name for g in self.inventory]
            print("🎒 In the bag:", ", ".join(names))
        else:
            print("🎒 Your bag is empty.")

import random

class Enemy:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def is_defeated(self):
        return self.hp <= 0

world["airlock"]["enemy"] = None
world["corridor"]["enemy"] = None
world["lab"]["enemy"] = None
world["reactor"]["enemy"] = Enemy("Robot", 15, 6)

def has_item(player, name):
    for item in player.inventory:
        if item.name == name:
            return True
    return False

def fight(player, enemy):
    print(f"⚔️ Fight: {player.name} against {enemy.name}!")
    bonus = 3 if has_item(player, "Welder") else 0
    while player.hp > 0 and not enemy.is_defeated():
        damage = random.randint(1, 6) + bonus
        enemy.hp -= damage
        print(f"   You hit for {damage} damage. ({enemy.name}: {max(enemy.hp, 0)} HP)")
        if enemy.is_defeated():
            break
        counter = random.randint(1, enemy.strength)
        player.hp -= counter
        print(f"   {enemy.name} hits you for {counter}. ({player.name}: {max(player.hp, 0)} HP)")
    return player.hp > 0

def check_enemy(player):
    enemy = world[player.position]["enemy"]
    if enemy is not None and not enemy.is_defeated():
        if fight(player, enemy):
            print(f"🎉 {enemy.name} was defeated!")

def execute(player, text):
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 I only understand commands of two words, e.g. 'go north' or 'take Keycard'.")
        return
    if action == "go":
        player.go(target)
        check_enemy(player)
    elif action == "take":
        player.take(target)
    else:
        print(f"🤔 '{action}' I don't know that. Try 'go' or 'take'.")

player = Player("Mira", "airlock")
def execute2(player, text):
    if text == "inventory":
        player.show_inventory()
    else:
        execute(player, text)

execute2(player, "take Keycard")
execute2(player, "inventory")
