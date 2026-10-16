# Farbe ins Spiel

Bisher hast du gesagt, **was** auf der Seite steht. Jetzt bestimmst du, **wie es aussieht** – mit einer zweiten Sprache: **CSS**.

## Der style-Block

CSS schreibst du in einen `<style>`-Block im Kopf der Seite, zwischen `<head>` und `</head>`:

```html
<style>
  body {
    background-color: lightyellow;
  }
  h1 {
    color: darkorange;
    font-family: Arial, sans-serif;
  }
</style>
```

So liest du eine **CSS-Regel**:

- Vorne steht, **wen** es betrifft – der **Selektor**. `h1` heißt: alle `<h1>`-Überschriften. `body` ist die ganze Seite.
- In geschweiften Klammern `{ }` stehen die **Eigenschaften**: erst der Name, dann ein Doppelpunkt, dann der Wert und am Ende ein Semikolon `;`.

## Drei Eigenschaften für den Anfang

| Eigenschaft | Was sie macht | Beispiel |
|---|---|---|
| `color` | Textfarbe | `color: navy;` |
| `background-color` | Hintergrundfarbe | `background-color: lightblue;` |
| `font-family` | Schriftart | `font-family: Verdana, sans-serif;` |

Farben kannst du mit englischen Namen angeben: `red`, `blue`, `green`, `orange`, `purple`, `pink`, `gold`, `lightblue`, `lightgreen`, `darkred` … Es gibt über 140 davon!

> 💡 Erinnerst du dich an `style="color: …"` aus der ersten Lektion? Das geht auch, gilt aber nur für ein einziges Element. Mit dem `<style>`-Block färbst du mit einer Regel **alle** Überschriften auf einmal.
