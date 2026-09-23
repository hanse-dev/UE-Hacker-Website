def kampfrunde(leben, schaden):
    neues_leben = leben - schaden
    if neues_leben < 0:
        return 0
    return neues_leben
def simuliere_kampf(leben, schaden, runden):
    for runde in range(1, runden + 1):
        leben = kampfrunde(leben, schaden)
        print(f"Runde {runde}: Leben {leben}")
    return leben

ende = simuliere_kampf(100, 30, 4)
print(f"Ende: {ende}")
