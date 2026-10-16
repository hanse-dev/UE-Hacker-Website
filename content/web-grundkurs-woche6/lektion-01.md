# Jedes Element ist eine Box

Für den Browser ist **jedes** Element ein Rechteck – eine **Box**. Sie besteht aus vier Schichten, von innen nach außen:

1. **Inhalt** (*content*) – Text oder Bild
2. **Innenabstand** `padding` – Luft zwischen Inhalt und Rahmen
3. **Rahmen** `border`
4. **Außenabstand** `margin` – Luft zu den Nachbarn

```css
.box {
  padding: 20px;
  border: 3px solid teal;
  margin: 16px;
}
```

## Einzelne Seiten

Jede Angabe gibt es auch für einzelne Seiten: `padding-top`, `margin-left`, `border-bottom` … Kurzschreibweisen:

| Schreibweise | bedeutet |
|---|---|
| `padding: 10px;` | alle vier Seiten |
| `padding: 10px 20px;` | oben/unten 10px, links/rechts 20px |
| `padding: 5px 10px 15px 20px;` | oben, rechts, unten, links (im Uhrzeigersinn) |

> 💡 Im echten Browser zeigen dir die **Entwicklerwerkzeuge** (Rechtsklick → *Untersuchen*) jede Box mit ihren Schichten farbig an.
