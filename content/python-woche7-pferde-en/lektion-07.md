# 🔬 Lesson 7: More math: factorial, gcd and primes

```python
import math

print(math.factorial(5))   # 5 · 4 · 3 · 2 · 1 = 120
print(math.gcd(24, 36))    # greatest common divisor: 12
print(math.lcm(12, 15))    # least common multiple: 60

angle = math.radians(90)   # convert degrees to radians
print(math.sin(angle))     # sine: 1.0
```

Angle functions (`sin`, `cos`, `tan`) work in **radians** – with `math.radians(degrees)` you convert degrees.

**Primes:** A number is a **prime** if it is only divisible by 1 and itself. You check divisibility with `%`:

```python
def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False    # found: divisible by something else
    return True
```
