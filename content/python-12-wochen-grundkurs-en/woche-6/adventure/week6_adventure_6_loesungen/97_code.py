numbers = []
for number in range(1, 21):
    numbers.append(number)
print(f"Count: {len(numbers)}")
print(numbers[1::2])
print(sorted(numbers, reverse=True)[:5])
