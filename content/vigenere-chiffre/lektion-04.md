# Die Entschlüsselungsfunktion

Zum Entschlüsseln machst du für jeden Buchstaben das Gegenteil: Statt die Schlüssel-Verschiebung zu **addieren**, ziehst du sie ab. Alles andere – das Nachschlagen des passenden Schlüsselbuchstabens per `%`, das Weiterzählen von `schluessel_index` – bleibt exakt gleich. So läuft das Prinzip ab:

```
def entschluesseln(text, schluesselwort):
    ergebnis = ""
    schluessel_index = 0
    für jedes zeichen in text:
        wenn zeichen ein Buchstabe ist (isalpha()):
            hole den passenden Schlüsselbuchstaben wie in Lektion 3
            berechne die Verschiebung aus diesem Schlüsselbuchstaben
            ziehe die Verschiebung diesmal ab statt sie zu addieren (% 26 nicht vergessen)
            hänge den neuen Buchstaben mit chr() an ergebnis an
            zähle schluessel_index um eins hoch
        sonst:
            hänge zeichen unverändert an ergebnis an
    gib ergebnis zurück
```

Das `% 26` sorgt wieder dafür, dass auch negative Zwischenergebnisse korrekt "umlaufen" – genau wie bei der Cäsar-Chiffre. Rufst du `entschluesseln("rejvs", "key")` auf, kommt wieder `"hallo"` heraus.

> 💡 Anders als beim Cäsar-Projekt kannst du hier **nicht** einfach `verschluesseln` mit einer negativen Zahl aufrufen, weil die Verschiebung nicht mehr eine einzelne Zahl ist, sondern für jeden Buchstaben neu aus dem Schlüsselwort berechnet wird.
