# Example 3: Importing multiple modules
import math
import random
import time

# Calculate a random riding duration
distance = 1000  # meters
speed = random.uniform(0.1, 0.9)  # fraction of max speed
riding_time = distance / speed

print("=== Riding Simulation ===")
print(f"Distance: {distance} meters")
print(f"Speed: {speed:.2f} m/s")
print(f"Riding time: {riding_time:.1f} minutes")
print(f"Waiting 2 seconds...")
time.sleep(2)
print(f"Arrived at the destination!")