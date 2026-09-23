# ⚔️ Etappe 2: Sich bewegen

*Wissen aus Woche 3–5: Bedingungen, Schleifen, Funktionen*

Jetzt kommt Bewegung ins Spiel. `gehe()` prüft mit `if ... in ...`, ob es in diese Richtung einen Ausgang gibt:

```python
def gehe(position, richtung):
    ausgaenge = welt[position]["ausgaenge"]
    if richtung in ausgaenge:
        neue_position = ausgaenge[richtung]
        beschreibe(neue_position)
        return neue_position
    print("🚫 Dort geht es nicht weiter!")
    return position
```

- Ja → der neue Raum wird zurückgegeben (`return`) und beschrieben
- Nein → eine Meldung erscheint, und die Position bleibt gleich

Eine `for`-Schleife spielt eine Liste von Befehlen ab.
