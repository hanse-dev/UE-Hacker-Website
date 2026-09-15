# Step 1 – Set passwords
stable_master_password = "GoldenHoof2024"
groom_password = "HayBale"

# Step 2 – Simulate input
entry = "GoldenHoof2024"

# Steps 3 & 4 – Access check
if entry == stable_master_password:
    print("Stable master recognized! Full access granted!")
    print("All feed supplies available: Hay, Oats, Carrots, Apples")
elif entry == groom_password:
    print("Groom recognized! Feed access granted.")
    print("Available: Hay and Oats")
else:
    print("Wrong password!")
    # Bonus: hints
    if len(entry) < 6:
        print("Tip: The password is longer than 6 characters.")
    else:
        print("Tip: Mind the upper and lower case!")
