# Step 1 – All numbers 1 to 20
print("=== All Numbers 1-20 ===")
for i in range(1, 21):
    print(f"Number: {i}")

# Step 2 – Only even numbers
print()
print("=== Even Numbers ===")
for i in range(2, 21, 2):
    print(f"Even: {i}")

# Step 2 – Reverse 20 to 1
print()
print("=== Countdown ===")
for i in range(20, 0, -1):
    print(f"Countdown: {i}")

# Step 3 – Sum 1 to 100
total = 0
for i in range(1, 101):
    total += i
print()
print(f"Sum from 1 to 100: {total}")

# Bonus – Multiplication triangle
print()
print("=== Magic Square Table ===")
for i in range(1, 11):
    print(f"{i} × {i} = {i * i}")