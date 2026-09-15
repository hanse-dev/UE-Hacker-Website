# Example: Consulting the oracle and converting the answer
# (run locally - comment out in static environments if needed)

name = input("What is your hero's name? ")
level_str = input("What level are they? ")
level = int(level_str)   # Fire -> Earth (str -> int)

print(f"Welcome, {name}!")
print(f"{name} is at level {level}.")
print(f"In 5 levels you will reach level {level + 5}.")
