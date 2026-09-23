def count_jumps(laps):
    total = 0
    for lap in range(1, laps + 1):
        total += lap
    return total

print(f"Jumps: {count_jumps(10)}")
