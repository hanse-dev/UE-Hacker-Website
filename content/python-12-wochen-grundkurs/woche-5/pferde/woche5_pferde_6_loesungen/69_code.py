def renne_runde(strecke, tempo):
    rest = strecke - tempo
    if rest < 0:
        return 0
    return rest

strecke = 100
strecke = renne_runde(strecke, 25)
print(f"Strecke: {strecke}")
strecke = renne_runde(strecke, 25)
print(f"Strecke: {strecke}")
