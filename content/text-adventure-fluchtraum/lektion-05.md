# Befehle einlesen

Bisher hast du Richtungen und Gegenstände fest in den Code geschrieben. Ein richtiges Text-Adventure liest stattdessen einen Befehl von der spielenden Person ein, zum Beispiel `"gehe westen"` oder `"nimm schluessel"`. Mit `input()` und `split()` zerlegst du so einen Satz in seine Wörter:

```python
befehl = input("Was tust du? ")
teile = befehl.split()

print(teile[0])
print(teile[1])
```

`split()` ohne Argument trennt einen String an jeder Lücke und gibt eine Liste der einzelnen Wörter zurück. `teile[0]` ist dann das Verb ("gehe", "nimm"), `teile[1]` das Ziel (die Richtung oder der Gegenstand).

Damit kannst du unterscheiden, was zu tun ist. So läuft das Prinzip ab:

```
wenn teile[0] gleich "gehe" ist:
    gib eine Meldung mit der Richtung (teile[1]) aus
sonst wenn teile[0] gleich "nimm" ist:
    gib eine Meldung mit dem Gegenstand (teile[1]) aus
```

> 💡 Beim Prüfen deiner Aufgabe wird der Befehl automatisch "eingetippt" – du siehst also kein Eingabefenster, aber dein Code bekommt trotzdem einen echten Text über `input()`.
