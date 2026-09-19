# Boss Quest 2: Your own mini adventure (sample solution: "The Cargo Ship")
freighter = {
    "dock": {
        "description": "A quiet dock. An old cargo ship lies in front of you.",
        "exits": {"north": "hallway"},
        "items": [Item("Key", "A heavy key.")],
        "enemy": None,
    },
    "hallway": {
        "description": "A narrow hallway with stairs going up and down.",
        "exits": {"south": "dock", "up": "cabin", "down": "hold"},
        "items": [],
        "enemy": None,
    },
    "hold": {
        "description": "A dark cargo hold. Something shines between the crates.",
        "exits": {"up": "hallway"},
        "items": [Item("Tool", "A sturdy multi-tool.")],
        "enemy": None,
    },
    "cabin": {
        "description": "The captain's cabin. A guard robot blocks the way!",
        "exits": {"down": "hallway", "north": "deck"},
        "items": [],
        "enemy": Enemy("Guard Robot", 12, 5),
    },
    "deck": {
        "description": "The ship's bridge. The energy crystal lies here!",
        "exits": {"south": "cabin"},
        "items": [Item("Crystal", "The energy crystal.")],
        "enemy": None,
    },
}

world = freighter  # the game functions work with the name "world" – we simply swap the world
hero = Player("Ida", "dock")
hero.hp = 30
play(hero, ["take Key", "go north", "go down", "take Tool", "go up", "go up", "go north", "take Crystal"], "Crystal")