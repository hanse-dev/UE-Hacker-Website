# Example 2: Function with conditional return
def check_training_level(experience):
    """Checks whether a horse is ready for advanced training"""
    if experience >= 50:
        return "Ready for advanced training!"
    else:
        return f"Still {50 - experience} training sessions needed"

print("=== Training Level Check ===")
status1 = check_training_level(25)
print(f"Experience 25: {status1}")

status2 = check_training_level(75)
print(f"Experience 75: {status2}")

status3 = check_training_level(40)
print(f"Experience 40: {status3}")