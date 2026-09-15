# Step 1 – Access data
rank = 4
has_id_card = True
emergency = False

# Steps 2 & 3 – Access rule
if rank >= 5 or has_id_card or emergency:
    print("Bridge access granted! Scanner confirmed.")
    # Bonus: ID card required for low rank
    if rank < 8 and not has_id_card:
        print("Note: ID card required for ranks below 8!")
else:
    print("Access denied!")
    print("Missing authorization. Scanner ID invalid.")