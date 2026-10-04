found = 0
for number in range(2, 31):
    is_prime = True
    for a in range(2, number):
        for b in range(2, number):
            if a * b == number:
                is_prime = False
    if is_prime:
        print(f"Prime: {number}")
        found += 1
print(f"Primes found: {found}")
