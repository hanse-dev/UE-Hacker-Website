# 🚀 Etappe 3: Gegenstände

*Wissen aus Woche 6 + 10: Listen und Klassen*

Jeder **Gegenstand** hat einen Namen und eine Beschreibung – dafür baust du die Klasse `Gegenstand` (Woche 10). Jeder Raum bekommt eine **Liste** seiner Gegenstände (Woche 6):

```python
class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["schleuse"]["gegenstaende"] = [Gegenstand("Zugangskarte", "Sie öffnet gesicherte Türen.")]
welt["korridor"]["gegenstaende"] = []
welt["labor"]["gegenstaende"] = [Gegenstand("Schweißbrenner", "Ein Werkzeug, das auch defekte Roboter stoppt.")]
welt["reaktorraum"]["gegenstaende"] = [Gegenstand("Notschalter", "Der rote Not-Aus-Schalter des Reaktors.")]
```

Ein Raum ohne Gegenstände hat einfach eine leere Liste `[]`.
