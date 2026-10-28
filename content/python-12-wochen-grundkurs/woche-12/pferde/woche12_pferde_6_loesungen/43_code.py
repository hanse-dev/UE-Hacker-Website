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

def fuehre_aus(spieler, text):
    try:
        aktion, ziel = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern, z.B. 'gehe norden' oder 'nimm Taschenlampe'.")
        return
    if aktion == "gehe":
        spieler.gehe(ziel)
        pruefe_ausreisser(spieler)
    elif aktion == "nimm":
        spieler.nimm(ziel)
    else:
        print(f"🤔 '{aktion}' kenne ich nicht. Versuche 'gehe' oder 'nimm'.")

import json

def speichern(spieler, dateiname="stand.json"):
    daten = {
        "name": spieler.name,
        "position": spieler.position,
        "puste": spieler.puste,
        "inventar": [{"name": g.name, "beschreibung": g.beschreibung} for g in spieler.inventar],
    }
    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)
    print(f"💾 Spielstand von {spieler.name} gespeichert.")

def laden(dateiname="stand.json"):
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            daten = json.load(f)
    except FileNotFoundError:
        print("📂 Es gibt noch keinen Spielstand.")
        return None
    spieler = Spieler(daten["name"], daten["position"])
    spieler.puste = daten["puste"]
    for entry in daten["inventar"]:
        spieler.inventar.append(Gegenstand(entry["name"], entry["beschreibung"]))
    print(f"📂 Spielstand von {spieler.name} geladen.")
    return spieler

def spiele(spieler, befehle, ziel_gegenstand="Fohlen"):
    for text in befehle:
        print(f"\n> {text}")
        fuehre_aus(spieler, text)
        if spieler.puste <= 0:
            print("💤 Keine Puste mehr – versuche es noch einmal!")
            return
        if hat_gegenstand(spieler, ziel_gegenstand):
            print("🏆 Du hast das Fohlen gefunden und in den Stall zurückgebracht. Der Reiterhof feiert dich!")
            return

spieler = Spieler("Mira", "hof")
spieler.nimm("Taschenlampe")
speichern(spieler, "test.json")
zurueck = laden("test.json")
print(f"Position: {zurueck.position}")
