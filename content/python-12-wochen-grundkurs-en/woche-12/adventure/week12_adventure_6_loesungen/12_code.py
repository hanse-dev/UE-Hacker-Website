# Mission 1: The new room
world["library"] = {
    "description": "Dusty shelves full of ancient scrolls.",
    "exits": {"south": "hall"},
    "items": [Item("Spellbook", "A book that turns its own pages.")],
    "enemy": None,
}
world["hall"]["exits"]["north"] = "library"

hero = Player("Mira", "hall")
hero.go("north")
hero.take("Spellbook")
hero.show_inventory()