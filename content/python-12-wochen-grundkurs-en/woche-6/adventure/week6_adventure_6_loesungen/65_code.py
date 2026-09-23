def show_list(items):
    for nr, entry in enumerate(items):
        print(f"{nr + 1}: {entry}")

treasures = ["Gold", "Crystal", "Amulet"]
show_list(treasures)
