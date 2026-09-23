# Verschlossene Türen

Jetzt verbindest du beide Zutaten: Manche Türen sollen sich nur öffnen, wenn der passende Gegenstand im Inventar liegt. Dafür prüfst du vor dem eigentlichen Raumwechsel, ob der Schlüssel dabei ist:

```python
if "schluessel" in inventar:
    aktueller_raum = raeume[aktueller_raum]["ausgaenge"]["norden"]
    print(raeume[aktueller_raum]["beschreibung"])
else:
    print("Die Tür ist verschlossen. Du brauchst einen Schlüssel.")
```

Wichtig: `aktueller_raum` ändert sich hier **nur im `if`-Zweig**. Ohne Schlüssel bleibt die spielende Person also im selben Raum stehen – die Tür lässt sich einfach nicht öffnen, statt dass das Spiel abstürzt oder sie versehentlich doch weiterkommt.

> 💡 Genau diese Kombination – ein Dictionary-Lookup abhängig vom Ergebnis einer `in`-Prüfung – ist der Kern jedes Rätsels in einem Text-Adventure.
