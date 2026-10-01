# Bonus-Items: dein Schläger wird schneller

Zum Schluss ein Belohnungs-Mechanismus: ein grünes **Bonus-Item** fällt wie Ball und Hindernis.
Fängst du es, wird dein Schläger schneller – er bewegt sich pro Tastendruck ein Stück weiter.

Dafür ersetzt du die feste Zahl `20` im Tastatur-Listener durch eine Variable `schrittweite`, die
mit jedem gefangenen Bonus wächst:

```js
let schrittweite = 20; // wie viele Pixel sich der Schläger pro Tastendruck bewegt

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') schlaegerX -= schrittweite;
  if (e.key === 'ArrowRight') schlaegerX += schrittweite;
  schlaegerX = begrenze(schlaegerX);
});
```

Wie immer zuerst als kleine, für sich testbare Funktion:

```js
function schnellerMachen(schrittweite) {
  return schrittweite + 5;
}
```

Beim Fangen des Bonus rufst du sie auf: `schrittweite = schnellerMachen(schrittweite);` – dieselbe
Kollisionserkennung wie beim Hindernis, nur mit einer dritten Konsequenz: nicht Punkte, nicht
Leben, sondern Tempo.
