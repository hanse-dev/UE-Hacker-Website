import random

with open("numbers.txt", "w") as f:
    for i in range(10):
        f.write(str(random.randint(1, 100)) + "\n")
numbers = []
with open("numbers.txt", "r") as f:
    for line in f:
        numbers.append(int(line))
all_ok = True
for n in numbers:
    if n < 1 or n > 100:
        all_ok = False
print(f"Count: {len(numbers)}")
print(f"All in range: {all_ok}")
