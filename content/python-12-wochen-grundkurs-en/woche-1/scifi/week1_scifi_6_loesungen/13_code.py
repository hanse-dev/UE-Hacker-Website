# Step 1 – Create ship data
ship_type = "Cruiser"
registration = "NCC-2048"
year_built = 2387

# Step 2 – Output structured data
print("=== SHIP PROTOCOL ===")
print("Ship type: " + ship_type)
print("Registration: " + registration)
print("Year built: " + str(year_built))

# Step 3 – Complete report
print()
print(ship_type + " " + registration + ", built " + str(year_built) + ", is ready for duty.")
print("=== END PROTOCOL ===")