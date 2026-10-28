# 🐴 Etappe 5: Ausreißer einfangen

*Wissen aus Woche 7 + 11: Module und Methoden*

Auf der Koppel ist der Ziegenbock ausgebüxt! Die Klasse `Ausreisser` bekommt eine Methode `ist_eingefangen()`. Das Modul `random` (Woche 7) würfelt aus, wie nah du ihm kommst:

```python
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
```

1. Du kommst näher: 1 bis 6 Schritte, mit dem Stallbesen **+3** (damit treibst du ihn in eine Ecke)
2. Ist der Ausreißer noch frei, springt er weg – das kostet dich Puste
3. Eine `while`-Schleife wiederholt das, bis er eingefangen ist oder du keine Puste mehr hast

Räume ohne Ausreißer haben `None` („nichts“).
