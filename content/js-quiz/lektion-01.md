# Fragen als Array von Objekten

In diesem Projekt baust du ein Quiz zum Anklicken. Am Ende trägst du deine eigenen Fragen ein und
kannst es von anderen spielen lassen.

Bevor es etwas zu klicken gibt, braucht dein Quiz **Daten**: die Fragen. Zu jeder Frage gehören
drei Dinge:

- der **Fragetext**,
- mehrere **Antworten** zur Auswahl,
- die Information, **welche Antwort richtig ist**.

Zusammengehörige Werte bündelst du in einem **Objekt** (Woche 6 im JS-Grundkurs). So sieht eine
Frage für dein Quiz aus:

```js
const frage1 = {
  frage: 'Wie viele Beine hat eine Spinne?',
  antworten: ['6', '8', '10'],
  richtig: 1,
};
```

Zwei Dinge sind hier neu:

- `antworten` ist ein **Array in einem Objekt**. Du liest es wie jede andere Property und greifst
  dann mit eckigen Klammern auf einen Eintrag zu: `frage1.antworten[0]` ist `'6'`.
- `richtig` ist kein Text, sondern die **Nummer** (der Index) der richtigen Antwort. Arrays zählen
  ab 0 – `richtig: 1` meint also die zweite Antwort, die `'8'`.

Den Text der richtigen Antwort bekommst du, indem du beides kombinierst:
`frage1.antworten[frage1.richtig]`.

## Viele Fragen: ein Array von Objekten

Ein Quiz hat mehr als eine Frage. Deshalb kommen alle Frage-Objekte in ein Array:

```js
const fragen = [
  { frage: '...', antworten: ['...', '...', '...'], richtig: 0 },
  { frage: '...', antworten: ['...', '...', '...'], richtig: 2 },
];
```

`fragen[0]` ist dann die erste Frage, `fragen[0].frage` ihr Text und `fragen.length` die Anzahl
der Fragen.

> 💡 Das ist die wichtigste Idee des ganzen Projekts: Die Fragen sind nur **Daten**. Der Rest
> deines Programms liest sie aus diesem Array. Willst du später ein anderes Quiz, änderst du nur
> das Array – der übrige Code bleibt gleich.

> ⚠️ Achte auf die Kommas: nach jeder Property im Objekt und nach jedem Objekt im Array. Ein
> vergessenes Komma ist hier der häufigste Fehler.
