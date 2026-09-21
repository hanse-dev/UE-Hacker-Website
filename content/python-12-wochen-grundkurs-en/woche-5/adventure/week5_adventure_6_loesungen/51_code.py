def can_do_quest(level, difficulty):
    return level >= difficulty * 2

print(f"Quest 3: {can_do_quest(8, 3)}")
print(f"Quest 5: {can_do_quest(8, 5)}")
