import random

# Steps 1–4 – Jumping course with 10 jumps
total_points = 0
high_jumps = 0
highest_height = 0
knockdowns = []

print("=== JUMPING COURSE ===")
for jump_nr in range(1, 11):
    # Step 1 – Random jump height
    height = random.randint(60, 140)  # cm

    # Step 2 – Award points
    if height >= 130:
        points = 100
    elif height >= 110:
        points = 80
    elif height >= 90:
        points = 60
    else:
        points = 40

    # Bonus – Random knockdown
    knockdown = random.choice([True, False, False, False])  # 25% chance
    if knockdown:
        points -= 20
        knockdowns.append(jump_nr)

    total_points += points

    # Step 2 – Count high jumps
    if height > 100:
        high_jumps += 1

    # Step 3 – Remember highest jump
    if height > highest_height:
        highest_height = height

    print(f"Jump {jump_nr:2d}: {height}cm | Points: {points}{'  ❌ Knockdown!' if knockdown else ''}")

# Step 4 – Statistics
print()
print("=== JUMP STATISTICS ===")
print(f"Total points: {total_points}")
print(f"Jumps over 100cm: {high_jumps}/10")
print(f"Highest jump: {highest_height}cm")
print(f"Average: {total_points / 10:.0f} points/jump")
if knockdowns:
    print(f"Knockdowns at jump: {knockdowns}")