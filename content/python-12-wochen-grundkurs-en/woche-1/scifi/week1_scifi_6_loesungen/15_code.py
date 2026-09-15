# Step 1 – Collect flight data
shuttle_number = "SH-09"
destination = "Space Station Delta"
pilot = "Chen"
cargo = "Medical supplies"

# Step 2 – Protocol header
print("=== FLIGHT PROTOCOL ===")
print()

# Step 3 – Mission description
print("Shuttle " + shuttle_number + " is launching shortly.")
print("Pilot " + pilot + " is flying towards " + destination + ".")
print("On board: " + cargo + ".")

# Step 4 – Countdown
print()
print("Launch in:")
print("3... 2... 1... Launch!")

# Bonus – Coordinates
x = 347
y = 892
z = 15
print()
print("Target coordinates – X: " + str(x) + " Y: " + str(y) + " Z: " + str(z))