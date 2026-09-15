# Example 3: Importing multiple modules
import math
import random
import time

# Calculate a random flight duration
distance = 1000  # light-years
speed = random.uniform(0.1, 0.9)  # fraction of the speed of light
flight_time = distance / speed

print("=== Space Flight Simulation ===")
print(f"Distance: {distance} light-years")
print(f"Speed: {speed:.2f}c")
print(f"Flight time: {flight_time:.1f} years")
print(f"Waiting 2 seconds...")
time.sleep(2)
print(f"Arrived at destination system!")