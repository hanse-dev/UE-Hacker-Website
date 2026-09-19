shields = 80
weapons = 40
drive = 90
if shields >= 50:
    if weapons >= 50:
        if drive >= 50:
            print("All systems ready")
        else:
            print("Drive too weak!")
    else:
        print("Weapons too weak!")
else:
    print("Shields too weak!")
