# Bedingungen verschachteln

Ein `if` kann ein weiteres `if` enthalten – so prüfst du erst eine grobe Bedingung, und nur wenn
die zutrifft, schaust du dir eine feinere Bedingung an:

```js
let eingeloggt = true;
let hatTicket = true;

if (eingeloggt) {
  if (hatTicket) {
    console.log('Zutritt gewährt');
  } else {
    console.log('Bitte Ticket kaufen');
  }
} else {
  console.log('Bitte zuerst einloggen');
}
```

Die innere Bedingung (`hatTicket`) wird nur überhaupt geprüft, wenn die äußere (`eingeloggt`)
schon `true` war – ist man gar nicht eingeloggt, spielt das Ticket keine Rolle mehr.

> 💡 Verschachtelte Bedingungen lassen sich oft auch mit `&&` (siehe letzte Lektion) als eine
> einzige Bedingung schreiben. Beide Wege sind richtig – Verschachtelung eignet sich besonders,
> wenn die beiden Fälle im `else`-Zweig unterschiedliche Meldungen brauchen, so wie hier.
