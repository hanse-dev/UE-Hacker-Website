# Problem: rounds is never increased
rounds = 0
while rounds < 5:
    print(f"Round {rounds}")
    rounds += 1  # This was missing!