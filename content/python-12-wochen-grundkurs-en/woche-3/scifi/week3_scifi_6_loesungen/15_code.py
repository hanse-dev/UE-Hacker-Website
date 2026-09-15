# Step 1 – Mission data
mission_level = 10
success_points = 95
losses = 0
time = 25  # seconds

# Step 2 – Overall score
score = success_points - (losses * 10) - (time / 5)
print(f"Level: {mission_level}, Points: {success_points}, Losses: {losses}, Time: {time}s")
print(f"Overall score: {score:.1f}")

# Step 3 – Legendary status
if mission_level >= 10 and score >= 85 and losses == 0:
    print("🏆 LEGENDARY! Absolute perfection – Galactic glory!")
elif mission_level >= 8 and score >= 70 and losses <= 2:
    print("⭐ EXCELLENT! Outstanding performance!")
elif mission_level >= 5:
    print("👍 GOOD – Mission accomplished!")
else:
    print("Mission completed with difficulties.")

# Step 5 – Speed bonus
if time < 30:
    print("+50 Bonus for lightning mission!")