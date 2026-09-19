# Etappe 3a: Gegenstände sind Objekte – und liegen in den Räumen
class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["eingang"]["gegenstaende"] = [Gegenstand("Fackel", "Sie leuchtet in dunklen Ecken.")]
welt["halle"]["gegenstaende"] = []
welt["quelle"]["gegenstaende"] = [Gegenstand("Schwert", "Ein scharfes Schwert, das neben der Quelle im Stein steckt.")]
welt["schatzkammer"]["gegenstaende"] = [Gegenstand("Schatz", "Der legendäre Schatz von Pyralia!")]

erster_raum = "eingang"
erster_gegenstand = welt[erster_raum]["gegenstaende"][0]
print(f"Im {erster_raum}: {erster_gegenstand.name} – {erster_gegenstand.beschreibung}")