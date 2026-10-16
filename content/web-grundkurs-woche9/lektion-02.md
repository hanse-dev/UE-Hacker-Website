# Hover und Übergänge

Mit `:hover` gilt eine Regel nur, **solange die Maus über dem Element ist**:

```css
.knopf {
  background-color: steelblue;
  transition: background-color 0.3s;
}
.knopf:hover {
  background-color: navy;
}
```

`:hover` ist eine **Pseudoklasse** – sie beschreibt einen Zustand. Weitere: `:focus` (Feld ist ausgewählt) und `:active` (wird gerade geklickt).

## Sanfte Übergänge

Ohne `transition` springt die Farbe sofort um. Mit `transition: background-color 0.3s;` wechselt sie in 0,3 Sekunden **fließend**.

> 💡 Die `transition` gehört an das Element **selbst**, nicht an `:hover` – sonst ist der Wechsel nur in eine Richtung sanft.

Auch Größe lässt sich animieren: `transform: scale(1.05);` vergrößert ein Element um 5 %.
