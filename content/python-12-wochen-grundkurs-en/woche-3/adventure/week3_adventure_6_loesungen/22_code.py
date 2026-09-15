# Step 1 – Quest phases
phase1_ok = True
phase2_ok = True
phase3_ok = False
phase4_ok = True
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
    print("Danger level 1: Easy peasy")
elif danger_level == 2:
    print("Danger level 2: Easy")
elif danger_level == 3:
    print("Danger level 3: Medium")
elif danger_level == 4:
    print("Danger level 4: Hard")
else:
    print("Danger level 5: EXTREME!")

# Step 3 – Random events
monster_attack = False
trap_triggered = True
treasure_found = True

if monster_attack:
    print("⚔️ Monster attack! -20 HP")
if trap_triggered:
    print("🪤 Trap triggered! -10 HP")
if treasure_found:
    print("💰 Treasure found! +200 XP")

# Step 4 – Success condition
print(f"Successful phases: {successful_phases}/5")
if successful_phases >= 4 and danger_level <= 3:
    print("🏆 Quest completed successfully!")
else:
    print("Quest not fully passed.")

# Step 5 – Special actions
if danger_level >= 4 and successful_phases < 3:
    print("🚨 Rescue required!")

# Step 6 – Evaluation
total_points = successful_phases * 100 - danger_level * 20
success_rate = (successful_phases / 5) * 100
print(f"Total points: {total_points}")
print(f"Success rate: {success_rate:.0f}%")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Sphinx of the Riddle Paths!")
print("⭐ Title earned: Master of Decisions")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 3!")
print("📚 Next week: Loops (for, while)!")