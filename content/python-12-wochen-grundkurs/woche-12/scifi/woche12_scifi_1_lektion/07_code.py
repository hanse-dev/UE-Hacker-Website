# Etappe 3a: Gegenstände sind Objekte – und liegen in den Räumen
class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["schleuse"]["gegenstaende"] = [Gegenstand("Zugangskarte", "Sie öffnet gesicherte Türen.")]
welt["korridor"]["gegenstaende"] = []
welt["labor"]["gegenstaende"] = [Gegenstand("Schweißbrenner", "Ein Werkzeug, das auch defekte Roboter stoppt.")]
welt["reaktorraum"]["gegenstaende"] = [Gegenstand("Notschalter", "Der rote Not-Aus-Schalter des Reaktors.")]

erster_raum = "schleuse"
erster_gegenstand = welt[erster_raum]["gegenstaende"][0]
print(f"Im {erster_raum}: {erster_gegenstand.name} – {erster_gegenstand.beschreibung}")