# Der automatische Knacker

Jetzt hast du alle Teile beisammen:

1. `zaehle_buchstaben` zählt jeden Buchstaben.
2. `haeufigster_buchstabe` findet den Spitzenreiter.
3. `errate_verschiebung` berechnet daraus die Verschiebung.
4. `entschluesseln` aus dem Cäsar-Projekt dreht die Verschiebung zurück.

Fehlt nur noch eine Funktion, die alles verbindet. So läuft das Prinzip ab:

```
def knacke(text):
    errate die Verschiebung für den text
    entschlüssele den text mit dieser Verschiebung
    gib das Ergebnis zurück
```

Das sind nur zwei Zeilen – die eigentliche Arbeit steckt in den Funktionen, die du schon gebaut hast. So entstehen große Programme: aus kleinen Bausteinen, von denen jeder genau eine Sache kann.

Vergleiche das mit dem Brute-Force-Knacker aus dem Cäsar-Projekt: Der gab 26 Zeilen aus und brauchte dich, um die richtige zu erkennen. Dein neuer Knacker gibt **eine** Zeile aus – die richtige.

> 💡 Deine `verschluesseln`- und `entschluesseln`-Funktionen aus dem [Cäsar-Projekt](/kurs/projekt-caesar-chiffre) stehen unverändert im Editor. Du musst sie nicht neu schreiben.
