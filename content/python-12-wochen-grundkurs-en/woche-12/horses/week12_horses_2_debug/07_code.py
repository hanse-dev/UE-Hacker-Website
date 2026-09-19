import json

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

mira = Player("Mira", 20)

with open("debug_save.json", "w") as file:
    json.dump(mira, file)

with open("debug_save.json", "r") as file:
    data = json.load(file)
print(data["name"])