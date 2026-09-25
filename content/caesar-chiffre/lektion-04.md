# Die Entschlüsselungsfunktion

Zum Entschlüsseln machst du genau das Gegenteil: Du verschiebst um dieselbe Anzahl Stellen zurück. Der Trick: Statt eine komplett neue Funktion zu schreiben, rufst du einfach `verschluesseln` mit einer negativen Verschiebung auf – das `% 26` aus Lektion 2 sorgt dafür, dass auch negative Verschiebungen richtig "umlaufen". So läuft das Prinzip ab:

```
def entschluesseln(text, verschiebung):
    ruft verschluesseln auf, aber mit der negativen Verschiebung
    gibt das Ergebnis zurück
```

So sparst du dir doppelten Code – eine Funktion nutzt die andere. Rufst du `entschluesseln("mcvbg", 2)` auf, kommt wieder `"katze"` heraus.

> 💡 Schreib `verschluesseln` (aus Lektion 3) sicherheitshalber mit in dein Codefeld, auch wenn du sie schon einmal definiert hast – so funktioniert dein Code auch nach einem Neuladen der Seite zuverlässig.
