# Step 1 – Create divisions
def create_division(division_id, size):
    return {"id": division_id, "size": size, "mana": 0}

divisions = [
    create_division("A", 10),
    create_division("B", 6),
    create_division("C", 8),
]

# Step 2 – Distribute mana
def distribute_mana(divisions, total_mana):
    total_size = sum(d["size"] for d in divisions)
    for d in divisions:
        d["mana"] = int(total_mana * d["size"] / total_size)

distribute_mana(divisions, 1000)

# Step 3 – Plan wizard shifts
def plan_wizard_shifts(num_wizards, shifts):
    per_shift = num_wizards // shifts
    remainder = num_wizards % shifts
    return [per_shift + (1 if i < remainder else 0) for i in range(shifts)]

shift_plan = plan_wizard_shifts(24, 3)

# Step 4 – Guild report
def generate_guild_report(divisions, total_mana, wizards_per_shift):
    report = "=== GUILD REPORT ===\n"
    for d in divisions:
        report += f"Division {d['id']}: Size {d['size']}, Mana {d['mana']}\n"
    report += f"Total mana: {total_mana}\n"
    report += f"Wizards per shift: {wizards_per_shift}"
    return report

print(generate_guild_report(divisions, 1000, shift_plan))

# Bonus – mana warning
def check_mana(division, min_mana=100):
    if division["mana"] < min_mana:
        return f"WARNING: Division {division['id']} has only {division['mana']} mana!"
    return None

for d in divisions:
    warning = check_mana(d, 200)
    if warning:
        print(warning)