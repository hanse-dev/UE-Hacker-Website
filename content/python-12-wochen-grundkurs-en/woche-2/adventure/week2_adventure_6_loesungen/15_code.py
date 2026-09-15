# Step 1 - Consult 🔥 Fire
name = input("What is your name? ")

# Step 2 - Consult 🪨 Earth
age = int(input("How old are you? "))

# Step 3 - Consult 💧 Water
magic_power = float(input("Your magic power (e.g. 7.5)? "))

# Step 4 - Determine 💨 Air
is_powerful = magic_power > 5.0

print(f"\n=== PROPHECY FOR {name.upper()} ===")
print(f"Age: {age} years")
print(f"Magic power: {magic_power}")
if is_powerful:
    print(f"{name}, your power exceeds the ordinary!")
else:
    print(f"{name}, your power will grow with time.")

# Bonus: elements of the answers
print(f"\nElement check:")
print(f"  Name:         {type(name)}")
print(f"  Age:          {type(age)}")
print(f"  Magic power:  {type(magic_power)}")
print(f"  Is powerful:  {type(is_powerful)}")
