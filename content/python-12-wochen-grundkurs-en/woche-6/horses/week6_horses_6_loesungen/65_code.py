def show_list(items):
    for nr, entry in enumerate(items):
        print(f"{nr + 1}: {entry}")

horses = ["Stormwind", "Lightning", "Luna"]
show_list(horses)
