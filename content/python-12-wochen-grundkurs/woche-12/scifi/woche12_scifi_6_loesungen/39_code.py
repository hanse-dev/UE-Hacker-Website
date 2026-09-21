welt = {
    "schleuse": {
        "beschreibung": "Du stehst in der Schleuse. Rote Warnlichter blinken, und die Station brummt bedrohlich.",
        "ausgaenge": {"norden": "korridor"},
    },
    "korridor": {
        "beschreibung": "Ein langer Korridor mit vielen Türen. Notbeleuchtung taucht alles in rotes Licht.",
        "ausgaenge": {"sueden": "schleuse", "osten": "reaktorraum", "westen": "labor"},
    },
    "labor": {"beschreibung": "Ein Labor voller Geräte. Auf einem Tisch liegt Werkzeug bereit.", "ausgaenge": {"osten": "korridor"}},
    "reaktorraum": {"beschreibung": "Der Reaktorraum! Der Reaktor summt – und davor steht ein defekter Wartungsroboter!", "ausgaenge": {"westen": "korridor"}},
}

def beschreibe(room_name):
    raum = welt[room_name]
    print(f"📍 {room_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

def gehe(position, richtung):
    ausgaenge = welt[position]["ausgaenge"]
    if richtung in ausgaenge:
        neue_position = ausgaenge[richtung]
        beschreibe(neue_position)
        return neue_position
    print("🚫 Dort geht es nicht weiter!")
    return position

class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["schleuse"]["gegenstaende"] = [Gegenstand("Zugangskarte", "Sie öffnet gesicherte Türen.")]
welt["korridor"]["gegenstaende"] = []
welt["labor"]["gegenstaende"] = [Gegenstand("Schweißbrenner", "Ein Werkzeug, das auch defekte Roboter stoppt.")]
welt["reaktorraum"]["gegenstaende"] = [Gegenstand("Notschalter", "Der rote Not-Aus-Schalter des Reaktors.")]

class Spieler:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hp = 20
        self.inventar = []

    def gehe(self, richtung):
        ausgaenge = welt[self.position]["ausgaenge"]
        if richtung in ausgaenge:
            self.position = ausgaenge[richtung]
            beschreibe(self.position)
            self.umschauen()
        else:
            print("🚫 Dort geht es nicht weiter!")

    def umschauen(self):
        gegenstaende = welt[self.position]["gegenstaende"]
        if gegenstaende:
            namen = [g.name for g in gegenstaende]
            print("👀 Du siehst:", ", ".join(namen))
        else:
            print("👀 Hier liegt nichts.")

    def nimm(self, item_name):
        raum = welt[self.position]
        for gegenstand in raum["gegenstaende"]:
            if gegenstand.name == item_name:
                raum["gegenstaende"].remove(gegenstand)
                self.inventar.append(gegenstand)
                print(f"🎒 Du nimmst: {gegenstand.name} – {gegenstand.beschreibung}")
                return
        print(f"❓ Hier gibt es kein '{item_name}'.")

    def zeige_inventar(self):
        if self.inventar:
            namen = [g.name for g in self.inventar]
            print("🎒 Im Beutel:", ", ".join(namen))
        else:
            print("🎒 Dein Beutel ist leer.")

spieler = Spieler("Mira", "schleuse")
spieler.nimm("Zugangskarte")
import json
data = {"name": spieler.name, "position": spieler.position, "hp": spieler.hp, "inventar": [g.name for g in spieler.inventar]}
print(json.dumps(data))
