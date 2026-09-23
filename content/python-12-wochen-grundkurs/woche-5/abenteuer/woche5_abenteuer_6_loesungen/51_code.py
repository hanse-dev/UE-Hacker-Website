def darf_quest(level, schwierigkeit):
    return level >= schwierigkeit * 2

print(f"Quest 3: {darf_quest(8, 3)}")
print(f"Quest 5: {darf_quest(8, 5)}")
