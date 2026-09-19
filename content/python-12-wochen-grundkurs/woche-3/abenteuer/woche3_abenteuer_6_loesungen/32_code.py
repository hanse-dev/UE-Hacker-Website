tuer_verschlossen = True
richtiger_schluessel = False

if tuer_verschlossen:
    print("Die Tür ist verschlossen.")
    if richtiger_schluessel:
        print("Die Tür öffnet sich!")
    else:
        print("Dieser Schlüssel passt nicht.")
else:
    print("Die Tür steht bereits offen.")
