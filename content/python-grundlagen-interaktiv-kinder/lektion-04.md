# f-Strings – Text und Variablen mischen ✨

Bisher konntest du entweder Text ausgeben oder eine Zahl – aber wie sagst du "Mein Lieblingstier ist eine Katze", wenn "Katze" in einer Variable steckt? Mit f-Strings kannst du Variablen direkt in einen Text einbauen. Schreibe einfach ein `f` vor die Anführungszeichen und `{variable}` an der Stelle, wo der Wert erscheinen soll.

```python
tier = "Katze"
print(f"Mein Lieblingstier ist eine {tier}!")
# gibt aus: Mein Lieblingstier ist eine Katze!
```

Das `f` ist wichtig – ohne das `f` davor würde Python die geschweiften Klammern einfach als Text ausgeben, statt den Wert der Variable einzusetzen. Du kannst auch mehrere Variablen in einem f-String mischen:

```python
tier = "Papagei"
alter = 3
print(f"{tier} ist {alter} Jahre alt.")
# gibt aus: Papagei ist 3 Jahre alt.
```

In den geschweiften Klammern kannst du sogar direkt rechnen:

```python
punkte = 15
print(f"Nach dem Bonus hast du {punkte * 2} Punkte!")
# gibt aus: Nach dem Bonus hast du 30 Punkte!
```

f-Strings sind heute die gängigste Art, Python-Programmierer:innen bauen Text und Werte zusammen – du wirst sie ab jetzt ständig benutzen.
