# 🏆 Das beste Merkmal wählen

Bisher hast du das Merkmal (`"regen"`) selbst ausgesucht. Bei mehreren Merkmalen kann ein Programm
aber auch das **beste Merkmal automatisch finden**: Für jedes Merkmal wird der beste Schwellenwert
gesucht, und am Ende gewinnt das Merkmal mit den wenigsten Fehlern.

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

def bestes_merkmal(daten, merkmale):
    bestes = None
    wenigste_fehler = None
    for merkmal in merkmale:
        _, fehler = bester_schwellenwert(daten, merkmal)
        if wenigste_fehler is None or fehler < wenigste_fehler:
            wenigste_fehler = fehler
            bestes = merkmal
    return bestes

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

print(bestes_merkmal(daten, ["regen", "temperatur"]))
```

`"regen"` gewinnt, weil es 0 Fehler hat, `"temperatur"` dagegen 3. Zusammen mit `baue_baum` aus der
letzten Lektion hast du jetzt alles zusammen, um aus einem Datensatz mit mehreren Merkmalen
**automatisch** einen einfachen, einstufigen Entscheidungsbaum abzuleiten – ganz ohne dass du das
Merkmal oder die Schwelle von Hand festlegen musst.
