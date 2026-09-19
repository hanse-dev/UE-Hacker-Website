# Kurzschreibweise: Arrow-Functions

Es gibt eine kürzere Schreibweise für Funktionen – die **Arrow-Function** (Pfeilfunktion), meist
in einer `const`-Variable gespeichert:

```js
function verdopple(x) {
  return x * 2;
}

const verdoppleKurz = (x) => x * 2;

console.log(verdopple(4));
console.log(verdoppleKurz(4));
```

Beide Funktionen tun exakt dasselbe. Bei einer Arrow-Function mit nur **einer** Zeile ohne
geschweifte Klammern `{ }` wird das Ergebnis automatisch zurückgegeben – ein `return` ist dort gar
nicht nötig (und würde sogar einen Fehler verursachen).

> ⚠️ Nutzt du dagegen geschweifte Klammern (`{ }`), brauchst du wieder ein explizites `return` –
> genau wie bei einer normalen Funktion:
> ```js
> const verdoppleMitKlammern = (x) => {
>   return x * 2;
> };
> ```
