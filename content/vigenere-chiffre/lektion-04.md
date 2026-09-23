# Die Entschlüsselungsfunktion

Zum Entschlüsseln machst du für jeden Buchstaben das Gegenteil: Statt die Schlüssel-Verschiebung zu **addieren**, ziehst du sie ab. Alles andere – das Nachschlagen des passenden Schlüsselbuchstabens per `%`, das Weiterzählen von `schluessel_index` – bleibt exakt gleich.

```python
def entschluesseln(text, schluesselwort):
    ergebnis = ""
    schluessel_index = 0
    for zeichen in text:
        if zeichen.isalpha():
            start = ord('a')
            position = ord(zeichen) - start
            schluessel_buchstabe = schluesselwort[schluessel_index % len(schluesselwort)]
            verschiebung = ord(schluessel_buchstabe) - start
            neue_position = (position - verschiebung) % 26
            ergebnis = ergebnis + chr(start + neue_position)
            schluessel_index = schluessel_index + 1
        else:
            ergebnis = ergebnis + zeichen
    return ergebnis

print(entschluesseln("rejvs", "key"))
```

Das `% 26` sorgt wieder dafür, dass auch negative Zwischenergebnisse korrekt "umlaufen" – genau wie bei der Cäsar-Chiffre.

> 💡 Anders als beim Cäsar-Projekt kannst du hier **nicht** einfach `verschluesseln` mit einer negativen Zahl aufrufen, weil die Verschiebung nicht mehr eine einzelne Zahl ist, sondern für jeden Buchstaben neu aus dem Schlüsselwort berechnet wird.
