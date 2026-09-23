def spell_name(element, level):
    return f"{element}-L{level}"

def calculate_power(element, level):
    if element == "FIRE":
        return level * 30
    elif element == "WATER":
        return level * 20
    else:
        return level * 15
def show_spell(element, level):
    print(f"{spell_name(element, level)} has power {calculate_power(element, level)}")

for level in range(1, 4):
    show_spell("FIRE", level)
