admin_password = "Nova-7"
guest_password = "Star-3"
entered = "Star-3"
if entered == admin_password:
    print("Full access granted")
elif entered == guest_password:
    print("Read access granted")
else:
    print("Access denied")
