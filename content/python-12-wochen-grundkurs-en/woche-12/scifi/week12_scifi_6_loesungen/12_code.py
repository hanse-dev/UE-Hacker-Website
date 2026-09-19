# Mission 1: The new room
world["bridge"] = {
    "description": "Screens flicker above an abandoned control console.",
    "exits": {"south": "corridor"},
    "items": [Item("Datapad", "A pad full of mission data.")],
    "enemy": None,
}
world["corridor"]["exits"]["north"] = "bridge"

hero = Player("Mira", "corridor")
hero.go("north")
hero.take("Datapad")
hero.show_inventory()