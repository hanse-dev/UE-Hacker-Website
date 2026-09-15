# Example 2: Function with conditional return
def check_system_status(energy_level):
    """Checks whether the system is ready for a mission"""
    if energy_level >= 75:
        return "System ready for mission!"
    else:
        return f"Still {75 - energy_level}% energy needed"

print("=== System Status Check ===")
status1 = check_system_status(60)
print(f"Energy 60%: {status1}")

status2 = check_system_status(90)
print(f"Energy 90%: {status2}")

status3 = check_system_status(70)
print(f"Energy 70%: {status3}")