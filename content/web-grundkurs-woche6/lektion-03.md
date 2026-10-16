# Zentrieren

Zwei Dinge werden gern verwechselt:

- **Text** in einer Box zentrierst du mit `text-align: center;`
- **eine ganze Box** zentrierst du mit `margin: 0 auto;` – das funktioniert aber nur, wenn die Box **schmaler** ist als ihr Platz, also eine `width` oder `max-width` hat.

```css
.inhalt {
  max-width: 300px;
  margin: 0 auto;      /* oben/unten 0, links/rechts automatisch */
  text-align: center;
}
```

`auto` heißt: Der Browser verteilt den freien Platz links und rechts gleichmäßig.

> 💡 So sind die meisten Websites gebaut: Der Inhalt steht in einer zentrierten Spalte mit `max-width`, damit die Zeilen auf großen Bildschirmen nicht endlos lang werden.
