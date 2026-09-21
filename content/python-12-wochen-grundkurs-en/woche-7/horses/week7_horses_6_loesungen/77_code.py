events = ["Rain", "Sun", "Wind", "Fog"]
import random

log = []
for floor in range(10):
    log.append(random.choice(events))
all_valid = True
for e in log:
    if e not in events:
        all_valid = False
print(f"Events: {len(log)}")
print(f"All valid: {all_valid}")
