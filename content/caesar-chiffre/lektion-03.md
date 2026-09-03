# Die Verschlüsselungsfunktion

Jetzt baust du das für einen ganzen Text statt nur für einen Buchstaben. Eine Funktion, die durch jeden Buchstaben des Textes läuft (eine Schleife!) und ihn verschiebt:

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
            ergebnis = ergebnis + zeichen   # Leerzeichen etc. bleiben unverändert
    return ergebnis

print(verschluesseln("katze", 2))
```

Die `if zeichen.isalpha()`-Prüfung sorgt dafür, dass Leerzeichen oder Satzzeichen einfach unverändert übernommen werden, statt einen Fehler zu verursachen.

> 💡 `for`-Schleifen aus [Woche 4](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) und eigene Funktionen aus [Woche 5 – Funktionen](/kurs/python-12-wochen-grundkurs?week=5&tab=lektion#woche-5) sind hier die Basis.
