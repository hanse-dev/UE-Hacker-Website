def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(f"17: {is_prime(17)}")
print(f"18: {is_prime(18)}")
