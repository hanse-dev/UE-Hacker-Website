schilde = 80
waffen = 60
antrieb = 30
if schilde >= 50:
    if waffen >= 50:
        if antrieb >= 50:
            print("Alle Systeme bereit")
        else:
            print("Antrieb zu schwach")
    else:
        print("Waffen zu schwach")
else:
    print("Schilde zu schwach")