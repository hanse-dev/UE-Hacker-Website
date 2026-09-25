# Verschlossene Türen

Jetzt verbindest du beide Zutaten: Manche Türen sollen sich nur öffnen, wenn der passende Gegenstand im Inventar liegt. Dafür prüfst du vor dem eigentlichen Raumwechsel, ob der Schlüssel dabei ist. So läuft das Prinzip ab:

```
wenn "schluessel" in inventar:
    aktueller_raum = raeume[aktueller_raum]["ausgaenge"] an der Richtung, in die du willst
    gib die neue Raumbeschreibung aus
sonst:
    gib eine Meldung aus, dass die Tür verschlossen ist
```

Wichtig: `aktueller_raum` ändert sich hier **nur im `if`-Zweig**. Ohne Schlüssel bleibt die spielende Person also im selben Raum stehen – die Tür lässt sich einfach nicht öffnen, statt dass das Spiel abstürzt oder sie versehentlich doch weiterkommt.

> 💡 Genau diese Kombination – ein Dictionary-Lookup abhängig vom Ergebnis einer `in`-Prüfung – ist der Kern jedes Rätsels in einem Text-Adventure.
