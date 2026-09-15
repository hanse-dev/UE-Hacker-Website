# Example: A waiting ritual and the current hour
import time
from datetime import datetime

print("A ritual begins to take effect...")
time.sleep(1)
print("The ritual is complete!")

now = datetime.now()
print(f"\nCurrent time: {now.strftime('%H:%M:%S')}")

if 6 <= now.hour < 18:
    print("It is day – the Sun Gates of the archive stand open.")
else:
    print("It is night – only the Moon Gates of the archive are open.")
