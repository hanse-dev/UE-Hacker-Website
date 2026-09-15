# Example 3: Advanced random functions
import random
import math

print("=== Advanced Random Functions ===")

# Normal distribution for energy values
print("Energy consumption (normal distribution):")
for i in range(5):
    energy = random.gauss(100, 20)  # mean 100, std dev 20
    print(f"  System {i+1}: {max(0, energy):.1f} MW")

# Exponential distribution for waiting times
print("\nWaiting times (exponential distribution):")
for i in range(5):
    wait = random.expovariate(0.1)  # lambda = 0.1
    print(f"  Wait time {i+1}: {wait:.1f} minutes")

# Random point in a circle
def random_point_circle(radius):
    angle = random.uniform(0, 2 * math.pi)
    r = radius * math.sqrt(random.random())
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return x, y

x, y = random_point_circle(10)
print(f"\nRandom point in circle r=10: ({x:.2f}, {y:.2f})")