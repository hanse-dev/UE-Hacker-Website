# Mission 1: The new room
world["feedroom"] = {
    "description": "Sacks of oats and hay are piled up to the ceiling.",
    "exits": {"south": "aisle"},
    "items": [Item("Oatsack", "A plump sack of fresh oats.")],
    "enemy": None,
}
world["aisle"]["exits"]["north"] = "feedroom"

hero = Player("Mira", "aisle")
hero.go("north")
hero.take("Oatsack")
hero.show_inventory()