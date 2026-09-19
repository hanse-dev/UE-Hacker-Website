# Schleifen steuern: break und continue

Manchmal willst du eine Schleife nicht ganz normal durchlaufen lassen:

- **`break`** beendet die Schleife **sofort komplett** – kein weiterer Durchlauf.
- **`continue`** überspringt nur den **aktuellen** Durchlauf und macht danach normal weiter.

```js
for (let i = 1; i <= 10; i++) {
  if (i === 6) {
    break;
  }
  console.log(i);
}
console.log('Fertig');
```

Sobald `i` gleich 6 ist, bricht die Schleife komplett ab – die Zahlen 6 bis 10 werden gar nicht
mehr angeschaut.

```js
for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue;
  }
  console.log(i);
}
```

Hier wird nur der Durchlauf mit `i === 3` übersprungen – die Schleife läuft danach ganz normal mit
4 und 5 weiter.

> 💡 Ein guter Merksatz: `break` = "raus aus der Schleife", `continue` = "weiter zum nächsten
> Durchlauf".
