def renne_runde(strecke, tempo):
    rest = strecke - tempo
    if rest < 0:
        return 0
    return rest
def simuliere_rennen(strecke, tempo, runden):
    for runde in range(1, runden + 1):
        strecke = renne_runde(strecke, tempo)
        print(f"Runde {runde}: Noch {strecke} m")
    return strecke

rest = simuliere_rennen(100, 30, 4)
print(f"Rest: {rest}")
