# Step 1 – Set passwords
admin_password = "Nexus-7-Alpha"
guest_password = "GalaxyGuest"

# Step 2 – Simulate input
entry = "Nexus-7-Alpha"

# Steps 3 & 4 – Access check
if entry == admin_password:
    print("Admin recognized! Full access granted!")
    print("All systems accessible: Navigation, Weapons, Communications")
elif entry == guest_password:
    print("Guest recognized! Read access granted.")
    print("Navigation data readable only.")
else:
    print("Wrong password! Access denied.")
    # Bonus: Hints
    if len(entry) < 8:
        print("Tip: The password is longer than 8 characters.")
    else:
        print("Tip: Check special characters and capital letters!")