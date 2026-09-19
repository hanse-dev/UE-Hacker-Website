# Elemente finden: document.querySelector

Bisher hat dein Code nur Ausgaben in der Konsole erzeugt. Ab jetzt kannst du eine echte kleine
Webseite verändern – sie steht rechts als Übungsfläche bereit, mit einer Überschrift, einem Text,
einem Knopf und einer Anzeige.

Mit `document.querySelector('#id')` findest du ein Element anhand seiner **ID** (das `#` davor
ist Pflicht):

```js
let ueberschrift = document.querySelector('#ueberschrift');
console.log(ueberschrift.textContent);
```

`.textContent` liest den **Text** eines Elements aus – genau wie eine Property bei einem Objekt
(Woche 6), nur dass das Element hier eine echte, sichtbare Webseite ist.

> ⚠️ Ohne das `#` sucht `querySelector` nach einem **Tag** mit diesem Namen (z.B. `<ueberschrift>`)
> – das gibt es hier nicht, du bekommst `null` zurück. Mehr dazu im Debug-Abschnitt dieser Woche.
