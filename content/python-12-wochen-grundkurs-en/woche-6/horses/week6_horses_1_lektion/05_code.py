# Example 3: Lists inside lists (nested lists)
horse_party = [
    ["Thunder", "Hanoverian", 8, "Show Jumping"],
    ["Luna", "Icelandic", 5, "Dressage"],
    ["Storm", "Quarter Horse", 6, "Western"]
]

print("=== Horse Party ===")
print(f"First horse: {horse_party[0]}")
print(f"Name of first horse: {horse_party[0][0]}")
print(f"Breed of second horse: {horse_party[1][1]}")
print(f"Age of third horse: {horse_party[2][2]} years")
print(f"Discipline of first horse: {horse_party[0][3]}")