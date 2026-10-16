# Verschachteln und Leerräume

Elemente dürfen andere Elemente enthalten – wie Kisten in Kisten:

```html
<p>Mein Trick ist der <strong>Ollie</strong>.</p>
```

Das `strong` steckt **im** Absatz. Die Regel dabei: **Was zuletzt geöffnet wurde, wird zuerst geschlossen.** `<p><strong>…</p></strong>` ist falsch – die Tags überkreuzen sich.

## Elemente ohne Inhalt

Manche Elemente umschließen nichts und haben deshalb **kein End-Tag**:

- `<br>` – Zeilenumbruch *innerhalb* eines Absatzes (z. B. in einer Adresse oder einem Gedicht)
- `<hr>` – eine Trennlinie zwischen zwei Themen

## Kommentare

```html
<!-- Notiz für mich: hier kommt später eine Galerie hin -->
```

Kommentare sieht nur, wer den Code liest – der Browser zeigt sie nicht an. Achte auf das genaue Ende `-->`.
