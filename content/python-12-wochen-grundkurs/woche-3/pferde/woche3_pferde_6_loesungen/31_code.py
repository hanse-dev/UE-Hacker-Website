stalltuer_verschlossen = True
richtiger_schluessel = False

if stalltuer_verschlossen:
    if richtiger_schluessel:
        print("Der Schlüssel passt – die Stalltür öffnet sich!")
    else:
        print("Dieser Schlüssel passt nicht.")
else:
    print("Die Stalltür steht bereits offen.")
