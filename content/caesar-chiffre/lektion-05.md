# Der Brute-Force-Knacker

Was, wenn du eine verschlüsselte Nachricht abfängst, aber die Verschiebung nicht kennst? Da eine Cäsar-Chiffre nur 26 mögliche Verschiebungen hat (0 bis 25), kannst du einfach *alle* durchprobieren – eine Schleife über `range(26)` reicht:

```python
def verschluesseln(text, verschiebung):
    ergebnis = ""
    for zeichen in text:
        if zeichen.isalpha():
            start = ord('a')
            position = ord(zeichen) - start
            neue_position = (position + verschiebung) % 26
            ergebnis = ergebnis + chr(start + neue_position)
        else:
            ergebnis = ergebnis + zeichen
    return ergebnis

def entschluesseln(text, verschiebung):
    return verschluesseln(text, -verschiebung)

geheimtext = "uwtojpy"
for versuch in range(26):
    print(versuch, entschluesseln(geheimtext, versuch))
```

Eine der 26 ausgegebenen Zeilen ist ein lesbares Wort – der Rest ist Buchstabensalat. Das ist der ganze Trick eines "Brute-Force"-Angriffs: nicht klug raten, sondern stur alle Möglichkeiten testen und die sinnvolle Ausgabe erkennen.

> 💡 Damit hast du das ganze Projekt zusammengebaut: Strings ([Woche 2](/kurs/python-12-wochen-grundkurs?week=2&tab=lektion#woche-2)), Schleifen ([Woche 4](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4)) und Funktionen ([Woche 5](/kurs/python-12-wochen-grundkurs?week=5&tab=lektion#woche-5)) — herzlichen Glückwunsch zu deinem ersten eigenen Projekt!
