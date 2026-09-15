# Step 1 – Access data
age = 14
has_helmet = True
has_permission = False

# Steps 2 & 3 – Access rule
if age >= 12 or has_helmet or has_permission:
    print("Stable access granted! Welcome!")
    # Bonus: helmet required under 16
    if age < 16 and not has_helmet:
        print("Note: Please put on a helmet!")
else:
    print("Access denied!")
    print("You need: age >= 12, a helmet, or permission.")
