admin_password = "nebula42"
guest_password = "visitor7"
entered = "visitor7"
if entered == admin_password:
    print("Full access granted")
elif entered == guest_password:
    print("Read access granted")
else:
    print("Wrong password!")
