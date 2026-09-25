# 🔍 Automatisch den besten Trennwert finden

Statt einen Schwellenwert zu raten, kann ein Programm einfach **alle sinnvollen Kandidaten
ausprobieren** und den mit den wenigsten Fehlern behalten. Sinnvolle Kandidaten liegen genau in
der Mitte zwischen zwei benachbarten, sortierten Werten des Merkmals:

```python
def teile_bei_schwellenwert(daten, merkmal, schwelle):
    links = [b for b in daten if b[merkmal] < schwelle]
    rechts = [b for b in daten if b[merkmal] >= schwelle]
    return links, rechts

def mehrheitsklasse(teil):
    anzahl_je_klasse = {}
    for beispiel in teil:
        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1

    beste_klasse = None
    bester_wert = -1
    for klasse in anzahl_je_klasse:
        anzahl = anzahl_je_klasse[klasse]
        if anzahl > bester_wert:
            bester_wert = anzahl
            beste_klasse = klasse
    return beste_klasse

def anzahl_falsch(teil):
    mehrheit = mehrheitsklasse(teil)
    falsch = 0
    for beispiel in teil:
        if beispiel["schirm"] != mehrheit:
            falsch += 1
    return falsch

def bester_schwellenwert(daten, merkmal):
    werte = sorted(set(b[merkmal] for b in daten))
    beste_schwelle = None
    wenigste_fehler = None
    for i in range(len(werte) - 1):
        kandidat = (werte[i] + werte[i + 1]) / 2
        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)
        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)
        if wenigste_fehler is None or fehler < wenigste_fehler:
            wenigste_fehler = fehler
            beste_schwelle = kandidat
    return beste_schwelle, wenigste_fehler

daten = [
    {"regen": 80, "temperatur": 18, "schirm": "ja"},
    {"regen": 90, "temperatur": 25, "schirm": "ja"},
    {"regen": 70, "temperatur": 10, "schirm": "ja"},
    {"regen": 60, "temperatur": 30, "schirm": "ja"},
    {"regen": 20, "temperatur": 22, "schirm": "nein"},
    {"regen": 10, "temperatur": 15, "schirm": "nein"},
    {"regen": 30, "temperatur": 28, "schirm": "nein"},
    {"regen": 15, "temperatur": 12, "schirm": "nein"},
]

print(bester_schwellenwert(daten, "regen"))
print(bester_schwellenwert(daten, "temperatur"))
```

`bester_schwellenwert` gibt ein Tupel `(schwelle, fehler)` zurück. Beim Merkmal `"regen"` findet
das Programm einen Schwellenwert mit 0 Fehlern – eine perfekte Trennung. Beim Merkmal
`"temperatur"` bleiben dagegen 3 Fehler übrig, egal welche Schwelle gewählt wird: Temperatur
allein sagt hier nicht viel über den Regenschirm aus.
