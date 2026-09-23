# 🐴 Stage 7: Saving and the Finale

*Knowledge from week 9: JSON and files*

An object like the player cannot be saved as JSON directly. So you first build a **dictionary** (name, position, HP, inventory as a list of dictionaries). Loading works backwards. If the file is missing, `try/except` catches the `FileNotFoundError`.

```python
import json

def save(player, filename="save.json"):
    data = {
        "name": player.name,
        "position": player.position,
        "hp": player.hp,
        "inventory": [{"name": g.name, "description": g.description} for g in player.inventory],
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💾 Saved game of {player.name} saved.")

def load(filename="save.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("📂 There is no saved game yet.")
        return None
    player = Player(data["name"], data["position"])
    player.hp = data["hp"]
    for entry in data["inventory"]:
        player.inventory.append(Item(entry["name"], entry["description"]))
    print(f"📂 Saved game of {player.name} loaded.")
    return player

def play(player, commands, goal_item="Foal"):
    for text in commands:
        print(f"\n> {text}")
        execute(player, text)
        if player.hp <= 0:
            print("💀 Game over – too strong. Try again!")
            return
        if has_item(player, goal_item):
            print("🏆 You found the foal and brought it back to the stable. The riding ranch celebrates you!")
            return
```

The function `play()` is the **game loop**: it runs commands and after every step checks whether you have won (goal item in the bag) or lost (HP 0).

> 🎓 Done! You used almost everything from the course in one project – now you can extend your game as you like.
