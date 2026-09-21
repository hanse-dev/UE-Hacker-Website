welt = {
    "hof": {
        "beschreibung": "Du stehst auf dem Hof. Der Mond scheint, und aus dem Stall hörst du ein leises Wiehern.",
        "ausgaenge": {"norden": "stallgasse"},
    },
    "stallgasse": {
        "beschreibung": "Eine lange Stallgasse. Rechts und links stehen die Boxen der Pferde.",
        "ausgaenge": {"sueden": "hof", "osten": "koppel", "westen": "sattelkammer"},
    },
    "sattelkammer": {"beschreibung": "Die Sattelkammer riecht nach Leder. An der Wand hängen Sättel und Zaumzeug.", "ausgaenge": {"osten": "stallgasse"}},
    "koppel": {"beschreibung": "Die nächtliche Koppel. Im Gras steht das Fohlen – und davor ein zorniger Ziegenbock!", "ausgaenge": {"westen": "stallgasse"}},
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

welt["hof"]["gegenstaende"] = [Gegenstand("Taschenlampe", "Sie leuchtet in dunklen Ecken.")]
welt["stallgasse"]["gegenstaende"] = []
welt["sattelkammer"]["gegenstaende"] = [Gegenstand("Stallbesen", "Ein kräftiger Besen. Er hilft, den Ziegenbock zu vertreiben.")]
welt["koppel"]["gegenstaende"] = [Gegenstand("Fohlen", "Das kleine Fohlen folgt dir vertrauensvoll.")]

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

spieler = Spieler("Mira", "hof")
spieler.nimm("Taschenlampe")
spieler.gehe("norden")
spieler.gehe("westen")
spieler.nimm("Stallbesen")
spieler.zeige_inventar()
