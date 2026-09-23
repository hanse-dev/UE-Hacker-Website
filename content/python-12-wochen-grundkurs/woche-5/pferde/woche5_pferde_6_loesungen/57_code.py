def berechne_zeitbonus(sekunden):
    if sekunden <= 60:
        return 20
    elif sekunden <= 90:
        return 10
    else:
        return 0
def berechne_gesamt(fehler, sekunden):
    return 100 - fehler * 4 + berechne_zeitbonus(sekunden)

print(f"Gesamt: {berechne_gesamt(3, 55)}")
