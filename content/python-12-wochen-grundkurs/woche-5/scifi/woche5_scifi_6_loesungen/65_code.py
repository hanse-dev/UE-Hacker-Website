def berechne_treibstoff(schiffe, tage):
    return schiffe * tage * 4

def reicht_treibstoff(bedarf, vorrat):
    return vorrat >= bedarf
def flottenbericht(flotte, schiffe, tage, vorrat):
    bedarf = berechne_treibstoff(schiffe, tage)
    print(f"Flotte {flotte}")
    print(f"Treibstoff: {bedarf}")
    print(f"Reicht: {reicht_treibstoff(bedarf, vorrat)}")

flottenbericht("Alpha", 10, 7, 300)
