# Step 1 – Mission phases
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

# Step 2 – Danger level
danger_level = 2
if danger_level == 1:
    print("Danger level 1: Green sector")
elif danger_level == 2:
    print("Danger level 2: Yellow sector")
elif danger_level == 3:
    print("Danger level 3: Orange sector")
elif danger_level == 4:
    print("Danger level 4: Red sector")
else:
    print("Danger level 5: BLACK HOLE!")

# Step 3 – Random events
meteor_hit = False
pirate_attack = True
system_failure = False

if meteor_hit:
    print("☄️ Meteor hit! -30 shields")
if pirate_attack:
    print("🏴‍☠️ Pirate attack! Defense systems activated!")
if system_failure:
    print("💻 System failure! Emergency program running...")

# Step 4 – Success condition
print(f"Successful phases: {successful_phases}/5")
if successful_phases >= 4 and danger_level <= 3:
    print("🏆 Mission successful! Galaxy saved!")
else:
    print("Mission not fully passed.")

# Step 5 – Special actions
if danger_level >= 4 and successful_phases < 3:
    print("🚨 Rescue operation required!")

# Step 6 – Mission evaluation
total_points = successful_phases * 100 - danger_level * 20
success_rate = (successful_phases / 5) * 100
print(f"Total points: {total_points}")
print(f"Success rate: {success_rate:.0f}%")

print()
print("🎉 Final challenge completed!")
print("🏆 You have defeated the AI Guardian of Paradoxical Decisions!")
print("⭐ Title earned: Master of Paths")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 3!")
print("🚀 Next week: Loops (for, while)!")