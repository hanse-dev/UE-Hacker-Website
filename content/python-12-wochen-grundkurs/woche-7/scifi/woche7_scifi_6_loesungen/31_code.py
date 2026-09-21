def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(f"17: {ist_primzahl(17)}")
print(f"18: {ist_primzahl(18)}")
