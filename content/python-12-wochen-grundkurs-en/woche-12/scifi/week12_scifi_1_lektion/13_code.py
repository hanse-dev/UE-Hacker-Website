# Stage 5: Catching wrong input
def execute(player, text):
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 I only understand commands made of two words, e.g. 'go north' or 'take Keycard'.")
        return
    if action == "go":
        player.go(target)
        check_enemy(player)
    elif action == "take":
        player.take(target)
    else:
        print(f"🤔 '{action}' is unknown to me. Try 'go' or 'take'.")

execute(hero, "hello")
execute(hero, "dance wildly")
execute(hero, "take Wand")