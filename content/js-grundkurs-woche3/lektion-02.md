# Wiederholen mit der while-Schleife

Eine `while`-Schleife läuft, solange ihre Bedingung `true` ist – ganz ohne festen Start/Schritt-
Teil wie bei `for`. Praktisch, wenn du vorher gar nicht weißt, wie oft sie laufen muss:

```js
let n = 5;
while (n > 0) {
  console.log(n);
  n--;
}
console.log('Start!');
```

Hier zählt `n` bei jedem Durchlauf um 1 runter (`n--`), bis die Bedingung `n > 0` nicht mehr
zutrifft.

> ⚠️ Vergisst du eine Zeile, die die Bedingung irgendwann `false` werden lässt (hier `n--`),
> läuft die Schleife für immer weiter – dein Code hängt dann fest. Prüfe bei jeder `while`-
> Schleife: **verändert sich hier innerhalb der Schleife etwas, das später die Bedingung
> stoppt?**

`while` eignet sich besonders, wenn die Anzahl der Durchläufe erst *während* der Schleife
feststeht – zum Beispiel, wenn du zählst, wie oft du etwas tun musst, bis ein Ziel erreicht ist.
