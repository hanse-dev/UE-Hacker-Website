# Step 1 – All horse numbers 1 to 20
print("=== All Horse Numbers ===")
for i in range(1, 21):
    print(f"Horse: {i}")

# Step 2 – Even numbers only
print()
print("=== Even Horse Numbers ===")
for i in range(2, 21, 2):
    print(f"Even Horse: {i}")

# Step 2 – Reverse 20 to 1
print()
print("=== Reverse Countdown ===")
for i in range(20, 0, -1):
    print(f"Horse: {i}")

# Step 3 – Total training hours (each horse 1 hour)
training_hours = 0
for i in range(1, 21):
    training_hours += 1
print()
print(f"Total training hours for 20 horses: {training_hours}h")

# Bonus – Training plan table
print()
print("=== Training Plan ===")
for i in range(1, 11):
    print(f"Horse {i:2d} | Training sessions: {i * i}")