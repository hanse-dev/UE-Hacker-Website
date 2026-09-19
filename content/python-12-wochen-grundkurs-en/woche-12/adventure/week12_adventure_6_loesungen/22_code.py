# Boss Quest 2: Your own mini adventure (sample solution: "The Abandoned Tower")
tower = {
    "courtyard": {
        "description": "An overgrown courtyard. An old tower rises in front of you.",
        "exits": {"north": "stairs"},
        "items": [Item("Lantern", "Gives warm light.")],
        "enemy": None,
    },
    "stairs": {
        "description": "A creaking spiral staircase.",
        "exits": {"south": "courtyard", "up": "lab", "down": "cellar"},
        "items": [],
        "enemy": None,
    },
    "cellar": {
        "description": "A damp cellar. Something glitters in the dark.",
        "exits": {"up": "stairs"},
        "items": [Item("Wand", "A wand full of magic.")],
        "enemy": None,
    },
    "lab": {
        "description": "The tower mage's lab. A golem blocks the way!",
        "exits": {"down": "stairs", "north": "roof"},
        "items": [],
        "enemy": Enemy("Golem", 12, 5),
    },
    "roof": {
        "description": "The roof of the tower. The Crown of Stars lies here!",
        "exits": {"south": "lab"},
        "items": [Item("Crown", "The Crown of Stars.")],
        "enemy": None,
    },
}

world = tower  # the game functions work with the name "world" – we simply swap the world
hero = Player("Ida", "courtyard")
hero.hp = 30
play(hero, ["take Lantern", "go north", "go down", "take Wand", "go up", "go up", "go north", "take Crown"], "Crown")