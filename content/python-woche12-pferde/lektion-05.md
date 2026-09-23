# 🐴 Etappe 5: Gegner und Kampf

*Wissen aus Woche 7 + 11: Module und Methoden*

Die Klasse `Gegner` bekommt eine Methode `ist_besiegt()`. Das Modul `random` (Woche 7) würfelt den Schaden aus:

```python
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
```

1. Der Spieler schlägt zu: 1 bis 6 Schaden, mit Stallbesen **+3**
2. Lebt der Gegner noch, schlägt er zurück
3. Eine `while`-Schleife wiederholt das, bis einer keine Lebenspunkte mehr hat

Räume ohne Gegner haben `None` („nichts“).
