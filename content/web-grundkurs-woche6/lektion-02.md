# Breite, Höhe und box-sizing

Mit `width` und `height` legst du die Größe einer Box fest. Aber Achtung – standardmäßig gilt die Breite nur für den **Inhalt**:

```css
.karte {
  width: 200px;
  padding: 20px;
  border: 5px solid navy;
}
```

Diese Karte ist in Wahrheit 200 + 2 × 20 + 2 × 5 = **250px** breit. Das sorgt ständig für Ärger.

## Die Lösung: border-box

```css
.karte {
  box-sizing: border-box;
}
```

Jetzt zählen Innenabstand und Rahmen **mit** zur Breite – die Karte ist genau 200px breit, und der Inhalt wird entsprechend schmaler. Viele Seiten schalten das gleich für alle Elemente ein:

```css
* {
  box-sizing: border-box;
}
```

Der Stern `*` ist der **Universal-Selektor**: Er trifft jedes Element.

> 💡 Statt fester Breiten ist `max-width` oft besser: Die Box wird höchstens so breit, darf auf kleinen Bildschirmen aber schmaler sein.
