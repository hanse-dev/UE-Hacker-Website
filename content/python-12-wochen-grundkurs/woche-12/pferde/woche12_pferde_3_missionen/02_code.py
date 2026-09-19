# 📦 STARTPAKET – führe diese Zelle zuerst aus! Sie enthält das komplette Spiel aus der Lektion.

import random

import json



class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

class Gegner:
    def __init__(self, name, hp, staerke):
        self.name = name
        self.hp = hp
        self.staerke = staerke

    def ist_besiegt(self):
        return self.hp <= 0

welt = {
    "hof": {
        "beschreibung": "Du stehst auf dem Hof. Der Mond scheint, und aus dem Stall hörst du ein leises Wiehern.",
        "ausgaenge": {"norden": "stallgasse"},
        "gegenstaende": [Gegenstand("Taschenlampe", "Sie leuchtet in dunklen Ecken.")],
        "gegner": None,
    },
    "stallgasse": {
        "beschreibung": "Eine lange Stallgasse. Rechts und links stehen die Boxen der Pferde.",
        "ausgaenge": {"sueden": "hof", "osten": "koppel", "westen": "sattelkammer"},
        "gegenstaende": [],
        "gegner": None,
    },
    "sattelkammer": {
        "beschreibung": "Die Sattelkammer riecht nach Leder. An der Wand hängen Sättel und Zaumzeug.",
        "ausgaenge": {"osten": "stallgasse"},
        "gegenstaende": [Gegenstand("Stallbesen", "Ein kräftiger Besen. Er hilft, den Ziegenbock zu vertreiben.")],
        "gegner": None,
    },
    "koppel": {
        "beschreibung": "Die nächtliche Koppel. Im Gras steht das Fohlen – und davor ein zorniger Ziegenbock!",
        "ausgaenge": {"westen": "stallgasse"},
        "gegenstaende": [Gegenstand("Fohlen", "Das kleine Fohlen folgt dir vertrauensvoll.")],
        "gegner": Gegner("Ziegenbock", 15, 6),
    },
}



def beschreibe(raum_name):
    raum = welt[raum_name]
    print(f"📍 {raum_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

def hat_gegenstand(spieler, name):
    for gegenstand in spieler.inventar:
        if gegenstand.name == name:
            return True
    return False

class Spieler:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hp = 20
        self.inventar = []  # eine Liste voller Gegenstand-Objekte

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
            print(f"🎉 Du hast den {gegner.name} besiegt!")

def fuehre_aus(spieler, text):
    try:
        aktion, ziel = text.split()
    except ValueError:
        print("🤔 Ich verstehe nur Befehle aus zwei Wörtern, z.B. 'gehe norden' oder 'nimm Taschenlampe'.")
        return
    if aktion == "gehe":
        spieler.gehe(ziel)
        pruefe_gegner(spieler)
    elif aktion == "nimm":
        spieler.nimm(ziel)
    else:
        print(f"🤔 '{aktion}' kenne ich nicht. Versuche 'gehe' oder 'nimm'.")

def spiele(spieler, befehle, ziel_gegenstand="Fohlen"):
    for text in befehle:
        print(f"\n> {text}")
        fuehre_aus(spieler, text)
        if spieler.hp <= 0:
            print("💀 Game Over – der Ziegenbock war zu stark. Versuche es noch einmal!")
            return
        if hat_gegenstand(spieler, ziel_gegenstand):
            print("🏆 Du hast das Fohlen gefunden und in den Stall zurückgebracht. Der Reiterhof feiert dich!")
            return

def speichern(spieler, dateiname="spielstand.json"):
    daten = {
        "name": spieler.name,
        "position": spieler.position,
        "hp": spieler.hp,
        "inventar": [{"name": g.name, "beschreibung": g.beschreibung} for g in spieler.inventar],
    }
    with open(dateiname, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=2)
    print(f"💾 Spielstand von {spieler.name} gespeichert.")

def laden(dateiname="spielstand.json"):
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
    except FileNotFoundError:
        print("📂 Es gibt noch keinen Spielstand.")
        return None
    spieler = Spieler(daten["name"], daten["position"])
    spieler.hp = daten["hp"]
    for eintrag in daten["inventar"]:
        spieler.inventar.append(Gegenstand(eintrag["name"], eintrag["beschreibung"]))
    print(f"📂 Spielstand von {spieler.name} geladen.")
    return spieler

print("📦 Startpaket geladen – die Welt ist bereit!")