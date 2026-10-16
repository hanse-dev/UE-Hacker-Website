# Handy-Ansicht

Mehr als die Hälfte aller Webseiten wird auf dem Handy angeschaut. Eine Seite, die sich an die Bildschirmbreite anpasst, heißt **responsiv**. Dafür brauchst du drei Dinge:

## 1. Das viewport-meta-Tag

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Ohne diese Zeile tut das Handy so, als wäre es ein breiter Bildschirm, und verkleinert alles winzig.

## 2. Bilder, die nicht überstehen

```css
img {
  max-width: 100%;
  height: auto;
}
```

Ein Bild wird nie breiter als sein Platz.

## 3. Media Queries

Mit `@media` gelten Regeln nur bei bestimmten Bildschirmbreiten:

```css
.raster {
  grid-template-columns: repeat(3, 1fr);
}
@media (max-width: 600px) {
  .raster {
    grid-template-columns: 1fr;   /* auf schmalen Bildschirmen nur eine Spalte */
  }
}
```

> 💡 Die Vorschau hier ist meist schmal wie ein Handy – deine Media Queries wirken also oft schon darin. Im echten Browser kannst du das Fenster schmaler ziehen und zusehen, wie die Seite umspringt.
