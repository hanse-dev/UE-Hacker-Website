def count_signals(sectors):
    total = 0
    for sector in range(1, sectors + 1):
        total += sector
    return total

print(f"Signals: {count_signals(10)}")
