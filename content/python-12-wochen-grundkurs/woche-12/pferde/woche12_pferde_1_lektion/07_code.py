# Etappe 3a: Gegenstände sind Objekte – und liegen in den Räumen
class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["hof"]["gegenstaende"] = [Gegenstand("Taschenlampe", "Sie leuchtet in dunklen Ecken.")]
welt["stallgasse"]["gegenstaende"] = []
welt["sattelkammer"]["gegenstaende"] = [Gegenstand("Stallbesen", "Ein kräftiger Besen. Er hilft, den Ziegenbock zu vertreiben.")]
welt["koppel"]["gegenstaende"] = [Gegenstand("Fohlen", "Das kleine Fohlen folgt dir vertrauensvoll.")]

erster_raum = "hof"
erster_gegenstand = welt[erster_raum]["gegenstaende"][0]
print(f"Im {erster_raum}: {erster_gegenstand.name} – {erster_gegenstand.beschreibung}")