# Boss Quest 1: The complete game state
def save_full(player, filename="complete.json"):
    rooms_data = {}
    for room_name, room in world.items():
        enemy = room["enemy"]
        rooms_data[room_name] = {
            "items": [{"name": i.name, "description": i.description} for i in room["items"]],
            "enemy_hp": enemy.hp if enemy is not None else None,
        }
    data = {
        "player": {
            "name": player.name,
            "position": player.position,
            "hp": player.hp,
            "inventory": [{"name": i.name, "description": i.description} for i in player.inventory],
        },
        "rooms": rooms_data,
    }
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print("💾 Complete game saved.")

def load_full(filename="complete.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("📂 No saved game found.")
        return None
    for room_name, state in data["rooms"].items():
        room = world[room_name]
        room["items"] = [Item(e["name"], e["description"]) for e in state["items"]]
        if room["enemy"] is not None:
            room["enemy"].hp = state["enemy_hp"]
    s = data["player"]
    player = Player(s["name"], s["position"])
    player.hp = s["hp"]
    for e in s["inventory"]:
        player.inventory.append(Item(e["name"], e["description"]))
    print("📂 Complete game loaded.")
    return player

# Test: take the weapon, save, wreck the world, load
hero = Player("Tom", "tackroom")
hero.take("Broom")
save_full(hero)
world["tackroom"]["items"] = [Item("Junk", "Just scrap.")]
hero = load_full()
hero.show_inventory()
print("In the tackroom contains:", [i.name for i in world["tackroom"]["items"]])