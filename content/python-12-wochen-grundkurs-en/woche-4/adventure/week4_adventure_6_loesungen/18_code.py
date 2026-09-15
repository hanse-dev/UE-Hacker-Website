# Steps 1–3 – Find prime numbers (magic numbers) from 2 to 100
magic_numbers = []

for number in range(2, 101):
    is_prime = True
    # Step 2 – Prime test with nested loop
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        magic_numbers.append(number)
        print(f"★ Magic number found: {number}")

# Step 4 – Visualisation
print()
print(f"Total of {len(magic_numbers)} magic numbers between 2 and 100:")
visualisation = ""
for n in magic_numbers:
    visualisation += f"★{n} "
print(visualisation)
print(f"Largest magic number: {magic_numbers[-1]}")
print(f"Sum of all magic numbers: {sum(magic_numbers)}")