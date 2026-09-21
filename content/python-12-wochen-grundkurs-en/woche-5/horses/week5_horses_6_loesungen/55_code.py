def calculate_time_bonus(seconds):
    if seconds <= 60:
        return 20
    elif seconds <= 90:
        return 10
    else:
        return 0

print(f"Bonus: {calculate_time_bonus(55)}")
print(f"Bonus: {calculate_time_bonus(80)}")
print(f"Bonus: {calculate_time_bonus(100)}")
