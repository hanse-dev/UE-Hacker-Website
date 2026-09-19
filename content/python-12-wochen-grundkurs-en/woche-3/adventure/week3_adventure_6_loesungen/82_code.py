shield = 60
attack = 40
healing = 55

if shield >= 50:
    if attack >= 50:
        print("Trial passed with attack")
    elif healing >= 50:
        print("Trial passed with healing")
    else:
        print("Trial failed: attack and healing too weak")
else:
    print("Trial failed: shield too weak")