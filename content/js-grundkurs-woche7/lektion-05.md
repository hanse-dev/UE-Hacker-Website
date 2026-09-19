# Klicks und Bedingungen kombinieren

Innerhalb einer Klick-Funktion kannst du alles verwenden, was du bisher gelernt hast – auch eine
Bedingung, die entscheidet, was angezeigt wird:

```js
let zaehlerWert = 0;
let knopf = document.querySelector('#knopf');
knopf.addEventListener('click', () => {
  zaehlerWert++;
  if (zaehlerWert >= 3) {
    document.querySelector('#anzeige').textContent = 'Geschafft!';
  } else {
    document.querySelector('#anzeige').textContent = zaehlerWert;
  }
});
```

Bei den ersten beiden Klicks zeigt die Anzeige `1` und `2`. Ab dem dritten Klick greift die
Bedingung `zaehlerWert >= 3`, und die Anzeige zeigt stattdessen `'Geschafft!'` – egal wie oft
danach noch geklickt wird.
