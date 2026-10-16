# CSS einbinden

HTML legt fest, **was** auf der Seite steht. **CSS** (*Cascading Style Sheets*) legt fest, **wie** es aussieht. CSS schreibst du in einen `style`-Block im `head`:

```html
<head>
  <style>
    h1 {
      color: darkblue;
      background-color: lightyellow;
    }
  </style>
</head>
```

Eine **Regel** besteht aus:

- dem **Selektor** (`h1`) – wen die Regel betrifft
- einem **Block** in `{ }` mit **Deklarationen**: `eigenschaft: wert;`

Jede Deklaration endet mit einem **Semikolon**. Fehlt es, wirft der Browser die betroffene Zeile weg – ohne Fehlermeldung.

> 💡 Mit `style="…"` direkt am Element geht es auch, gilt aber nur für dieses eine Element. Ein `style`-Block gestaltet mit einer Regel alle passenden Elemente – und HTML und Design bleiben getrennt.
