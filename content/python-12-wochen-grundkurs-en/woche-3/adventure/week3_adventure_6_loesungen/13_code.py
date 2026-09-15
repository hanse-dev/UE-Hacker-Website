# Step 1 – Define passwords
master_password = "DragonBlade99"
guest_password = "SilverArrow"

# Step 2 – Simulate input
entered = "DragonBlade99"

# Steps 3 & 4 – Access check
if entered == master_password:
    print("Master recognized! Full treasure granted!")
    print("You receive: 500 gold + magical artifacts!")
elif entered == guest_password:
    print("Guest recognized! Partial treasure granted.")
    print("You receive: 100 gold.")
else:
    print("Wrong password!")
    # Bonus: hints
    if len(entered) < 5:
        print("Hint: The password is longer than 5 characters.")
    else:
        print("Hint: Maybe you forgot a capital letter?")