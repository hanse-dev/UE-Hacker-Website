def create_mission(name, target, priority):
    return {"name": name, "target": target, "priority": priority, "status": "active"}

missions = [
    create_mission("Operation Nova", "Andromeda Cluster", 5),
    create_mission("Recon X", "Oort Belt", 2),
    create_mission("Rescue Alpha", "Titan Station", 4),
]

print("=== Mission Database ===")
for m in missions:
    print(f"  {m['name']} | Target: {m['target']} | Prio: {m['priority']}")

high_priority = [m for m in missions if m["priority"] >= 4]
print(f"\nHigh Priority: {[m['name'] for m in high_priority]}")

print()
print("🎉 Boss Quest completed!")
print("🏆 You defeated the Data Archivist of Infinite Arrays!")
print("⭐ Title earned: Master of Data Collections")