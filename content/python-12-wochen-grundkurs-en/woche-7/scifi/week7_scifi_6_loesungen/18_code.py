import random

objectives = ["Gather resources", "Scout the enemy", "Secure outpost", "Investigate signal"]
planets = ["Kepler-9b", "Proxima-II", "Orion-5", "Nova-Prime"]
danger_levels = [1, 2, 3, 4, 5]
crew_members = ["Commander Zara", "Pilot Rex", "Dr. Nova", "Engineer Kai"]

# Steps 2 & 3: Mission briefing
print("=== MISSION BRIEFING ===")
total_danger = 0
for i in range(1, 4):
    objective = random.choice(objectives)
    planet = random.choice(planets)
    danger = random.choice(danger_levels)
    leader = random.choice(crew_members)  # Bonus
    total_danger += danger
    print(f"\nMission {i}:")
    print(f"  Objective:    {objective}")
    print(f"  Planet:       {planet}")
    print(f"  Danger level: {danger}/5")
    print(f"  Leader:       {leader}")

average_danger = round(total_danger / 3, 1)
print(f"\nAverage danger level: {average_danger}")