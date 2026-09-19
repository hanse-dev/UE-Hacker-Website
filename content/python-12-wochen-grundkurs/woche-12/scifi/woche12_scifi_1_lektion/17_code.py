# Das Finale: Spielschleife, Speichern, Laden – alles zusammen!
def spiele(spieler, befehle, ziel_gegenstand="Notschalter"):
    for text in befehle:
        print(f"\n> {text}")
        fuehre_aus(spieler, text)
        if spieler.hp <= 0:
            print("💀 Game Over – der Roboter war zu stark. Versuche es noch einmal!")
            return
        if hat_gegenstand(spieler, ziel_gegenstand):
            print("🏆 Du hast den Reaktor abgeschaltet. Nebula-7 ist gerettet, die Crew feiert dich!")
            return

# Mira wurde gespeichert und geladen – jetzt geht ihr Abenteuer weiter:
spiele(geladen, ["gehe osten", "gehe osten", "nimm Notschalter"])