def show_list(items):
    for nr, entry in enumerate(items):
        print(f"{nr + 1}: {entry}")

modules = ["Drive", "Sensor", "Shield"]
show_list(modules)
