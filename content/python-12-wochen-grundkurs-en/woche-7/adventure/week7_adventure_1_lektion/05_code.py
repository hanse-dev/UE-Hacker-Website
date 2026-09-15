# Example 3: Using several modules together
import random
import time

print("=== The Archivist tests your first invocation ===")
waiting_time = random.uniform(0.5, 1.5)
print(f"A seal spell begins to activate ({waiting_time:.1f} seconds)...")
time.sleep(waiting_time)
print("The first seal lights up!")
