# The finale: game loop, saving, loading – all together!
def play(player, commands, goal_item="Powerkey"):
    for text in commands:
        print(f"\n> {text}")
        execute(player, text)
        if player.hp <= 0:
            print("💀 Game over – the robot was too strong. Try again!")
            return
        if has_item(player, goal_item):
            print("🏆 You shut down the reactor. Nebula-7 is saved, the crew celebrates you!")
            return

# Mira was saved and loaded – now her adventure continues:
play(loaded, ["go east", "go east", "take Powerkey"])