def berechne_dauer(runden):
    return runden * 5

def ist_trainierbar(fitness, dauer):
    return fitness >= dauer * 2
def zeige_training(name, fitness, runden):
    dauer = berechne_dauer(runden)
    if ist_trainierbar(fitness, dauer):
        print(f"{name}: Training {dauer} Minuten")
    else:
        print(f"{name}: braucht Pause")

zeige_training("Sturmwind", 90, 8)
zeige_training("Blitz", 60, 8)
