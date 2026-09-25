# Die Collatz-Vermutung

Nimm eine beliebige Zahl. Ist sie gerade, teile sie durch 2. Ist sie ungerade, verdreifache sie und addiere 1. Wiederhole das immer wieder. Die **Collatz-Vermutung** behauptet: Egal, mit welcher Zahl du startest, du landest irgendwann bei 1. Bis heute konnte niemand beweisen, dass das für *jede* Zahl stimmt – aber für alle bisher getesteten Zahlen war es so. So läuft das Prinzip ab:

```
def collatz_schritte(zahl):
    schritte = 0
    solange zahl nicht gleich 1 ist:
        wenn zahl gerade ist: zahl = zahl // 2
        sonst: zahl = zahl * 3 + 1
        zähle schritte um eins hoch
    gib schritte zurück
```

Rufst du z.B. `collatz_schritte(9)` auf, kommt `19` heraus. Manche Zahlen sehen harmlos aus, brauchen aber überraschend viele Schritte, bevor die Folge bei 1 ankommt.

> 💡 Falls dir `while`-Schleifen noch nicht so vertraut sind, wirf einen Blick in [Woche 4 – Der Kreislauf der Macht](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) des 12-Wochen-Kurses.
