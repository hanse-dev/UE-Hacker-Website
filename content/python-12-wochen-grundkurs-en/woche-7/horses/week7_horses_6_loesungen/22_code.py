import random
import math

obstacle_types = ["Pole", "Water Ditch", "Curve", "Double Pole", "Wall"]
difficulties = [1, 2, 3, 4, 5]

# Steps 1 & 2: Create and print the course
print("=== RANDOM COURSE ===")
total_difficulty = 0
for i in range(1, 7):
    obstacle_type = random.choice(obstacle_types)
    difficulty = random.choice(difficulties)
    total_difficulty += difficulty
    print(f"Obstacle {i}: {obstacle_type} | Difficulty: {difficulty}/5")

# Step 3: Total difficulty and technique factor
technique_factor = round(math.sqrt(total_difficulty), 2)
print(f"\nTotal difficulty: {total_difficulty}")
print(f"Technique factor: {technique_factor}")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Smith of Infinite Tools!")
print("⭐ Title earned: Master of Toolboxes")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 7!")
print("📚 Next week: Dictionaries and Tuples!")