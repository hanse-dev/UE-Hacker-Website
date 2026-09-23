def calculate_reward(difficulty):
    return difficulty * 50

def can_do_quest(level, difficulty):
    return level >= difficulty * 2
def show_quest(name, difficulty, level):
    if can_do_quest(level, difficulty):
        print(f"{name}: reward {calculate_reward(difficulty)}")
    else:
        print(f"{name}: too hard")

show_quest("Dragon Hunt", 4, 9)
show_quest("Treasure Hunt", 2, 3)
