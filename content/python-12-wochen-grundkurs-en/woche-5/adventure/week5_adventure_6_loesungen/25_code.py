def sum_to(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total

print(f"Sum: {sum_to(10)}")
