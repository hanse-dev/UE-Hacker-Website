number = 15
is_prime = True
for a in range(2, number):
    for b in range(2, number):
        if a * b == number:
            is_prime = False
print(f"{number} is prime: {is_prime}")
