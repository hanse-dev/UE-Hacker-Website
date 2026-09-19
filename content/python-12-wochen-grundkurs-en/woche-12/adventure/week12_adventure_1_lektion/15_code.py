# Stage 6: Saving and loading the game
import json

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

save_game(hero)
loaded = load_game()
loaded.show_inventory()