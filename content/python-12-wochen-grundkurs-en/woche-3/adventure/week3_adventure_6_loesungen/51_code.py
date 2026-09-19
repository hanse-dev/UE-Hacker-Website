master_password = "Dragon42"
guest_password = "Visitor7"
entered = "Visitor7"

if entered == master_password:
    print("Full treasure granted")
elif entered == guest_password:
    print("Partial treasure granted")
else:
    print("Access denied")