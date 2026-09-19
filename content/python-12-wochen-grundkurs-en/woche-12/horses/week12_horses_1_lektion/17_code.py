# The finale: game loop, saving, loading – all together!
def play(player, commands, goal_item="Foal"):
    for text in commands:
        print(f"\n> {text}")
        execute(player, text)
        if player.hp <= 0:
            print("💀 Game over – the billy goat was too strong. Try again!")
            return
        if has_item(player, goal_item):
            print("🏆 You found the foal and brought it back to the stable. The riding stable celebrates you!")
            return

# Mira was saved and loaded – now her adventure continues:
play(loaded, ["go east", "go east", "take Foal"])