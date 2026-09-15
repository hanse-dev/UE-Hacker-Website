# Example 3: Lists within lists (nested lists)
hero_party = [
    ["Aria", "Mage", 15],
    ["Thorin", "Warrior", 12],
    ["Luna", "Rogue", 8]
]

print("=== Hero Party ===")
print(f"First hero: {hero_party[0]}")
print(f"Name of first hero: {hero_party[0][0]}")
print(f"Class of second hero: {hero_party[1][1]}")
print(f"Level of third hero: {hero_party[2][2]}")