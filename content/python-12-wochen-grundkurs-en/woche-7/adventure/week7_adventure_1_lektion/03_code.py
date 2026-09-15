# Example 1: Importing modules
import random
import time

print(f"Random number: {random.randint(1, 10)}")

# Import with a nickname
import random as r
print(f"Again (via nickname r): {r.randint(1, 10)}")

# Import only specific spells
from string import ascii_letters
print(f"First 5 letters of the rune alphabet: {ascii_letters[:5]}")
