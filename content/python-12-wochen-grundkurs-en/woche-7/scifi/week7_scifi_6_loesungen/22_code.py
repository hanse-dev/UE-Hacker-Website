import random
import math

sector_types = ["Asteroid Field", "Nebula", "Open Space", "Ion Storm", "Rest Zone"]
events = ["Enemy contact", "Resource find", "Empty sector", "Distress signal", "Quiet"]
dangerous_sectors = ["Asteroid Field", "Ion Storm", "Enemy contact"]

print("=== EXPLORATION REPORT ===")
fuel = 0
for i in range(1, 6):
    sector_type = random.choice(sector_types)
    event = random.choice(events)
    is_dangerous = sector_type in dangerous_sectors or event in dangerous_sectors
    cost = 2 if is_dangerous else 1
    fuel += cost
    status = "⚠️ DANGEROUS" if is_dangerous else "✓ Safe"
    print(f"Sector {i}: {sector_type} | {event} | {status} | Cost: {cost}")

print(f"\nTotal fuel consumption: {math.ceil(fuel)} units")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Code Archivist of Infinite Functions!")
print("⭐ Title received: Master of Modules")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 7!")
print("📚 Next week: Dictionaries and Tuples!")