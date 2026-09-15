# Example 2: Function with conditional return
def check_level(level):
    """Checks whether a character is ready for a quest"""
    if level >= 10:
        return "Ready for the quest!"
    else:
        return f"Still {10 - level} levels needed"

print("=== Level Check ===")
status1 = check_level(5)
print(f"Level 5: {status1}")

status2 = check_level(12)
print(f"Level 12: {status2}")

status3 = check_level(8)
print(f"Level 8: {status3}")