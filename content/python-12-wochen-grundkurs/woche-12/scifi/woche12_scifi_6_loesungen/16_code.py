# Mission 3: Einwort-Befehle
def fuehre_aus(spieler, text):
    if text == "inventar":
        spieler.zeige_inventar()
        return
    if text == "hilfe":
        print("📖 Befehle: gehe <richtung>, nimm <gegenstand>, benutze <gegenstand>, inventar, hilfe")
        return
    try:
        aktion, ziel = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern. Tippe 'hilfe' für eine Liste.")
        return
    if aktion == "gehe":
        spieler.gehe(ziel)
        pruefe_gegner(spieler)
    elif aktion == "nimm":
        spieler.nimm(ziel)
    elif aktion == "benutze":
        spieler.benutze(ziel)
    else:
        print(f"🤔 '{aktion}' kenne ich nicht. Tippe 'hilfe' für eine Liste.")

held = Spieler("Lena", "schleuse")
spiele(held, ["hilfe", "nimm Zugangskarte", "inventar", "benutze Zugangskarte", "tanze wild"])