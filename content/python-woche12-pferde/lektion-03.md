# 🐴 Etappe 3: Gegenstände

*Wissen aus Woche 6 + 10: Listen und Klassen*

Jeder **Gegenstand** hat einen Namen und eine Beschreibung – dafür baust du die Klasse `Gegenstand` (Woche 10). Jeder Raum bekommt eine **Liste** seiner Gegenstände (Woche 6):

```python
class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["hof"]["gegenstaende"] = [Gegenstand("Taschenlampe", "Sie leuchtet in dunklen Ecken.")]
welt["stallgasse"]["gegenstaende"] = []
welt["sattelkammer"]["gegenstaende"] = [Gegenstand("Stallbesen", "Ein kräftiger Besen. Er hilft, den Ziegenbock zu vertreiben.")]
welt["koppel"]["gegenstaende"] = [Gegenstand("Fohlen", "Das kleine Fohlen folgt dir vertrauensvoll.")]
```

Ein Raum ohne Gegenstände hat einfach eine leere Liste `[]`.
