# Kein Paar? Zurückdrehen!

Dein Spiel erkennt Paare. Aber falsche Karten bleiben einfach offen liegen – so kann man nicht spielen. Sie sollen sich wieder umdrehen. Allerdings nicht sofort, sonst sieht man die zweite Karte ja gar nicht!

## Etwas später erledigen: setTimeout

Mit `setTimeout` sagst du: „Mach das – aber erst in einer Weile.“

```js
setTimeout(() => {
  // dieser Code läuft erst später
}, 1000);
```

Die Zahl am Ende ist die Wartezeit in **Millisekunden**. 1000 Millisekunden sind eine Sekunde. Wichtig: Dein Programm bleibt in der Zwischenzeit nicht stehen. Es läuft weiter, und der Code im Timer kommt später dran.

## Schummeln verboten: das Brett sperren

Genau das wird zum Problem: Während zwei falsche Karten noch offen liegen, könnte man schnell eine dritte anklicken. Dann kommt dein Spiel durcheinander.

Die Lösung ist ein Schalter wie in Lektion 2. Er heißt `gesperrt`:

```
wenn kein Paar:
  gesperrt = true
  nach kurzer Wartezeit:
    beide Karten wieder verdecken
    erste = null
    gesperrt = false
```

Und ganz am Anfang der Klick-Funktion steht eine Prüfung: Ist das Brett gesperrt, passiert bei einem Klick nichts. Das zweite Beispiel zeigt so eine Sperre an einem Knopf.

Schau dir in der Aufgabe den Code genau an: `erste = null` steht jetzt nur noch beim gefundenen Paar. Beim falschen Paar brauchst du `erste` noch ein bisschen länger – sonst wüsstest du im Timer nicht mehr, welche Karte du zurückdrehen sollst.

> 💡 Dein Spiel hat jetzt drei Zustände: „wartet auf die erste Karte“, „wartet auf die zweite Karte“ und „gesperrt“. Die Zustandsmaschine aus Lektion 5 ist gewachsen.
