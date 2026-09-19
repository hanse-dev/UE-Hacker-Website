# Mission 3: One-word commands
def execute(player, text):
    if text == "inventory":
        player.show_inventory()
        return
    if text == "help":
        print("📖 Commands: go <direction>, take <item>, use <item>, inventory, help")
        return
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 I only understand commands made of two words. Type 'help' for a list.")
        return
    if action == "go":
        player.go(target)
        check_enemy(player)
    elif action == "take":
        player.take(target)
    elif action == "use":
        player.use(target)
    else:
        print(f"🤔 '{action}' is unknown to me. Type 'help' for a list.")

hero = Player("Lena", "airlock")
play(hero, ["help", "take Keycard", "inventory", "use Keycard", "dance wildly"])