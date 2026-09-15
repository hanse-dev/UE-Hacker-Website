import random

fleet = [
    {"name": "Nebula-1", "ship_class": "Cruiser"},
    {"name": "Nebula-2", "ship_class": "Frigate"},
    {"name": "Nebula-3", "ship_class": "Destroyer"},
]

def describe_fleet_movement(ship, target):
    return f"{ship['name']} ({ship['ship_class']}) flies to {target}."

def calculate_fleet_efficiency(formation):
    efficiency = {"Wedge": 80, "Line": 65, "Defence": 90}
    return efficiency.get(formation, 50)

def communication_stable(distance_km):
    return distance_km <= 10000

def create_fleet_report(fleet, efficiency):
    report = "=== FLEET REPORT ===\n"
    report += f"Ships: {len(fleet)}\n"
    for s in fleet:
        report += f"  {s['name']} – {s['ship_class']}\n"
    report += f"Total efficiency: {efficiency}%\n"
    return report

for s in fleet:
    print(describe_fleet_movement(s, "Sector Gamma-7"))

formation = "Wedge"
efficiency = calculate_fleet_efficiency(formation)
print(f"\nFormation: {formation} → Efficiency: {efficiency}%")

for distance in [5000, 12000]:
    status = "stable" if communication_stable(distance) else "unstable"
    print(f"Communication at {distance} km: {status}")

print()
print(create_fleet_report(fleet, efficiency))

# Bonus – fleet comparison
fleet_b_efficiency = calculate_fleet_efficiency("Line")
print(f"Fleet A (Wedge): {efficiency}% | Fleet B (Line): {fleet_b_efficiency}%")
if efficiency >= fleet_b_efficiency:
    print("Fleet A has higher total efficiency.")
else:
    print("Fleet B has higher total efficiency.")