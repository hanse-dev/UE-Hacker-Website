def fliege_etappe(distanz, tempo):
    rest = distanz - tempo
    if rest < 0:
        return 0
    return rest

distanz = 100
distanz = fliege_etappe(distanz, 25)
print(f"Distanz: {distanz}")
distanz = fliege_etappe(distanz, 25)
print(f"Distanz: {distanz}")
