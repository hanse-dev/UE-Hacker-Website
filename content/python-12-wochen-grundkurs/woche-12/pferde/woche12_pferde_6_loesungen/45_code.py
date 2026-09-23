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

import random

class Gegner:
    def __init__(self, name, hp, staerke):
        self.name = name
        self.hp = hp
        self.staerke = staerke

    def ist_besiegt(self):
        return self.hp <= 0

welt["hof"]["gegner"] = None
welt["stallgasse"]["gegner"] = None
welt["sattelkammer"]["gegner"] = None
welt["koppel"]["gegner"] = Gegner("Ziegenbock", 15, 6)

def hat_gegenstand(spieler, name):
    for gegenstand in spieler.inventar:
        if gegenstand.name == name:
            return True
    return False

def kampf(spieler, gegner):
    print(f"⚔️ Kampf: {spieler.name} gegen {gegner.name}!")
    bonus = 3 if hat_gegenstand(spieler, "Stallbesen") else 0
    while spieler.hp > 0 and not gegner.ist_besiegt():
        schaden = random.randint(1, 6) + bonus
        gegner.hp -= schaden
        print(f"   Du triffst für {schaden} Schaden. ({gegner.name}: {max(gegner.hp, 0)} HP)")
        if gegner.ist_besiegt():
            break
        gegenschlag = random.randint(1, gegner.staerke)
        spieler.hp -= gegenschlag
        print(f"   {gegner.name} trifft dich für {gegenschlag}. ({spieler.name}: {max(spieler.hp, 0)} HP)")
    return spieler.hp > 0

def pruefe_gegner(spieler):
    gegner = welt[spieler.position]["gegner"]
    if gegner is not None and not gegner.ist_besiegt():
        if kampf(spieler, gegner):
            print(f"🎉 {gegner.name} wurde besiegt!")

def fuehre_aus(spieler, text):
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern, z.B. 'gehe norden' oder 'nimm Taschenlampe'.")
        return
    if action == "gehe":
        spieler.gehe(target)
        pruefe_gegner(spieler)
    elif action == "nimm":
        spieler.nimm(target)
    else:
        print(f"🤔 '{action}' kenne ich nicht. Versuche 'gehe' oder 'nimm'.")

spieler = Spieler("Mira", "hof")
def spiele(spieler, commands, goal_item):
    for text in commands:
        fuehre_aus(spieler, text)
        if hat_gegenstand(spieler, goal_item):
            print("🏆 Ziel erreicht!")
            return

spiele(spieler, ["gehe norden", "gehe westen", "nimm Stallbesen"], "Stallbesen")
