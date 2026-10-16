# Nebeneinander

Bisher stehen alle Kisten **untereinander**. Für eine Bildergalerie oder eine Navigationsleiste sollen sie aber **nebeneinander** stehen. Das macht **Flexbox**.

## Flexbox einschalten

Du brauchst eine äußere Kiste, die die anderen umschließt. Ihr gibst du `display: flex`:

```html
<div class="galerie">
  <img src="/web-bilder/katze.svg" alt="Katze" width="100">
  <img src="/web-bilder/hund.svg" alt="Hund" width="100">
  <img src="/web-bilder/fisch.svg" alt="Fisch" width="100">
</div>
```

```css
.galerie {
  display: flex;
  gap: 16px;
}
```

- `display: flex` stellt alle Kinder der Kiste in eine Reihe.
- `gap` ist der Abstand **zwischen** den Kindern.

## Noch mehr Möglichkeiten

| Eigenschaft | Was sie macht |
|---|---|
| `justify-content: center;` | schiebt alles in die Mitte |
| `justify-content: space-between;` | verteilt alles über die ganze Breite |
| `flex-wrap: wrap;` | wenn kein Platz mehr ist, geht es in der nächsten Zeile weiter |

> 💡 Eine **Navigationsleiste** ist auch nur eine Flexbox – mit Links statt Bildern. Mit `href="#abschnitt"` springt ein Link zu einem Element mit `id="abschnitt"` auf derselben Seite.
