schleuse_verriegelt = True
richtiger_code = False
if schleuse_verriegelt:
    print("Die Schleuse ist verriegelt.")
    if richtiger_code:
        print("Der Code stimmt – die Schleuse öffnet sich!")
    else:
        print("Falscher Code! Zugang verweigert.")
else:
    print("Die Schleuse steht bereits offen.")