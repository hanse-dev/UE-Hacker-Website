# 📏 Wie gut ist eine Aufteilung?

Um einen Entscheidungsbaum aus Daten abzuleiten, musst du zuerst Beispiele anhand eines
Schwellenwerts in zwei Gruppen teilen können:

```python
def teile_bei_schwellenwert(daten, merkmal, schwelle):
    links = [b for b in daten if b[merkmal] < schwelle]
    rechts = [b for b in daten if b[merkmal] >= schwelle]
    return links, rechts

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

links, rechts = teile_bei_schwellenwert(daten, "regen", 50)
print(len(links))
print(len(rechts))
```

Aber ist diese Aufteilung auch **gut**? Eine gute Aufteilung landet möglichst nur eine Klasse auf
jeder Seite (das nennt man "rein"). Dafür brauchst du zwei weitere Funktionen: welche Klasse
kommt in einer Gruppe am häufigsten vor (`mehrheitsklasse`), und wie viele Beispiele weichen davon
ab (`anzahl_falsch` – die "Fehler" dieser Aufteilung)?

```python
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

print(mehrheitsklasse(links))
print(mehrheitsklasse(rechts))
print(anzahl_falsch(links))
print(anzahl_falsch(rechts))
```

Bei `schwelle=50` sind beide Seiten komplett rein (0 Fehler) – eine perfekte Aufteilung! Ein
anderer Schwellenwert wäre schlechter (siehe die nächste Aufgabe).
