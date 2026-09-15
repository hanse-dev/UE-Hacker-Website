import random

# Step 1 – Generate treasures
def generate_treasure(material, rarity):
    base_names = {
        "Gold": ["Coin", "Bar", "Crown"],
        "Crystal": ["Shard", "Fragment", "Core"],
        "Silver": ["Ring", "Chain", "Goblet"],
    }
    names = base_names.get(material, ["Treasure"])
    name = random.choice(names)
    return [f"{material}-{name}-R{rarity}", material, rarity]

# Step 2 – Calculate statistics
def calculate_treasure_stats(treasure_list):
    length = len(treasure_list)
    rarities = [t[2] for t in treasure_list]
    average = sum(rarities) / length if length > 0 else 0
    return {"count": length, "average_rarity": round(average, 1)}

# Step 3 – Create multiple treasures
treasures = []
materials = ["Gold", "Crystal", "Silver"]
for i in range(1, 11):
    mat = materials[i % 3]
    treasures.append(generate_treasure(mat, i))

print("Treasure list:")
for t in treasures:
    print(f"  {t[0]}")

# Step 4 – Filter and sort
def filter_treasures(treasure_list, search_term):
    return [t for t in treasure_list if search_term.lower() in t[0].lower()]

treasures.sort(key=lambda t: t[0])
gold_treasures = filter_treasures(treasures, "Gold")

# Step 5 – Assemble the catalogue
stats = calculate_treasure_stats(treasures)
print(f"\nNumber of treasures: {stats['count']}")
print(f"Average rarity: {stats['average_rarity']}")
print(f"Gold treasures found: {len(gold_treasures)}")
