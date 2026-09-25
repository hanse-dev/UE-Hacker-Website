# Die Verschlüsselungsfunktion

Jetzt baust du das für einen ganzen Text statt nur für einen Buchstaben. Eine Funktion, die durch jeden Buchstaben des Textes läuft (eine Schleife!) und ihn verschiebt. So läuft das Prinzip ab:

```
def verschluesseln(text, verschiebung):
    ergebnis = ""
    für jedes zeichen in text:
        wenn zeichen ein Buchstabe ist (isalpha()):
            berechne die neue Position wie in Lektion 2 (ord, Verschiebung, % 26)
            hänge den neuen Buchstaben mit chr() an ergebnis an
        sonst:
            hänge zeichen unverändert an ergebnis an
    gib ergebnis zurück
```

Die `isalpha()`-Prüfung sorgt dafür, dass Leerzeichen oder Satzzeichen einfach unverändert übernommen werden, statt einen Fehler zu verursachen. Rufst du deine fertige Funktion z.B. mit `verschluesseln("katze", 2)` auf, kommt `"mcvbg"` heraus.

> 💡 `for`-Schleifen aus [Woche 4](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) und eigene Funktionen aus [Woche 5 – Funktionen](/kurs/python-12-wochen-grundkurs?week=5&tab=lektion#woche-5) sind hier die Basis.
