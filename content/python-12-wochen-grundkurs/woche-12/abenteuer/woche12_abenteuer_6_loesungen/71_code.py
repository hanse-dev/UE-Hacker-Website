welt = {
    "eingang": {
        "beschreibung": "Du stehst am Eingang der Drachenhöhle. Es riecht nach Rauch.",
        "ausgaenge": {"norden": "halle"},
    },
    "halle": {
        "beschreibung": "Eine riesige Halle. Fackeln flackern an den Wänden.",
        "ausgaenge": {"sueden": "eingang", "osten": "schatzkammer", "westen": "quelle"},
    },
    "quelle": {"beschreibung": "Eine stille Quelle. Das Wasser funkelt magisch.", "ausgaenge": {"osten": "halle"}},
    "schatzkammer": {"beschreibung": "Gold, so weit du blicken kannst – und mittendrin schläft der Drache!", "ausgaenge": {"westen": "halle"}},
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

welt["eingang"]["gegenstaende"] = [Gegenstand("Fackel", "Sie leuchtet in dunklen Ecken.")]
welt["halle"]["gegenstaende"] = []
welt["quelle"]["gegenstaende"] = [Gegenstand("Schwert", "Ein scharfes Schwert, das neben der Quelle im Stein steckt.")]
welt["schatzkammer"]["gegenstaende"] = [Gegenstand("Schatz", "Der legendäre Schatz von Pyralia!")]

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

welt["eingang"]["gegner"] = None
welt["halle"]["gegner"] = None
welt["quelle"]["gegner"] = None
welt["schatzkammer"]["gegner"] = Gegner("Drache", 15, 6)

def hat_gegenstand(spieler, name):
    for gegenstand in spieler.inventar:
        if gegenstand.name == name:
            return True
    return False

def kampf(spieler, gegner):
    print(f"⚔️ Kampf: {spieler.name} gegen {gegner.name}!")
    bonus = 3 if hat_gegenstand(spieler, "Schwert") else 0
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

welt["halle"]["gegner"] = Gegner("Wache", 1, 1)
spieler = Spieler("Mira", "halle")
pruefe_gegner(spieler)
