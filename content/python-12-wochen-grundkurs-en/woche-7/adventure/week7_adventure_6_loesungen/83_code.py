primes = []
for n in range(2, 101):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        primes.append(n)
print(f"Count: {len(primes)}")
print(f"Largest: {primes[-1]}")
