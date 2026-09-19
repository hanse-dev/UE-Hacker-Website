# Das Finale: Spielschleife, Speichern, Laden – alles zusammen!
def spiele(spieler, befehle, ziel_gegenstand="Fohlen"):
    for text in befehle:
        print(f"\n> {text}")
        fuehre_aus(spieler, text)
        if spieler.hp <= 0:
            print("💀 Game Over – der Ziegenbock war zu stark. Versuche es noch einmal!")
            return
        if hat_gegenstand(spieler, ziel_gegenstand):
            print("🏆 Du hast das Fohlen gefunden und in den Stall zurückgebracht. Der Reiterhof feiert dich!")
            return

# Mira wurde gespeichert und geladen – jetzt geht ihr Abenteuer weiter:
spiele(geladen, ["gehe osten", "gehe osten", "nimm Fohlen"])