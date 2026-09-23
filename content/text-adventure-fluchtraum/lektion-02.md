# Mehrere Räume verknüpfen

Ein einzelner Raum ist noch kein Spiel. Jetzt kommt die eigentliche Idee eines Text-Adventures: Du legst **mehrere** Räume in einem großen Dictionary ab – die Schlüssel sind die Raumnamen, die Werte sind die Räume selbst (wieder Dictionaries):

```python
raeume = {
    "gang": {
        "beschreibung": "Ein kalter, steinerner Gang.",
        "ausgaenge": {"norden": "halle"}
    },
    "halle": {
        "beschreibung": "Eine große Halle mit hohen Fenstern.",
        "ausgaenge": {"sueden": "gang"}
    }
}

aktueller_raum = "gang"
```

Um sich zu bewegen, schlägst du zuerst im aktuellen Raum den gewünschten Ausgang nach, und aktualisierst dann `aktueller_raum`:

```python
naechster_raum = raeume[aktueller_raum]["ausgaenge"]["norden"]
aktueller_raum = naechster_raum
print(raeume[aktueller_raum]["beschreibung"])
```

`raeume[aktueller_raum]` findet also immer den *gerade aktiven* Raum – ändert sich `aktueller_raum`, "springst" du sofort zu einem anderen Eintrag im Dictionary.

> 💡 Das ist derselbe Trick wie bei den Räumen selbst: Ein Name (der Raumname) zeigt auf die eigentlichen Daten.
