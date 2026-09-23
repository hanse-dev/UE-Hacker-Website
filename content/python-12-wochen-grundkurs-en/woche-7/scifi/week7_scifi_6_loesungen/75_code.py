import random

values = []
for i in range(10):
    values.append(random.randint(60, 140))
all_ok = True
total = 0
highest = values[0]
for value in values:
    if value < 60 or value > 140:
        all_ok = False
    total += value
    if value > highest:
        highest = value
average = total / len(values)
print(f"Count: {len(values)}")
print(f"All in range: {all_ok}")
print(f"Highest at least average: {highest >= average}")
