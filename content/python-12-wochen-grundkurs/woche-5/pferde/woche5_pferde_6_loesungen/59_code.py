def berechne_zeitbonus(sekunden):
    if sekunden <= 60:
        return 20
    elif sekunden <= 90:
        return 10
    else:
        return 0

def berechne_gesamt(fehler, sekunden):
    return 100 - fehler * 4 + berechne_zeitbonus(sekunden)
def zeige_wertung(name, fehler, sekunden):
    print(f"{name}: {berechne_gesamt(fehler, sekunden)} Punkte")

for fehler in range(3):
    zeige_wertung("Sturmwind", fehler, 55)
