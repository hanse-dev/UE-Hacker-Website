# 🔍 Exercises with append() and insert()

# Example 1: Adding elements
mission_log = []
print(f"Empty mission log: {mission_log}")

# Add to the end with append()
mission_log.append("Planet Exploration")
print(f"After append: {mission_log}")

mission_log.append("Asteroid Mining")
mission_log.append("First Contact Mission")
print(f"Fully populated: {mission_log}")

# Insert at a specific position with insert()
mission_log.insert(0, "System Check")  # At the beginning
print(f"After insert(0): {mission_log}")

mission_log.insert(2, "Maintenance")  # At position 2
print(f"After insert(2): {mission_log}")