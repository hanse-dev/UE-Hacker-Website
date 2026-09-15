# Step 1 – Define missions
m1_goal = "Place Alpha Centauri probe"
m1_days = 180
m1_cost = 85000000
m1_crew = 12
m1_success = 0.75

m2_goal = "Expand moon station"
m2_days = 30
m2_cost = 25000000
m2_crew = 6
m2_success = 0.95

# Step 2 – Mission protocol
print("=== MISSION PROTOCOL ===")
print(f"Mission 1: {m1_goal}")
print(f"  Duration: {m1_days} days, Cost: {m1_cost} CC, Crew: {m1_crew}, Success: {m1_success * 100}%")
print(f"Mission 2: {m2_goal}")
print(f"  Duration: {m2_days} days, Cost: {m2_cost} CC, Crew: {m2_crew}, Success: {m2_success * 100}%")
print()

# Step 3 – Totals
total_cost = m1_cost + m2_cost
total_crew = m1_crew + m2_crew
print(f"Total cost: {total_cost} CC")
print(f"Total crew: {total_crew} people")
print()

# Step 4 – Forecast success
expected1 = m1_cost * m1_success
expected2 = m2_cost * m2_success
print(f"Expected return on investment M1: {expected1:.0f} CC")
print(f"Expected return on investment M2: {expected2:.0f} CC")
print()

# Step 5 – Compare missions
print(f"Cost difference: {m1_cost - m2_cost} CC")
print(f"Duration difference: {m1_days - m2_days} days")
print(f"Success difference: {(m2_success - m1_success) * 100}%")

# Step 6 – Profitability
m2_more_profitable = expected2 > expected1
print(f"Mission 2 more profitable: {m2_more_profitable}")

# Bonus: cost per crew member
print()
print(f"Cost per crew member M1: {m1_cost / m1_crew:.0f} CC")
print(f"Cost per crew member M2: {m2_cost / m2_crew:.0f} CC")

print()
print("🎉 Final challenge complete!")
print("🏆 You defeated the Shapeshifter of Unstable Data!")
print("⭐ Title earned: Master of Quantum Types")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 2!")
print("🚀 Next week: Conditions (if-else)!")