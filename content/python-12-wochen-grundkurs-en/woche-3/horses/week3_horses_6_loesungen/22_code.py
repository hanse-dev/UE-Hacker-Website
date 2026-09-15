# Step 1 – Tournament phases
phase1_ok = True
phase2_ok = True
phase3_ok = True
phase4_ok = False
phase5_ok = True

successful_phases = 0
if phase1_ok:
    successful_phases += 1
if phase2_ok:
    successful_phases += 1
if phase3_ok:
    successful_phases += 1
if phase4_ok:
    successful_phases += 1
if phase5_ok:
    successful_phases += 1

# Step 2 – Difficulty level
difficulty = 3
if difficulty == 1:
    print("Difficulty 1: Beginner")
elif difficulty == 2:
    print("Difficulty 2: Advanced")
elif difficulty == 3:
    print("Difficulty 3: Tournament")
elif difficulty == 4:
    print("Difficulty 4: Championship")
else:
    print("Difficulty 5: OLYMPICS!")

# Step 3 – Random events
obstacle_knocked = False
horse_spooked = False
saddle_slipped = True

if obstacle_knocked:
    print("❌ Obstacle knocked! -5 points")
if horse_spooked:
    print("😨 Horse spooked! -10 points")
if saddle_slipped:
    print("⚠️ Saddle slipped! -3 points")

# Step 4 – Success condition
print(f"Successful phases: {successful_phases}/5")
if successful_phases >= 4 and difficulty <= 3:
    print("🏆 Tournament victory! Outstanding performance!")
else:
    print("Tournament not won – better luck next time!")

# Step 5 – Special actions
if difficulty >= 4 and successful_phases < 3:
    print("📋 Extra training required!")

# Step 6 – Evaluation
total_points = successful_phases * 100 - difficulty * 20
placement = (successful_phases / 5) * 100
print(f"Total points: {total_points}")
print(f"Placement: {placement:.0f}%")

print()
print("🎉 Final Challenge completed!")
print("🏆 You have mastered the horse of the undecided paths!")
print("⭐ Title earned: Master of the Crossroads")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 3!")
print("🐴 Next week: Loops (for, while)!")
