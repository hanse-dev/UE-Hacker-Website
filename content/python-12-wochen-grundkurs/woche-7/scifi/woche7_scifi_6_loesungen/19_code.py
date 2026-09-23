import time

start = time.time()
time.sleep(0.2)
ende = time.time()
print(f"Lange genug gewartet: {ende - start >= 0.15}")
