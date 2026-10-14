# Nochmal spielen – und dein eigenes Quiz

Dein Quiz läuft von der ersten Frage bis zur Auswertung. Zwei Dinge fehlen noch: Man soll es noch
einmal spielen können, ohne den Code neu zu starten. Und es soll **dein** Quiz werden.

## Alles auf Anfang

Jetzt kommt der Knopf zurück, den du seit Lektion 2 versteckst. Er wird zum Knopf „Nochmal
spielen“ und erscheint erst bei der Auswertung.

Bei einem Neustart muss alles wieder so aussehen wie zu Beginn. Überlege, was sich während eines
Spiels verändert hat:

- die Variablen `nummer` und `punkte`,
- die Überschrift (dort steht jetzt „Auswertung“),
- die Rückmeldung in `#anzeige` und die Punkte-Anzeige,
- die Antwort-Knöpfe (versteckt) und der Knopf „Nochmal spielen“ (sichtbar),
- der Text in `#text`.

Das alles setzt eine Funktion `neuStart()` zurück. Der Trick dabei: Dieselbe Funktion startet das
Quiz auch **beim allerersten Mal**. Statt Anfang und Neustart zweimal zu schreiben, rufst du
`neuStart()` einfach ganz unten im Code einmal auf.

> 💡 Vergisst du eine Sache, merkst du es erst in der zweiten Runde – zum Beispiel, wenn die Punkte
> vom letzten Mal weiterzählen. Spiel dein Quiz deshalb immer zweimal hintereinander durch.

## Dein eigenes Quiz

Jetzt zahlt sich aus, dass die Fragen nur Daten sind: Du änderst das Array `fragen`, und der ganze
Rest funktioniert sofort mit deinen Fragen – egal, ob es drei sind oder zehn.

Ein paar Tipps für gute Quizfragen:

- Such dir ein **Thema**, bei dem du dich auskennst: Tiere, Fußball, dein Lieblingsbuch, Weltall,
  Musik …
- Eine Frage braucht **genau eine** richtige Antwort. Prüfe im Zweifel nach, ob sie wirklich
  stimmt.
- Falsche Antworten sollen **möglich klingen**. „Wie viele Beine hat eine Spinne? – 8, 1000 oder
  Banane“ ist zu leicht.
- Verteile die richtige Antwort: mal vorne, mal in der Mitte, mal hinten. Sonst reicht es, immer
  auf denselben Knopf zu klicken.
- Kontrolliere bei jeder Frage die Nummer bei `richtig` – gezählt wird ab 0.

## Ideen zum Weiterbauen

Dein Quiz ist fertig, aber du kannst es noch ausbauen:

- **Farben:** Färbe die Rückmeldung mit `anzeige.style.color = 'green'` bei einer richtigen und
  `'crimson'` bei einer falschen Antwort.
- **Fortschritt:** Zeige vor der Frage an, wie weit man ist, zum Beispiel „Frage 2 von 5“.
- **Vier Antworten:** Überall, wo im Code die Zahl 3 für die Anzahl der Knöpfe steht, brauchst du
  dann eine 4 – und jede Frage eine Antwort mehr.
- **Eigene Kommentare:** Ändere die Texte in `bewertung` oder füge eine weitere Stufe hinzu.
