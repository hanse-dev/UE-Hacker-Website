import random

# Steps 1-2: Time loop
jumps = 0
year = 2024

while True:
    jump = random.choice([-50, -20, -10, 10, 25, 100])
    year += jump
    jumps += 1
    print(f"Jump {jumps}: Year {year} (jump: {jump:+d})")

    # Step 3: Check condition
    if 1900 <= year <= 2100:
        print(f"Stable time found! {jumps} jumps needed.")
        break
    if jumps >= 20:
        print("Time paradox too strong! Aborting.")
        break