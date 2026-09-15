# Step 1 – Define training units
u1_goal = "Dressage Exam Class A"
u1_days = 5
u1_cost = 350
u1_participants = 8
u1_success = 0.85

u2_goal = "Show Jumping Preparation"
u2_days = 3
u2_cost = 200
u2_participants = 5
u2_success = 0.90

# Step 2 – Training protocol
print("=== TRAINING PROTOCOL ===")
print(f"Unit 1: {u1_goal}")
print(f"  Duration: {u1_days} days, Cost: {u1_cost} £, Participants: {u1_participants}, Success: {u1_success * 100}%")
print(f"Unit 2: {u2_goal}")
print(f"  Duration: {u2_days} days, Cost: {u2_cost} £, Participants: {u2_participants}, Success: {u2_success * 100}%")
print()

# Step 3 – Totals
total_cost = u1_cost + u2_cost
total_participants = u1_participants + u2_participants
print(f"Total cost: {total_cost} £")
print(f"Total participants: {total_participants}")
print()

# Step 4 – Forecast success
expected1 = u1_participants * u1_success
expected2 = u2_participants * u2_success
print(f"Expected successful participants U1: {expected1}")
print(f"Expected successful participants U2: {expected2}")
print()

# Step 5 – Compare units
print(f"Cost difference: {u1_cost - u2_cost} £")
print(f"Duration difference: {u1_days - u2_days} days")
print(f"Success difference: {(u2_success - u1_success) * 100}%")

# Step 6 – Efficiency
u1_more_efficient = (u1_cost / u1_participants) < (u2_cost / u2_participants)
print(f"Unit 1 more cost-efficient: {u1_more_efficient}")

# Bonus: cost per participant
print()
print(f"Cost per participant U1: {u1_cost / u1_participants:.2f} £")
print(f"Cost per participant U2: {u2_cost / u2_participants:.2f} £")

print()
print("🎉 Final challenge complete!")
print("🏆 You mastered the dressage horse with stubborn hooves!")
print("⭐ Title earned: Master of Hoof-Beat Types")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 2!")
print("🐴 Next week: Conditions (if-else)!")