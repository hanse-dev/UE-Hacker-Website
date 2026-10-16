# Klassen

Mit `p { … }` gestaltest du **alle** Absätze gleich. Was aber, wenn nur **manche** Elemente besonders aussehen sollen – zum Beispiel drei Steckbrief-Karten? Dafür gibt es **Klassen**.

## Eine Klasse vergeben

Eine Klasse ist ein Name, den du einem Element als Attribut gibst:

```html
<div class="karte">
  <h2>Mia</h2>
  <p>Katze, 3 Jahre</p>
</div>
```

`<div>` ist eine leere Kiste ohne eigene Bedeutung – ideal, um mehrere Elemente zusammenzupacken.

## Eine Klasse gestalten

Im CSS steht vor dem Klassennamen ein **Punkt**:

```css
.karte {
  background-color: white;
  border: 2px solid orange;
  border-radius: 10px;
  padding: 10px;
}
```

Jetzt sieht **jedes** Element mit `class="karte"` so aus – egal, wie viele es gibt. Eine Änderung im CSS, und alle Karten ändern sich mit.

## Mehrere Klassen

Ein Element darf mehrere Klassen haben, getrennt durch Leerzeichen:

```html
<div class="karte besonders">…</div>
```

So bekommt eine Karte alles von `.karte` **und** zusätzlich das, was in `.besonders` steht – zum Beispiel eine andere Farbe für deinen Liebling.
