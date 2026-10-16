# Ein Knopf mit JavaScript

HTML legt den Inhalt fest, CSS das Aussehen. Damit eine Seite auf Klicks **reagiert**, braucht es eine dritte Sprache: **JavaScript**. Es steht in einem `script`-Block, am besten am Ende des `body`:

```html
<button id="modus">Dunkelmodus</button>

<script>
  document.querySelector('#modus').addEventListener('click', () => {
    document.body.classList.toggle('dunkel');
  });
</script>
```

Zeile für Zeile:

- `document.querySelector('#modus')` – suche das Element mit `id="modus"` (der Selektor wie im CSS)
- `.addEventListener('click', () => { … })` – wenn darauf geklickt wird, führe aus, was in `{ }` steht
- `document.body.classList.toggle('dunkel')` – schalte die Klasse `dunkel` am `body` an oder aus

Das Aussehen steht weiter im CSS:

```css
body.dunkel {
  background-color: #222;
  color: white;
}
```

JavaScript schaltet also nur die Klasse um – CSS macht den Rest.

> 💡 Mehr über JavaScript lernst du im JavaScript-Grundkurs.
