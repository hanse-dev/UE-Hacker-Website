# Der häufigste Buchstabe

Im Diagramm hast du den längsten Balken sofort gesehen. Jetzt soll dein Programm ihn selbst finden – ohne dass jemand hinschaut.

Das Muster dafür heißt "Bestenliste mit einem Platz": Du gehst alle Einträge durch und merkst dir immer nur den besten, den du bisher gesehen hast. So läuft das Prinzip ab:

```
def haeufigster_buchstabe(text):
    zaehlung = zaehle_buchstaben(text)
    bester = ""            (noch kein Buchstabe gefunden)
    hoechste_anzahl = 0
    für jeden buchstabe in zaehlung:
        wenn zaehlung[buchstabe] größer ist als hoechste_anzahl:
            merke dir buchstabe als bester
            merke dir seine Anzahl als hoechste_anzahl
    gib bester zurück
```

Am Anfang ist die höchste Anzahl `0` – der erste Buchstabe schlägt das sofort. Danach wird nur noch ersetzt, wenn ein Buchstabe wirklich **öfter** vorkommt als der bisherige Rekordhalter.

Zum Vergleich, so häufig sind die Spitzenreiter in deutschen Texten ungefähr:

| Buchstabe | E | N | I | S | R | A | T |
|---|---|---|---|---|---|---|---|
| Anteil | 17 % | 10 % | 8 % | 7 % | 7 % | 7 % | 6 % |

Etwa jeder sechste Buchstabe ist also ein E – deutlich mehr als jeder andere. In der Bonus-Aufgabe prüfst du das an einem ganz normalen deutschen Satz nach.

> 💡 Dieses "Merke dir den bisher besten"-Muster brauchst du beim Programmieren ständig: für den höchsten Punktestand, den längsten Namen, den billigsten Preis.
