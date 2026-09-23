import time

start = time.time()
time.sleep(0.2)
end = time.time()
print(f"Waited long enough: {end - start >= 0.15}")
