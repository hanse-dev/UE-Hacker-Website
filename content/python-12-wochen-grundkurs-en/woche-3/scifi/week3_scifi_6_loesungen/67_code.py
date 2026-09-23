shields = 80
weapons = 60
drive = 30
if shields >= 50:
    if weapons >= 50:
        if drive >= 50:
            print("All systems ready")
        else:
            print("Drive too weak")
    else:
        print("Weapons too weak")
else:
    print("Shields too weak")
