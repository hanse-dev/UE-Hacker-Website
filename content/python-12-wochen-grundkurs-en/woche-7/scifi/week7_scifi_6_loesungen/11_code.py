import math as m
import random as r
import time as t

# Step 1: Try out the modules
print("=== Nebula-7 Module Bank ===")
print(f"math.pi: {m.pi}")
print(f"Random number (1-10): {r.randint(1, 10)}")

# Step 2: Wait time simulation
wait_time = r.randint(1, 3)
print(f"\nSystem loading ... ({wait_time} seconds)")
t.sleep(wait_time)
print("System ready!")

# Step 3: Flight path calculation
angle_degrees = 90
angle_radians = m.radians(angle_degrees)
flight_height = m.sin(angle_radians)
print(f"\nFlight path at {angle_degrees}°: Height = {flight_height:.2f}")

# Step 4: Crew generator
crew = ["Commander Zara", "Pilot Rex", "Dr. Nova", "Engineer Kai", "Scientist Luna"]
selected_member = r.choice(crew)
print(f"\nSelected crew member: {selected_member}")

# Bonus: datetime
from datetime import datetime
now = datetime.now()
print(f"Station time: {now.strftime('%H:%M:%S')}")