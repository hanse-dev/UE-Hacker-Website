# Der Schläger hört auf die Tastatur

Jedes Fang-Spiel braucht einen Schläger, den man steuern kann. Dafür brauchst du zwei Dinge: eine **Funktion**, die aus der aktuellen Position und der gedrückten Taste die neue Position berechnet, und ein bisschen Logik, damit der Schläger nicht aus dem Spielfeld läuft.

Eine Funktion mit Parametern und Rückgabewert sieht so aus:

```js
function verdopple(zahl) {
  return zahl * 2;
}

console.log(verdopple(5)); // 10
```

`taste` ist bei echten Tastatur-Events der Wert `event.key` – zum Beispiel `'ArrowLeft'` oder `'ArrowRight'`, wenn eine Pfeiltaste gedrückt wird. Du bekommst diesen Wert in dieser Aufgabe direkt als Parameter, ohne selbst auf ein echtes `keydown`-Event zu hören.

Damit der Schläger nicht verschwindet, muss seine Position **begrenzt** werden:

```js
if (neueX < 0) neueX = 0;
if (neueX > 320) neueX = 320;
```

Das nennt man **Clamping** – einen Wert an einen erlaubten Bereich „festklammern".

> 💡 Später, wenn du dein ganzes Spiel zusammenbaust, hörst du mit `canvas.addEventListener('keydown', e => ...)` auf echte Tastendrücke und rufst dort `bewegeSchlaeger(x, e.key)` auf.
