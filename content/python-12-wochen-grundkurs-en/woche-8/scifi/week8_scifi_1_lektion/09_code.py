# Example 2: Tuples are immutable
system_status = ("Online", "Stable", "Active")
print(f"System status: {system_status}")

# Access works fine
print(f"Status: {system_status[0]}")

# Changing does NOT work!
try:
    system_status[0] = "Offline"
except TypeError as e:
    print(f"Error: {e}")

# But tuples inside lists can be replaced
systems = [
    ("Navigation", "Online"),
    ("Drive", "Stable"),
    ("Communications", "Active")
]
systems[1] = ("Drive", "Offline")
print(f"\nSystems after change: {systems}")