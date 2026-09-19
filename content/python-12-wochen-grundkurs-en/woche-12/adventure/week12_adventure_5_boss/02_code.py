# 📦 STARTER PACK – run this cell first! It contains the complete game from the lesson.

import random

import json



class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Enemy:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def is_defeated(self):
        return self.hp <= 0

world = {
    "entrance": {
        "description": "You are standing at the entrance of the dragon cave. It smells of smoke.",
        "exits": {"north": "hall"},
        "items": [Item("Torch", "It shines in dark corners.")],
        "enemy": None,
    },
    "hall": {
        "description": "A huge hall. Torches flicker on the walls.",
        "exits": {"south": "entrance", "east": "treasury", "west": "spring"},
        "items": [],
        "enemy": None,
    },
    "spring": {
        "description": "A quiet spring. The water sparkles magically.",
        "exits": {"east": "hall"},
        "items": [Item("Sword", "A sharp sword stuck in the stone next to the spring.")],
        "enemy": None,
    },
    "treasury": {
        "description": "Gold as far as you can see – and in the middle sleeps the dragon!",
        "exits": {"west": "hall"},
        "items": [Item("Treasure", "The legendary treasure of Pyralia!")],
        "enemy": Enemy("Dragon", 15, 6),
    },
}



def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

def has_item(player, name):
    for item in player.inventory:
        if item.name == name:
            return True
    return False

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

def fight(player, enemy):
    print(f"⚔️ Fight: {player.name} vs. {enemy.name}!")
    bonus = 3 if has_item(player, "Sword") else 0
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
            print(f"🎉 You defeated the {enemy.name}!")

def execute(player, text):
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 I only understand commands made of two words, e.g. 'go north' or 'take Torch'.")
        return
    if action == "go":
        player.go(target)
        check_enemy(player)
    elif action == "take":
        player.take(target)
    else:
        print(f"🤔 '{action}' is unknown to me. Try 'go' or 'take'.")

def play(player, commands, goal_item="Treasure"):
    for text in commands:
        print(f"\n> {text}")
        execute(player, text)
        if player.hp <= 0:
            print("💀 Game over – the dragon was too strong. Try again!")
            return
        if has_item(player, goal_item):
            print("🏆 You found the treasure of Pyralia. The guild celebrates you!")
            return

def save_game(player, filename="savegame.json"):
    data = {
        "name": player.name,
        "position": player.position,
        "hp": player.hp,
        "inventory": [{"name": i.name, "description": i.description} for i in player.inventory],
    }
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print(f"💾 Saved the game of {player.name}.")

def load_game(filename="savegame.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("📂 There is no saved game yet.")
        return None
    player = Player(data["name"], data["position"])
    player.hp = data["hp"]
    for entry in data["inventory"]:
        player.inventory.append(Item(entry["name"], entry["description"]))
    print(f"📂 Loaded the game of {player.name}.")
    return player

print("📦 Starter pack loaded – the world is ready!")