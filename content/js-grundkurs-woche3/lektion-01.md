# Wiederholen mit der for-Schleife

Bisher hast du jede Zeile Code nur einmal ausgeführt. Eine **Schleife** wiederholt einen
Code-Block mehrmals – ohne ihn mehrfach abzutippen. Die häufigste Form ist die `for`-Schleife:

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

Eine `for`-Schleife hat drei Teile, getrennt durch `;`:

| Teil | Bedeutung | Hier |
|---|---|---|
| Start | einmal am Anfang | `let i = 1` |
| Bedingung | vor jedem Durchlauf geprüft | `i <= 5` |
| Schritt | nach jedem Durchlauf | `i++` |

Solange die Bedingung `true` ist, läuft der Code im `{ }`-Block erneut – hier also fünfmal, mit
`i` = 1, 2, 3, 4, 5. Danach ist `i` = 6, die Bedingung wird `false`, und die Schleife stoppt.

Das Ergebnis einer Schleife lässt sich in einer Variable **aufsummieren**, indem du sie vor der
Schleife anlegst und in jedem Durchlauf veränderst:

```js
let summe = 0;
for (let i = 1; i <= 3; i++) {
  summe += i;
}
console.log(summe);
```
