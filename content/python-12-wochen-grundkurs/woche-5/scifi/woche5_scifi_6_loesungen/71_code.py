def fliege_etappe(distanz, tempo):
    rest = distanz - tempo
    if rest < 0:
        return 0
    return rest
def simuliere_jagd(distanz, tempo, etappen):
    for etappe in range(1, etappen + 1):
        distanz = fliege_etappe(distanz, tempo)
        print(f"Etappe {etappe}: Noch {distanz} km")
    return distanz

rest = simuliere_jagd(100, 30, 4)
print(f"Rest: {rest}")
