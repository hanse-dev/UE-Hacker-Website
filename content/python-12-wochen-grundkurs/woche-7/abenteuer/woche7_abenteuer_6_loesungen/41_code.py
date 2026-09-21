import random
import time

wartezeit = random.uniform(0.1, 0.3)
print("Ritual beginnt")
start = time.time()
time.sleep(wartezeit)
ende = time.time()
print("Ritual vollendet")
print(f"Gewartet: {ende - start >= 0.08}")
