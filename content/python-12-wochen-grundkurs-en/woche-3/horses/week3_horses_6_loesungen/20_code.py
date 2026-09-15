successes = 0
print("=== OBSTACLE SIMULATOR STARTED ===")
print()

# Level 1: Mounting
horse_height = 1.70  # meters
rider_weight = 65    # kg
if horse_height >= 1.60 and rider_weight <= 80:
    print("Level 1 ✅ – Mounting successful! Horse and rider are a good match.")
    successes += 1
else:
    print("Level 1 ❌ – Mounting failed!")

# Level 2: Gait choice
gait = "Walk"
if gait == "Walk":
    print("Level 2 ✅ – Walk chosen. Calm start!")
    successes += 1
else:
    print("Level 2 ✅ – Trot chosen. Good pace!")
    successes += 1

# Level 3: Speed
speed = 72
if speed >= 90:
    print("Level 3 ✅ – GALLOP! Full speed!")
    successes += 1
elif speed >= 70:
    print("Level 3 ✅ – Strong trot! Very good!")
    successes += 1
elif speed >= 50:
    print("Level 3 ✅ – Light trot. Good!")
    successes += 1
elif speed >= 30:
    print("Level 3 ❌ – Walk. Too slow for obstacles!")
else:
    print("Level 3 ❌ – Stopped!")

# Level 4: Obstacle check
height = 80
width = 60
difficulty = 40
if height <= 100:
    if width <= 80:
        print("Level 4 ✅ – Obstacle cleared! Height and width within limits.")
        successes += 1
    else:
        print("Level 4 ❌ – Obstacle too wide!")
else:
    print("Level 4 ❌ – Obstacle too high!")

# Level 5: Dismount
time = 58
errors = 0
style = 85
if time <= 60 or (errors == 0 and style >= 80):
    print("Level 5 ✅ – Perfect dismount! Flawless!")
    successes += 1
else:
    print("Level 5 ❌ – Dismount not passed!")

# Result
print()
print(f"=== RESULT: {successes}/5 levels passed ===")
if successes == 5:
    print("🏆 RIDING MASTER! Perfect run!")
elif successes >= 3:
    print("⭐ Well done! Keep it up!")
else:
    print("💪 Keep practicing – you can do it!")
