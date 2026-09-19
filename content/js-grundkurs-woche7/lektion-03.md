# Auf Klicks reagieren: addEventListener

Mit `.addEventListener('click', ...)` reagierst du auf einen Klick – du gibst eine Funktion mit,
die immer dann läuft, wenn geklickt wird:

```js
let knopf = document.querySelector('#knopf');
knopf.addEventListener('click', () => {
  document.querySelector('#anzeige').textContent = 'Geklickt!';
});
```

`() => { ... }` ist die Arrow-Function aus Woche 4 – hier ohne Namen, direkt als Argument an
`addEventListener` übergeben. Diese Funktion wird **nicht sofort** ausgeführt, sondern erst
**jedes Mal**, wenn auf `#knopf` geklickt wird.

> ⚠️ Der Name des Events muss exakt `'click'` heißen (kleingeschrieben, ohne Tippfehler) – ein
> falscher Name führt zu keinem Fehler, die Funktion wird einfach nie aufgerufen.
