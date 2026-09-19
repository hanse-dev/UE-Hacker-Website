# Boss Quest 2: Your own mini adventure (sample solution: "The Old Barn")
barn = {
    "path": {
        "description": "A dusty country path. An old barn stands in front of you.",
        "exits": {"north": "floor"},
        "items": [Item("Ladder", "A sturdy wooden ladder.")],
        "enemy": None,
    },
    "floor": {
        "description": "The barn floor. A ladder leads up.",
        "exits": {"south": "path", "up": "loft", "east": "box"},
        "items": [],
        "enemy": None,
    },
    "loft": {
        "description": "The hayloft. It smells of summer.",
        "exits": {"down": "floor"},
        "items": [Item("Hay", "Soft, dry hay.")],
        "enemy": None,
    },
    "box": {
        "description": "A box where a tomcat hisses!",
        "exits": {"west": "floor", "north": "treasure"},
        "items": [],
        "enemy": Enemy("Tomcat", 12, 5),
    },
    "treasure": {
        "description": "Behind the box hangs the golden saddle of the tournament winner!",
        "exits": {"south": "box"},
        "items": [Item("Saddle", "The golden saddle.")],
        "enemy": None,
    },
}

world = barn  # the game functions work with the name "world" – we simply swap the world
hero = Player("Ida", "path")
hero.hp = 30
play(hero, ["take Ladder", "go north", "go up", "take Hay", "go down", "go east", "go north", "take Saddle"], "Saddle")