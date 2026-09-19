# The finale: game loop, saving, loading – all together!
def play(player, commands, goal_item="Treasure"):
    for text in commands:
        print(f"\n> {text}")
        execute(player, text)
        if player.hp <= 0:
            print("💀 Game over – the dragon was too strong. Try again!")
            return
        if has_item(player, goal_item):
            print("🏆 You found the treasure of Pyralia. The guild celebrates you!")
            return

# Mira was saved and loaded – now her adventure continues:
play(loaded, ["go east", "go east", "take Treasure"])