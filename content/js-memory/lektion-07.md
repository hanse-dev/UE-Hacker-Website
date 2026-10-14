# Züge zählen und gewinnen

Dein Memory funktioniert! Jetzt fehlt nur noch, was jedes Spiel spannend macht: ein Ergebnis.

## Züge zählen

Ein **Zug** besteht aus zwei aufgedeckten Karten. Gezählt wird also immer bei der zweiten Karte. Den Zähler kennst du aus [Woche 7](/kurs/js-grundkurs?week=7): eine Variable, die bei jedem Mal um 1 wächst, und eine Anzeige, die den neuen Wert zeigt.

Damit klar ist, wo die zweite Karte anfängt, ist die Klick-Funktion in den Aufgaben ein wenig umgebaut: Bei der ersten Karte endet sie mit `return`. Alles, was danach steht, läuft nur noch bei der zweiten Karte.

## Gewonnen?

Dein Spiel ist gewonnen, wenn alle Paare gefunden sind. Dafür zählst du die gefundenen Paare mit. Wie viele Paare es gibt, musst du nicht selbst abzählen: Es sind halb so viele wie Karten.

```
bei jedem gefundenen Paar:
  zähle gefunden um 1 hoch
  wenn gefunden so groß ist wie die Anzahl der Paare:
    zeige die Gewinn-Meldung mit der Zahl der Züge
```

## Dein eigenes Memory

In der letzten Aufgabe baust du alles zusammen und machst das Spiel zu deinem eigenen. Du gibst nur noch die Symbole **einmal** an – `concat` verdoppelt die Liste für dich (das zeigt das Beispiel). Dann wird gemischt, und los geht's!

> 💡 Ideen zum Weiterbauen: Nimm sechs Symbole statt vier – dann hast du zwölf Karten. Ändere die Wartezeit im Timer und mach das Spiel schwerer. Oder gib den Karten mit `karte.style.background = 'gold'` eine eigene Farbe, sobald ein Paar gefunden ist.
