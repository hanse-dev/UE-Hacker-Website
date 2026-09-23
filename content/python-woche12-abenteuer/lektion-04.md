# ⚔️ Etappe 4: Spieler und Inventar

*Wissen aus Woche 10: Klassen*

Der **Spieler** merkt sich, wo er ist, wie viele Lebenspunkte er hat und was im Beutel steckt. `gehe()` aus Etappe 2 wird zur **Methode**.

### 💡 Neu: Objekte in Objekten (Komposition)

Ein Objekt kann **andere Objekte enthalten**: Der Spieler hat ein Inventar – eine Liste voller `Gegenstand`-Objekte. Das nennt man **Komposition** („hat ein“). Vererbung (Woche 11) sagt dagegen „ist ein“.

```python
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
```

`self.inventar = []` steht in `__init__`, damit **jeder** Spieler seinen eigenen Beutel bekommt.
