# Step 1: Artifacts as tuples
artifact1 = ("Fire Sword", 30, "Fire")
artifact2 = ("Ice Ring", 12, "Ice")
print(f"Artifact 1: {artifact1} | Length: {len(artifact1)}")
print(f"Artifact 2: {artifact2} | Length: {len(artifact2)}")

# Step 2: Tuple unpacking
name1, strength1, element1 = artifact1
print(f"\nUnpacking Artifact 1: Name={name1}, Strength={strength1}, Element={element1}")

name2, strength2, element2 = artifact2
print(f"Unpacking Artifact 2: Name={name2}, Strength={strength2}, Element={element2}")

# Step 3: Artifact dictionary
artifacts = {
    "Fire Staff": ("Staff", 15, "Fire"),
    "Ice Ring": ("Ring", 5, "Ice"),
    "Lightning Axe": ("Axe", 25, "Lightning")
}
print(f"\nArtifact dictionary: {artifacts}")
print(f"Fire Staff: {artifacts['Fire Staff']}")

# Step 4: Compare strengths
difference = abs(strength1 - strength2)
print(f"\nStrength difference between {name1} and {name2}: {difference}")

# Bonus: 4D artifact
artifact_4d = ("Time Staff", 50, "Time", 3)  # Name, Strength, Element, Dimensions
a_name, a_st, a_el, a_dim = artifact_4d
print(f"\nBonus 4D artifact: {a_name} | {a_dim} dimensions")