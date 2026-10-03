sektor_sicher = True
treibstoff = 15
if sektor_sicher:
    if treibstoff >= 20:
        print("Sprung wird gestartet!")
    else:
        print("Treibstoff nachfüllen!")
else:
    print("Sektor meiden!")