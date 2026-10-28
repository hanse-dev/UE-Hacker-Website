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

def beschreibe(raumname):
    raum = welt[raumname]
    print(f"📍 {raumname.capitalize()}: {raum['beschreibung']}")
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
        self.puste = 20
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

    def nimm(self, gegenstand_name):
        raum = welt[self.position]
        for gegenstand in raum["gegenstaende"]:
            if gegenstand.name == gegenstand_name:
                raum["gegenstaende"].remove(gegenstand)
                self.inventar.append(gegenstand)
                print(f"🎒 Du nimmst: {gegenstand.name} – {gegenstand.beschreibung}")
                return
        print(f"❓ Hier gibt es kein '{gegenstand_name}'.")

    def zeige_inventar(self):
        if self.inventar:
            namen = [g.name for g in self.inventar]
            print("🎒 Im Beutel:", ", ".join(namen))
        else:
            print("🎒 Dein Beutel ist leer.")

import random

class Ausreisser:
    def __init__(self, name, puste, tempo):
        self.name = name
        self.puste = puste
        self.tempo = tempo

    def ist_eingefangen(self):
        return self.puste <= 0

welt["hof"]["ausreisser"] = None
welt["stallgasse"]["ausreisser"] = None
welt["sattelkammer"]["ausreisser"] = None
welt["koppel"]["ausreisser"] = Ausreisser("Ziegenbock", 15, 6)

def hat_gegenstand(spieler, name):
    for gegenstand in spieler.inventar:
        if gegenstand.name == name:
            return True
    return False

def einfangen(spieler, ausreisser):
    print(f"🪢 Einfangen: {spieler.name} will {ausreisser.name} einfangen!")
    bonus = 3 if hat_gegenstand(spieler, "Stallbesen") else 0
    while spieler.puste > 0 and not ausreisser.ist_eingefangen():
        naeher = random.randint(1, 6) + bonus
        ausreisser.puste -= naeher
        print(f"   Du kommst {naeher} Schritte näher. ({ausreisser.name}: {max(ausreisser.puste, 0)} Puste)")
        if ausreisser.ist_eingefangen():
            break
        wegsprung = random.randint(1, ausreisser.tempo)
        spieler.puste -= wegsprung
        print(f"   {ausreisser.name} springt weg – du verlierst {wegsprung} Puste. ({spieler.name}: {max(spieler.puste, 0)} Puste)")
    return spieler.puste > 0

def pruefe_ausreisser(spieler):
    ausreisser = welt[spieler.position]["ausreisser"]
    if ausreisser is not None and not ausreisser.ist_eingefangen():
        if einfangen(spieler, ausreisser):
            print(f"🎉 {ausreisser.name} ist eingefangen!")

welt["stallgasse"]["ausreisser"] = Ausreisser("Hofhund", 1, 1)
spieler = Spieler("Mira", "stallgasse")
pruefe_ausreisser(spieler)
