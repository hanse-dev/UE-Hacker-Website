def calculate_lives(monster_count):
    return (monster_count + 1) // 2

print(f"Lives: {calculate_lives(5)}")
print(f"Lives: {calculate_lives(4)}")
print(f"Lives: {calculate_lives(0)}")
