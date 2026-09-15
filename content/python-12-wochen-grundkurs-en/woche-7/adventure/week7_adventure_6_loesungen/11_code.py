import random as r
import time as t
import string

# Step 1: Summon the three guardians
print("=== The Three Guardians ===")
print(f"random.randint(1, 6): {r.randint(1, 6)}")
print(f"len(string.ascii_letters): {len(string.ascii_letters)}")
print(f"time.time(): {t.time():.2f}")

# Step 2: Time Guardian's waiting ritual
waiting_time = r.uniform(1, 3)
print(f"\nThe seal begins to glow ... ({waiting_time:.1f} seconds)")
t.sleep(waiting_time)
print("The seal glows brightly!")

# Step 3: Word Guardian's rune fragment
fragment = r.choice(string.ascii_letters)
print(f"\nRune fragment found: {fragment}")

# Step 4: Open the seal
print(f"\nAll three guardians are defeated – the seal opens!")

# Bonus: timestamp
from datetime import datetime
now = datetime.now()
print(f"Opened on: {now.strftime('%d.%m.%Y at %H:%M:%S')}")
