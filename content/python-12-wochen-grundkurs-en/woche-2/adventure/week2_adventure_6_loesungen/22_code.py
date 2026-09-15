# Step 1 - Define quests
q1_goal = "Clear the Dragon's Lair"
q1_duration = 7
q1_reward = 1200
q1_group_size = 5
q1_success = 0.8

q2_goal = "Recover lost relics"
q2_duration = 3
q2_reward = 600
q2_group_size = 3
q2_success = 0.95

# Step 2 - Quest log
print("=== QUEST LOG ===")
print(f"Quest 1: {q1_goal}")
print(f"  Duration: {q1_duration} days, Reward: {q1_reward} gold, Group: {q1_group_size}, Success: {q1_success * 100}%")
print(f"Quest 2: {q2_goal}")
print(f"  Duration: {q2_duration} days, Reward: {q2_reward} gold, Group: {q2_group_size}, Success: {q2_success * 100}%")
print()

# Step 3 - Totals
total_reward = q1_reward + q2_reward
total_group = q1_group_size + q2_group_size
print(f"Total reward: {total_reward} gold")
print(f"Total group size: {total_group} people")
print()

# Step 4 - Forecast success
expected_reward1 = q1_reward * q1_success
expected_reward2 = q2_reward * q2_success
print(f"Expected reward Quest 1: {expected_reward1} gold")
print(f"Expected reward Quest 2: {expected_reward2} gold")
print()

# Step 5 - Compare quests
print(f"Reward difference: {q1_reward - q2_reward} gold")
print(f"Duration difference: {q1_duration - q2_duration} days")
print(f"Success difference: {(q2_success - q1_success) * 100}%")

# Step 6 - Profitability
q1_profitable = expected_reward1 > expected_reward2
print(f"Quest 1 more profitable: {q1_profitable}")

# Bonus: reward per group member
print()
print(f"Reward per person Quest 1: {q1_reward / q1_group_size} gold")
print(f"Reward per person Quest 2: {q2_reward / q2_group_size} gold")

print()
print("🎉 Boss Quest complete!")
print("🏆 You have defeated the Golem of Confused Forms!")
print("⭐ The Tower Guardian nods: Master of the Four Elements!")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 2!")
print("📚 Next week: Conditions (if-else)!")
