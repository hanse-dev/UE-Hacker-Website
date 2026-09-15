import math as m
import random as r
import time as t

# Step 1: Try out the tools
print("=== Ranch Tools ===")
print(f"math.pi: {m.pi}")
print(f"Random number (1-10): {r.randint(1, 10)}")

# Step 2: Wait time simulation
wait_time = r.randint(1, 3)
print(f"\nWaiting for horse ... ({wait_time} seconds)")
t.sleep(wait_time)
print("Horse is ready!")

# Step 3: Jump calculation
angle_deg = 90
angle_rad = m.radians(angle_deg)
jump_height = m.sin(angle_rad)
print(f"\nJump height at {angle_deg}°: {jump_height:.2f} m")

# Step 4: Rider generator
riders = ["Lena", "Tom", "Sophie", "Max", "Clara"]
selected_rider = r.choice(riders)
print(f"\nSelected rider: {selected_rider}")

# Bonus: datetime
from datetime import datetime
now = datetime.now()
print(f"Training time: {now.strftime('%H:%M:%S')}")