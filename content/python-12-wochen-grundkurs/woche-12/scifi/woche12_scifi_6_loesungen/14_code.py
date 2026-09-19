# Mission 2: Der Heiltrank
welt["labor"]["gegenstaende"].append(Gegenstand("Medkit", "Stellt 10 Lebenspunkte wieder her."))

def benutze(self, gegenstand_name):
    for gegenstand in self.inventar:
        if gegenstand.name == gegenstand_name:
            if gegenstand_name == "Medkit":
                self.hp += 10
                self.inventar.remove(gegenstand)
                print(f"🧪 Du benutzt {gegenstand_name}. Du hast jetzt {self.hp} HP.")
            else:
                print(f"🤷 Mit {gegenstand_name} kann man hier nichts anfangen.")
            return
    print(f"❓ Du hast kein '{gegenstand_name}' im Beutel.")

Spieler.benutze = benutze

held = Spieler("Ben", "labor")
held.hp = 5
held.nimm("Medkit")
held.benutze("Medkit")
held.benutze("Medkit")