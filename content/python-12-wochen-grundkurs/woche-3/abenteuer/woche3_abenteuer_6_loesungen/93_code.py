gefahrenstufe = 5
erfolgreiche_phasen = 2

if gefahrenstufe >= 4:
    if erfolgreiche_phasen < 3:
        print("Rettung erforderlich!")
    else:
        print("Der Trupp hält durch.")
else:
    print("Keine Gefahr für den Trupp.")
