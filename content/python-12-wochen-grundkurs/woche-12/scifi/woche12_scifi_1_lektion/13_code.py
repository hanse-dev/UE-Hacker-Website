# Etappe 5: Falsche Eingaben abfangen
def fuehre_aus(spieler, text):
    try:
        aktion, ziel = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern, z.B. 'gehe norden' oder 'nimm Zugangskarte'.")
        return
    if aktion == "gehe":
        spieler.gehe(ziel)
        pruefe_gegner(spieler)
    elif aktion == "nimm":
        spieler.nimm(ziel)
    else:
        print(f"🤔 '{aktion}' kenne ich nicht. Versuche 'gehe' oder 'nimm'.")

fuehre_aus(held, "hallo")
fuehre_aus(held, "tanze wild")
fuehre_aus(held, "nimm Zauberstab")