# Mehrere Enden — dein Fluchtraum

Jetzt fügst du alles zu einem spielbaren Fluchtraum zusammen: mehrere Räume, ein Inventar, eine verschlossene Tür – und eine `while`-Schleife, die so lange neue Befehle einliest, bis das Spiel vorbei ist.

```python
while aktueller_raum != "flur":
    befehl = input("Was tust du? ")
    teile = befehl.split()

    if teile[0] == "gehe":
        richtung = teile[1]
        if richtung in raeume[aktueller_raum]["ausgaenge"]:
            ziel = raeume[aktueller_raum]["ausgaenge"][richtung]
            if ziel == "flur" and "schluessel" not in inventar:
                print("Die Tür ist verschlossen. Du brauchst einen Schlüssel.")
            else:
                aktueller_raum = ziel
                print(raeume[aktueller_raum]["beschreibung"])
        else:
            print("Dort geht es nicht weiter.")
    elif teile[0] == "nimm":
        inventar.append(teile[1])
        print("Du nimmst: " + teile[1])

print("Du hast die Bibliothek verlassen!")
```

Die Schleife läuft, solange `aktueller_raum` nicht `"flur"` ist – erst wenn die spielende Person dort ankommt, ist das Spiel gewonnen und die letzte Zeile nach der Schleife wird ausgeführt. Ohne den Schlüssel bleibt die Tür zum Flur für immer verschlossen: ein zweites, "schlechtes" Ende, in dem die Schleife nie endet.

> 💡 Damit hast du dein eigenes, spielbares Text-Adventure gebaut – aus genau zwei Grundbausteinen: Dictionaries für die Welt, Listen für das Inventar.
