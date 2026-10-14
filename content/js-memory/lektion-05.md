# Zwei Karten vergleichen

Jetzt kommt das Herz des Spiels. Beim Memory deckst du immer **zwei** Karten nacheinander auf. Dein Programm muss also wissen: Ist das gerade die erste Karte – oder schon die zweite?

Dafür merkt es sich die erste Karte in einer Variable. Am Anfang steht dort `null`. Das bedeutet: „Hier ist noch nichts.“

```
erste = null

bei jedem Klick auf eine Karte:
  wenn erste noch null ist:
    → das ist die erste Karte. Merke sie dir in erste.
  sonst:
    → das ist die zweite Karte. Vergleiche sie mit erste.
    → setze erste wieder auf null, damit die nächste Runde beginnen kann.
```

Dein Spiel hat damit zwei Zustände: „wartet auf die erste Karte“ und „wartet auf die zweite Karte“. Bei jedem Klick wechselt es vom einen in den anderen. Programmiererinnen und Programmierer nennen so etwas eine **Zustandsmaschine** – klingt kompliziert, ist aber genau das, was du hier siehst.

In der ersten Aufgabe baust du diese Logik erst einmal ohne Brett, nur mit Symbolen. In der zweiten Aufgabe kommt sie auf das echte Brett. Dort merkst du dir nicht das Symbol, sondern gleich die ganze Karte. Ihr Symbol kannst du jederzeit mit `.textContent` auslesen.

Eine Zeile ist auf dem Brett schon für dich vorbereitet:

```js
if (karte.textContent !== rueckseite) return;
```

Sie sagt: Liegt die Karte schon offen, passiert bei einem Klick gar nichts. `return` beendet die Klick-Funktion sofort. Ohne diese Zeile könntest du zweimal auf dieselbe Karte klicken – und hättest ein „Paar“ aus nur einer Karte!

> 💡 `!==` bedeutet „ist nicht gleich“. `===` kennst du schon – das ist das Gegenteil.
