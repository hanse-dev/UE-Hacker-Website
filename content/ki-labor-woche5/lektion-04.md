# 🌲 Der Baum selbst

Mit dem besten Schwellenwert kannst du jetzt einen **echten kleinen Entscheidungsbaum** bauen: ein
Dictionary, das sich merkt, welches Merkmal geprüft wird, wo die Schwelle liegt, und welche Klasse
auf jeder Seite vorhergesagt wird.

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

def baue_baum(daten, merkmal):
    schwelle, _ = bester_schwellenwert(daten, merkmal)
    links, rechts = teile_bei_schwellenwert(daten, merkmal, schwelle)
    return {
        "merkmal": merkmal,
        "schwelle": schwelle,
        "links": mehrheitsklasse(links),
        "rechts": mehrheitsklasse(rechts),
    }

def klassifiziere(baum, beispiel):
    if beispiel[baum["merkmal"]] < baum["schwelle"]:
        return baum["links"]
    else:
        return baum["rechts"]

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

baum = baue_baum(daten, "regen")
print(baum)
print(klassifiziere(baum, {"regen": 65, "temperatur": 20}))
print(klassifiziere(baum, {"regen": 5, "temperatur": 20}))
```

`baum` ist jetzt ein Dictionary wie `{"merkmal": "regen", "schwelle": 45.0, "links": "nein",
"rechts": "ja"}` – und `klassifiziere` sagt für ein **neues, unbekanntes** Beispiel vorher, ob ein
Schirm nötig ist, indem es einfach den Wert des passenden Merkmals mit der Schwelle vergleicht.
