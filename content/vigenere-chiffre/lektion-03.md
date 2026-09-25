# Die Verschlüsselungsfunktion

Jetzt kombinierst du beide Ideen aus den letzten Lektionen: Für jeden Buchstaben im Text holst du dir den passenden Schlüsselbuchstaben (mit `%`, wie eben gelernt) und verschiebst wie bei Cäsar – nur ist die Verschiebung dieses Mal für jeden Buchstaben anders. So läuft das Prinzip ab:

```
def verschluesseln(text, schluesselwort):
    ergebnis = ""
    schluessel_index = 0
    für jedes zeichen in text:
        wenn zeichen ein Buchstabe ist (isalpha()):
            hole den passenden Schlüsselbuchstaben: schluesselwort an Stelle (schluessel_index modulo Länge von schluesselwort)
            berechne die Verschiebung aus diesem Schlüsselbuchstaben (wie bei Cäsar)
            hänge den verschobenen Buchstaben mit chr() an ergebnis an
            zähle schluessel_index um eins hoch
        sonst:
            hänge zeichen unverändert an ergebnis an (schluessel_index bleibt unverändert)
    gib ergebnis zurück
```

Der einzige neue Trick: `schluessel_index` zählt nur bei echten Buchstaben hoch (deshalb steht er *innerhalb* des `if`) – Leerzeichen oder Satzzeichen überspringen den Schlüssel, statt ihn zu "verbrauchen". Rufst du deine fertige Funktion z.B. mit `verschluesseln("hallo", "key")` auf, kommt `"rejvs"` heraus.

> 💡 Die restliche Struktur (Schleife, `if zeichen.isalpha()`, `ord`/`chr`) ist genau [deine Verschlüsselungsfunktion aus dem Cäsar-Projekt](/kurs/projekt-caesar-chiffre) – nur die Verschiebung kommt jetzt aus dem Schlüsselwort statt aus einer festen Zahl.
