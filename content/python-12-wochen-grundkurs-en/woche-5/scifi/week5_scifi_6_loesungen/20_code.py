def create_sector(sector_id, size):
    return {"id": sector_id, "size": size, "energy": 0}

sectors = [
    create_sector("Alpha", 5),
    create_sector("Beta", 3),
    create_sector("Gamma", 7),
]

def distribute_energy(sectors, total_energy):
    total_size = sum(s["size"] for s in sectors)
    for s in sectors:
        s["energy"] = round(total_energy * s["size"] / total_size, 1)

distribute_energy(sectors, 1500)

def plan_shifts(num_personnel, shifts):
    per_shift = num_personnel // shifts
    remainder = num_personnel % shifts
    return [per_shift + (1 if i < remainder else 0) for i in range(shifts)]

shift_plan = plan_shifts(15, 3)

def generate_station_report(sectors, total_energy, personnel):
    report = "=== STATION REPORT NEBULA-7 ===\n"
    for s in sectors:
        report += f"  Sector {s['id']}: Size {s['size']}, Energy {s['energy']} EU\n"
    report += f"Total energy: {total_energy} EU\n"
    report += f"Personnel per shift: {personnel}"
    return report

print(generate_station_report(sectors, 1500, shift_plan))

def energy_emergency(sector, min_energy=100):
    if sector["energy"] < min_energy:
        return f"EMERGENCY: Sector {sector['id']} – only {sector['energy']} EU available!"
    return None

for s in sectors:
    warning = energy_emergency(s)
    if warning:
        print(warning)