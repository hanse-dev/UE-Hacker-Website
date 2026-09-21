def calculate_shield_bonus(modules):
    if modules >= 5:
        return 20
    elif modules >= 3:
        return 10
    else:
        return 0

def calculate_shield(energy, modules):
    return energy * 3 + calculate_shield_bonus(modules)
def show_shield(name, energy, modules):
    print(f"{name}: shield {calculate_shield(energy, modules)}")

for modules in range(2, 7, 2):
    show_shield("Nova", 30, modules)
