# Problem: time is never incremented
time = 0
while time < 5:
    print(f"Time {time}")
    time += 1  # This was missing!