shield = 80
attack = 60
healing = 20
if shield >= 50:
    if attack >= 50:
        if healing >= 50:
            print("Magic trial passed")
        else:
            print("Healing too weak")
    else:
        print("Attack too weak")
else:
    print("Shield too weak")
