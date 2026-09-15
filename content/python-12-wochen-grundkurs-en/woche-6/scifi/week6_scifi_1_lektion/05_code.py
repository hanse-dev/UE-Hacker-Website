# Example 3: Lists inside lists (nested lists)
crew_members = [
    ["Captain Alex", "Commander", 35, "Alpha-Quadrant"],
    ["Dr. Zara", "Scientist", 28, "Beta-Quadrant"],
    ["Lt. Nova", "Pilot", 26, "Gamma-Sector"]
]

print("=== Crew Members ===")
print(f"First crew member: {crew_members[0]}")
print(f"Name of first: {crew_members[0][0]}")
print(f"Rank of second: {crew_members[1][1]}")
print(f"Age of third: {crew_members[2][2]} years")
print(f"Sector of first: {crew_members[0][3]}")