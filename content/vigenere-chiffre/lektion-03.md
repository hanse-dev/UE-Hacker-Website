# Die Verschlüsselungsfunktion

Jetzt kombinierst du beide Ideen aus den letzten Lektionen: Für jeden Buchstaben im Text holst du dir den passenden Schlüsselbuchstaben (mit `%`, wie eben gelernt) und verschiebst wie bei Cäsar – nur ist die Verschiebung dieses Mal für jeden Buchstaben anders.

```python
def verschluesseln(text, schluesselwort):
    ergebnis = ""
    schluessel_index = 0
    for zeichen in text:
        if zeichen.isalpha():
            start = ord('a')
            position = ord(zeichen) - start
            schluessel_buchstabe = schluesselwort[schluessel_index % len(schluesselwort)]
            verschiebung = ord(schluessel_buchstabe) - start
            neue_position = (position + verschiebung) % 26
            ergebnis = ergebnis + chr(start + neue_position)
            schluessel_index = schluessel_index + 1
        else:
            ergebnis = ergebnis + zeichen   # Leerzeichen etc. bleiben unverändert und zählen nicht mit
    return ergebnis

print(verschluesseln("hallo", "key"))
```

Der einzige neue Trick: `schluessel_index` zählt nur bei echten Buchstaben hoch (deshalb steht er *innerhalb* des `if`) – Leerzeichen oder Satzzeichen überspringen den Schlüssel, statt ihn zu "verbrauchen".

> 💡 Die restliche Struktur (Schleife, `if zeichen.isalpha()`, `ord`/`chr`) ist genau [deine Verschlüsselungsfunktion aus dem Cäsar-Projekt](/kurs/projekt-caesar-chiffre) – nur die Verschiebung kommt jetzt aus dem Schlüsselwort statt aus einer festen Zahl.
