# Problem: counter is never incremented
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1  # This was missing!