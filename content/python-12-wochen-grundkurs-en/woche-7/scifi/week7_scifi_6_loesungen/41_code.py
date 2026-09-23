import random
import time

waiting_time = random.uniform(0.1, 0.3)
print("Ritual begins")
start = time.time()
time.sleep(waiting_time)
end = time.time()
print("Ritual complete")
print(f"Waited: {end - start >= 0.08}")
