def berechne_wartung(stunden):
    return stunden * 5

def ist_wartbar(energie, dauer):
    return energie >= dauer * 2
def zeige_wartung(schiff, energie, stunden):
    dauer = berechne_wartung(stunden)
    if ist_wartbar(energie, dauer):
        print(f"{schiff}: Wartung {dauer} Minuten")
    else:
        print(f"{schiff}: braucht Aufladung")

zeige_wartung("Nebula", 90, 8)
zeige_wartung("Comet", 60, 8)
