# Prime numbers from 2 to 100
primes = []
for number in range(2, 101):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)

print(f"Primes up to 100: {primes}")
print(f"Count: {len(primes)}")
print(f"Largest prime: {primes[-1]}")
print(f"Sum: {sum(primes)}")