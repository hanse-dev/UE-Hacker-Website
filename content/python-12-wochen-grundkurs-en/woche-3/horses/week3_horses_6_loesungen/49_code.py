stable_master_pw = "hay123"
groom_pw = "oats456"
entered = "carrot"
if entered == stable_master_pw:
    print("Full access granted")
elif entered == groom_pw:
    print("Feed access granted")
else:
    print("Wrong password: no feed today")