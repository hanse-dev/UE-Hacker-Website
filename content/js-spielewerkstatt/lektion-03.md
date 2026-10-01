# Der Schläger hört auf die Tastatur

Jetzt bekommt dein Schläger ein Steuer: die Pfeiltasten. Dafür hört dein Code auf
Tastatur-Ereignisse:

```js
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') schlaegerX -= 20;
  if (e.key === 'ArrowRight') schlaegerX += 20;
});
```

`e.key` verrät, welche Taste gedrückt wurde. Ohne Begrenzung könnte der Schläger aber über den
Rand hinauslaufen – deshalb brauchst du eine kleine Funktion, die eine Position immer im
erlaubten Bereich hält (0 bis 320, denn der Schläger ist 80 Pixel breit und das Spielfeld 400):

```js
function begrenze(x) {
  if (x < 0) return 0;
  if (x > 320) return 320;
  return x;
}
```

Diese Funktion ist kein Selbstzweck – sie wird im Beispiel unten direkt beim Tastendruck benutzt
(`schlaegerX = begrenze(schlaegerX)`), du siehst ihre Wirkung also sofort am echten Schläger, wenn
du im Spielfeld die Pfeiltasten drückst. Bevor du sie einbaust, prüfst du sie kurz für dich mit
`console.log` – das ist die zuverlässigste Art, dein Ergebnis zu kontrollieren, bevor es im Spiel
steckt.
