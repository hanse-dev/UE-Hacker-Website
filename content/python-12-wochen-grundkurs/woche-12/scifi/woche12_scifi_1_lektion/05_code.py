# Etappe 2: Sich durch die Welt bewegen
def gehe(position, richtung):
    ausgaenge = welt[position]["ausgaenge"]
    if richtung in ausgaenge:
        neue_position = ausgaenge[richtung]
        beschreibe(neue_position)
        return neue_position
    print("🚫 Dort geht es nicht weiter!")
    return position

position = "schleuse"
for befehl in ["norden", "osten", "norden", "westen", "westen"]:
    print(f"\n> {befehl}")
    position = gehe(position, befehl)