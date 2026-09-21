def calculate_health(level, class_name):
    if class_name == "Warrior":
        return level * 20
    else:
        return level * 10

def create_title(name, class_name):
    return f"{name} the {class_name}"
def show_character_sheet(name, class_name, level):
    print(create_title(name, class_name))
    print(f"Health: {calculate_health(level, class_name)}")
    print(f"Level: {level}")

show_character_sheet("Thorin", "Warrior", 4)
