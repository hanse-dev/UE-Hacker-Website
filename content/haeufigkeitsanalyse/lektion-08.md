# Warum Vigenère standhält

Dein Knacker entziffert jede längere Cäsar-Nachricht in einem Wimpernschlag. Und wie sieht es mit der Chiffre aus deinem [Vigenère-Projekt](/kurs/projekt-vigenere-chiffre) aus?

Erinnere dich: Vigenère benutzt ein **Schlüsselwort**, und jeder Buchstabe des Schlüsselworts liefert eine andere Verschiebung. Damit fällt genau die Schwäche weg, die du bei Cäsar ausgenutzt hast. Bei Cäsar wird jedes `e` zum **selben** Geheimbuchstaben – bei Vigenère wird es mal zu diesem, mal zu jenem, je nachdem, an welcher Stelle es steht.

Das hat eine sichtbare Folge für dein Balkendiagramm: Der eine riesige E-Balken wird auf mehrere kleinere Balken verteilt. Der Berg, an dem sich dein Knacker orientiert, ist weg.

In der ersten Aufgabe siehst du, was aus sechs gleichen Buchstaben wird. In der zweiten vergleichst du dieselbe Nachricht in beiden Verschlüsselungen – einmal mit Cäsar, einmal mit Vigenère und dem Schlüsselwort `"key"`. Dafür brauchst du zwei deiner Funktionen hintereinander:

```
buchstabe = häufigster Buchstabe im text
anzahl = der Eintrag für buchstabe in zaehle_buchstaben(text)
gib beides aus
```

**Ist Vigenère also unknackbar?** Fast 300 Jahre lang dachte man das. Dann fand man den Haken: Das Schlüsselwort wiederholt sich. Bei `"key"` werden der 1., 4., 7., 10. … Buchstabe alle mit `k` verschoben – diese Buchstaben für sich genommen sind eine ganz normale Cäsar-Chiffre! Wer die **Länge** des Schlüsselworts herausfindet, teilt den Text in entsprechend viele Stapel auf und knackt jeden Stapel mit genau der Häufigkeitsanalyse, die du gerade gebaut hast.

Deshalb gilt bis heute: Je länger und zufälliger der Schlüssel, desto sicherer die Nachricht. Moderne Verschlüsselung in deinem Handy benutzt Schlüssel, die so lang sind, dass kein Diagramm der Welt mehr hilft.

> 💡 Damit hast du die Geheimschrift-Reihe abgeschlossen: Im [Cäsar-Projekt](/kurs/projekt-caesar-chiffre) hast du verschlüsselt, im [Vigenère-Projekt](/kurs/projekt-vigenere-chiffre) die Chiffre verstärkt – und jetzt weißt du, wie Code-Knacker denken. Herzlichen Glückwunsch!
