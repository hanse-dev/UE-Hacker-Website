# ⚔️ Etappe 3: Gegenstände

*Wissen aus Woche 6 + 10: Listen und Klassen*

Jeder **Gegenstand** hat einen Namen und eine Beschreibung – dafür baust du die Klasse `Gegenstand` (Woche 10). Jeder Raum bekommt eine **Liste** seiner Gegenstände (Woche 6):

```python
class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["eingang"]["gegenstaende"] = [Gegenstand("Fackel", "Sie leuchtet in dunklen Ecken.")]
welt["halle"]["gegenstaende"] = []
welt["quelle"]["gegenstaende"] = [Gegenstand("Schwert", "Ein scharfes Schwert, das neben der Quelle im Stein steckt.")]
welt["schatzkammer"]["gegenstaende"] = [Gegenstand("Schatz", "Der legendäre Schatz von Pyralia!")]
```

Ein Raum ohne Gegenstände hat einfach eine leere Liste `[]`.
