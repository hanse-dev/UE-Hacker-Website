# Step 1 – Generate spell names
def generate_spell_name(element_type, tier):
    return f"{element_type.upper()}-T{tier}"

# Step 2 – Calculate spell power
def calculate_power(complexity, element_type):
    factors = {"Fire": 1.5, "Water": 1.0, "Earth": 0.8, "Air": 1.2}
    factor = factors.get(element_type, 1.0)
    return min(100, int(complexity * factor * 10))

# Step 3 – Create spell data
def create_spell(element_type, tier, complexity):
    name = generate_spell_name(element_type, tier)
    power = calculate_power(complexity, element_type)
    return {"name": name, "element": element_type, "tier": tier, "power": power}

# Step 4 – Manage spellbook
spellbook = []

def save_spell(book, spell):
    book.append(spell)

# Step 5 – Use generator
save_spell(spellbook, create_spell("Fire", 3, 7))
save_spell(spellbook, create_spell("Water", 1, 4))
save_spell(spellbook, create_spell("Earth", 2, 5))
save_spell(spellbook, create_spell("Air", 4, 6))
save_spell(spellbook, create_spell("Fire", 5, 9))

print("=== SPELLBOOK ===")
for s in spellbook:
    print(f"{s['name']} – Element: {s['element']}, Tier: {s['tier']}, Power: {s['power']}")

total_power = sum(s["power"] for s in spellbook)
average = total_power // len(spellbook)
print(f"\nSpell count: {len(spellbook)}")
print(f"Average power: {average}")

# Bonus – sorted by power
print("\n--- Sorted by power ---")
for s in sorted(spellbook, key=lambda s: s["power"], reverse=True):
    print(f"  {s['name']}: {s['power']}")